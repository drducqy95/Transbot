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
 kế tước vị
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

## Chapter 0038 - Chương 38: Norven: Ta thật sự không muốn làm tà thần

### Summary
Chapter 38 completed via pipeline.


## Source Chapter 39 - 0039 德思礼
# 第39章 德思礼

话分两头。
下城区，一家名为“血色轮盘”的地下赌场。
这家赌场的入口是一堵不起眼的墙壁，只有按动对应的机关才能进入。
内部大厅宽敞而昏暗，布局复杂，一张张桌台上摆着轮盘、骰子、纸牌和筹码等赌具，形形色色的客人或站或坐地围在赌台边上，时不时地爆发出欢呼或是怒骂，显得十分喧闹。
环境中混杂着浓郁的烟草和酒精的味道。
赌场深处，VIP房间门外。
埃文正紧张地等待着。
大门从里面打开，走出一名身着黑衣的男人。
“德思礼大人回来了，你进去吧。”
埃文只跟他对视了一眼，就被对方金色瞳孔中透出的强烈气势给吓得低下了头。
“是，是！”
“德莱尔大人，我这就进去！”
德莱尔，最早跟随德思礼加入血牙帮的小弟，一直鞍前马后地服侍德思礼。
后来德思礼上位成了血牙帮的首领，这位小弟的地位也水涨船高。
虽然他的实力连职业1阶都没到，但在帮中的身份很高，相当于德思礼的副手。
摄人气势逐渐远去，埃文这才松了口气。
“奇怪，以前没感觉德莱尔有这么吓人啊。”
刚刚在德莱尔说话的时候，埃文不知怎的，硬是有种喘不上气的窒息感，仿佛面前的不是人，而是一头恐怖的魔物。
“大概是我太紧张了吧……”
“……希望……德思礼大人这回能放我一马。”
埃文想着，小心地推开雕饰着精美浮雕的VIP房间的厚重大门。
房间内的装修奢华而清静，与外面赌场大厅那喧哗的氛围截然不同。
天花板上悬挂着由魔法水晶照明的巨大吊灯，散发着柔和而明亮的光芒。四周的墙壁上挂满精心绘制的画作，连地面都铺着兽皮制成的宽大地毯。
由珍稀木材打造而成的桌台后，坐着一个眼神阴翳的中年男子。
身材不高，但体格十分壮实，光是坐在那里便透露着危险的气息。
男子脸上有一道穿过左眼的伤疤，更显得凶气逼人。
“说说吧，怎么回事？”
“为什么老莫尼的那间酒馆还在开着？”
听到问话，埃文不知怎的，感觉这次对方的气势变得比以前更凶悍了。
腿不由自主地一软，当场跪倒在地，头也不敢抬地哭诉道。
“大人，您听我解释啊。”
“本来我们已经快要让他干不下去关门了，兄弟们按着我的要求，每天都会去酒馆里大闹一场。”
“五天前，老莫尼的女儿，那个叫蕾娜的小妞，不知道从哪里请来了一位法师！而且还是位2阶法师！对方二话不说，把我派的人都给打跑了！”
“据兄弟们偷偷观察，那位法师这段时间经常出现在莫尼兄弟酒馆，很可能是他们请来提供保护的！”
“有位法师在酒馆坐镇，兄弟们不敢去闹事啊。”
埃文，血牙帮的5名头目之一，1阶战士。
先前那些去莫尼兄弟酒馆砸门闹事的血牙帮混混，便是埃文手下的人。
埃文一开始接到命令，去骚扰一家酒馆逼到对方关门走人的时候，他没怎么当回事。
毕竟对方只是普通人，派些手下过去多闹几天事，酒馆的生意十有八九就得被搅黄。
不止一家在格林港下城区开店做生意的，都是被埃文这样赶走的。
这种手段他用的很熟练。
刚开始，一切进行的也很顺利，因为时不时有血牙帮的混混闹事，酒馆很快就不得不闭门歇业，没法正常招待客人。      然而，埃文的计划却被蕾娜邀请来的培特给打乱掉了。
一名法师，而且是最少2阶的法师，这就超出了混混们的战力上限！
没看人家【奥术飞弹】点名一下一个吗？
更重要的是，法师可不是那么好得罪的。
对血牙帮的混混来说，他们去酒馆闹事就是听命行事，领个赏钱。
真要把那位法师阁下给惹恼了，万一对方记恨上自己，打算事后报复怎么办？
他们这种底层混混，加入黑帮是想欺负别人，不是真卖命啊！
一时间，谁也不敢上去当这个出头鸟。
无论埃文怎么动员，他手下的混混们就是各种推诿。
埃文没有办法，只能来血牙帮的总部——“血色轮盘”地下赌场，找他的老大，也就是血牙帮首领德思礼求援。
“就这？”
中年男子，也就是德思礼听完埃文战战兢兢的哭诉，嗤笑道。
“区区一个2阶法师，就能把你们给吓成这样？”
“果然，底层人就是没什么屁用，连这点小事都搞不定。”
埃文有苦难言，试图辩解：“可是大人，我的手下连1阶职业的都没有，他们当然害怕那位2阶法师的报复……”
德思礼手一挥打断道：“停。”
“我不想听你在这给我哔哔这些废话。”
“我就问你，把你手下都换成1阶职业者，让你晋升到2阶战士，能不能把事情给我办好！”
埃文愣了。
他听到了什么？
手下全换成1阶职业者？
让他自己晋升到2阶？！
这话说的他反应不过来了。
在埃文的记忆里，血牙帮一百多成员，总共也才5名1阶职业者，外加首领德思礼这个2阶战士。
这种水平就已经是能在下城区横行霸道的程度。
他手下可是有十几个人啊！
要是能让他们都达到1阶，那岂不是直接统治下城区了？
仿佛预料到了埃文的反应，德思礼不屑道：
“没见识的东西，真TM给老子丢人，让他们都成为1阶职业者就把你给吓到了？”
“睁大你的狗眼好好看看，老子现在是几阶了？”
埃文瑟瑟发抖地抬起头，只见德思礼的体表正覆盖着一层厚实的“气盾”，透明流转的气体中，透着些许血红。
“怒气护体！”
这是3阶战士最明显的特征，怒气浓郁到可以激发透体而出，在身体周围形成一层气盾，大幅度降低受到的各种伤害。
“告诉你，血牙帮已经和过去不一样了。”
“职业者很难？”
“那是你们不懂什么叫力量的真谛！”
“我已经得到了真正伟大存在的青睐，什么1阶2阶，随随便便的事！”
“赶紧把你那些废物手下都叫过来，那位伟大存在会赐予他们真正的力量！”
德思礼狰狞大笑着宣布。
“称霸下城区只是开始！”
“以后，血牙帮要做格林港的无冕之王！”
“那些上城区的大人物都要跪下来给老子舔鞋！”
……


## Output Format
Return ONLY valid JSON matching this schema:
{
  "chapter_number": 39,
  "chapter_title_vi": "Chương 39: <Vietnamese title>",
  "segments": [
    {
      "segment_id": "XXXX",
      "source": "...",
      "target": "..."
    }
  ]
}
