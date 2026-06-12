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
loodfang vô pháp vô thiên, không coi luật pháp ra gì
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


## Source Chapter 55 - 0055 邪神祭坛？能拆吗？
# 第55章 邪神祭坛？能拆吗？

诺文通过神谕发给培特的推荐地点共有3处。
其中，隐蔽系数最高、最不容易发现的那个选项，培特一看地点的相关描述，人直接麻了。
【推荐位置一：格林港的不知名隐秘地窟】
【描述：数日前，此地发生了一场邪神祭祀仪式导致的严重事故，好在灾难最终消弭于无形，所有秘密都随着邪教徒的凋零被彻底埋葬。】
这描述指向的地点简直再明确不过！
格林港又不是什么三天两头闹邪神的危险地区。
符合这些关键词的地方，显然就是培特当初被骗去参加祭祀仪式的神秘地窟！
培特对那个地窟毫无疑问是抵触的。
毫无心理准备的直面3阶畸变怪，差点在那丢掉性命。
一想到那地方，他就会回忆起当时的惨痛经历。
更重要的是，要是鬼鬼祟祟地领着教派其他人去那里躲上几天，培特总有种莫名的既视感！
谁家好人闲着没事躲在邪神信徒的据点啊！
如果有得选，他肯定不想把那地方当成临时据点。
可是对比另外两个选项后，培特沉默了。
【推荐位置二：下城区的废弃民居】
【描述：半年前，因为一场蓄意纵火，此地的房屋被尽数烧毁，现在只剩残垣断壁。】
【暴露概率：13%】
培特找酒馆里了解那附近情况的人问了下。
与其说是废弃民居，那地方其实就是几座破屋，只剩几堵矮墙和随时都有可能倒塌的屋顶。
临时藏匿2、3个人还有可能。
几十号人全躲进去，暴露的概率绝对会大大增加。
第三个选项，培特更是没眼看。
【推荐位置三：码头附近的荒废洞穴】
【描述：靠近下城区边缘的山体洞穴，每逢涨潮，这里便会被彻底淹没一段时间。】
【暴露概率：19%】
培特脑补了下藏在那里的场面。
每隔几个小时，他们就全得被涌入的海水赶出来一次。
这还让他们怎么保持隐秘行事？
那画面培特都不敢想！
至于那个所谓的自由选项，意思是，培特可以自行挑选他认为合适的地点，消耗对应的知识点数，可以得知这个地方暴露的概率有多少。
问题在于，培特对下城区本就不怎么熟悉。
要在短时间内让他找到难以被发现的藏身处，还不如从这3个选项里挑呢！
对比了一番，培特自我安慰：
“好吧，往好处想。”
“既然能被邪神的信徒当作祭祀的据点，说明那个地方肯定符合他们对隐秘的要求。”
“毕竟他们要躲避的可不是血牙帮这种黑帮，而是辉光神教圣教军的搜捕。”
“能在圣教军的眼皮底下搞出祭祀仪式来，也算侧面证明了这点。”
“我们只是过去蛰伏几天，争取些能安稳提升实力的时间，又不是要搞什么危险的祭祀仪式。”
“求知教派又不是什么信仰邪神的异端教会，身正不怕影子斜！”
……
第二次来到隐秘地窟。
上回是被那些邪教徒黑袍人领着，培特还没怎么注意到这个地方的隐蔽程度。
这次靠着诺文给予的指引，从下城区一个不起眼的下水道入口进入，在错综复杂的排水渠旁行进，路上连续经过7、8个岔路，地势愈发向下，人为建筑的痕迹越来越少。
直到熟悉的地窟出现在培特面前。      培特不得不承认，哪怕有着求知之神提供的路线，这一路上他都差点迷路。
格林港的下水道本就环境复杂，还要在没有路标和指示的情况下，走过多个岔路，想发现这里的难度极高。
难怪当初那些黑袍人会将这里选做祭祀仪式的地点。
如果不知道具体路线的话，大概率会在下水道中迷失方向。
地窟深处那狰狞怪异的土质祭坛几乎还是原来的样子，只不过周围原本那些不知道是动物还是人类的肉块内脏骨骼之类的东西，都随着那只畸变怪的诞生而融为一体。
地窟洞壁上挂着的蜡烛灯被点燃，不知里面加入了什么材料，火焰呈现幽幽的绿色，而非温暖的黄光。
地面上还有培特当时释放【哈达之饥渴】消灭畸变怪时，怪物洒下的黄色脓水，虽然已经几近干涸，但还是能闻到些许怪异的味道。
祭坛周围满是暗红色的凝固血迹，这都是那只怪物留下的杰作。
培特总感觉在进入这隐秘地窟后有种莫名的压力。
尤其是这回他还带了其他求知教派的信徒们一起来到这里。
而且为了隐蔽行事，众人也是先披上了能隐藏身形的宽松长袍，才来到这里。
一群行事遮遮掩掩的信徒，危险的邪神祭祀地窟。
培特总有种既视错觉，仿佛下一刻周围就会有哪位求知之神的信徒转化成血肉怪物似的。
“呼，大家不要担心啊。”
培特既是在给众人解释，也是在安慰自己，干巴巴地努力解释。
“这个地方曾经是一群邪神信徒的祭祀据点。”
“不过那些危险的家伙已经被彻底消灭了。”
“大家不要看到祭坛啊、血迹啊什么的多想，这地方现在很安全，也很正常。”
“我们可是正经教派！”
出乎培特意料的是，这群求知教派的同伴们不仅没有被地窟中怪异的环境和布置给吓到，反倒……爆发出了强烈的好奇。
培特原本预想中众人对那座祭坛敬而远之的场面并没有出现。
反倒是：
“哎？这就是传说中邪神的祭坛？”
“看起来是有点吓人，不过上面刻的这些花纹是啥意思？”
“我也不懂，估计是沟通邪神用的吧？”
“为什么他们想跟自己信仰的神明沟通还那么费劲，还得借助祭坛？”
“大概是邪神看不上这些家伙，懒得搭理他们吧！”
“血牙帮背后也有位邪神在作乱，那他们的据点里应该也有类似的祭坛吧？”
“很有可能！”
“那我们只要把那座祭坛摧毁了，是不是邪神威胁就解除了？”
“我觉得你说的有道理！”
“话说既然这祭坛跟邪神有关，我们靠这么近不会被邪神注视吗？”
“怕什么，血牙帮走狗都被我们干掉那么多了，也没见他们背后的邪神来找我们麻烦啊！”
培特眼角抽搐地看着同伴们纷纷凑上前去，围着祭坛左摸摸右看看。
别说敬畏害怕了。
这帮家伙分明是已经开始琢磨起该怎么拆了！
……


## Output Format
Return ONLY valid JSON matching this schema:
{
  "chapter_number": 55,
  "chapter_title_vi": "Chương 55: <Vietnamese title>",
  "segments": [
    {
      "segment_id": "XXXX",
      "source": "...",
      "target": "..."
    }
  ]
}
