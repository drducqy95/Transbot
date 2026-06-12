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
 chân chính (真信徒): tín đồ tuân thủ nghiêm ngặt giáo lý
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

## Chapter 0039 - Chương 39: Desley

### Summary
Chapter 39 completed via pipeline.


## Source Chapter 40 - 0040 教派公告
# 第40章 教派公告

比起肮脏杂乱的下城区，贸易集市北边位于更高地势的上城区环境要好得多。
市政厅、财富之神教会、公正教派分会、辉光教派分会、战士公会，魔法隐修会等组织尽皆坐落于此；
卡罗恩学院、锈水商行等等亦在上城区占据一席之地；
随处可见精心设计的花园套房，任何一套都造价不菲，动辄上百金币的售卖价格。
这座自由港口的上城区，就连空气中都透着令人心旷神怡的香甜气息。
这并非错觉，而是由大地精、大财阀卡罗恩·拉杆的《大名鼎鼎正牌卡罗恩联合商业集团》专门雇佣数位4阶大法师，利用4阶魔法【化雨术】，定期将他旗下工坊生产的柠檬薄荷香水混入雨水，喷洒到上城区的每个角落所造成的效果。
卡罗恩还专门安排市政厅，给他出台了一项名为“香甜空气税”的新税务政策。
卡罗恩声称，他为了让格林港的居民享受到最高质量的空气，斥巨资提供了相关服务。
为此，要征收上城区居民每月1枚银币的税款，用以补贴他的商业集团。
当然，能在上城区拥有户权居住的人大部分倒也不在意这1枚银币的支出，他们更看重的是这里优越的地理位置和自由的贸易环境。
虽然格林港下城区的治安混乱、缺乏管理，但那也得看是跟谁比较。
倘若跟靠近邪神占领、魔物横行的边境镇子比起来，那下城区的环境已经算得上安全，至少不用担心夜里睡觉被魔物偷袭咬断喉咙。
格林港北边只隔着一片暮色荒原便是雷亚克王国的南部边境。
有雷亚克王国顶在前面，这片荒原还没有受到严重的邪神影响，魔物阶位不高，数量有限，还达不到爆发魔物潮冲击城市的程度。
近几年雷亚克王国的边境战事愈发吃紧，有不少条件还算宽裕的雷亚克王国贵族都在考虑着来格林港买套房产。
如果爆发魔物潮，他们可以在收到消息后及时乘坐地精飞艇来格林港避难，顺便逃避王国宫廷的参战征召。
因为这个原因，格林港上城区近些年来变得越来越繁华。
不过这些上城区的繁华，基本都和正在唉声叹气的培特·奇纳尔没什么关系。
“求知之神在上啊！您这三阶魔法的兑换条件是认真的吗？！”
培特面色悲戚地哀嚎着。
脑中挂着明晃晃的信息。
【目标：法师3阶魔法，奥术弹幕】
【需求：150知识点数】
“150点？！我把自己献祭了能值这么多点数吗？”
他作为求知之神的第一位正式信徒，刚开始的时候确实享受到了不少红利，比如最开始的【哈达之饥渴】，【真名知晓】，还有那个1阶魔法【奥术飞弹】。
培特学习这些魔法的时候，诺文还没有推出知识点数的兑换体系。
现在信徒数量变多，红利期结束。
他想兑换一个3阶魔法用来应付卡罗恩学院的毕业考核，结果看到需求150知识点数这个数字的时候，眼前一黑差点没晕过去。
虽说他已经掌握了3阶魔法【哈达之饥渴】，然而，这个魔法……不能用来考核！
卡罗恩学院奥法学派的考核标准是，成功释放一个奥术系的3阶魔法即为合格，给予3阶法师认证。
【哈达之饥渴】不属于奥术系，甚至不属于正常魔法。
培特去卡罗恩学院的图书馆查过，【哈达之饥渴】被记录在“禁用魔法”的类别中。
书上的描述是，这一魔法的原理是通过魔网的力量沟通虚空，借助虚空腐蚀并吞噬受其影响的生物。
传说中，邪神便诞生于虚空。
正因如此，几乎所有跟虚空搭得上关系的魔法、物品，现在基本都被禁用，以防因为过度使用而招来邪神的注视。      那个时候培特没得选，只能有什么用什么。
现在这个3阶魔法不敢再用，他只能想办法重新掌握一个新的，可以通过考核的法术。
从蕾娜家的酒馆回到卡罗恩学院提供的学员宿舍，培特原本舒适的生活条件倒是回归了没错，但原本增长迅速的知识点数一下子就显得捉襟见肘了！
稳定的知识点数来源，培特知道的就3条。
每天一次的冥想，提升自己精神力的同时，可以完成【冥想】日常任务，能够获得从0.01点到1点不等的知识点数。
每日一次的祈祷礼拜，可以获得1点知识点数。
再就是去完成周常任务【吾主的真理普照大地】，如果传教成功的话，可以得到5点知识点数的奖励！
培特算了一下。
就算他把这3项任务的奖励都给拿满，满打满算，每周也就是不到20知识点数！
加上他手头现有的10知识点数。
相当于要7个多周的时间，才能攒够兑换一个3阶魔法需要的点数！
“7个星期！我根本等不了那么久啊！”
培特很急，非常急。
此刻已经是6月下旬，距离卡罗恩学院的毕业考核只剩下不到一个月的时间。
准确点来说，还有最后15天。
如果在考核到来前没法掌握一个合适的3阶法术，那他就拿不到学院开出的3阶法师证明。
至于将来去魔法隐修会参加考核这条路，对培特来说更是没戏。
原因很简单。
魔法隐修会的考核标准里有一条：
他们只接受通过信仰魔法女神而掌握施法奥秘的人参与考核！
传说中魔法女神掌控着魔网，但祂慷慨地将使用魔网的权限给予了其他神明。
因此某些外神的信徒，在得到他们信仰外神的力量后，也能通过沟通魔网来施法。
这种人不被魔法隐修会认可，没有评级，无论实力如何，他们被统称为野法师。
只有卡罗恩学院的考核可以睁一只眼闭一只眼，不管是什么神的信徒，只要能放出3阶奥术魔法，就可以给予认证。
培特学会的魔法知识来自于求知之神诺文，他已经不再向魔法女神祈祷了，根本就不符合魔法隐修会的条件。
虽说培特已经改变了心态，不打算单单混个3阶认证，就这么回去继承他父亲的贵族爵位混吃等死。
但是否拥有3阶职业者的认证，会直接影响到他将来能不能名正言顺地在雷亚克王国境内拥有封地，招募私军！
这关系到他的野心！
正当培特一筹莫展之际，一条新的信息毫无征兆地出现在他的脑海中。
【求知教派公告】
【第一次限定活动即将开始！】
【活动：清理血牙帮】
……
感谢书海游鱼投出的1张月票，蟹蟹


## Output Format
Return ONLY valid JSON matching this schema:
{
  "chapter_number": 40,
  "chapter_title_vi": "Chương 40: <Vietnamese title>",
  "segments": [
    {
      "segment_id": "XXXX",
      "source": "...",
      "target": "..."
    }
  ]
}
