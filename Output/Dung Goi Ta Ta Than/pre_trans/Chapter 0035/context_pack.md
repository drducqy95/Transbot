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
 Lena rủ Pete đến quán rượu nhà mình để tạ ơn.

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

## Chapter 0034 - Chương 34: Những hạt giống đầu tiên

### Summary
Chapter 34 completed via pipeline.


## Source Chapter 35 - 0035 滚滚螺栓工坊
# 第35章 滚滚螺栓工坊

集会结束，布兰登拖着因为修习怒气而疲惫不已的身体回到家里。
布兰登家的房子是下城区最常见的那种建筑，外部结构由厚重的石块垒砌而成，经过岁月的洗礼显得有几分斑驳，木质屋顶上覆盖着一层海边特有的苔藓和藤蔓。
屋内的结构也很简单，进门的主要空间承担了客厅和厨房的作用，摆放着些朴素的家具和装饰品，往里走的房间被布帘分隔开来，布置成两间卧室。
较大的那个是布兰登父母的，较小的属于他自己，空间不大，摆下一张柔软的单人床后便不剩多少地方。
布兰登的父母两人白天都要去各自的工作地点上工，他回来的时候，家里很安静。
桌上留了两块软面包、一块煎蛋，一杯温热的牛奶。
闻到金黄面包散发着的甜美香气，布兰登这才察觉到腹中饥饿。
坐在餐桌前一顿狼吞虎咽，看了眼墙上挂着的月历的日期，布兰登打了个长长的哈欠，无奈地站起身来。
“万恶的地精财阀啊，他们都应该被吊死在港口的路灯上！”
尽管刚刚熬了个通宵，但现在却不得不强压下困意。
因为他得抓紧时间赶去他打工的地精工坊。
他倒是很想现在就把工作扔了，改行去注册冒险者，周游大陆。
但他实在囊中羞涩！
战士的修行同样相当烧钱。
武器、防具哪一样不要钱？
求知之神可以给他知识，但没法直接给他变出装备。
那些能赚钱的冒险者委托，可都是有风险的！
实力不够，装备也差，万一刚去冒险就被野外的魔物单杀，岂不是血亏！
布兰登计划着。
这段时间他辛苦一些，白天打工赚钱，晚上按照求知之神的指引，继续练习驾驭怒气。
等他正式成为1阶战士，差不多刚好也是发工钱的日子，他要狠狠朝地精工坊的那个死要钱的地精老板竖一根中指，告诉他，爷不干了！
……
布兰登一路打着哈欠，穿过几条小街，走到一座名为“滚滚螺栓工坊”的建筑前。
格林港下城区里大大小小的工坊有不少都是被地精投资建设起来。
来自大陆各地的原料在格林港的下城区被加工成各种各样的商品，然后再随着货船运往各处，赚取丰厚的利润。
虽说这些绿色小矮子地精们自身没什么战斗力，但财富积累到一定程度，靠着花钱雇佣保镖，购置各种“地精工程学”防身产品，本身便是一种实力。
“滚滚螺栓工坊”的规则，迟到、早退，统统视作当天旷工；
上六休一，早九晚六，不管吃，不管住，工伤不负责。
条件各种苛刻，工作量比其他地方高不说，环境还特别恶劣。
要不是因为这家地精工坊承诺给开出的报酬比其他人类开的工坊要高不少，布兰登压根不会来这里打工。
门口坐着的食人魔监工正照着画像挨个核对身份。
“嗯……让我看看。”
“你跟画像看起来差不多，那你应该就是……”
“勃兰顿！”
“勃兰顿！你今天的工位在第二排左数第6个。”
布兰登脸色一黑，小声骂了句。
“Asshole！”
这个食人魔监工是滚滚螺栓工坊老板雇佣的，他给自己起了个名字叫“杜姆”。
这个词是食人魔语里“智慧”的发音。
杜姆一直觉得他是个食人魔里充满智慧的智者。
因为他认字。      实际上，这家伙的通用语水平完全就是个半吊子，十处发音他能有九处错误。
比如，直到现在杜姆都认为布兰登的名字读作勃兰顿！
不跟傻子一般见识，布兰登收拾了下心情，踏入工坊。
混杂着汗液臭味和机油油脂味、金属铁锈味道的气息瞬间扑面而来。
布兰登倒是对这股怪味习以为常，走到属于他的那个空的工位坐下，熟练地拿起工作台上的工具，开始打磨螺栓。
他的工作内容倒是很简单。
把粗加工的螺栓按照要求的规格，手工打磨成合适的尺寸。
按完成的个数计算工钱，每月一结算。
……
因为夜里通宵练习驾驭怒气，白天精神不济，布兰登打磨的效率有所下降。
忙活一上午，他的产出还不到平时正常的一半。
好不容易捱到中午短暂的休息时间，只见从旁边的工位挤过来个小个子男性，朝他挤眉弄眼。
“怎么回事，布兰登，昨天晚上猪头酒吧打牌的里面没见到你，干嘛去了？”
“看你这没精打采的样子，该不会是去玫瑰情人那快活了吧？”
“你这体力也不行啊！”
“还天天说自己将来要成为大陆闻名的战士，这才一晚上就虚了啊？”
布兰登顿时没好气地开骂。
“放你的狗屁！”
“我就知道你这狗嘴里吐不出什么好话。”
“你才虚！老子身体结实的很！”
“给我瞧好吧，过两天老子就能成为真正的1阶战士，到时候我就去当冒险者，名声大到去哪都能刷脸吃饭那种！”
“你就继续在这破地方混吃等死吧！”
对方是布兰登的工友，两人平日里关系还算不错，经常在下工后找地方一起喝酒打牌吹牛。
他跟布兰登的情况差不多，因为没什么希望成为职业者，就跟大部分下城区人一样，找个地方打工。
干个几年时间，差不多攒够钱，考虑回雷亚克王国找个小镇子买套房产安顿下来；
毕竟，格林港下城区虽然环境差，但是劳工的报酬还是比雷亚克王国的普通小镇要高不少的。
听到布兰登的话，工友本以为又是布兰登天天挂在嘴边的“将来他会成为伟大的传奇战士”之类的说辞。
正打算取笑几句，却见布兰登先是一愣。。
下一刻，布兰登突然开始动力十足地低下头继续打磨起螺栓！
工友愕然：“什么情况？”
按着他们往常的习惯，平时可是一秒钟都不会多干，休息的铃声一响，立马就会放下的手头的活计才对。
布兰登手中动作不停，头也不抬地回道：“你懂个蛋！”
“那是因为我刚刚突然意识到，打磨螺栓其实是个很有意义的劳动！”
工友的好奇心顿时就起来了。
“不对劲，你很不对劲啊布兰登，你这是有事！”
“到底是什么事情，还是不是好哥们了，赶紧分享一下啊！”
……


## Output Format
Return ONLY valid JSON matching this schema:
{
  "chapter_number": 35,
  "chapter_title_vi": "Chương 35: <Vietnamese title>",
  "segments": [
    {
      "segment_id": "XXXX",
      "source": "...",
      "target": "..."
    }
  ]
}
