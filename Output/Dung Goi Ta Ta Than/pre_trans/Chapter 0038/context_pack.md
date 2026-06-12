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


## Source Chapter 38 - 0038 诺文：我真不想当邪神
# 第38章 诺文：我真不想当邪神

“搞定！”
神国中，诺文兴奋地搓了搓手。
他的面前此刻多出了一个半透明的巨大光幕。
上面就像他穿越前玩过的RTS（即时战略）游戏那样，正呈现着格林港下城区的地图，一个一个的绿点不断闪烁。
刚开始的时候只有那么零星的几个，现在数量已经增加到上百，而且还在随着时间推移逐渐增多。
这些绿色光点，自然是诺文获得的信徒数量。
格林港下城区的传教计划起步相当顺利，短短一天时间，成为浅信徒的人数便从第一批的6人，增加到上百人。
“照这个进度，估计信徒数量很快就能突破千人，最后应该能覆盖大部分下城区。”
随着信徒数量的增多，诺文能通过信徒们得到的信息越来越多，他对这个世界的了解也越来越全面。
各个神明、教派的信息，大陆的局势，野外的魔物等等，海量的信息被诺文收集起来。
类似玩游戏，刚开始没有信徒的时候，这个世界对诺文而言便布满了“战争迷雾”。
什么情况都不了解，诺文就只能靠着培特、蕾娜这孤零零几个信徒去观察世界，效率低下不说，还很难得到全面的信息。
随着传教而转化成的新信徒，就相当于诺文手中的资源。
有【神之眼】的观察效果，每一位信徒都能随时变成诺文的“视野”，让他可以借此观察世界的情况。
信徒们不断提供给诺文的信仰，总算让他原本捉襟见肘的神力逐渐充裕起来。
上百位信徒，每天光是他们日常的祈祷就能给诺文带来上百神力。
更不用说还有普通人每天“劳动”，职业者“修炼、冥想”给他带来的神力。
诺文获得的这些神力，不但够动用权柄回应信徒们的诉求，还能产生不少盈余。
经过这段时间的摸索，诺文搞清了一些关于这片神国空间的“规则”。
在这片布满灰雾的空间中，神力几乎是万能的，甚至能随着诺文的心意做到凭空造物。
当然，诺文目前只造出了死物，他尝试着捏了朵花，结果只是个徒具其表的假花，不会生长，也无法凋谢。
神国空间里的这块巨大光幕就是诺文用了一部分神力搓出来的。
毕竟，随着信徒数量的增多，光靠【神之眼】去感知信徒的情况，效率跟不上不说，得到的信息也不够直观。
光幕上可以随诺文的心意展现各种信息，让他能更方便地观察到信徒们的各种情况。
……
对普兰蒂斯大陆有了更加广阔的认知后，诺文才明白为什么普兰蒂斯大陆的各大教会都在宣传着邪神的危害。
他本以为这个世界的邪神都是那种躲在不为人知角落里策划着搞个大新闻的阴暗角色，一旦冒头就会被各大主神的教会派人围剿。
实际情况嘛。
不能说和诺文想的大差不差，只能说是相去甚远。
邪神的力量远比诺文预想的要强。
各个文明种族与受到邪神影响而转化诞生的魔物间的战斗从未停止。
甚至于，邪神还是略占优势的一方！
因为想培养一名职业者很麻烦，要有足够的天赋，要得到神明的认可，更要经过漫长的修行。
邪神转化一名魔物的速度却很快。
包括动物、植物在内，只要受到邪神影响，快的话，在短短数天时间里就能发生巨大变化。
变得更加危险，充满攻击性。
邪神就仿佛文明之癌，秩序之瘤，不断地制造着新的魔物，冲击着文明的防线。      祂们不需要征服或控制文明，所过之处，留下的只有混乱与疯狂的废墟。
职业者的数量有限，因此各个文明种族只能联合起来，逐渐收缩防线，集中精锐力量，抵抗着魔物的进攻。
事实上，目前为止，整片普兰蒂斯大陆已经有接近一半的区域被邪神攻陷，沦为魔物的地盘。
外部压力重重不说，文明内部的环境也同样恶劣。
时不时地就会有投靠邪神的走狗混入城市中，暗中组织各种危险的献祭仪式，或是传播邪恶的理念，转化出更多的邪神仆从。
一旦成功，可能整座城市都会因此而沦陷，彻底变成魔物横行的禁忌乐园。
得知这些信息后，诺文也很无奈。
“如果有的选，我真的不想当个邪神啊！”
诺文不清楚自己到底怎么来到这个世界，又是怎么成为“邪神”的。
从力量层面上来说，诺文的神力会将凡人污染，变成魔物的一种——畸变怪。
这个特点，邪神无疑。
一旦被人发现他的信徒在接收神力后会转化成魔物，要不了第二天，各大教会的围剿队伍就得对格林港下城区展开神圣的大清洗。
至于干脆不当人，投奔邪神阵营，诺文则直接排除了这个选项。
因为邪神根本就没有什么理智可言，几乎就是无序和混乱的代名词。
信仰祂们，从邪神手中获取力量的凡人种族，轻则变得嗜血、暴躁、疯癫，重则直接失去理智，被污染成各种魔物。
换句话说，邪神阵营里，只有疯子，和更疯的疯子。
真要让邪神彻底攻破文明种族的防线，那这个世界只会变成魔物狂欢的废墟，不会有任何理智和秩序。
问题在于，诺文是有理智的！
到那个时候，世界都崩溃了，文明都毁灭了，只剩下他有理智，那他还有什么存在下去的意义？
既不能暴露自己的身份，又没法加入邪神阵营，诺文只剩下最后一个选项：
扮演一个正常的神！
至少成为看起来像是正常神明的存在！
好消息是：他的伪装到目前为止都还算成功。
教派初步建立，第一批信徒撒出去后，也如诺文所预料的那样，快速为他拉来了更多的新信徒。
只要把自己“求知之神”的这个人设给演绎好。
诺文就能有一个正当地获得秩序文明阵营认可的身份。
坏消息是：他的信徒们的实力不怎么够看，如果暴露他的真实身份，估计还是露头就秒。
不过诺文很有耐心。
等到他积累足够多的信徒，拥有足够的实力，到那个时候，诺文不信还有哪个教会敢说他是邪神！
想要扮演正常神明，自然需要有足够大的名声。
或者说，得以神的名义，做些能被凡人记住的大事！
格林港下城区糟糕的治安环境和海量的犯罪行为，正好成为了一个适合诺文发挥的完美契机。
诺文的目光自然而然地盯上了那个在下城区横行霸道的黑恶势力：
血牙帮！
……
感谢一条狗竟然投出的2张月票，感谢投推荐票的书友们，蟹蟹~


## Output Format
Return ONLY valid JSON matching this schema:
{
  "chapter_number": 38,
  "chapter_title_vi": "Chương 38: <Vietnamese title>",
  "segments": [
    {
      "segment_id": "XXXX",
      "source": "...",
      "target": "..."
    }
  ]
}
