# Translation Context Pack

## Project
- Branch: Dung Goi Ta Ta Than
- Title: Đừng Gọi Ta Tà Thần
- Author: Thủy Quả Trung Đích Đồng Thần
- Genre: Fantasy / Western Fiction
- Source language: zh (Chinese)
- Target language: vi (Vietnamese)

## Translation Rules
1. Dịch đúng theo ngữ cảnh, tự nhiên như truyện tiếng Việt.
2. Xưng hô người dẫn truyện: dùng "hắn" cho Norven (góc nhìn thứ ba).
3. Xưng hô nhân vật: Norven tự xưng "ta" với tín đồ; Pete xưng "tôi/con" tùy ngữ cảnh; Bahamut xưng "tôi" với Pete.
4. Tên riêng phương Tây giữ nguyên Latin (Norven, Pete Chinar, Bahamut, Hada).
5. Thuật ngữ tôn giáo phương Tây: "thần thánh", "tín đồ", "giáo hội", "thần dụ", "tà thần", "chính thần", "ngoại thần".
6. Không Hán Việt hóa sai văn hóa phương Tây.
7. KHÔNG để sót chữ Hán/CJK trong bản dịch cuối, trừ tên riêng được phép.

## Character Table
| Nhân vật | Vai trò | Xưng hô |
|---|---|---|
| Norven (诺文) | Nhân vật chính, tà thần tri thức | Người dẫn truyện: "hắn"; tự xưng "ta" với tín đồ; "tôi" khi thân thiết |
| Pete Chinar (培特·奇纳尔) | Học viên ma pháp, tín đồ đầu tiên | Xưng "tôi" với người ngoài; "con" với thần |
| Bahamut (巴哈姆特) | Người thẩm vấn/thẩm phán | Xưng "tôi" với Pete; Professional, nghiêm túc |
| Hada | Thực thể/sức mạnh huyền bí | Tên riêng, giữ nguyên |

## Glossary (liên quan đến chương 8)
| Thuật ngữ | Dịch | Ghi chú |
|---|---|---|
| 外神 | ngoại thần | Thần ngoại lai, thần cấp thấp, giữa chính thần và tà thần |
| 次级神明 | thần cấp thấp | Đồng nghĩa với ngoại thần |
| 正神 | chính thần | Thần chính thống có tín đồ đông đảo |
| 邪神 | tà thần | Thần tà ác, làm hư hỏng tín đồ |
| 马甲 | vỏ bọc/thân phận giả | Danh tính giả Norven tự tạo |
| 神职权柄 | thần chức quyền bính | Quyền năng gắn với thần chức |
| 神谕 | thần dụ | Thông điệp từ thần gửi đến tín đồ |
| 亲和度 | mức độ tương thích (affinity) | Mức hòa hợp giữa tín đồ và thần |
| 【哈达之饥渴】 | 【Cơn Đói Khát của Hada】 | Pháp thuật cấp 3 |
| 畸变体 | quái vật dị biến | Sinh vật bị dị biến do thần lực hỗn loạn |
| 辉光神教 | Giáo hội Huy Quang | Tổ chức tôn giáo trong truyện |

## Previous Story (tóm tắt)
- Norven xuyên không thành tà thần, thần lực của hắn mang khí tức hỗn loạn gây dị biến cho tín đồ.
- Pete Chinar bị lừa vào hang ổ quái vật, trước khi chết nhận được nhiệm vụ từ Norven: học 【Cơn Đói Khát của Hada】 và tiêu diệt quái vật.
- Pete đang bị thẩm vấn bởi Bahamut, người nghi ngờ Pete là tín đồ tà thần.
- Tại cuối chương 7, Norven đã nghĩ ra thân phận giả "Thần Tri Thức" (求知之神).

## Chapter 8 Context
Norven tự tạo thân phận "Thần Tri Thức" làm vỏ bọc. Hắn tự biên tự diễn một background: một ngoại thần vừa tỉnh dậy sau giấc ngủ dài. Chương này giải thích về hệ thống phân loại thần minh: chính thần, ngoại thần, tà thần. Pete thuyết phục Bahamut rằng hắn không phải tín đồ tà thần mà là tín đồ của một ngoại thần vừa tỉnh dậy.

## Critical Requirements
1. Tiêu đề chương phải là tiếng Việt tự nhiên (dùng cho filename và toc.title).
2. Tên file final: Chương 0008 - <tiêu đề tiếng Việt>.md
3. Tiêu đề chương gốc "背景全靠自己编" → gợi ý: "Bối cảnh tự biên tự diễn" hoặc "Background tự xào nấu"
4. KHÔNG GIỮ chữ Hán/CJK trong bản dịch cuối.
5. Giữ segment_id, không đổi thứ tự segment.

## Segments to Translate
[segments từ segments.json - 50 segments]

## Required Output Format
Return valid JSON only:
{
  "chapter_number": 8,
  "chapter_title_vi": "Chương 8: <tiếng Việt>",
  "filename_title": "<tiêu đề tiếng Việt không có số chương>",
  "segments": [
    {
      "segment_id": "0001",
      "source": "...",
      "target": "...",
      "notes": ""
    }
  ]
}
