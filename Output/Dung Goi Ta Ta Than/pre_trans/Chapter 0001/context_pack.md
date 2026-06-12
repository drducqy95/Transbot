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

## Chapter 0059 - Chương 59: Nữ thần Ma pháp, chó cũng không thèm tin

### Summary
Chapter 59 completed via pipeline.


## Source Chapter 1 - 0001 穿越成了邪神怎么办
```json
[
  {
    "segment_id": "0001",
    "text": "# 第1章 穿越成了邪神怎么办"
  },
  {
    "segment_id": "0002",
    "text": "一片白茫茫的广袤空间，诺文逐渐恢复了意识。"
  },
  {
    "segment_id": "0003",
    "text": "“我……真的遇到传说中的穿越了？”"
  },
  {
    "segment_id": "0004",
    "text": "诺文还清晰记得他上辈子发生的事情。"
  },
  {
    "segment_id": "0005",
    "text": "一次见义勇为，为了救下即将被卡车撞飞的小男孩，诺文舍身将对方扑飞出去，代价则是自己被送进ICU度过了大半个月。虽然侥幸捡回了一条命，但是却彻底失去了行动能力。"
  },
  {
    "segment_id": "0006",
    "text": "大脑严重受损，加上身体受创导致的中枢神经系统感染，让诺文进入了一种近似于植物人的状态，只剩勉强维持、时断时续的意识。"
  },
  {
    "segment_id": "0007",
    "text": "因为意识都无法连贯，所以诺文也不清楚他究竟在病床上躺了多久，直到有一刻，他依稀“听”到冥冥中传来的声音。"
  },
  {
    "segment_id": "0008",
    "text": "“诺文，要出发吗？”"
  },
  {
    "segment_id": "0009",
    "text": "“什么东西？”诺文忽然发现他的意识变得清醒起来，虽然依然无法控制身体，但是至少能让他恢复思考，听到这声音的时候，他想到传说中的地狱冥河，“该不会真有什么摆渡人要来牵引我去转世投胎了吧？”"
  },
  {
    "segment_id": "0010",
    "text": "“诺文，要出发吗？”"
  },
  {
    "segment_id": "0011",
    "text": "幽远不知从何处传来的声音再度响起。"
  },
  {
    "segment_id": "0012",
    "text": "“出发？不是，我该去哪里啊？这没头没尾的，至少给点提示行吗！”诺文不禁有些急切。"
  },
  {
    "segment_id": "0013",
    "text": "“留下维持现状，或者，另一个世界正在向你发起呼唤。”"
  },
  {
    "segment_id": "0014",
    "text": "“诺文，要出发吗？”"
  },
  {
    "segment_id": "0015",
    "text": "声音第三次响起，不知怎的，诺文有种预感，如果他不做出决定，可能就不会再有机会了。"
  },
  {
    "segment_id": "0016",
    "text": "仅仅只考虑了一秒，诺文便下定了决心。"
  },
  {
    "segment_id": "0017",
    "text": "他在这个世界已经没有什么可留恋的，从小无父无母在孤儿院长大，一人吃饱全家不饿，因为英勇救人而导致余生都可能要在植物人瘫痪状态度过，与其这么苟延残喘下去，不如抓住这不知是何方存在给他提供的机会。"
  },
  {
    "segment_id": "0018",
    "text": "“如果真的能给我第二次生命的机会，那么，当然，出发吧！”"
  },
  {
    "segment_id": "0019",
    "text": "……"
  },
  {
    "segment_id": "0020",
    "text": "诺文尝试着打量他周围的环境，脑海中突然涌现出一段信息。"
  },
  {
    "segment_id": "0021",
    "text": "他所处的地方名为神国，顾名思义，这方空间便是神明所依存的地方，诺文的的确确来到了一个和他原本生活的世界有着完全不同规则的新世界。"
  },
  {
    "segment_id": "0022",
    "text": "这个世界早在文明诞生前便有着所谓的“神明”存在，那些开天辟地，捏土造人之类的神话也并非虚无缥缈的传说，而是有着切实的记载和证据，文明的发展路线也和拥有伟力的众多神明密不可分。"
  },
  {
    "segment_id": "0023",
    "text": "这里的神灵不仅是一种精神寄托，更重要的是，万灵众生通过诚心实意地向神祈祷献上信仰，便有机会得到对应神明的回馈，获得护佑加持，甚至脱离凡俗迈入超凡。"
  },
  {
    "segment_id": "0024",
    "text": "了解了这个世界的发展模式与规律，诺文顿觉惊喜："
  },
  {
    "segment_id": "0025",
    "text": "“好家伙，本以为我拿的是王道勇者冒险升级剧本，原来直接是神明降世幕后布局的设定。”"
  },
  {
    "segment_id": "0026",
    "text": "“不就是收拢信徒，发展教派，然后一步步增强神力，最后制霸众神吗？这我熟啊！”"
  },
  {
    "segment_id": "0027",
    "text": "诺文脑子里瞬间有了一揽子对应的计划，没吃过猪肉还没看过猪跑吗，前世那种只存在于传说的所谓神啊仙啊都能吸引到那么多的信众，何况这个世界的运转规则里，神明是有着实打实的权与力，可以将赐福直接给予信徒。      “让我看看，现在的我有多少信徒？有什么权柄？”"
  },
  {
    "segment_id": "0028",
    "text": "因为瘫痪躺了不知道多久的诺文，此刻拥有“第二次生命”，而且还是神的身份，行动力高到爆棚，瞬间进入角色。"
  },
  {
    "segment_id": "0029",
    "text": "先前那段信息不仅让诺文认识了这个世界的基本规则，同时也让他宛若本能般掌握了神明最基础的权能。"
  },
  {
    "segment_id": "0030",
    "text": "神明很难本体离开神国抵达凡世，需要借助向其献上信仰的万灵作为跳板，通过他们的视角来观察世界，乃至降下神迹。"
  },
  {
    "segment_id": "0031",
    "text": "这种手段被诺文称之为【神之眼】，毫无疑问，他拥有的信徒越多，那自然就会掌握更多的信息来源。"
  },
  {
    "segment_id": "0032",
    "text": "诺文沉下心神，很快便察觉到一道似乎是指向他的祈祷声。"
  },
  {
    "segment_id": "0033",
    "text": "……"
  },
  {
    "segment_id": "0034",
    "text": "阴暗潮湿的地下洞窟，明灭不定的幽绿烛火，还有造型狰狞怪异的祭坛，以及不知是什么动物的肉块骨头内脏血水混杂着堆在一起，再加上几名身披黑袍遮掩身形，看不清面相的鬼祟之徒，正盘坐在祭坛下方，低声吟诵着什么。"
  },
  {
    "segment_id": "0035",
    "text": "这便是诺文睁开【神之眼】视角时，第一眼看到的情况。"
  },
  {
    "segment_id": "0036",
    "text": "“嘶……”"
  },
  {
    "segment_id": "0037",
    "text": "虽然神明形态下的他并没有所谓固定的形体，但诺文还是习惯性地为自己捏塑了人形的外观，因此看到这邪门的一幕时，他当场没忍住吸了口凉气。"
  },
  {
    "segment_id": "0038",
    "text": "“什么情况？！这些玩意……该不会就是我的信徒吧？”"
  },
  {
    "segment_id": "0039",
    "text": "诺文懵逼。"
  },
  {
    "segment_id": "0040",
    "text": "他本以为自己会是个那种传播正义，予以信徒新生的正派主神，结果就眼下这画面看来的话……"
  },
  {
    "segment_id": "0041",
    "text": "“我好像穿越的是个邪神啊妈耶！”"
  },
  {
    "segment_id": "0042",
    "text": "神之眼视角下正在吟诵的几名黑袍人似乎感觉到了诺文投来的“注视”，为首的一人顿时激动起来，宽大的兜帽下响起沙哑低沉的怪声："
  },
  {
    "segment_id": "0043",
    "text": "“很好，非常好……兄弟姐妹们，无上的、至尊的、不灭的、不可名状的全知之父、启蒙之主已经认可了我们献上的祭品……祂正准备赐予我们宝贵的禁忌知识，真实世界即将向我们敞开大门！”"
  },
  {
    "segment_id": "0044",
    "text": "“伟大的主啊！请将哈达的饥渴之力交予我们吧！”"
  },
  {
    "segment_id": "0045",
    "text": "黑袍人的声音愈发高昂，配上其他几人整齐的吟诵，祭坛上还在淌着血水的新鲜不知名动物尸体，让场面变得邪恶非常，整个就一恐怖教派的仪式现场的感觉。"
  },
  {
    "segment_id": "0046",
    "text": "诺文只觉眼前一黑。"
  },
  {
    "segment_id": "0047",
    "text": "确定了，他虽然穿越成了神明没错，但问题在于，这些向他祈祷献上信仰的家伙明显不是什么好东西，要是放在他曾经看过的小说电影里，他少说也得是个那种会被正义的伙伴在冒险路上讨伐消灭的邪神，还得是那种动不动就为非作歹、祸害众生，喜欢躲在阴暗的角落里时不时策划几个意图毁灭世界的计划的大坏种。"
  },
  {
    "segment_id": "0048",
    "text": "“谁能告诉我，我好像穿越成邪神了怎么办啊？？？”"
  },
  {
    "segment_id": "0049",
    "text": "……"
  },
  {
    "segment_id": "0050",
    "text": "兜兜转转，还是回到点娘怀抱，敬请见证。"
  }
]
```

## Output Format
CRITICAL INSTRUCTION: You MUST translate the source text EXACTLY paragraph by paragraph, preserving the original order perfectly. DO NOT skip, drop, merge, or reorder any paragraphs. Each paragraph in the source MUST be translated.
Return ONLY valid JSON matching this schema:
{
  "chapter_number": 1,
  "chapter_title_vi": "Chương 1: <Vietnamese title>",
  "segments": [
    {
      "segment_id": "XXXX",
      "source": "...",
      "target": "..."
    }
  ]
}
