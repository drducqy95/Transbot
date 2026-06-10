# Translation Context Pack - Chapter 9

## Project
- Branch: Dung Goi Ta Ta Than (Đừng Gọi Ta Tà Thần)
- Title: Đừng Gọi Ta Tà Thần
- Author: Thủy Quả Trung Đích Đồng Thần
- Genre: fantasy / western_fiction
- Source language: zh (Chinese)
- Target language: vi (Vietnamese)
- Name setting: keep_original (tên phương Tây giữ gốc latin, không Hán Việt hóa)
- Pronoun mode: hybrid

## Translation Rules (BẮT BUỘC)
1. Dịch đúng ngữ cảnh, tự nhiên như truyện tiếng Việt.
2. **Xưng hô người dẫn truyện:** giọng kể chuyện linh hoạt theo bối cảnh phương Tây fantasy. Dùng cách kể gián tiếp tự nhiên.
3. **Xưng hô nhân vật:** Pete dùng "tôi" khi tự xưng với Bahamut (quan hệ thẩm vấn/cấp dưới). Bahamut dùng "tôi" với Pete. Pete gọi Bahamut là "ông", "ngài" (kính trọng, xa lạ). Bahamut gọi Pete là "cậu" (kẻ dưới, trẻ hơn).
4. Tên riêng phương Tây: GIỮ NGUYÊN gốc Latin (không Hán Việt hóa). Pete Chinar, không "Bồi Đặc Kỳ Nạp Nhĩ". Bahamut, không "Ba Cáp Mục Đặc".
5. Thuật ngữ: "Ma Võng" (魔网) = Ma Võng. "Thần dụ" (神谕) = Thần dụ.
6. **Không để sót chữ Hán/CJK trong bản dịch cuối (trừ tên riêng TÂY PHƯƠNG được phép giữ gốc Latin)**.
7. **Không tóm tắt thay cho dịch.**
8. **Không thêm bình luận ngoài truyện.**
9. **Không thêm giải thích tiếng Anh trong ngoặc.**
10. **Tiêu đề chương (segment 0001) PHẢI được dịch sang tiếng Việt tự nhiên.** Dùng title phù hợp cho filename và toc. File sẽ đặt tên là "Chương 0009 - <tiêu đề tiếng Việt>.md"
11. **Giữ nguyên segment_id trong output. Không đổi thứ tự. Không thiếu segment.**

## Character Table (liên quan chương 9)
| Tên gốc | Tên dịch | Ghi chú |
|---------|----------|---------|
| 诺文 | Norven | Nhân vật chính, xưng thần/tự xưng Thần Tri Thức |
| 培特·奇纳尔 | Pete Chinar | Tín đồ, học viên Học viện Carone, người thi triển cấp 2 |
| 培特 | Pete | Gọi tắt của Pete Chinar |
| 巴哈姆特 | Bahamut | Pháp sư cấp 5, thẩm vấn viên |
| 巴哈姆特·康克敦特斯格拉兹查尔登 | Bahamut·Concadontesglazchalden | Tên đầy đủ |
| 魔法女神 | Nữ thần Ma pháp | |
| 辉光之神 | Thần Huy Quang | |

## Glossary (liên quan chương 9)
| Thuật ngữ | Dịch | Ghi chú |
|-----------|------|---------|
| 魔网 | Ma Võng | Mạng lưới ma pháp, KHÔNG dịch là Ma Lưới |
| 神谕 | Thần dụ | Chỉ dẫn từ thần |
| 真名知晓 | Biết Tên Thật | Tên pháp thuật mới |
| 法术反制 | Phản Chế Pháp Thuật | Counterspell |
| 奥术 | Huyền thuật /奥术 magic |
| 权能 | Quyền năng | Quyền năng thần chức |
| 神职权柄 | Thần chức quyền bính | |
| 外神 | Ngoại thần | |
| 神国 | Thần quốc | |

## Previous Story Context (tóm tắt đến chương 8)
- Norven xuyên không thành tà thần, có quyền năng tri thức.
- Pete Chinar, học viên yếu kém Học viện Carone, bị lừa vào ổ quái vật dị biến, được Norven ban pháp thuật【Cơn Đói Khát của Hada】và sống sót.
- Pete bị Bahamut (pháp sư cấp 5) thẩm vấn. Ban đầu tin tưởng 17%, bị giảm xuống 13% sau khi Pete bịa chuyện bị lộ.
- Norven tạo thân phận "Thần Tri Thức" (外神) làm vỏ bọc.
- Bahamut yêu cầu Pete cầu nguyện vị thần đó để chứng minh không phải tà thần.

## Chapter 9 Summary (for understanding)
Pete cầu nguyện Norven. Norven nhận được pháp thuật mới【真名知晓】(Biết Tên Thật) - pháp thuật cấp 2 có thể dò tìm tên thật, phá vỡ ngụy trang. Norven suy luận rằng Bahamut có thể đang che giấu điều gì đó. Pete thi triển pháp thuật, và khi sắp đọc tên thật của Bahamut, Bahamut giật mình dùng Counterspell ngăn lại. Ngay lập tức Bahamut tin Pete (trust 77%), ký giấy rời đi vội vã.

## Segments to Translate
Input format: mỗi segment có segment_id, type, source text.

Output format REQUIRED (valid JSON):
```json
{
  "chapter_number": 9,
  "segments": [
    {
      "segment_id": "0001",
      "source": "...",
      "target": "...",
      "notes": ""
    }
  ]
}
```

**QUAN TRỌNG:**
- Dịch TIÊU ĐỀ (segment 0001 "第9章 真名知晓") sang tiếng Việt tự nhiên. Ví dụ: "Chương 9: Biết Tên Thật" hoặc tương tự. Đây sẽ dùng làm filename "Chương 0009 - <title>.md".
- Notes để trống "" trừ khi có ghi chú dịch thuật.
- KHÔNG bỏ segment nào. Phải có đủ 39 segment.
- Không thêm segment mới.
- Dịch sát, tự nhiên, Việt Nam hóa phù hợp bối cảnh phương Tây.
