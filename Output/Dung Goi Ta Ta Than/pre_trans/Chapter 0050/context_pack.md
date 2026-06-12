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
anh tiến độ

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


## Source Chapter 50 - 0050 最吃香的职业
# 第50章 最吃香的职业

形成人数优势后，虽然战斗的时候，还是难以避免地会因为血牙帮的人反抗而导致有人受伤，但最终肯定能有惊无险地拿下敌人。
至于那些受伤的人。
大部分情况下只是皮外伤，稍微包扎休息一下就能恢复不少。
实在运气不好，被打到了身体脆弱的部位，出现骨折之类的伤势，就只能将其送到酒馆去休养治疗。
酒馆里有3个选择了牧师路线的诺文信徒，虽然他们也只是刚刚入门，勉强会个【次级治疗】之类的小神术，但也足够让伤者尽快恢复行动力。
小神术的效果比不上辉光神教圣教军里专业牧师的【治愈真言】，但胜在数量够多！
虽然使用的是辉光之神的神术，但从诺文这里学会神术的牧师信徒们亦不会受到神术位限制，而同样是被精神力所限制。
只要精神力还没耗尽，他们就能连续释放神术！
主打一个以量取胜！
1、2次的【次级治疗】治不好，那就堆上个10次、20次。
积少成多，一样能达到跟辉光神教专业牧师同样的治疗效果！
很快便有人发现：
哎？
好像能提供治疗的牧师才是最吃香的职业啊！
其他职业路线都要正面跟血牙帮的混混对抗。
血牙帮的混混在得到邪神的力量后，个体实力并不算弱。
战斗过程中，如果想作出更多贡献，拿到更多的正义点数，那就不能怂在后面。
可是第一批攻击的人又容易因为敌人的反击而受伤。
受伤失去行动能力就没法继续参与活动，不能继续获取正义点数。
反倒是这3个选择牧师路线的诺文信徒，只要安逸地待在酒馆里，等着伤员被送上门，然后施展神术治疗就行。
因为被他们治疗的人是“阻止血牙帮犯罪”而受伤，所以他们同样能被视为在活动中做出了贡献，一样能拿正义点数！
没有危险。
点数进账稳定。
后来培特和盖尔两人带领的队伍往酒馆送伤员的时候，一听这3个牧师路线的诺文信徒已经靠着治疗伤员得到了300多点正义点数。
盖尔当时，就当时，他改修牧师的心都有了！
他辛苦半天好不容易攒够正义点数！
刚把【奥术飞弹】兑换出来。
结果这帮牧师在酒馆里喝着饮料吹着风，挥挥手放几个【次级治疗】就有大把的正义点数进账！
事实上，一开始的时候，这批选择职业修行的诺文信徒里面压根没有打算走牧师这条路线的人。
传教过程中，9成多的人不约而同地选择兑换了法师入门的知识。
毕竟在格林港这种地方，法师地位高、收入高几乎是所有人的共识。
当然，虽然兑换了知识，也不是所有人都能顺利成为1阶法师。
即使能看到练习进度，但每个人天赋不同，练习的速度也不同。
有的人与魔法女神亲和度高，更容易感知到环境中游离的奥术能量，练习进度更快。
可能只需要几次的尝试就能达到100%目标，完成法师入门。
与魔法女神亲和度不够的那些人，则可能每次尝试只能推进个1%或者2%的进度。
要花费别人数倍甚至十倍以上的时间精力，才能达到同样的效果。
头铁的人终究还是少数。
意识到自己不是做法师那块儿料，自然会退而求其次，选择其他的职业路线。
这才有了修行其他职业路线的信徒。
这些人本来还因为没法成为高贵的法师稍微有些失落。
结果一看在活动中的表现。
1阶法师？
也没那么强势啊！
法师没法顶在前面，拿不到正面对抗那部分的贡献奖励；      施法有精神力限制。
短时间内连放3、4次【奥术飞弹】就会头晕眼花，必须找地方休息半天才能恢复精力。
别说跟轻松安逸的牧师比较了。
就连战士、潜行者、游侠这几种跟人肉搏的职业都比不上！
一时间，不少人都起了跟盖尔类似的心思。
反正才刚刚起步，随时可以再向求知之神祈祷兑换其他职业路线的修行知识。
要不……不当法师了，改修其他职业？
……
关于信徒们职业选择趋势的变化，暂且不表。
一晚上的时间，在正义点数的激励下，趁着血牙帮还没反应过来，求知教派众多信徒四处出击。
在众人共同的努力下，不但第1个特殊技能【状态显示】得到了足够的正义点数成功解锁，就连【罪恶感知】都完成了不少进度。
【状态显示】的效果非常简单直接：
当诺文的信徒们视线里出现血牙帮成员时，他们会立刻收到提醒。
无论血牙帮成员准备什么伪装，在【状态显示】面前都会被直接识破！
有了特殊技能的帮助，而且随着打击血牙帮次数的增多，为了尽可能减少战损、增加效率，众人也纷纷开动脑筋，各显神通，想出不同的办法！
……
次日。
两名混混刚从血牙帮控制的妓院出来没一会儿，就莫名地感觉背后有些发毛。
“怎么感觉好像有什么东西在跟着我们？”
一名混混数次回头，可却只看到了街道上来来往往的行人。
似乎一切如常。
另一混混不屑道：“泄火泄出幻觉了吧你？下城区这地界谁敢招惹我们啊。”
“赶紧的，今天要收3家的保护费，抓紧时间，早点完事，还能回去玩上两盘骰子！”
先前说话的混混还是有些疑神疑鬼，直到他俩大摇大摆地踢开商户大门，强行收走一大笔“保护费”后，依然跟往常没什么区别。
“是我的错觉？”
第二家商户的“保护费”的也收的很顺利，店主根本不敢反抗，老老实实地交出了钱袋。
直到第三家商户，他们两个还没来得及踹门，眼前骤然一黑。
两条带着汗臭味的粗布麻袋兜头罩了下来！
甚至来不及反抗，俩人就在数次【奥术飞弹】的冲击下失去平衡，摔倒在地。
各种各样的攻击立马招呼上来！
俩人被套着麻袋，根本没有抵抗能力，听着外面热闹的叫喊声，只能被动挨打！
“犯罪行为成立，证据确凿！”
“血牙帮的人，错不了，状态显示都提醒好几遍了，就是他俩！”
“还是培特先生聪明！先给他们套上麻袋，这样就不用担心被反击了！”
“跟了一路，这俩人已经连续强收了两家商户的保护费！”
“现在再干掉他们，肯定能有不少正义点数！”
……
感谢书友20230321120407896，书友20230326221043464，毕竟东流去W投出的1张月票，感谢各位投出推荐票的书友，蟹蟹你们


## Output Format
Return ONLY valid JSON matching this schema:
{
  "chapter_number": 50,
  "chapter_title_vi": "Chương 50: <Vietnamese title>",
  "segments": [
    {
      "segment_id": "XXXX",
      "source": "...",
      "target": "..."
    }
  ]
}
