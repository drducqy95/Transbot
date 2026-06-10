#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Transbot chapter splitter.

Input : Transbot/Source/Source full/*
Output: Transbot/Source/Source Split/<branch>/Chapter 0001 <title>.md

Supports headings such as:
- 第1章 标题
- 406.第403章 聚众看片
- 第001章 标题
- 第四百二十一章 标题
- 第1回 标题
- 第1节 标题
- Chương 1: Tiêu đề
- Chapter 1: Title
"""

from pathlib import Path
import re
import unicodedata

ROOT = Path('/sdcard/My Agent/Transbot')
SOURCE_FULL = ROOT / 'Source' / 'Source full'
SOURCE_SPLIT = ROOT / 'Source' / 'Source Split'
EXPECTED_CHAPTERS = {
    'Dung Goi Ta Ta Than': 968,
}

CN_NUM = {
    '零': 0, '〇': 0, '○': 0,
    '一': 1, '二': 2, '三': 3, '四': 4, '五': 5,
    '六': 6, '七': 7, '八': 8, '九': 9,
    '十': 10, '百': 100, '千': 1000, '万': 10000,
}


def remove_diacritics(text: str) -> str:
    text = unicodedata.normalize('NFD', text)
    text = ''.join(ch for ch in text if unicodedata.category(ch) != 'Mn')
    return text.replace('Đ', 'D').replace('đ', 'd')


def branch_name_from_full_file(path: Path) -> str:
    name = path.stem
    story_title = name.split('_', 1)[0].strip()
    branch = remove_diacritics(story_title)
    branch = re.sub(r'[^\w\s-]', '', branch, flags=re.UNICODE)
    branch = re.sub(r'\s+', ' ', branch).strip()
    return branch or remove_diacritics(name)


def safe_filename_part(text: str) -> str:
    text = text.strip()
    text = re.sub(r'[\\/:*?"<>|]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text[:120] if len(text) > 120 else text


def chinese_numeral_to_int(s: str):
    s = s.replace('兩', '二').replace('两', '二').replace('〇', '零').replace('○', '零')
    if not s:
        return None
    if s.isdigit():
        return int(s)

    total = 0
    section = 0
    number = 0
    has_cn = False

    for ch in s:
        if ch in CN_NUM:
            has_cn = True
            val = CN_NUM[ch]
            if val < 10:
                number = val
            elif val == 10:
                if number == 0:
                    number = 1
                section += number * 10
                number = 0
            elif val == 100:
                if number == 0:
                    number = 1
                section += number * 100
                number = 0
            elif val == 1000:
                if number == 0:
                    number = 1
                section += number * 1000
                number = 0
            elif val == 10000:
                section += number
                total += section * 10000
                section = 0
                number = 0
        else:
            return None

    if not has_cn:
        return None
    return total + section + number


def normalize_heading(s: str) -> str:
    s = s.strip().lstrip('\ufeff')
    s = s.replace('　', ' ')
    s = re.sub(r'^\s*\d+\s*[\.\-、:]\s*', '', s)
    return s.strip()


def detect_chapter_heading(line: str):
    s = normalize_heading(line)
    if not s:
        return None

    # Chinese numeric: 第403章, 第003章, 第1回, etc.
    # Important: only match from start after optional numeric prefix; do NOT match 第x卷/第x篇 in author notes.
    m = re.match(r'^第\s*([0-9０-９]+)\s*[章节回]\s*[:：、.．\-—–]?\s*(.*)$', s)
    if m:
        raw_num = m.group(1).translate(str.maketrans('０１２３４５６７８９', '0123456789'))
        title = m.group(2).strip() or s
        return int(raw_num), title, s

    # Chinese numeral: 第四百二十一章
    m = re.match(r'^第\s*([零〇○一二三四五六七八九十百千万兩两]+)\s*[章节回]\s*[:：、.．\-—–]?\s*(.*)$', s)
    if m:
        num = chinese_numeral_to_int(m.group(1))
        if num is not None:
            title = m.group(2).strip() or s
            return int(num), title, s

    # Vietnamese / English.
    m = re.match(r'^(?:Chương|Chapter|CHƯƠNG|Chap|CHAP)\s*([0-9]+)\s*[:：\-—–]?\s*(.*)$', s, re.IGNORECASE)
    if m:
        num = int(m.group(1))
        title = m.group(2).strip() or s
        return num, title, s

    return None


def split_file(path: Path):
    branch = branch_name_from_full_file(path)
    branch_dir = SOURCE_SPLIT / branch

    if branch_dir.exists():
        existing_md = list(branch_dir.glob('*.md'))
        if existing_md:
            print(f'⏩ Skip existing branch: {branch} ({len(existing_md)} md files)')
            return

    print(f'📖 Reading: {path.name}')
    text = path.read_text(encoding='utf-8-sig', errors='replace')
    lines = text.splitlines(keepends=True)

    chapters = []
    for idx, line in enumerate(lines):
        found = detect_chapter_heading(line)
        if found:
            chapters.append((found[0], found[1], found[2], idx))

    if not chapters:
        print(f'⚠️ No chapter headings found: {path.name}')
        return

    branch_dir.mkdir(parents=True, exist_ok=True)

    for pos, (chapter_number, title, original_heading, start_idx) in enumerate(chapters):
        end_idx = chapters[pos + 1][3] if pos + 1 < len(chapters) else len(lines)
        body = ''.join(lines[start_idx + 1:end_idx]).strip()

        clean_title = safe_filename_part(title)
        filename = f'Chapter {chapter_number:04d} {clean_title}.md' if clean_title else f'Chapter {chapter_number:04d}.md'
        out_path = branch_dir / filename
        out_path.write_text(f'# {original_heading}\n\n{body}\n', encoding='utf-8')

    print(f'✅ {branch}: created {len(chapters)} chapters')


def main():
    print('📚 Transbot chapter splitter')
    if not SOURCE_FULL.exists():
        print(f'❌ Missing source folder: {SOURCE_FULL}')
        return

    files = [p for p in sorted(SOURCE_FULL.iterdir()) if p.is_file() and not p.name.startswith('.')]
    if not files:
        print('📂 No full source files found')
        return

    for p in files:
        split_file(p)

    # Validation report for known titles.
    for branch, expected in EXPECTED_CHAPTERS.items():
        branch_dir = SOURCE_SPLIT / branch
        if branch_dir.exists():
            count = len(list(branch_dir.glob('Chapter *.md')))
            if count != expected:
                print(f'⚠️ Expected {expected} chapters for {branch}, but found {count}.')
            else:
                print(f'✅ Validation passed for {branch}: {count} chapters.')


if __name__ == '__main__':
    main()
