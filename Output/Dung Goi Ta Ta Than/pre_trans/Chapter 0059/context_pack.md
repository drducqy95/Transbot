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
eted via pipeline.

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

## Chapter 0058 - Chương 58: Cấp độ huyền thoại

### Summary
Chapter 58 completed via pipeline.


## Source Chapter 59 - 0059 魔法女神，狗都不信
```json
[
  {
    "segment_id": "0001",
    "text": "# 第59章 魔法女神，狗都不信"
  },
  {
    "segment_id": "0002",
    "text": "最先开始兑换自己所需战技、分配各项自由属性的是少女蕾娜。"
  },
  {
    "segment_id": "0003",
    "text": "由她先来试验一下传奇等级提升带来的效果，相当于是给其他信徒们探路。"
  },
  {
    "segment_id": "0004",
    "text": "在种类繁多的潜行者路线技能中，她花费30知识点数，得到了【连击】和【剔骨】这两个战技的相关知识。"
  },
  {
    "segment_id": "0005",
    "text": "【连击】，被动战技，在连续使用消耗暗影能量的战技时，可以在短时间内累计连击层数。"
  },
  {
    "segment_id": "0006",
    "text": "【剔骨】，消耗当前积攒的所有连击层数，对目标造成一次精准的弱点攻击。"
  },
  {
    "segment_id": "0007",
    "text": "简单直接的搭配方式。"
  },
  {
    "segment_id": "0008",
    "text": "蕾娜选择兑换这两个战技知识的原因很简单。"
  },
  {
    "segment_id": "0009",
    "text": "它们的预计练习时间最短，只需要不到10个小时，而且推荐的传奇等级也最低。"
  },
  {
    "segment_id": "0010",
    "text": "虽说有将近3天的时间用来让求知教派的信徒们提升自己、积蓄力量，但蕾娜并没有选择那种要练习30多小时的复杂搭配。"
  },
  {
    "segment_id": "0011",
    "text": "毕竟她现在只是一次探路的尝试，自然是越简单越快越好。"
  },
  {
    "segment_id": "0012",
    "text": "得到相关的知识后，蕾娜查看了下战技的学习要求。"
  },
  {
    "segment_id": "0013",
    "text": "“连击最少需要25敏捷，剔骨除了30敏捷，还需要12体质、14力量，还有12意志的属性需求。”"
  },
  {
    "segment_id": "0014",
    "text": "“伟大的求知之神，请您赐予我智慧与知识，展现奥秘吧。”"
  },
  {
    "segment_id": "0015",
    "text": "吟诵神谕中传下的祷词，蕾娜得到了她自己的传奇等级情况。"
  },
  {
    "segment_id": "0016",
    "text": "【1阶，传奇等级12级】"
  },
  {
    "segment_id": "0017",
    "text": "【体质4，力量4，敏捷13，智力4，精神5，意志7】"
  },
  {
    "segment_id": "0018",
    "text": "【自由属性：36】"
  },
  {
    "segment_id": "0019",
    "text": "蕾娜稍微估算了下。"
  },
  {
    "segment_id": "0020",
    "text": "“想达到这两个战技的学习需求，我的自由属性不够。”"
  },
  {
    "segment_id": "0021",
    "text": "她明白为什么修行模拟器上推荐的传奇等级是14级了。"
  },
  {
    "segment_id": "0022",
    "text": "“各位，在搭配自己想要的组合前，记得注意自己的传奇等级是否能达到推荐，不然的话，可能没法满足相关技能的属性要求。”"
  },
  {
    "segment_id": "0023",
    "text": "蕾娜将前几天消灭血牙帮混混得来的500点传奇经验消耗掉。"
  },
  {
    "segment_id": "0024",
    "text": "传奇等级从12级提升到14级。"
  },
  {
    "segment_id": "0025",
    "text": "纯净神力赐福的效果十分奇特，仿佛有股暖流从额前涌入身体，先是脑海变得更加清明，思绪变得更加流畅，面色也红润起来，紧接着，四肢百骸逐渐坚实。"
  },
  {
    "segment_id": "0026",
    "text": "蕾娜隐约能感觉到，身体正在发生着微妙的变化，以让她能够适应更强的力量。"
  },
  {
    "segment_id": "0027",
    "text": "14级后拥有的42点自由属性依次投入到对应的属性。"
  },
  {
    "segment_id": "0028",
    "text": "符合两个新战技的属性要求后，蕾娜再按照神谕传来的知识进行练习时，效率跟她先前练习【潜行】和【影袭】时候比起来，又快上了一大截！"
  },
  {
    "segment_id": "0029",
    "text": "原本的她只是在按照知识，去技巧性驾驭这些战技。"
  },
  {
    "segment_id": "0030",
    "text": "那个时候的暗影能量愿意被她调动，但充满了惰性，蕾娜需要时时分心去掌控。"
  },
  {
    "segment_id": "0031",
    "text": "当肉体强度达标后再使用战技，顿时有了如臂指使的感觉。"
  },
  {
    "segment_id": "0032",
    "text": "周围环境中的暗影能量这次是在踊跃地主动回应着她的呼唤！"
  },
  {
    "segment_id": "0033",
    "text": "当她尝试再度发动潜行，融入阴影中后，更是感到一阵莫名的亲切感，仿佛暗影之神亲自投下注视一般，被略带清冷的浓郁暗影紧紧包裹。"
  },
  {
    "segment_id": "0034",
    "text": "第一次练习，【连击】的学习进度就被推进了17%！"
  },
  {
    "segment_id": "0035",
    "text": "……"
  },
  {
    "segment_id": "0036",
    "text": "有了蕾娜尝试摸索出的经验，培特这边也开始兑换起他需要的魔法知识。"
  },
  {
    "segment_id": "0037",
    "text": "因为有毕业考核的目标，培特攒下的知识点数没打算向其他信徒那样兑换出成体系的技能组合搭配，而是盯准了3阶魔法【奥术弹幕】。"
  },
  {
    "segment_id": "0038",
    "text": "体系这种东西他可以后面再慢慢学习其他魔法，补上进度。"
  },
  {
    "segment_id": "0039",
    "text": "但卡罗恩学院的毕业考核可是越来越近了。"
  },
  {
    "segment_id": "0040",
    "text": "培特直接砸了150知识点数的“重金”把相关知识给兑换了出来。      【奥术弹幕】作为3阶魔法，其学习需求可比那些一阶技能也苛刻多了。"
  },
  {
    "segment_id": "0041",
    "text": "除了15精神的属性要求，最重要的是，它需要足足75点智力属性！"
  },
  {
    "segment_id": "0042",
    "text": "“伟大的求知之神，请您赐予我智慧与知识，展现奥秘吧。”"
  },
  {
    "segment_id": "0043",
    "text": "【2阶，传奇等级27级】"
  },
  {
    "segment_id": "0044",
    "text": "【体质8，力量6，敏捷6，智力66，精神18，意志7】"
  },
  {
    "segment_id": "0045",
    "text": "【自由属性：0】"
  },
  {
    "segment_id": "0046",
    "text": "看到那个大大的“零”时，培特脸色当场就黑了。"
  },
  {
    "segment_id": "0047",
    "text": "他已经明白自己为什么以前在卡罗恩学院天天向魔法女神祈祷、冥想，结果却怎么努力也没法让女神赐予他3阶魔法【奥术弹幕】了。"
  },
  {
    "segment_id": "0048",
    "text": "【奥术弹幕】需要调动更多的魔网脉络，汇聚足够的奥术能量才能维持完整的法术引导过程。"
  },
  {
    "segment_id": "0049",
    "text": "因此需要施法者有足够的智力属性。"
  },
  {
    "segment_id": "0050",
    "text": "蕾娜和其他求知教派的信徒们，一开始踏上职业者道路的时候是从诺文这里得到的知识，然后加以练习掌握，并没有得到对应那些神明的赐福。"
  },
  {
    "segment_id": "0051",
    "text": "所以他们的传奇等级只有基础的部分，所有的自由属性都还保留着。"
  },
  {
    "segment_id": "0052",
    "text": "想要学习一个新的战技、魔法时。"
  },
  {
    "segment_id": "0053",
    "text": "如果他们属性不够，可以消耗自由属性，请求诺文赐予纯净神力。"
  },
  {
    "segment_id": "0054",
    "text": "将属性加上去，提升对应的肉体强度便是。"
  },
  {
    "segment_id": "0055",
    "text": "培特跟他们不同，他过去是魔法女神的信徒，得到过女神的神力赐福。"
  },
  {
    "segment_id": "0056",
    "text": "换而言之，他的六维属性，也就是肉体强度，在魔法女神赐福的时候已经被分配过了！"
  },
  {
    "segment_id": "0057",
    "text": "他根本没有什么保留的自由属性！"
  },
  {
    "segment_id": "0058",
    "text": "“魔法女神！狗都不信！”"
  },
  {
    "segment_id": "0059",
    "text": "“废我时间！乱我属性！”"
  },
  {
    "segment_id": "0060",
    "text": "“我怎么就没早点遇到求知之神啊！”"
  },
  {
    "segment_id": "0061",
    "text": "培特现在的感觉就是后悔，非常后悔。"
  },
  {
    "segment_id": "0062",
    "text": "虽然兑换了3阶魔法，但是——属性不够！"
  },
  {
    "segment_id": "0063",
    "text": "至于消耗传奇经验升级？"
  },
  {
    "segment_id": "0064",
    "text": "培特看了眼他的升级需求，顿时心凉了。"
  },
  {
    "segment_id": "0065",
    "text": "【升级需求：7000传奇经验】"
  },
  {
    "segment_id": "0066",
    "text": "他跟蕾娜不一样。"
  },
  {
    "segment_id": "0067",
    "text": "1阶阶段，传奇等级提高1级，还是以百为单位。"
  },
  {
    "segment_id": "0068",
    "text": "从12级提升到14级，只需要200+300，也就是500传奇经验。"
  },
  {
    "segment_id": "0069",
    "text": "但是像培特这样的2阶法师，他想提升等级，经验要求就变成了千为单位！"
  },
  {
    "segment_id": "0070",
    "text": "虽然靠着打击血牙帮混混，培特现在也有1000多点传奇经验，但比起这庞大的升级需求，根本就是杯水车薪。"
  },
  {
    "segment_id": "0071",
    "text": "掌握【奥术弹幕】，需要75智力。"
  },
  {
    "segment_id": "0072",
    "text": "拥有75智力属性，最少还需要提升3级！"
  },
  {
    "segment_id": "0073",
    "text": "合起来那可是足足24000传奇经验！"
  },
  {
    "segment_id": "0074",
    "text": "传奇经验从哪里来？"
  },
  {
    "segment_id": "0075",
    "text": "击败消灭那些血牙帮的家伙。"
  },
  {
    "segment_id": "0076",
    "text": "想到这里，培特差一点就按捺不住他躁动的心情。"
  },
  {
    "segment_id": "0077",
    "text": "要不是他一个人打不过，他恨不得立马就出去跟血牙帮爆了！"
  },
  {
    "segment_id": "0078",
    "text": "“拜托了，诸位！抓紧时间，赶快修行！”"
  },
  {
    "segment_id": "0079",
    "text": "“我等不及要出去跟投靠邪神的血牙帮决一死战了！！！”"
  },
  {
    "segment_id": "0080",
    "text": "……"
  },
  {
    "segment_id": "0081",
    "text": "PS：修改了58章，有关传奇等级提升获得属性的数值机制，以现在的版本为准，抱歉。"
  }
]
```

## Output Format
CRITICAL INSTRUCTION: You MUST translate the source text EXACTLY paragraph by paragraph, preserving the original order perfectly. DO NOT skip, drop, merge, or reorder any paragraphs. Each paragraph in the source MUST be translated.
Return ONLY valid JSON matching this schema:
{
  "chapter_number": 59,
  "chapter_title_vi": "Chương 59: <Vietnamese title>",
  "segments": [
    {
      "segment_id": "XXXX",
      "source": "...",
      "target": "..."
    }
  ]
}
