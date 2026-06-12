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
ị giai, học viên Học viện Caroen)
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

## Chapter 0034 - Chương 34: Những hạt giống đầu tiên

### Summary
Chapter 34 completed via pipeline.

## Chapter 0035 - Chương 35: Xưởng Bu-lông Lăn Tròn

### Summary
Chapter 35 completed via pipeline.


## Source Chapter 36 - 0036 你知道的，我嘴巴最严实了
# 第36章 你知道的，我嘴巴最严实了

布兰登闻言思考了几秒，还真放下手中的活计，朝工友勾了勾手指。
“行，你靠过来点儿，我悄悄告诉你。”
见布兰登的表情十分认真，工友反倒讶异了。
“真的有事儿？”
布兰登嗯了一声：“告诉你，搓螺栓也是一种修行。”
“我现在能通过搓螺栓，最终学到属于战士职业者的战技。”
“噗！”
“这个笑话还不错，我承认被你逗笑了！”工友大笑起来：“就靠这个？靠着搓螺栓？”
“照你的意思，难不成那些传奇战士都是靠搓螺栓练出来的？”
“傻蛋，爱信不信！”布兰登骂道。
工友笑了半天，忍不住继续逗布兰登：“要不然，你具体解释一下，这搓螺栓和战士职业之间的关系在哪里？”
“你知道的，我嘴巴最严实了。”
“要是真能靠搓螺栓成为战士职业者的话，你把方法告诉我，我将来打出名堂，赚到大钱了，这钱我分你三成好吧！”
布兰登面色略显古怪地看向对方：“你确定？”
工友还是一副没当回事的样子：“那当然啊，有什么好办法，赶紧分享一下呗。”
布兰登询问：“如果我告诉你，有一位强大的神明，只要向祂献上信仰，祂就会赐予你成为职业者的方法，你信吗？”
“等会儿等会儿……”
工友狐疑地看了眼布兰登。
“你这描述，我怎么听起来有点像是个邪神啊。”
“辉光教会不是说了吗，邪神可以强制进行力量灌注，让凡人在短时间内获得强大的实力，快速成为职业者，但最后一定会失去理智堕落成魔物来着。”
布兰登纠正道：“不不不，不是邪神！”
“对方是正常的神明，只是神职比较特殊而已。”
“那废话，要不是邪神的话，我肯定信啊！”
工友想都没想就给出了答案。
“这种事还用问信不信吗，要是真有这样伟大的存在，那我也不用天天问普鲁斯特（财富之神）我啥时候才能暴富了，保证立马改信！”
“你想想啊，不管想修行哪条道路，那压根不是献上信仰就能成职业者的，得找教会，让他们领着，去祈求神明给点儿注视。”
“你说的那种神明，献上信仰就能成为职业者。”
“那这哪是什么神明啊，这明明是我的亲爹亲祖宗啊！”
布兰登被工友略显夸张的说辞逗得笑了一下，旋即正色道：
“我没有在说笑，因为——真的有这样一位神明。”
“我说的那些是真的。”
“我向祂献上信仰后，祂真的回应了我，告诉了我该如何去练习才能驾驭掌控怒气。”
说完，布兰登微微闭眼，按着之前练习的经验，一点点激发调动怒气。
虽然还没法将怒气附着于战技，但他已经能靠着怒气激发出些许属于战士职业者独有的“气势”。
这下工友笑不出来了。
本以为大家是在开玩笑，结果布兰登玩到真的了！
“当真？”
“当真！”
“真的有这样的存在？”
“真的！”
“祂真的能回应信徒……”
“哎呀我说你有完没完！说过了保真，我都收到祂的赐福了，还能有假不成？”布兰登被问烦了，打断道。
工友：“嘶！！那如果我想向祂献上信仰，我需要付出什么？教会在哪里？入教想聆听神谕要交多少钱？”
布兰登想起他祈祷时收到的神谕。
“祂的神号是求知之神诺文，为了引领迷途的凡人，传播伟大真理，行走于世间。”
“因此不需要以传教为由收取钱财。”
“求知教派需要信徒付出的只有自己的努力。”      “一切的奖励都要靠努力来获取。”
布兰登转述了遍他收到的神谕，认真地提醒工友道：“我先把话说明白，求知之神愿意平等地对待每一位信徒没错。”
“但既然你想要从祂那里获取知识，那就要真正虔诚的信仰，感恩这份来自求知之神的馈赠。”
“成为祂的信徒的机会很宝贵。”
“求知之神会时刻注视着祂的信徒。”
“如果你有歪心思的话，他也随时能收回所有给予你的力量。”
工友的态度也变得认真起来。
“当然，这些不用你说我也懂的。”
“如此珍贵的机会，我肯定会全心全意地信仰！”
“你知道的，我这人嘴巴特别严，我肯定不会拿出去乱传，保证这件事，天知地知，你知我知！”
“所以，我具体该怎么做才能成为求知之神的信徒？”
……
向朋友传播求知之神的信仰成功，布兰登很高兴。
因为他的【知识点数】快要攒够了！
想成为1阶战士，驾驭怒气只是第一步。
接下来的步骤是要最少掌握一个战技，并且能够将怒气附着到战技上。
布兰登自然是不会什么战技的，于是继续向诺文祈祷，寻求帮助。
他确实得到了回应。
【目标：战士1阶战技，英勇打击】
【需求：15知识点数】
这个数额的点数需求，可是一开始驾驭怒气需要点数的整整5倍！
新信徒福利只有10点知识点数，兑换知识消耗了一部分后，就更少了。
想要兑换新的知识，他就得想办法赚到更多的点数。
他打磨螺栓忙活了一上午，最后触发了名为【劳动】的奖励，才只给了他0.3点知识点数。
顺理成章地，布兰登注意到了【吾主的真理普照大地】这个任务。
只要向一个人传教成功，就能拿到5点知识点数奖励！
换句话说，只要他能传教3个人，相当于立刻得到【英勇打击】战技的知识！
比起慢吞吞的祈祷、劳动。
成功传教获得的知识点数明显来得更快啊！
意识到这点之后，刚好工友询问，布兰登便顺水推舟地将求知之神的信仰传播给了对方！
他得到了【知识点数】；
工友成为了新的信徒；
他们都有光明的未来。
只不过嘛。
此刻的布兰登还没有意识到：
想明白这点的，不止他一个人！
……
当晚，猪头酒吧。
“我告诉你啊，这是个非常宝贵的机会，我是把你当成好兄弟才告诉你的，你可一定要珍惜，不要外传！”
被布兰登传教完成的那位工友坐在墙边的木桌旁，神神秘秘地和他的朋友低声介绍道。
对方满脸兴奋。
“放心，我懂，我懂！”
“你知道的，我这人嘴巴最严了！”
“这么好的事情，我肯定不会再告诉其他人啊！你知我知，绝对不会让第三个人知道！”
“快讲讲，我要怎么做才能向求知之神献上信仰！”
……
爆兵发育，开始推图！
感谢风水曲流殇打赏的100起点币，祝老板永远不死。


## Output Format
Return ONLY valid JSON matching this schema:
{
  "chapter_number": 36,
  "chapter_title_vi": "Chương 36: <Vietnamese title>",
  "segments": [
    {
      "segment_id": "XXXX",
      "source": "...",
      "target": "..."
    }
  ]
}
