#!/usr/bin/env python3
"""
Scan Source/Source Split/ for branch directories and output info
for creating missing branch cronjobs.
"""
import os
import re
import unicodedata
import json

SOURCE_SPLIT = "/sdcard/My Agent/Transbot/Source/Source Split"
CRON_PREFIX = "transbot-branch-"

def slugify(name):
    """Convert a directory name to a cronjob-safe slug."""
    name = unicodedata.normalize('NFD', name)
    name = re.sub(r'[\u0300-\u036f]', '', name)  # remove diacritics
    name = name.lower().strip()
    name = re.sub(r'[^a-z0-9\-]', '-', name)     # replace special chars with hyphens
    name = re.sub(r'-+', '-', name)               # collapse multiple hyphens
    name = name.strip('-')
    return name

def main():
    print("=" * 60)
    print("📋 Transbot — Branch Manager Scanner")
    print("=" * 60)

    if not os.path.isdir(SOURCE_SPLIT):
        print(f"❌ Directory not found: {SOURCE_SPLIT}")
        return

    branches = sorted([
        d for d in os.listdir(SOURCE_SPLIT)
        if os.path.isdir(os.path.join(SOURCE_SPLIT, d))
    ])

    if not branches:
        print("📂 No branch directories found.")
        return

    print(f"\nFound {len(branches)} branch(es):\n")

    for branch in branches:
        cron_name = CRON_PREFIX + slugify(branch)
        branch_path = os.path.join(SOURCE_SPLIT, branch)
        file_count = len([f for f in os.listdir(branch_path) if os.path.isfile(os.path.join(branch_path, f))])
        print(f"  📁 {branch}")
        print(f"     ├─ Path: {branch_path}")
        print(f"     ├─ Files: {file_count}")
        print(f"     └─ Cron name: {cron_name}")

    print("\n--- JSON Output (for parsing) ---")
    result = []
    for branch in branches:
        cron_name = CRON_PREFIX + slugify(branch)
        result.append({
            "branch": branch,
            "cron_name": cron_name,
            "path": os.path.join(SOURCE_SPLIT, branch)
        })
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
