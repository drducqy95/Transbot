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
 triển trước rồi tính sổ sau

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

## Chapter 0056 - Chương 56: Chuyên tinh và kiêm tu

### Summary
Chapter 56 completed via pipeline.


## Source Chapter 57 - 0057 修行模拟器已上线！
```json
[
  {
    "segment_id": "0001",
    "text": "# 第57章 修行模拟器已上线！"
  },
  {
    "segment_id": "0002",
    "text": "争论不出结果，战士信徒们最后一致决定，将分歧告知求知之神，由诺文来指引他们选择合适的发展道路。"
  },
  {
    "segment_id": "0003",
    "text": "不过这一次，诺文没有立刻降下对应的神谕给出答案。"
  },
  {
    "segment_id": "0004",
    "text": "早在信徒们尝试用知识点数向诺文兑换更多一阶能够修习的战技时，诺文就已然知晓了凡人战士职业道路的各类战技。"
  },
  {
    "segment_id": "0005",
    "text": "有一点令诺文很是在意。"
  },
  {
    "segment_id": "0006",
    "text": "在收到信徒的诉求后，发动权能，他确实得到了一份关于战士修行道路的“计划”。"
  },
  {
    "segment_id": "0007",
    "text": "从掌控怒气，到各类武器、盾牌、防具的使用，再到各种战技的研习。"
  },
  {
    "segment_id": "0008",
    "text": "这些信息非常的系统而全面。"
  },
  {
    "segment_id": "0009",
    "text": "可以说，只要照着上面的步骤去做，最后都能达到差不多的效果。"
  },
  {
    "segment_id": "0010",
    "text": "问题便在于此："
  },
  {
    "segment_id": "0011",
    "text": "诺文感觉有些怪异，因为这份计划实在太过完美。"
  },
  {
    "segment_id": "0012",
    "text": "完美到甚至不需要凡人去思考。"
  },
  {
    "segment_id": "0013",
    "text": "就仿佛所有的一切都被提前安排好了。"
  },
  {
    "segment_id": "0014",
    "text": "凡人需要做的只有执行的部分。"
  },
  {
    "segment_id": "0015",
    "text": "这是诺文先前发动权柄时没有遇到过的情况。"
  },
  {
    "segment_id": "0016",
    "text": "知识代表真理，真理具有唯一性。"
  },
  {
    "segment_id": "0017",
    "text": "信息代表因果，因果具有逻辑性。"
  },
  {
    "segment_id": "0018",
    "text": "当信徒向诺文祈祷请求获取知识，或者有关某件事物的信息时，诺文可以放心大胆地直接降下神谕。"
  },
  {
    "segment_id": "0019",
    "text": "这些东西的结果都是明确的，不存在其他的可能性。"
  },
  {
    "segment_id": "0020",
    "text": "可是有关职业道路的发展计划不一样。"
  },
  {
    "segment_id": "0021",
    "text": "凡人的选择不同，明明可以引向不同的、全新的发展方向！"
  },
  {
    "segment_id": "0022",
    "text": "但这份计划却将那些未知的可能性完全扼杀。"
  },
  {
    "segment_id": "0023",
    "text": "诺文可以预想到。"
  },
  {
    "segment_id": "0024",
    "text": "如果他将这些信息传达给战士职业的信徒们，他们肯定都会严格按照这份计划去操作。"
  },
  {
    "segment_id": "0025",
    "text": "最后的结果就是会培养出一堆同一个模子里刻出来的战士信徒。"
  },
  {
    "segment_id": "0026",
    "text": "这让诺文感觉有些不对劲。"
  },
  {
    "segment_id": "0027",
    "text": "他获知的战士职业的战技可谓五花八门，光是1阶的主动战技就有十几种，更不用说那些被动生效的战技。"
  },
  {
    "segment_id": "0028",
    "text": "如果真要琢磨搭配的话，光是诺文能想到的组合方式就有6、7种，都有不同的侧重，各有各的优点和缺点。"
  },
  {
    "segment_id": "0029",
    "text": "可是诺文得到的这份计划里，却只用到了其中的几种以形成一种特定流派。"
  },
  {
    "segment_id": "0030",
    "text": "至于其他的？"
  },
  {
    "segment_id": "0031",
    "text": "都被这份计划无情地放弃掉了。"
  },
  {
    "segment_id": "0032",
    "text": "被认为乃是“价值不足、并非最优解”的部分，不值得花费时间精力。"
  },
  {
    "segment_id": "0033",
    "text": "但诺文并不这样认为。"
  },
  {
    "segment_id": "0034",
    "text": "就如同那些战士信徒产生的争执。"
  },
  {
    "segment_id": "0035",
    "text": "布兰登认为战士应该走刚猛输出的路线，学习能够增加双手剑威力的被动战技，以及可以获得更多怒气的【怒气勃发】，如此最大化双手剑【英勇打击】的攻击能力。"
  },
  {
    "segment_id": "0036",
    "text": "但在这份战士修行计划中，却压根没考虑双手剑体系发展的可能性。"
  },
  {
    "segment_id": "0037",
    "text": "给出的方案是剑盾搭配，整体思路偏向于承受攻击的防御向定位。"
  },
  {
    "segment_id": "0038",
    "text": "诺文皱起了眉头。"
  },
  {
    "segment_id": "0039",
    "text": "“最优解的标准是怎么划分的？”"
  },
  {
    "segment_id": "0040",
    "text": "“这份计划……又是怎么制订的呢？”"
  },
  {
    "segment_id": "0041",
    "text": "“布兰登的想法也没什么问题，他也有自己向往的发展方向，为什么却将其判定为价值不足？”"
  },
  {
    "segment_id": "0042",
    "text": "这份“完美的计划”给诺文一种感觉："
  },
  {
    "segment_id": "0043",
    "text": "修行像一份早就被安排好的方案。"
  },
  {
    "segment_id": "0044",
    "text": "凡人不需要思考原因，只要依据神谕执行就好。"
  },
  {
    "segment_id": "0045",
    "text": "对此，连一秒钟都没犹豫，诺文做出的选择很简单："
  },
  {
    "segment_id": "0046",
    "text": "去TM的！"
  },
  {
    "segment_id": "0047",
    "text": "什么狗屁“完美计划”，哪凉快哪待着去！"
  },
  {
    "segment_id": "0048",
    "text": "他有自己的思路，有自己的想法！"
  },
  {
    "segment_id": "0049",
    "text": "诺文决定这次不再依照权柄得到的信息去传达神谕！      他不是自己神职权柄的传声筒，他的信徒也不是只会听从指挥的傀儡。"
  },
  {
    "segment_id": "0050",
    "text": "他现在的身份是一位拥有着无尽伟力的神明，不管正神还是邪神，是诺文在驾驭着他的职能权柄，而不是反过来被自己的权柄所束缚！"
  },
  {
    "segment_id": "0051",
    "text": "诺文要走出自己的道路！"
  },
  {
    "segment_id": "0052",
    "text": "随着信徒的数量增多，通过信徒们的各类诉求，诺文能够得到的信息也越来越多。"
  },
  {
    "segment_id": "0053",
    "text": "这让诺文已经有了一定能力，可以不借助权柄来实现自己目的！"
  },
  {
    "segment_id": "0054",
    "text": "……"
  },
  {
    "segment_id": "0055",
    "text": "地窟中，布兰登收到新的神谕信息。"
  },
  {
    "segment_id": "0056",
    "text": "【目标：1阶战士职业修行】"
  },
  {
    "segment_id": "0057",
    "text": "【建议策略：使用“修行模拟器”（1阶），自行对比各战技搭配加成模拟后效果】"
  },
  {
    "segment_id": "0058",
    "text": "【需求：5知识点数/次】"
  },
  {
    "segment_id": "0059",
    "text": "“哎？这是什么意思？”"
  },
  {
    "segment_id": "0060",
    "text": "在将正义点数差不多兑换成相应的知识点数后，布兰登拥有的点数倒是挺富裕，100多知识点数，够他兑换7、8个一阶战技还能有剩。"
  },
  {
    "segment_id": "0061",
    "text": "试探性地消耗了5知识点数，布兰登旋即得到一个新的提醒；"
  },
  {
    "segment_id": "0062",
    "text": "【请选择希望模拟搭配效果的战技】"
  },
  {
    "segment_id": "0063",
    "text": "【当前可选战技：……】"
  },
  {
    "segment_id": "0064",
    "text": "“我想想，那就【双手剑掌握-基础】，【怒气勃发】，还有【破甲打击】吧？”"
  },
  {
    "segment_id": "0065",
    "text": "布兰登在琳琅满目的一阶战技里选了3个他觉得自己喜欢的。"
  },
  {
    "segment_id": "0066",
    "text": "数秒后，随着“叮”的一声，回应传来。"
  },
  {
    "segment_id": "0067",
    "text": "【自定义模拟方案，已完成】"
  },
  {
    "segment_id": "0068",
    "text": "【预计物理攻击能力提升：24%】"
  },
  {
    "segment_id": "0069",
    "text": "【预计修行时间：41小时】"
  },
  {
    "segment_id": "0070",
    "text": "【推荐传奇等级：15】"
  },
  {
    "segment_id": "0071",
    "text": "布兰登一下子愣住了。"
  },
  {
    "segment_id": "0072",
    "text": "“这……等等，我好像知道是怎么回事了？”"
  },
  {
    "segment_id": "0073",
    "text": "又消耗了5个知识点数，再次启动“修行模拟器”，这回，布兰登选择了【双手剑掌握-基础】，【怒气勃发】和【横扫剑术】三个战技。"
  },
  {
    "segment_id": "0074",
    "text": "“叮！”"
  },
  {
    "segment_id": "0075",
    "text": "【自定义模拟方案，已完成】"
  },
  {
    "segment_id": "0076",
    "text": "【预计物理攻击能力提升：29%】"
  },
  {
    "segment_id": "0077",
    "text": "【预计修行时间：37小时】"
  },
  {
    "segment_id": "0078",
    "text": "【推荐传奇等级：13】"
  },
  {
    "segment_id": "0079",
    "text": "布兰登嘶的一声吸了口气！"
  },
  {
    "segment_id": "0080",
    "text": "“求知之神在上啊！”"
  },
  {
    "segment_id": "0081",
    "text": "“我明白了！”"
  },
  {
    "segment_id": "0082",
    "text": "这个“修行模拟器”的功能并不复杂，简单的两次尝试，布兰登已经搞清楚了它的具体效果。"
  },
  {
    "segment_id": "0083",
    "text": "可以让他提前测试出各种战技搭配后效果！"
  },
  {
    "segment_id": "0084",
    "text": "两次模拟过后，布兰登甚至有点上头，还想再多试几次！"
  },
  {
    "segment_id": "0085",
    "text": "毕竟光是他现在可选的1阶战技就有那么多种组合。"
  },
  {
    "segment_id": "0086",
    "text": "如果直接兑换出战技，他需要花费大量的时间精力去练习。"
  },
  {
    "segment_id": "0087",
    "text": "完全掌握之后，还得去实战测试，才能得知具体效果。"
  },
  {
    "segment_id": "0088",
    "text": "即使最终结果没有那么理想，他消耗掉的时间精力也没法返还。"
  },
  {
    "segment_id": "0089",
    "text": "但有了这个修行模拟器后就不一样了！"
  },
  {
    "segment_id": "0090",
    "text": "比如刚刚的两次模拟，布兰登就能得知，【横扫剑术】搭配的效果比【破甲打击】要好，而且掌握起来也更加容易！"
  },
  {
    "segment_id": "0091",
    "text": "布兰登完全可以提前将他想研习的战技放进去模拟一番，找到最合他心意，效果最好的那个，再花费知识点数兑换出来！"
  },
  {
    "segment_id": "0092",
    "text": "……"
  }
]
```

## Output Format
CRITICAL INSTRUCTION: You MUST translate the source text EXACTLY paragraph by paragraph, preserving the original order perfectly. DO NOT skip, drop, merge, or reorder any paragraphs. Each paragraph in the source MUST be translated.
Return ONLY valid JSON matching this schema:
{
  "chapter_number": 57,
  "chapter_title_vi": "Chương 57: <Vietnamese title>",
  "segments": [
    {
      "segment_id": "XXXX",
      "source": "...",
      "target": "..."
    }
  ]
}
