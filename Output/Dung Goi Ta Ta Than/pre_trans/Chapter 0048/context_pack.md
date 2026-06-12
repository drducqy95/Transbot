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
 Lena tập 【Ẩn Nấp】 lần đầu thất bại nhưng thấy thanh tiến độ 7%, biết nguyên nhân thất bại
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


## Source Chapter 48 - 0048 加大力度
# 第48章 加大力度

一阵沉默过后，布兰登最先拍桌而起。
“妈的！干了！”
“不就是邪神吗？怕个卵蛋！”
“要是真的能亲手干掉一位邪神，大陆上的吟游诗人以后都得传唱我的故事！”
“是求知之神给了我知识，让我能拥有力量，可以自由选择自己的命运。”
“既然现在祂向我发出了征召，那我必须响应！”
“那几个血牙帮的混混也是两个眼睛一张嘴，两根胳膊两条腿。”
“最后他们不也被我们打败了吗，看起来这邪神的走狗也没辉光神教说的那么吓人啊！”
有了第一个站出来带动气氛的人，酒馆中其他人也接二连三地下定了决心。
“没错！布兰登说得对！”
“辉光神教靠不住，那我们就靠自己！”
“这是伟大的求知之神赐予我们的使命！”
“既然选择成为职业者，那就有跟魔物战斗的觉悟了！不然的话还不如老老实实继续当个普通人混日子！
“我不知道为什么血牙帮投靠了邪神，也不知道他们在哪里，但我知道我要大开杀戒了口牙！”
神国中，诺文看着酒馆中一片群情激奋，决定再给这火热的气氛添一把火。
新的神谕编写完成，加入到先前的活动神谕中，只要加入活动便可查看。
【格林港下城区邪神威胁爆发进度：21%】
【注：通过击败血牙帮成员、破坏血牙帮据点可降低此进度，当进度降至0%时，邪神威胁消除。】
新的进度条出现，有了明确的目标，酒馆中的求知教派的成员们更是充满了动力。
“大家看到了吗？求知之神在注视着我们！祂在鼓励我们！”
……
血牙帮与邪神勾结这件事。
对信徒来说意味着一场挑战。
但对诺文来说，却是个绝对的“意外之喜”。
最开始的时候，诺文的计划只是通过清理血牙帮这个下城区的黑恶帮派，给自己的教派建立名望。
当时的诺文都做好了自掏腰包的准备，打算用他这段时间收集的神力作为奖励，用来兑换信徒们在活动中刷到的点数。
活动的3项特殊技能效果的本质都是诺文利用自己的神职权柄，消耗神力得到相应的信息，然后再传达给信徒。
为了防止储备的神力不够用，诺文还特意给3个特殊技能设置了激活门槛，用来回收一部分“正义点数”，降低他开启这次教派活动的成本。
但是，当那五名血牙帮的混混被信徒们不断攻击的时候，诺文这边却开始凭空冒出一股股神力！
诺文仔细一查看。
神力的来源不是别人，正是血牙帮的几个混混！
像是吞噬一样，对方身上的某种能量随着诺文信徒的攻击而被不断掠夺，变成了属于诺文的力量！
这意味着诺文的信徒讨伐这些受到邪神力量影响的敌人时，诺文可以以战养战，获取神力作为战利品！
而且，真正令诺文“喜”的地方不止于此。
这次获取神力的方式跟属于他的信徒祈祷转化不同。
从混混们身上获得的能量也有着大量疯嚣狂乱的混乱气息。
但当这股能量被掠夺到诺文的神国，即将成为他的神力的一部分时，诺文却从他自己的神力中察觉到了一种“嫌弃”的情绪。
两者混合时。
外来的能量先是析出了一些纯净、平和、稳定的神力。
在变得更加混乱、无序后，才融入了诺文原有的神力！      注意到这一点的诺文简直哭笑不得。
“看起来，我在邪神里真的也是最邪门的那一类！”
这“嫌弃”的意思，诺文估计大概是他的神力觉得外来的家伙不够邪恶，不够混乱，不够格成为自己的一部分。
硬逼着对方将那些秩序、稳定的部分丢掉后，才配融入诺文的力量。
离谱归离谱，诺文随之产生了一个大胆的想法。
“那部分被抛弃的纯净神力，虽然我拥有的神力看不上，弃之敝屣，但其实可以被从另一种方式利用啊！”
诺文当即做了个尝试：
从血牙帮混混身上掠夺来的混乱能量向外析出纯净神力的时候，诺文并没有让其就此逸散到神国的茫茫灰雾中，而是有意识地将其汇聚起来。
最终。
一个拳头大小，完全由纯净神力汇聚而成的透明神力球体出现在诺文的面前。
感受了下神力球体中那圆润、稳定、平静的气息，诺文简直泪流满面。
“神啊！”
“哦，不对，我自己啊！”
“我终于也拥有可以直接赐予凡人的力量了！”
先前困扰了诺文许久的最大问题就是：他的神力充满着混乱气息，只能通过神谕之类的方式传达信息。
加持神力则是想都别想，哪怕只有一丁点神力赐下，都会让凡人变成可怖的血肉怪物。
诺文很清楚，求知教派的信徒们存在着一个难以规避的弱点：
他的信徒们只能获取知识，没法得到神力的赐福。
神力赐福的基础效果是提高肉体强度，除此之外，各个神明还有各自不同的特点。
辉光之神的信徒们得到神力祝福后，还能在战斗时得到辉光之力的加持，造成额外的伤害效果；或是在使用神术时，辉光加持产生额外的治愈效果。
暗影之神的信徒会被暗影庇护，打向他们的攻击会更容易被暗影偏移而无法命中，他们的攻击则更容易命中敌人的弱点；
其他几条职业道路对应的神明也有类似的赐福效果。
这也是职业者比普通人强大的地方之一，他们的肉体已经从凡俗完成了晋升。
过去的职业者评级，因为默认在掌握了对应的战技、神术时，肯定得到了神明的赐福，所以根本没有考核肉体强度这一项。
求知教派的信徒则是空有技能，没有肉体基础。
诺文没想到的是，他的缺点居然会被这样解决：
血牙帮与不知道哪位邪神勾结，成为了邪神的眷属，快速获取了力量；
诺文的信徒击败血牙帮的人，这股力量能够被他掠夺。
掠夺来的能量中被他的神力“看不上”的部分，却可以拿来用于给信徒赐福，提高他们的肉体强度！
信徒们消灭的邪神眷属越多，诺文能使用的“赐福”就越多！
确认了这个新的神力来源，诺文看向血牙帮的目光也骤然变得火热起来。
原本还只是打算清扫个黑恶势力立威，给自己争取点名望。
现在诺文改主意了！
加大力度！
必须加大力度！
……
叮，升级系统已解锁。如果可以的话，求个投票支持，蟹蟹~~


## Output Format
Return ONLY valid JSON matching this schema:
{
  "chapter_number": 48,
  "chapter_title_vi": "Chương 48: <Vietnamese title>",
  "segments": [
    {
      "segment_id": "XXXX",
      "source": "...",
      "target": "..."
    }
  ]
}
