# Translation Context Pack

## Project
- Branch: Dung Goi Ta Ta Than
- Title: Đừng Gọi Ta Tà Thần
- Author: Thủy Quả Trung Đích Đồng Thần
- Genre: fantasy / western_fiction
- Source language: zh
- Target language: vi
- Chapter: 11
- Source file: Chapter 0011 神力的限制.md

## Translation Rules
- Dịch đúng theo ngữ cảnh, tự nhiên như truyện tiếng Việt.
- Xưng hô người dẫn truyện: giọng kể hiện đại, phương Tây (fantasy). Dùng "hắn" cho nam, "nó" cho vật/sinh vật phi nhân.
- Xưng hô nhân vật: Pete với Norven = con/ngài (tôn kính thần). Pete với cảnh sát = tôi/anh. Cảnh sát với Pete = mày/cậu/anh tùy ngữ cảnh.
- Norven (thần) tự xưng: ta, gọi người khác = ngươi.
- Tên riêng phương Tây GIỮ NGUYÊN dạng Latin (Pete Chinar, Norven, Bahamut, Carone, Prantis, Reak, Green Haven, etc.) - KHÔNG Hán Việt hóa tên phương Tây.
- Địa danh: Frostfire Plateau → Cao Nguyên Sương Lửa (dịch nghĩa), Green Haven → Green Haven (giữ tên gốc), các địa danh như Misty Sea → Biển Sương Mù, Darkwood → Rừng U Ám.
- 【Tên Pháp Thuật】: giữ dấu 【】 format. "法术反制" → Phản Chế Pháp Thuật, "真名知晓" → Biết Tên Thật.
- Thuật ngữ: "神职权柄" → quyền năng thần chức, "神力" → thần lực, "神谕" → thần dụ, "传教" → truyền giáo.
- "马甲" → vỏ bọc/thân phận giả. "外神" → ngoại thần.
- KHÔNG để sót chữ Hán/CJK trong bản dịch, trừ tên riêng được phép.
- KHÔNG tóm tắt thay cho dịch.
- KHÔNG thêm bình luận ngoài truyện.
- TIÊU ĐỀ CHƯƠNG phải dịch sang tiếng Việt: "第11章 神力的限制" → "Chương 11: Giới hạn của thần lực"
  -> Dùng title này cho filename.

## Characters
- Norven (诺文): nhân vật chính, xuyên không thành thần/tà thần tri thức
- Pete Chinar (培特·奇纳尔): học viên trường phái Huyền thuật Học viện Carone
- Bahamut (巴哈姆特): nhân vật bí ẩn Pete gặp ở đồn cảnh sát
- Cảnh sát mập (胖警员): cảnh sát
- Cảnh sát trưởng Trent (特伦警长): sếp của cảnh sát mập

## Glossary relevant to this chapter
- 【法术反制】: Phản Chế Pháp Thuật (spell)
- 【真名知晓】: Biết Tên Thật (spell)
- 神国: thần quốc
- 神力: thần lực
- 神职权柄: quyền năng thần chức
- 神谕: thần dụ
- 传教: truyền giáo
- 全知之父: Cha Toàn Tri
- 启蒙之主: Chúa Tể Khai Sáng
- 马甲: vỏ bọc
- 外神: ngoại thần
- 信徒: tín đồ
- 霜火高原: Cao Nguyên Sương Lửa (địa danh, dịch nghĩa)
- 格林港: Green Haven (giữ tên gốc Latin)
- 普兰蒂斯大陆: Lục địa Prantis
- 雷亚克王国: Vương quốc Reak
- 卡罗恩学院: Học viện Carone
- 锻锤镇: Thị trấn Rèn Búa
- 迷雾海: Biển Sương Mù
- 幽暗森林: Rừng U Ám

## Previous Story Summary
Norven đã giúp Pete Chinar thoát khỏi hang ổ quái vật dị biến, dạy Pete cách hack Ma lưới để thi triển ma pháp cấp 3. Pete sau đó tỉnh dậy trong đồn cảnh sát, bị thẩm vấn vì bị nhầm là đồng bọn của bọn áo choàng đen. Tại đồn cảnh sát, Pete gặp một người tên Bahamut có hành vi kỳ lạ, và khi vừa rời khỏi phòng thẩm vấn, Bahamut đã biến mất, cảnh sát phủ nhận sự tồn tại của người này. Pete dùng 【Biết Tên Thật】để gọi tên đầy đủ của Bahamut.

## Segments to Translate

Below are the 52 segments. For EACH segment, provide:
- segment_id: giữ nguyên
- source: giữ nguyên
- target: bản dịch tiếng Việt
- notes: (trống hoặc ghi chú nếu cần)

CRITICAL OUTPUT REQUIREMENT:
- Trả về tiêu đề segment 0001 là "Chương 11: Giới hạn của thần lực" (KHÔNG phải "第11章 神力的限制")
- Title này sẽ được dùng làm filename: "Chương 0011 - Giới hạn của thần lực.md"

Return valid JSON only:
```json
{
  "chapter_number": 11,
  "chapter_title": "Chương 11: Giới hạn của thần lực",
  "segments": [
    {
      "segment_id": "0001",
      "source": "# 第11章 神力的限制",
      "target": "Chương 11: Giới hạn của thần lực",
      "notes": ""
    }
  ]
}
```
