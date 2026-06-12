# Translation Context Pack

## Project
- Branch: Dung Goi Ta Ta Than
- Title: 
- Author: 
- Genre: /
- Language: zh → vi

## Translation Rules
### Translation Goal
Dịch truyện Trung sang tiếng Việt tự nhiên, dễ đọc, đúng nghĩa, đúng mạch truyện, đúng văn cảnh, đúng xưng hô, đúng tên riêng và thuật ngữ.
Style: văn xuôi tiếng Việt mượt, rõ nghĩa, không máy móc
Priorities:
  • đúng nghĩa và đúng văn cảnh
  • đúng tên riêng
  • đúng thuật ngữ theo loại và bối cảnh
  • đúng xưng hô và quan hệ nhân vật
  • giữ ổn định thuật ngữ/tên riêng/xưng hô đã khóa
  • tự nhiên trong tiếng Việt
  • giữ nhịp văn, cảm xúc và giọng kể gốc
Anti-goals:
  • không dịch từng chữ máy móc
  • không Hán Việt hóa tên Nhật, Hàn, phương Tây, fandom, thương hiệu, kỹ thuật
  • không áp VietPhrase/LuatNhan lên tên riêng đã khóa
  • không đổi thuật ngữ đã khóa nếu văn cảnh giống nhau
  • không dùng một bản dịch cứng cho từ đa nghĩa khi văn cảnh khác nhau
  • không làm lộ thông tin ngoài POV nếu bản gốc chưa tiết lộ

### Output Rules
  • keep paragraph structure
  • keep dialogue structure
  • do not merge paragraphs
  • do not split paragraphs unnecessarily
  • preserve punctuation when reasonable
  • convert chinese quotes to vietnamese
  • remove unnecessary explanation
  • output only translation
  • do not add notes inside translation
  • mark uncertain items for audit only

### Tone Guidelines
  • narration: tự nhiên, rõ ràng, có chất truyện
  • dialogue: phù hợp thân phận, quan hệ, tuổi tác, quyền lực và bối cảnh
  • ancient_setting: cổ phong vừa phải, không lạm dụng Hán Việt khó hiểu
  • modern_setting: hiện đại, đời thường, không cổ hóa lời thoại
  • game_system: rõ ràng, gọn, quen thuộc với văn phong game/system
  • comedy: giữ nhịp hài nếu có
  • serious: giữ sắc thái căng thẳng, trang trọng nếu có

### Term Normalization
Purpose: Chuẩn hóa thuật ngữ theo văn cảnh truyện, bao gồm chiêu thức, nghề nghiệp, chức vị, cảnh giới, kỹ năng, vật phẩm, danh hiệu, tổ chức, hệ thống, khái niệm thế giới quan và cụm cố định lặp lại.
Core principles:
  • context first
  • not word by word
  • same source can have different translation if context differs
  • same source same context must be consistent
  • same term type should keep style consistent
  • locked translation only applies to matching context
  • source plus type plus context equals translation
Decision rules:
  • Không dịch thuật ngữ chỉ theo mặt chữ.
  • Một source có thể có nhiều bản dịch nếu văn cảnh khác nhau.
  • Một bản dịch đã khóa chỉ áp dụng cho đúng loại văn cảnh đã khóa.
  • Tên chiêu thức, cảnh giới, pháp bảo quan trọng nên dùng dạng Hán Việt chuẩn, viết hoa nếu là danh từ riêng.
  • Vật phẩm phổ thông không cần Hán Việt hóa quá mức.
  • Nghề nghiệp phải xét bối cảnh.
  • Chức vị phải xét hệ thống xã hội.
  • Nếu cùng source và cùng văn cảnh, phải giữ nhất quán.
  • Nếu không chắc văn cảnh, đánh dấu audit.

### Engine Rules
  • use context pack
  • use previous chapter summary
  • use character profile
  • use story timeline
  • use glossary
  • use name scan
  • use segment context
  • avoid over literal translation
  • avoid over smoothing that changes meaning

## Characters

- Norven: nhân vật chính, xuyên không thành thần/tà thần trong thế giới fantasy.


## Chương 3
- Pete Chinar (培特·奇纳尔): học viên trường phái Huyền thuật Học viện Caroen, trình độ thấp, thiếu tương thích với Nữ thần Ma pháp.
- Người áo choàng đen (黑袍人): kẻ môi giới lừa Pete vào ổ dị biến.
- Nữ thần Ma pháp (魔法女神): vị thần ma pháp trong thế giới.
- Học viện Caroen (卡罗恩学院): học viện ma pháp nơi Pete theo học.

## Chương 12
- Lena Monia (蕾娜·莫妮娅): thiếu nữ khoảng 18-20 tuổi, tóc nâu dài, mắt xanh, con gái chủ quán rượu ở Green Port. Người Vương quốc Rayak, sinh ra ở thủ đô Starosh. Là tín đồ của Thần Huy Quang. Một trong những người sống sót được Pete cứu trong hang ổ dị biến.
- Vương quốc Rayak (雷亚克王国): vương quốc nơi Pete và Lena sinh sống.
- Thủ đô Starosh (斯塔罗什): thủ đô Vương quốc Rayak.
- Cha của Pete (奇纳尔先生): Nam tước nhỏ của Vương quốc Rayak.
- Thần Huy Quang / Chúa Tể Huy Quang (辉光之主/辉光之神): thần chính của Vương quốc Rayak, tín ngưỡng phổ biến nhất vương quốc.
- Caroen Lever (卡罗恩·拉杆): đại tài phiệt tinh linh, người sáng lập Học viện Caroen và Cảng Green, giàu có bậc nhất Lục địa Prantis.

## Chương 13
- Green Port (格林港): thành phố cảng tự do, trung tâm thương mại Lục địa Prantis, do Caroen Lever sáng lập và khống chế.
- Khu Hạ Thành (下城区): khu vực cảng của Green Port, nơi tập trung lao động bình dân.
- Khu Thượng Thành (上城区): khu vực cao của Green Port, nơi ở của tầng lớp thượng lưu.
- Chợ Mậu Dịch (贸易集市): khu chợ đường dài phân cách giữa Thượng Thành và Hạ Thành.
- Hoang Nguyên Chạng Vạng (暮色荒原): vùng đồng hoang giữa Vương quốc Rayak và Green Port, nguy hiểm, có ma vật ẩn nấp.
- Rừng U Ám (幽暗森林): khu rừng tăm tối phía đông, tỏa khí tức âm trầm ra Hoang Nguyên Chạng Vạng.
- Quán rượu Moni Brotherhood (莫尼兄弟酒馆): quán rượu của gia đình Lena ở Khu Hạ Thành, Green Port.
- Rayak Court Arcane Academy (雷亚克宫廷奥法学院): học viện ma pháp danh giá tại Vương quốc Rayak, khó đỗ hơn Học viện Caroen.


## Glossary

- Thần quốc: không gian nơi thần minh ngự trị.
- 【Mắt Thần】: quyền năng quan sát phàm giới qua tín đồ.
- Cha Toàn Tri / Chúa Tể Khai Sáng: thần danh mà tín đồ tà giáo dùng để gọi Norven.
- Hada: nguồn/sức mạnh được nhóm áo choàng đen cầu xin.
- 【Cơn Đói Khát của Hada】: ma pháp mạnh được thi triển bằng mô hình thuật pháp; lời cầu xin của nhóm áo choàng đen.
- Quyền năng thần chức: quyền năng gắn với thần chức của thần linh; với Norven là tri thức và khai sáng nhưng có lẫn khí tức hỗn loạn.
- Thể dị biến/quái vật dị biến: trạng thái phàm nhân bị thần lực hỗn loạn của Norven làm biến dạng, mất lý trí.
- Pete Chinar: nhân vật mới, học viên ma pháp.
- Người áo choàng đen: kẻ môi giới lừa người đến ổ dị biến.
- Nữ thần Ma pháp: vị thần ma pháp trong thế giới.
- Học viện Caroen: học viện ma pháp.
- Trường phái Huyền thuật: phân khoa tại Học viện Caroen.
- 【Cơn Đói Khát của Hada】: ma pháp cấp ba mà Norven ban cho Pete.
- Quái vật dị biến thần nghiệt: quái vật do thần lực hỗn loạn tạo ra.
- Quái vật dị biến: quái vật biến dạng do thần lực hỗn loạn.
- Cấp một/cấp hai/cấp ba: hệ thống phân cấp thực lực trong thế giới.
- Ma Võng: mạng lưới ma pháp do Nữ thần Ma pháp quản lý.
- 【Khóa Bí Thuật】: ma pháp cấp hai loại phụ trợ.
- 【Dò Tìm Ý Nghĩ】: ma pháp cấp hai loại phụ trợ.
- 【Thuật Mạng Nhện】: ma pháp loại hạn chế.
- Mức độ tương thích (affinity): mức độ hòa hợp giữa tín đồ và thần.
- Quyền năng: năng lực đặc thù của thần minh.
| Ma Võng | Ma Võng | thuật ngữ | Mạng lưới ma pháp/kết nối ma thuật, không dịch là Ma Lưới |

- Chúa Tể Huy Quang / Thần Huy Quang / Giáo Hội Huy Quang (辉光之主/辉光之神/辉光神教): thần chính của Vương quốc Rayak, tín ngưỡng phổ biến nhất, mang bối cảnh phương Tây (tương tự thần Ánh Sáng/thần Mặt Trời).
- Tín đồ chân chính (真信徒): tín đồ tuân thủ nghiêm ngặt giáo lý và giới luật của thần, khác với tín đồ nông cạn có thể tin hoặc bỏ bất cứ lúc nào.
- Học viện Huyền thuật Hoàng gia Rayak (雷亚克宫廷奥法学院): học viện ma pháp danh giá của Vương quốc Rayak, khó đỗ hơn Học viện Caroen.
- Thuế quyền thừa kế (继承权利税金): thuế mà người thừa kế phải nộp cho quốc vương để giữ tước vị.

| Caroen Lever (卡罗恩·拉杆) | Caroen Lever | nhân vật | Đại tài phiệt tinh linh, người sáng lập Học viện Caroen và Cảng Green. Latin chuẩn, không dịch một phần. |
| Học viện Caroen | Học viện Caroen | tổ chức | Học viện ma pháp tại Cảng Green, do Caroen Lever sáng lập. |

## Chương 13
| Hí pháp (戏法) | Hí pháp | kỹ năng | Ma pháp đơn giản, không tiêu hao Pháp thuật vị, có thể thi triển bất cứ lúc nào khi kết nối được Ma Võng. |
| Tịnh Tức Thuật (净息术) | Tịnh Tức Thuật | kỹ năng | Hí pháp tạo màng lọc mũi, lọc mùi. |
| Thanh Khiết Thuật (清洁术) | Thanh Khiết Thuật | kỹ năng | Hí pháp làm sạch. |
| Vũ Quang Thuật (舞光术) | Vũ Quang Thuật | kỹ năng | Hí pháp tạo ánh sáng nhảy múa. |
| Pháp thuật cấp 1 (1阶法术) | Pháp thuật cấp 1 | hệ thống | Cấp bậc thấp nhất trong hệ thống phân cấp pháp thuật. |
| Độ tương thích ma pháp (魔法亲和度) | độ tương thích | hệ thống | Mức độ hòa hợp giữa cá nhân và Nữ thần Ma pháp, quyết định khả năng thi triển pháp thuật. |
| Pháp thuật vị (法术位) | Pháp thuật vị | hệ thống | Quy tắc: tín đồ Nữ thần Ma pháp cầu nguyện và thiền định từ hôm trước để nhận số lần dùng pháp thuật cho hôm sau. |
| Người thi triển pháp thuật (施法者) | Thi Pháp Giả | nghề nghiệp | Người có khả năng sử dụng pháp thuật thông qua Ma Võng. |
| Chức nghiệp giả (职业者) | Chức nghiệp giả | nghề nghiệp | Người hành nghề chuyên nghiệp, có chứng nhận trong thế giới. |
| Đại Pháp Sư (大法师) | Đại Pháp Sư | nghề nghiệp | Pháp sư cấp cao mạnh mẽ. |
| Ma pháp học đồ (魔法学徒) | ma pháp học đồ | nghề nghiệp | Người mới học ma pháp, còn ở giai đoạn căn bản. |

| 施法者 (Thi Pháp Giả) | Thi Pháp Giả | nghề nghiệp | Người thi triển pháp thuật. Viết hoa Hán Việt. |

## Story Timeline (latest)
ia pipeline.

## Chapter 0034 - Chương 34: Những hạt giống đầu tiên

### Summary
Chapter 34 completed via pipeline.

## Chapter 0035 - Chương 35: Xưởng Bu-lông Lăn Tròn

### Summary
Chapter 35 completed via pipeline.

## Chapter 0036 - 0036 你知道的，我嘴巴最严实了

### Summary
Chapter 36 completed via pipeline.

## Chapter 0037 - Chương 37: Cách dùng mới của Điểm Tri Thức

### Summary
Chapter 37 completed via pipeline.

## Chapter 0033 - Chương 33: Lộ trình Chiến Sĩ

### Summary
Chapter 33 completed via pipeline.

## Chapter 0034 - Chương 34: Những hạt giống đầu tiên

### Summary
Chapter 34 completed via pipeline.

## Chapter 0035 - Chương 35: Xưởng Bu-lông Lăn Tròn

### Summary
Chapter 35 completed via pipeline.

## Chapter 0036 - Chương 36: Cậu biết mà, tôi kín miệng lắm

### Summary
Chapter 36 completed via pipeline.

## Chapter 0037 - Chương 37: Cách dùng mới của Điểm Tri Thức

### Summary
Chapter 37 completed via pipeline.

## Chapter 0038 - Chương 38: Norven: Ta thật sự không muốn làm tà thần

### Summary
Chapter 38 completed via pipeline.

## Chapter 0039 - Chương 39: Desley

### Summary
Chapter 39 completed via pipeline.

## Chapter 0040 - Chương 40: Thông báo giáo phái

### Summary
Chapter 40 completed via pipeline.

## Chapter 0041 - Chương 41: Bắt đầu sự kiện giới hạn

### Summary
Chapter 41 completed via pipeline.

## Chapter 0042 - Chương 42: Đụng trúng họng súng rồi

### Summary
Chapter 42 completed via pipeline.

## Chapter 0043 - Chương 43: Tình hình hoàn toàn khác so với dự đoán

### Summary
Chapter 43 completed via pipeline.

## Chapter 0044 - Chương 44: Dụ địch vào sâu!

### Summary
Chapter 44 completed via pipeline.

## Chapter 0045 - Chương 45: Ỷ đông hiếp yếu

### Summary
Chapter 45 completed via pipeline.

## Chapter 0046 - Chương 46: Kỹ năng sự kiện

### Summary
Chapter 46 completed via pipeline.

## Chapter 0047 - Chương 47: Giáo Hội Huy Quang không đáng tin cậy

### Summary
Chapter 47 completed via pipeline.

## Chapter 0048 - Chương 48: Mạnh tay hơn nữa

### Summary
Chapter 48 completed via pipeline.

## Chapter 0049 - Chương 49: Cơ hội tuyệt hảo

### Summary
Chapter 49 completed via pipeline.

## Chapter 0050 - Chương 50: Chức nghiệp đắt khách nhất

### Summary
Chapter 50 completed via pipeline.

## Chapter 0051 - Chương 51: Trổ hết thần thông

### Summary
Chapter 51 completed via pipeline.

## Chapter 0052 - Chương 52: Evan: Tay sai của ta đâu?

### Summary
Chapter 52 completed via pipeline.

## Chapter 0053 - Chương 53: Ý nghĩa đích thực trong giáo lý của Thần Cầu Tri

### Summary
Chapter 53 completed via pipeline.

## Chapter 0054 - Chương 54: Cứ điểm tạm thời

### Summary
Chapter 54 completed via pipeline.

## Chapter 0055 - Chương 55: Tế đàn tà thần? Có thể phá không?

### Summary
Chapter 55 completed via pipeline.

## Chapter 0056 - Chương 56: Chuyên tinh và kiêm tu

### Summary
Chapter 56 completed via pipeline.

## Chapter 0057 - Chương 57: Trình mô phỏng tu hành đã ra mắt!

### Summary
Chapter 57 completed via pipeline.


## Source Chapter 58 - 0058 传奇等级
```json
[
  {
    "segment_id": "0001",
    "text": "# 第58章 传奇等级"
  },
  {
    "segment_id": "0002",
    "text": "有了模拟功能，众人的争论直接被终结。"
  },
  {
    "segment_id": "0003",
    "text": "这还吵什么？"
  },
  {
    "segment_id": "0004",
    "text": "你觉得自己的思路好，那就用“修行模拟器”自己测试一下呗。"
  },
  {
    "segment_id": "0005",
    "text": "搭配出来，提升幅度是最直观也是最有说服力的证据。"
  },
  {
    "segment_id": "0006",
    "text": "随着“修行模拟器”上线，很快，地窟中各个修行职业路线的信徒们纷纷上手自己测试起来。"
  },
  {
    "segment_id": "0007",
    "text": "就连知道成熟的奥术法师专精体系的培特和盖尔俩人，在得知消息后，也忍不住将自己计划的“构筑”放进去测试了一番。"
  },
  {
    "segment_id": "0008",
    "text": "培特和盖尔两个都是2阶法师，因此他们使用的修行模拟器，其效果跟1阶职业者的有些许区别。"
  },
  {
    "segment_id": "0009",
    "text": "每次模拟消耗的知识点数提升到了10点。"
  },
  {
    "segment_id": "0010",
    "text": "当然，可供选择的各种魔法也多出了大量的2阶魔法。"
  },
  {
    "segment_id": "0011",
    "text": "培特将卡罗恩学院传授的奥术法师专精体系应当掌握的7、8个魔法放了进去。"
  },
  {
    "segment_id": "0012",
    "text": "最后模拟显示的结果是："
  },
  {
    "segment_id": "0013",
    "text": "奥术魔法威力会得到68%的提升；"
  },
  {
    "segment_id": "0014",
    "text": "预计需要花费377个小时的时间去学习，他才能将这些魔法全部学会。"
  },
  {
    "segment_id": "0015",
    "text": "培特尝试着替换掉了其中的一、二个魔法。"
  },
  {
    "segment_id": "0016",
    "text": "模拟结果，威力提升立马降低到了55%。"
  },
  {
    "segment_id": "0017",
    "text": "预计花费时间则增长到了459小时。"
  },
  {
    "segment_id": "0018",
    "text": "对于这个结果，培特并不奇怪。"
  },
  {
    "segment_id": "0019",
    "text": "情理之中，意料之内。"
  },
  {
    "segment_id": "0020",
    "text": "卡罗恩学院的奥法学派传授的法师修行路线，可是经过多年研究、调整、优化之后得出来的相对优秀、稳定的魔法搭配方案。"
  },
  {
    "segment_id": "0021",
    "text": "替换掉其中的任何一环，都有可能引起连锁反应。"
  },
  {
    "segment_id": "0022",
    "text": "若是他能找到比传统奥术专精法师更好的魔法搭配方案，经过时间沉淀和验证后，那都算是可以写进教科书里的东西。"
  },
  {
    "segment_id": "0023",
    "text": "不过，培特已经意识到："
  },
  {
    "segment_id": "0024",
    "text": "“修行模拟器”这种东西，如果有实体的话，若是放在其他神明的教会里，保底也是个神器、圣物级别，甚至成为镇教之宝都不为过。"
  },
  {
    "segment_id": "0025",
    "text": "比如公正之神，祂本身的神力并不算强大，信徒也不像那些能成为评级职业者的神明信徒一样拥有超凡的战斗能力，公正之神的神术只是能裁定一位凡人与众多正神的亲和度。"
  },
  {
    "segment_id": "0026",
    "text": "但偏偏就这一个独家神术，便奠定了公正教会的高贵地位。"
  },
  {
    "segment_id": "0027",
    "text": "其他人想成为职业者，为了避免选了不适合自己的神明信仰，唯一的办法就是借助公正之神的神术进行测试。"
  },
  {
    "segment_id": "0028",
    "text": "虽然不能提升实力，但可以确保自己不走歪路。"
  },
  {
    "segment_id": "0029",
    "text": "同样的道理。"
  },
  {
    "segment_id": "0030",
    "text": "表面上看起来，修行模拟器的效果，只是让求知教派的信徒都能找到合适自己的发展路线，无需高阶职业者总结的经验或思路。"
  },
  {
    "segment_id": "0031",
    "text": "理论来说，如果信徒们跟培特和盖尔那样，能得到前人的经验的话，他们即使不用修行模拟器，也能知道该怎么选择合适的技能搭配组合。"
  },
  {
    "segment_id": "0032",
    "text": "关键在于，那些高阶职业者们总结出来的办法，也是他们当初花费了大量的努力，去一点点试错、摸索出来的结果！"
  },
  {
    "segment_id": "0033",
    "text": "效率低，成本高，还没有任何替代方法。"
  },
  {
    "segment_id": "0034",
    "text": "修行模拟器则完全打破了这个困境！"
  },
  {
    "segment_id": "0035",
    "text": "在前人已经走过的地方，修行模拟器的作用的确可以被平替。"
  },
  {
    "segment_id": "0036",
    "text": "但越是靠近未知的领域，模拟的作用就会越大！"
  },
  {
    "segment_id": "0037",
    "text": "虽然现在求知教派还只是一群普遍1阶，刚刚成为职业者的家伙，没法完全发挥出修行模拟器的效果。"
  },
  {
    "segment_id": "0038",
    "text": "但培特已经可以预想到，修行模拟器的意义，只会随着求知教派的发展而越来越重要！"
  },
  {
    "segment_id": "0039",
    "text": "……"
  },
  {
    "segment_id": "0040",
    "text": "另一边，测试完自己想要的几个战技的蕾娜，则注意到了模拟结果中提醒的“推荐传奇等级”。"
  },
  {
    "segment_id": "0041",
    "text": "她选择了一套感觉不错的潜行者技能搭配，但最后建议是14级传奇等级。      通过向诺文祈祷，蕾娜已经得知，她现在的传奇等级为12级。"
  },
  {
    "segment_id": "0042",
    "text": "传奇等级，是先前诺文跟传奇经验一起推出的，用来在求知教派内部完善那套老旧的职业者评级体系的新定义。"
  },
  {
    "segment_id": "0043",
    "text": "这个世界原本的职业者评级很简单。"
  },
  {
    "segment_id": "0044",
    "text": "以牧师为例。"
  },
  {
    "segment_id": "0045",
    "text": "信仰神明，如果能得到辉光之神赐予的祝福和神术，那就可以成为牧师职业者。"
  },
  {
    "segment_id": "0046",
    "text": "赐予的祝福和神术被划分为6个阶段，即1阶到6阶。"
  },
  {
    "segment_id": "0047",
    "text": "6阶之上则为一代传奇。"
  },
  {
    "segment_id": "0048",
    "text": "每次晋升都能得到更强大的赐福，越是向上，晋升便越困难。"
  },
  {
    "segment_id": "0049",
    "text": "两者的获得顺序是："
  },
  {
    "segment_id": "0050",
    "text": "先得到祝福强化肉体。"
  },
  {
    "segment_id": "0051",
    "text": "而后才能得到神术。"
  },
  {
    "segment_id": "0052",
    "text": "是否拥有对应阶段的神术，被作为评定牧师职业者阶位的标准。"
  },
  {
    "segment_id": "0053",
    "text": "可是在诺文这里，这一评级标准明显不太适用！"
  },
  {
    "segment_id": "0054",
    "text": "诺文可以直接将相关知识给予信徒们。"
  },
  {
    "segment_id": "0055",
    "text": "对求知教派的信徒而言，学习高阶的战技或法术不存在障碍，哪怕是一位普通人，只要知识点数够，完全可以兑换出6阶的大型魔法进行学习。"
  },
  {
    "segment_id": "0056",
    "text": "问题在于。"
  },
  {
    "segment_id": "0057",
    "text": "其他神明先赐福肉体强度，而后才会赐下神术是有原因的。"
  },
  {
    "segment_id": "0058",
    "text": "更加强大的技能，需要更好的肉体强度支撑才能正常使用！"
  },
  {
    "segment_id": "0059",
    "text": "否则的话，就会像培特那次强行释放3阶法术【哈达之饥渴】一样，直接把自己的精神力给抽干透支，放完就晕了过去。"
  },
  {
    "segment_id": "0060",
    "text": "求知教派的情况跟那些信仰其他神明，因为没获得赐福而学不到相关法术不同。"
  },
  {
    "segment_id": "0061",
    "text": "诺文的信徒是可以提前学会高阶的能力，却会因为肉体强度不够而没法释放。"
  },
  {
    "segment_id": "0062",
    "text": "为了避免信徒们出现这种学习超过自己能力范围技能的情况，这才有了诺文设计的【传奇等级】体系。"
  },
  {
    "segment_id": "0063",
    "text": "诺文将不同的战技、魔法、神术需求的肉体强度，进行了分类。"
  },
  {
    "segment_id": "0064",
    "text": "体质，力量，智力，敏捷，精神，意志。"
  },
  {
    "segment_id": "0065",
    "text": "共计6类属性，对应着不同的身体强度特性。"
  },
  {
    "segment_id": "0066",
    "text": "信徒们可以消耗他们得到的传奇经验，提升传奇等级。"
  },
  {
    "segment_id": "0067",
    "text": "每次提升等级，都可以获得3点供信徒们自行分配的自由属性，用来强化他们的身体。"
  },
  {
    "segment_id": "0068",
    "text": "更加强大的技能，诺文也根据其相关特性，提供了建议的各项属性数值作为参考。"
  },
  {
    "segment_id": "0069",
    "text": "这相当于提醒信徒们，如果自己实力不到位的话，就别好高骛远去尝试那些高阶的能力。"
  },
  {
    "segment_id": "0070",
    "text": "诺文希望信徒们能自由选择他们想要行走的道路，也希望他们能脚踏实地，从基础开始努力。"
  },
  {
    "segment_id": "0071",
    "text": "只不过。"
  },
  {
    "segment_id": "0072",
    "text": "当“修行模拟器”与“传奇等级”二者结合，却爆发出了连诺文都没想到的奇妙化学反应！"
  },
  {
    "segment_id": "0073",
    "text": "……"
  },
  {
    "segment_id": "0074",
    "text": "感谢恋心C投出的2张月票，感谢 Roy_DB，火腿de，啊这Dc投出的1张月票！万分感谢各位投出推荐票的读者朋友，谢谢你们！"
  },
  {
    "segment_id": "0075",
    "text": "PS：至此，第一卷诺文能力已全部解锁。欢迎加入求知教派，走上人生巅峰。"
  }
]
```

## Output Format
CRITICAL INSTRUCTION: You MUST translate the source text EXACTLY paragraph by paragraph, preserving the original order perfectly. DO NOT skip, drop, merge, or reorder any paragraphs. Each paragraph in the source MUST be translated.
Return ONLY valid JSON matching this schema:
{
  "chapter_number": 58,
  "chapter_title_vi": "Chương 58: <Vietnamese title>",
  "segments": [
    {
      "segment_id": "XXXX",
      "source": "...",
      "target": "..."
    }
  ]
}
