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
 cảnh tượng này biết không thể giải quyết dễ dàng
- Có Thần Tri Thức làm chỗ dựa, Pete quyết tâm phát triển trước rồi tính sổ sau

## Chapter 0033 - Chương 33: Lộ trình Chiến Sĩ

### Summary
Chapter 33 completed via pipeline.

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


## Source Chapter 56 - 0056 专精与兼修
```json
[
  {
    "segment_id": "0001",
    "text": "# 第56章 专精与兼修"
  },
  {
    "segment_id": "0002",
    "text": "事实证明，人的底线一旦被打破，滑坡速度飞快。"
  },
  {
    "segment_id": "0003",
    "text": "求知教派的信徒们不仅胆子大，动手能力也强的可怕。"
  },
  {
    "segment_id": "0004",
    "text": "围着地窟中的祭坛一边讨论着，一边就有人上手尝试着从上面掰点儿什么下来。"
  },
  {
    "segment_id": "0005",
    "text": "“咔嚓。”"
  },
  {
    "segment_id": "0006",
    "text": "土质的祭坛并不怎么结实。"
  },
  {
    "segment_id": "0007",
    "text": "一块雕刻成可怖魔物面孔的塑像被咔得一下掰掉了半个脑袋。"
  },
  {
    "segment_id": "0008",
    "text": "“就这？”"
  },
  {
    "segment_id": "0009",
    "text": "“这邪神的祭坛看着也不怎么危险啊！”"
  },
  {
    "segment_id": "0010",
    "text": "这帮求知教派的信徒现在对邪神眷属的理解，就是那群血牙帮的混混。"
  },
  {
    "segment_id": "0011",
    "text": "刚开始还会因为对邪神的固有印象而有些害怕。"
  },
  {
    "segment_id": "0012",
    "text": "现在嘛。"
  },
  {
    "segment_id": "0013",
    "text": "打得多了，根本不带怕的。"
  },
  {
    "segment_id": "0014",
    "text": "还有人倒反天罡，开始嫌弃落单的血牙帮不够多，拿不到足够的正义点数和传奇经验。"
  },
  {
    "segment_id": "0015",
    "text": "有几个思维跳脱的信徒，甚至好奇地盯着祭坛，产生了大胆的想法："
  },
  {
    "segment_id": "0016",
    "text": "“如果我们用这个祭坛人为的制造魔物出来，然后立马消灭掉，能不能得到传奇经验啊？”"
  },
  {
    "segment_id": "0017",
    "text": "“我们又不是邪神的信徒，怎么制造魔物？”"
  },
  {
    "segment_id": "0018",
    "text": "“那还不简单！”"
  },
  {
    "segment_id": "0019",
    "text": "“有求知之神在，你不是暗影之神的信徒也能用出潜行，那同样的道理，只要知道邪神相关的祷词，应该也能让邪神回应吧？”"
  },
  {
    "segment_id": "0020",
    "text": "培特在旁边听得脸色发黑。"
  },
  {
    "segment_id": "0021",
    "text": "再让这帮大胆的家伙思维发散下去，求知教派怕是真的要成信仰邪神的异端教会了！"
  },
  {
    "segment_id": "0022",
    "text": "赶紧清了清嗓子，吸引了地窟中众人的注意。"
  },
  {
    "segment_id": "0023",
    "text": "“别惦记那个祭坛了，我们还有正事要做！”"
  },
  {
    "segment_id": "0024",
    "text": "……"
  },
  {
    "segment_id": "0025",
    "text": "正义点数的兑换比例被临时调高到5:1，意味着所有参与打击血牙帮活动的信徒们可以获得的知识点数直接翻倍。"
  },
  {
    "segment_id": "0026",
    "text": "不过，拿到知识点数，具体兑换成哪些知识，这无疑是个需要谨慎考虑的问题。"
  },
  {
    "segment_id": "0027",
    "text": "无论战士、法师，还是潜行者、牧师、游侠。"
  },
  {
    "segment_id": "0028",
    "text": "每条职业道路都有种类繁多的内容。"
  },
  {
    "segment_id": "0029",
    "text": "起步阶段，大家入门的部分基本一致。"
  },
  {
    "segment_id": "0030",
    "text": "以法师为例。"
  },
  {
    "segment_id": "0031",
    "text": "如果从未接触过魔法，首先需要花费3个知识点数得到调动魔网的相关知识。"
  },
  {
    "segment_id": "0032",
    "text": "练习完成后，再花费15知识点数，根据得到的知识，开始尝试第一个1阶魔法【奥术飞弹】。"
  },
  {
    "segment_id": "0033",
    "text": "至于后续的知识兑换，存在着不同的路线。"
  },
  {
    "segment_id": "0034",
    "text": "有【寒冷射线】、【火焰冲击】之类的攻击魔法，以及【造水术】、【油腻术】、【蛛网术】、【羽落术】之类的生活魔法。"
  },
  {
    "segment_id": "0035",
    "text": "除此之外，还有诸如【奥术亲和】、【冰霜亲和】、【火焰亲和】之类能够长期存在、可以改变自身状态的“加成魔法”。"
  },
  {
    "segment_id": "0036",
    "text": "重点在于，这些“加成魔法”之间的使用效果可能是互斥的。"
  },
  {
    "segment_id": "0037",
    "text": "比如，一位法师给自己加持了【奥术亲和】状态，那他就不能再令自己获得【冰霜亲和】的魔法状态。"
  },
  {
    "segment_id": "0038",
    "text": "强行施加的话，会导致前一个魔法状态消散。"
  },
  {
    "segment_id": "0039",
    "text": "为了最大化利用这些加成魔法的效果。"
  },
  {
    "segment_id": "0040",
    "text": "法师职业者们衍生出了不同的流派。"
  },
  {
    "segment_id": "0041",
    "text": "尽量将有限的精力投入到与流派相关的魔法，这种策略被称之为“专精”。      即，专精于某个类型的魔法。"
  },
  {
    "segment_id": "0042",
    "text": "培特和盖尔都是卡罗恩学院奥法学派的学员，他们两个学习的流派便是“奥术亲和”路线。"
  },
  {
    "segment_id": "0043",
    "text": "如果能顺利毕业的话，他们的3阶法师证明上也会写明，他们属于“奥术法师”。"
  },
  {
    "segment_id": "0044",
    "text": "下城区这些被传教拉进求知教派的信徒，过去都是些普通人，对魔法的种类不怎么了解。"
  },
  {
    "segment_id": "0045",
    "text": "受到培特影响，绝大部分都选择了【奥术飞弹】作为自己的第一个1阶魔法。"
  },
  {
    "segment_id": "0046",
    "text": "“如果各位打算继续选择奥术路线，我的建议是，优先将知识点数用来兑换【奥术亲和】和【节能施法（1阶）】这两个加成魔法。”培特向其他法师信徒们科普。"
  },
  {
    "segment_id": "0047",
    "text": "“奥术亲和可以小幅度增加奥术系魔法的威力。”"
  },
  {
    "segment_id": "0048",
    "text": "“节能施法（1阶）则是在释放1阶奥术魔法时，有一定概率得到魔网馈赠，补充消耗的法术位……哦，不对，是消耗的精神力。”"
  },
  {
    "segment_id": "0049",
    "text": "“即使是后面尝试学习掌控高阶的奥术魔法，这些加成魔法也可以继续发挥作用。”"
  },
  {
    "segment_id": "0050",
    "text": "这些加成魔法都是培特以前在卡罗恩学院的课上听说过的。"
  },
  {
    "segment_id": "0051",
    "text": "跟攻击魔法一样，虽然他懂该怎么选择合适的魔法，可以前怎么向魔法女神祈祷都得不到回应。"
  },
  {
    "segment_id": "0052",
    "text": "现在就不一样了。"
  },
  {
    "segment_id": "0053",
    "text": "有求知之神罩着，只要知识点数够，他想学哪个就能学哪个！"
  },
  {
    "segment_id": "0054",
    "text": "有人提出疑问："
  },
  {
    "segment_id": "0055",
    "text": "“那如果我还想试试引动火焰或凝结寒冰的魔法，我就不能把他们都学了，然后想用哪个用哪个嘛？”"
  },
  {
    "segment_id": "0056",
    "text": "培特耸了耸肩，淡定的解释道：“可以是肯定可以的。”"
  },
  {
    "segment_id": "0057",
    "text": "“事实上，有不少人都有类似你这样的想法。”"
  },
  {
    "segment_id": "0058",
    "text": "“只不过，对那些信仰魔法女神的法师来说，这意味着要花费更多的努力去祈求女神赐福相应的法术，修行难度会大幅度增加。”"
  },
  {
    "segment_id": "0059",
    "text": "“即使是在求知教派，虽然学习魔法不用再看魔法女神的脸色。”"
  },
  {
    "segment_id": "0060",
    "text": "“但兑换相应知识需要知识点数吧？”"
  },
  {
    "segment_id": "0061",
    "text": "“将一个魔法练习到能够熟练施展需要时间精力吧？”"
  },
  {
    "segment_id": "0062",
    "text": "“兼修虽然能力更加全面，但想达到跟同阶专精某流派法师差不多的效果，那就需要付出更多的努力，更长的时间。”"
  },
  {
    "segment_id": "0063",
    "text": "“可能你还没追上人家，说不定对方已经晋升到下个阶段了。”"
  },
  {
    "segment_id": "0064",
    "text": "“具体是要专精还是兼修，取决于自己的选择。”"
  },
  {
    "segment_id": "0065",
    "text": "地窟另一边，布兰登为首的十几名战士职业的信徒也在激烈讨论着。"
  },
  {
    "segment_id": "0066",
    "text": "“要我说，就该先兑换这个【双手剑掌握-基础】，然后再兑换一个【怒气勃发】，这样就能打出更多威力更大的【英勇打击】。”"
  },
  {
    "segment_id": "0067",
    "text": "布兰登对剑类武器，尤其是双手剑情有独钟。"
  },
  {
    "segment_id": "0068",
    "text": "虽然还没找到趁手的武器，这两天一直用着他在滚滚螺栓工坊偷拿的撬棍，但总惦记着要找把适合自己的双手大剑。"
  },
  {
    "segment_id": "0069",
    "text": "另一名战士信徒反驳。"
  },
  {
    "segment_id": "0070",
    "text": "“我觉得布兰登的思路不对！”"
  },
  {
    "segment_id": "0071",
    "text": "“我们这种近身作战的打法，应该侧重于尽可能少受伤，我建议兑换【盾牌掌握-基础】和【盾牌格挡】这两个战技的知识！”"
  },
  {
    "segment_id": "0072",
    "text": "“能扛得住最重要！”"
  },
  {
    "segment_id": "0073",
    "text": "“不然万一上去就被对方撂倒了，哪里有机会用什么英勇打击。”"
  },
  {
    "segment_id": "0074",
    "text": "又一人反驳："
  },
  {
    "segment_id": "0075",
    "text": "“我觉得你们都不对，应该兑换【盾牌掌握-基础】和【怒气勃发】，能抗又能打才是王道！”"
  },
  {
    "segment_id": "0076",
    "text": "可以兑换的知识种类实在太多，战士这边又不像法师，有培特那种接受了成体系教学，可以指点思路的领路者。"
  },
  {
    "segment_id": "0077",
    "text": "以至于，一时之间谁也说服不了谁。"
  },
  {
    "segment_id": "0078",
    "text": "……"
  },
  {
    "segment_id": "0079",
    "text": "感谢书友20170130193406151投出的1张月票，感谢各位投推荐票的书友，谢谢支持！另，新书期如果可以的话，求个追读（指读完最新章节），蟹蟹~"
  },
  {
    "segment_id": "0080",
    "text": "PS：另稍作解释，求知教派职业体系魔改自WOW，如有雷同，不是巧合"
  }
]
```

## Output Format
CRITICAL INSTRUCTION: You MUST translate the source text EXACTLY paragraph by paragraph, preserving the original order perfectly. DO NOT skip, drop, merge, or reorder any paragraphs. Each paragraph in the source MUST be translated.
Return ONLY valid JSON matching this schema:
{
  "chapter_number": 56,
  "chapter_title_vi": "Chương 56: <Vietnamese title>",
  "segments": [
    {
      "segment_id": "XXXX",
      "source": "...",
      "target": "..."
    }
  ]
}
