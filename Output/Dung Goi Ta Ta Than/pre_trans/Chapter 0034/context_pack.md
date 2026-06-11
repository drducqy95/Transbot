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
g buộc bởi giáo lý hay mất tiền.
- Cậu theo học tại Học viện Caroen nhưng ba năm vẫn chưa lên cấp ba.
- Lena rủ Pete đến quán rượu nhà mình để tạ ơn.

### Nhân vật xuất hiện
- Pete Chinar (Thi Pháp Giả nhị giai, học viên Học viện Caroen)
- Lena Monia (thiếu nữ sống sót, người Vương quốc Rayak, con gái chủ quán rượu)
- Cha của Pete (Nam tước Chinar, được nhắc đến)
- Thần Huy Quang (được nhắc đến)

### Thuật ngữ xuất hiện
- Người thi triển cấp hai (二阶施法者): cấp bậc ma pháp của Pete
- Chức nghiệp giả cấp ba (3阶职业者): mục tiêu của Pete để thừa kế tước vị
- Giáo Hội Huy Quang (辉光神教): giáo phái lớn nhất Vương quốc Rayak
- Tín đồ chân chính (真信徒): tín đồ tuân thủ nghiêm ngặt giáo lý
- Tín đồ nông cạn (浅信徒): tín đồ có thể tin hoặc bỏ đạo bất cứ lúc nào
- Thuế quyền thừa kế (继承权利税金): thuế duy trì tước vị
- Học viện Huyền thuật Hoàng gia Rayak (雷亚克宫廷奥法学院)
- Học viện Caroen (卡罗恩学院)

### Thay đổi quan trọng cần nhớ
- Lena Monia là tín đồ mới của Pete (người thường không có năng lực ma pháp).
- Pete có động cơ rõ ràng để trở thành chức nghiệp giả cấp ba: thừa kế tước vị.
- Pete học tại Học viện Caroen vì bị Học viện Huyền thuật Hoàng gia từ chối do thiếu tương thích với Nữ thần Ma pháp.

## Chương 26: Cách tu luyện có thể thấy thanh tiến độ
- Norven thiết lập cơ chế Điểm Tri Thức với tỷ lệ 1:1, tận dụng khả năng tái sử dụng tri thức một lần đầu tư → thu hồi vô hạn
- Lena cầu nguyện xin hướng dẫn tu luyện Tiềm Hành Giả, trả 3 Điểm Tri Thức
- Lena tập 【Ẩn Nấp】 lần đầu thất bại nhưng thấy thanh tiến độ 7%, biết nguyên nhân thất bại
- Pete chấn động: Thần Tri Thức có thể vòng qua các chủ thần, ban trực tiếp lộ trình tu luyện có thanh tiến độ

## Chương 29: Chợ Đen
- Pete và Lena đến chợ đen ở Khu Hạ Thành, nơi phát triển từ khu nhà kho bỏ hoang sau vụ địa tinh vận chuyển hàng cấm tà thần
- Chợ đen là nơi tụ tập của đủ loại kẻ giao dịch phi pháp, có người vô gia cư làm bình phong tự nhiên
- Bầu không khí ngột ngạt, ai cũng che giấu thân phận
- Pete thấy lồng sắt giam phụ nữ ở góc đông nam — băng Bloodfang buôn bán người
- Lena tức giận: Bloodfang mở sòng bạc và hội quán, ép nữ tiếp tân không đạt chỉ tiêu ra chợ đen phục vụ cưỡng bức
- Pete nhận ra Bloodfang vô pháp vô thiên, không coi luật pháp ra gì
- Pete vốn định chỉ phát triển giáo phái răn đe, nhưng thấy cảnh tượng này biết không thể giải quyết dễ dàng
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


## Source Chapter 34 - 0034 第一批种子
# 第34章 第一批种子

布兰登依照蕾娜教的方法，消耗3点知识点数。
大量有关如何激发、驾驭、掌控怒气的知识，快速涌入他的脑海。
【感知怒气于体内的来源，期间保持理智与冷静】
【深度呼吸，状态平稳，气贯全身，游弋胸腹，将不同强度的内气引导至对应的部位，逐渐转化为可被调动控制的怒气】
【调整强度，依照特定的经络通道，便于随时将怒气附着于战技】
【……】
一条一条的相关训练要点，细化到了每个步骤、每个阶段的目标。
就差没手把手帮他修行了！
以前的布兰登哪里见过如此全面细致的知识！
他到战士公会偷听过，但是那里的教学主打一个大力出奇迹，根本没有什么具体的方法，只说让自己想办法处于怒气勃发的状态，然后什么时候能让这股怒气不消散并可以利用其增加自己的战技的威力，就算战士职业入门了。
至于具体该怎么维持不消散？
具体该怎么利用怒气增加武技威力？
不好意思，就连已经成为战士职业者的人都说不明白。
他们只能将其形容为一种感觉，说是感觉到了就会了，然后就会变成一种本能。
战士公会里经常能看到那种憋气把自己憋的满脸通红，便秘似的家伙。
无他，都在跟自己的怒气较劲呢。
这种笼统的方法，绝大部分人都会倒在找到那种“感觉”之前，没法踏过门槛。
可是布兰登发现，求知之神给予他的方法里，准确地告诉了他，该如何去找到“感觉”，驾驭怒气！
有了切实可行的方法，布兰登顿时迸发出无穷的动力！
第一次尝试，进度1%，失败，没能激发稳定的怒气来源；
第二次尝试，进度2%，失败，没能激发稳定的怒气来源；
第三次尝试，进度6%，失败，这回找到了体内的怒气，但情绪出现了些许波动，怒气消散；
……
第十七次尝试，进度31%，失败，将怒气引导至胸口位置时，没能控制好速度，怒气消散。
……
虽然一次次的努力都以失败告终，全是各种各样的原因导致的失败，但布兰登反倒越来越有劲头！
过去的他不是不努力，他只是找不到努力的方向！
他付出了很多的时间精力却看不到努力的结果，自然会觉得泄气。
这回则不一样！
他能切实地看到，他的每一次努力都是有成果的！
一开始连激发怒气这一最简单的步骤都会失败；
现在的他已经能维持一段时间怒气的运转，能明显感觉到，自己的体内仿佛有一团火在燃烧。
那蓬勃的怒气正呼之欲出，想要发挥其中的强大破坏力。
几个小时的努力，顶得上他过去十年的摸索！
这让他怎么可能不激动。
天色正在慢慢放亮，日出即将到来。
要不是体力因为练习而消耗的差不多了，布兰登恨不得一口气把他的练习进度推进到100%！
因为这意味着他将能实现自己的梦想——成为一名战士职业者。
虽然身体无比疲惫，但布兰登的精神却是无比兴奋的。
“感谢求知之神！”
“我从未见过您这样伟大的存在，请接受您的信徒最虔诚的感谢！”
布兰登恨不得给求知之神磕一个！
此时他再看向地下酒窖周遭的环境和引导他信仰求知之神的蕾娜，感观顿时大变样。
原本透着阴暗神秘的酒窖，此刻变得无比神圣。
这哪是什么秘密集会场所啊！分明是让他能够实现梦想，重获新生的圣地！
哪有什么身份不明的少女，不知名的诡异教派！
这都是他异父异母的兄弟姐妹啊！
尝到甜头，布兰登现在已经成了求知之神最坚定的拥护者。
……      眼看天色放亮，蕾娜按照培特给她准备的“台词”，提醒众人道：
“各位，求知之神是一位特殊而伟大的存在，祂刚从久远的长眠中苏醒，我等便是祂在这个时代的首批信徒，理应传播祂的真理。”
“每个火曜日的午夜，我们都会在这里举行交流集会，欢迎更多的同行者加入我们。”
“求知之神给予我们宝贵的知识，请诸位善加利用”
“主在注视。”
……
信徒的数量从2人提高到了6人，诺文十分满意。
培特和蕾娜这次的传教成功率高达100%。
只要是因为纸条而动心来莫尼兄弟酒馆一探究竟的人，在培特的“带动”下，最后都选择了向诺文献上信仰。
四名新人，布兰登选择了战士职业的修行路线。
其他3人，无论他们和各个职业者主神的亲和度如何，最后都选择了法师职业。
为此诺文花费了些许神力，使用权柄获取了有关的起步修行知识。
这样一来，诺文便拥有了三条职业道路的入门知识。
往后如果再有新信徒想成为战士、潜行者或法师，诺文便无需再消耗神力，只需要将他现有的知识复制粘贴一份给对方即可。
至于为何那3个新信徒都要选择法师？
原因很简单。
法师算是目前大陆上最吃香的职业。
即使不参与征召去消灭各种被邪神污染的魔物，或者当个冒险者佣兵接受委托；
只要有3阶法师的认证，就能成为不少贵族的魔法顾问，拥有稳定的收入；
最不济，当个魔法民工，每天抄写魔法卷轴，也能赚不少钱。
因此当选择的机会摆在面前时，这些普通人的第一反应都是想成为法师。
当然，诺文很清楚一件事。
他并不能让每个信徒都成为传奇战士或者大法师。
虽说将通过权柄获取的知识给予信徒后，能让他们无需受到信仰的限制，可以自由选择想行走的道路。
但是人的天赋是有区别的。
比如蕾娜和布兰登。
蕾娜与暗影之神的亲和度非常高。
按照诺文的理解，这说明暗影之神墨菲掌管的暗影力量更加青睐她。
因此在潜行者的入门上，蕾娜仅仅花了一晚上多点的时间，不到10次尝试就能完整的掌握【潜行】战技。
布兰登的天赋就差了不少。
尝试了十几次，有关驾驭怒气的进度还没到三分之一。
诺文估计着，少说还得2、3天时间，布兰登才有可能成功驾驭怒气，完成战士入门。
后面职业进阶的难度更高，需要花费的时间更多，差距也会更大。
诺文能做的，是告诉他的每一位信徒，该如何去努力，以及——距离成功还有多远。
现在有了这批信徒作为“种子”，诺文相信他们很快便会在格林港下城区生根发芽，然后……
扩散开来！
……
感谢：木召草，一条狗竟然，投出的月票。感谢各位投出推荐票的读者，蟹蟹。


## Output Format
Return ONLY valid JSON matching this schema:
{
  "chapter_number": 34,
  "chapter_title_vi": "Chương 34: <Vietnamese title>",
  "segments": [
    {
      "segment_id": "XXXX",
      "source": "...",
      "target": "..."
    }
  ]
}
