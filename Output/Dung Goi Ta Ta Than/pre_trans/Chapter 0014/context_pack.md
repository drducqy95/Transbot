# Translation Context Pack

## Project
- Branch: Dung Goi Ta Ta Than
- Title: Đừng Gọi Ta Tà Thần
- Author: Thủy Quả Trung Đích Đồng Thần
- Genre: western_fiction/fantasy
- Source language: zh
- Target language: vi

## Chapter 14 - Tổng quan
- Source: Chapter 0014 心态转变.md
- Nội dung: Pete trải qua sự thay đổi tâm lý — từ kẻ yếu hèn sợ hãi thành tự tin hơn nhờ có Thần Tri Thức gia trì. Cậu quyết định đối đầu với bọn côn đồ đến đe dọa quán rượu nhà Lena, cầu nguyện Norven và nhận nhiệm vụ học 【O Thuật Phi Đạn】 (Arcane Missiles).

## Translation Rules
1. Dịch đúng ngữ cảnh, tự nhiên như tiếng Việt, không tóm tắt.
2. Tiêu đề chương (segment 0001): Dịch "心态转变" → "Thay đổi tâm lý"
3. Xưng hô người dẫn truyện: dùng 'hắn' cho Pete.
4. Pete tự xưng "ta" với Lena (vai vế cao hơn là pháp sư).
5. Lena gọi Pete là "anh" hoặc "Pete" (quan hệ bạn bè, trẻ).
6. Tên riêng phương Tây: giữ nguyên Latin (Pete, Lena, Norven, Bahamut, Dussley).
7. KHÔNG Hán Việt hóa tên phương Tây.
8. KHÔNG để sót chữ Hán/CJK trong bản dịch.
9. KHÔNG thêm giải thích/chú thích ngoài truyện.
10. KHÔNG tóm tắt thay cho dịch.

## Thuật ngữ bắt buộc
| Source | Target | Ghi chú |
|--------|--------|---------|
| 魔网 | Ma Võng | KHÔNG dịch là Ma Lưới |
| 施法者 | Thi Pháp Giả | Hán Việt chuẩn |
| 法师 | Pháp Sư | |
| 大法师 | Đại Pháp Sư | |
| 魔法学徒 | Ma Pháp Học Đồ | |
| 职业者 | Chức Nghiệp Giả | |
| 法术位 | Pháp thuật vị | |
| 戏法 | Hí pháp | |
| 奥术飞弹 | 【O Thuật Phi Đạn】 | Tên pháp thuật, để trong 【】 |
| 奥术能量 | năng lượng O Thuật | |
| 法术模型 | mô hình pháp thuật | |
| 神谕 | thần dụ | |
| 畸变怪 | quái vật dị biến | |
| 地精 | tinh linh | |
| 大地精 | đại tinh linh | |
| 上城区 | Khu Thượng Thành | |
| 下城区 | Khu Hạ Thành | |
| 格林港 | Green Port | |
| 卡罗恩学院 | Học viện Caroen | |
| 卡罗恩·拉杆 | Caroen Lever | Latin chuẩn, không đổi |
| 求知之神 | Thần Tri Thức | |
| 魔法女神 | Nữ thần Ma pháp | |
| 巴哈姆特 | Bahamut | |
| 诺文 | Norven | |
| 培特 | Pete | |
| 蕾娜 | Lena | |
| 德思礼 | Dussley | |
| 老莫尼 | Old Moni | |
| 3阶 | cấp 3 | |
| 1阶 | cấp 1 | |

## Forbidden
- KHÔNG để sót chữ Hán/CJK trong target.
- KHÔNG thêm giải thích/chú thích ngoài truyện.
- KHÔNG đổi segment_id.
- KHÔNG tóm tắt.
- KHÔNG thêm tiếng Anh trong ngoặc đơn.

## Segments to Translate
```json
{
  "chapter_number": 14,
  "chapter_title": "Thay đổi tâm lý",
  "source_file": "Source/Source Split/Dung Goi Ta Ta Than/Chapter 0014 心态转变.md",
  "segments": [
    {
      "segment_id": "0001",
      "type": "title",
      "source": "# 第14章 心态转变",
      "target": "# Chương 14: Thay đổi tâm lý"
    }
  ]
}
```

## Required Output Format
Return valid JSON only (no markdown wrapping, no explanations):
```json
{
  "chapter_number": 14,
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
