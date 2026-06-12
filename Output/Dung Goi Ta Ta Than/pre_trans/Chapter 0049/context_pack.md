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
te chấn động: Thần Tri Thức có thể vòng qua các chủ thần, ban trực tiếp lộ trình tu luyện có thanh tiến độ

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


## Source Chapter 49 - 0049 绝佳机会
# 第49章 绝佳机会

是夜。
夜幕的掩护下，下城区的邪恶正蠢蠢欲动。
“开门！开门！”
一名血牙帮混混正猛烈地砸着一户民居的大门。
眼看过了几分钟还是没有回应。
“不用喊了，上家伙！”
另一名混混提着锤斧，三下五除二将房门钻了个大洞，直接破门！
两个混混大摇大摆地走了进去。
“血牙帮办事！”
屋内一对年轻男女正面色惊恐地抱在一起躲在角落。
“该还钱了！今天再拿不出钱来，别怪我们不客气啊！”
混混凶神恶煞地威胁道。
年轻女子声音里带着哭腔：
“两位大哥，求求你们再宽限两天吧，就两天。”
“我们现在真的没钱了，两天后才能发工钱，到时候我们一定还钱，再饶我们这一回行吗？”
血牙帮混混轻蔑笑道：“上回已经宽限了你们5天，利上加利，你们现在已经欠了2枚金币外加81块银币，再给你们两天就能把钱还上了？”
年轻女子顿时面露绝望。
“怎么会这么多，上回不是还只有2枚金币吗？”
“废话！多的那些是利息，还有大爷我过来催债的跑腿费！”血牙帮混混恶狠狠道。
这对儿年轻夫妇，之前男人生了场病，为了请辉光神教的牧师使用神术治疗，需要50块雷亚克银元。
两人拿不出那么多钱，走投无路的时候，血牙帮的人出现了。
可以借钱给他们，不过要收取利息。
为了治病，年轻女子只能咬着牙答应下来，打算等男子治好病后努力干活还债，结果血牙帮却压根没打算让他们还得起债务，辛辛苦苦赚来的钱，连利息都填不上！
几次三番的催债下来，俩人几乎变卖了所有能卖的东西，债务还是不见变少，反而越来越多。
“两位大哥，我们实在是没有那么多钱……”年轻女子哭着求饶道。
血牙帮混混闻言，仿佛早有预料似的，不怀好意地看向女子。
虽然穿着十分朴素，但依然能看出对方那曲线优美的身体。
“嘿嘿，拿不出钱，也有别的办法。”
“跟我们走一趟，黑市最近缺人了，刚好，你去上几天班，就给你把债务免去一半，怎么样，够划算吧？”
说着，混混从衣服口袋里掏出个皮质项圈，丢到女子面前。
年轻夫妇的脸色变得难看起来。
让她去黑市，做什么还用说吗？
眼看年轻女子抗拒无比，混混正欲走上去强行将对方拉走时，却忽然感觉自己的肩膀被人从后面轻轻拍了下。
“谁？”
混混回过头去。
映入视线的是一位身形壮实的年轻男子。
布兰登微笑着开口确认道：“你们两个是血牙帮的，对吧？”
混混下意识地一点头，条件反射般：“废话！看不出来血牙帮在办事……”
“砰！”
附带着怒气的拳头狠狠地招呼到了混混的脸上！
英勇打击！小子！
带着血沫的一颗牙齿被打飞出去。
乍一下挨了记狠的，血牙帮混混先是被打得整个人一懵，旋即勃然大怒！
从来都只有他们血牙帮的人在下城区欺负别人，何时还能被人给打了？      这他能忍？
他刚在血色轮盘接受了秘术，实力大增，正是自信心膨胀的时候！
“不是，你特么……”
正欲激活体内的那股燥动能量发起反击，好好给对方个教训时，混混却看到那被破开的大门外，一个接一个的人们鱼贯而入，很快便将这不大的屋子挤得满满当当。
“……特么……您是什么来头？”
混混的嚣张气焰顿时就萎了下去。
布兰登懒得搭理对方，挥手号召道：
“没跑了！这俩家伙也是血牙帮的！”
“朋友们，老规矩，排队啊！一人一下，平分贡献，不准多打！”
“还有，千万注意别直接打死了，不然后面的人就拿不到正义点数了！”
“上回有个憨货，下手那么重，直接给人弄死了，简直血亏！”
众人轰然响应：
“嗷！明白！”
“好嘞！”
“大伙效率一点，这才第二批，听说培特那边的队伍已经收拾完第三批血牙帮的人了，我们落后了！”
跟先前的情景几乎完全一致，两名血牙帮的混混先是试图反抗。
勉强用体内那股能量击倒了几个人，随后便彻底被人海战术淹没。
别看求知教派的成员们暂时没有足够的肉体强度支撑，造成的伤害不高，但驾驭怒气或掌握基础的魔法后，至少他们的攻击是可以稳定产生效果的！
相当于即使不破防也能最少造成1点伤害的保底输出！
密密麻麻如雨点般的拳脚落下，很快，这两个血牙帮的抵抗越来越微弱，燥动的能量也越来越少，直到最终彻底晕死过去，完全无法再提供正义点数。
屋内先前那对走投无路的年轻夫妇此刻已经是完全呆滞的状态。
他们看到了什么？
先前对他们来说无法反抗的血牙帮混混，现在被人打得跟死狗一样？
这是他们梦中的场景照进现实了吗？
“感谢救了我们……请问……你们是……”
年轻女子小心翼翼地询问。
布兰登礼貌笑道：“求知教派，我们为维护下城区的安全而来！”
“如果再有血牙帮的人来骚扰你们，欢迎去莫尼兄弟酒馆寻求帮助。”
……
与此同时，类似的场景，在下城区的各处轮番上演着。
酒馆商议好后，求知教派的众人分成了三组，分别由培特、蕾娜、布兰登带队，沿不同的方向寻找“落单”的血牙帮成员。
夜晚总是血牙帮混混作恶的高峰期。
他们用着各种各样的方式，破坏下城区的安定秩序。
给急需用钱的穷人放贷，然后强行收取对方根本还不起的高额利息，榨干对方的所有财产，最后再逼迫着男人去给帮派打黑工、女人就拉去黑市或其他血牙帮控制的服务场所，这就是他们最常用的手段。
血牙帮的成员获得了强大力量后，行事更是肆无忌惮，根本不掩饰动静。
原本需要5、6个人一起行动的任务，现在只要有1、2个人就敢上门强闯闹事。
不过，这恰好为求知教派的众人提供了将他们各个击破击破的绝佳机会！
倘若血牙帮还像过去那样抱团，他们对付不了那么多敌人，甚至要反过来担心别被血牙帮找上门来。
可若是只有落单的那么1、2个人？
攻守之势异也！
……


## Output Format
Return ONLY valid JSON matching this schema:
{
  "chapter_number": 49,
  "chapter_title_vi": "Chương 49: <Vietnamese title>",
  "segments": [
    {
      "segment_id": "XXXX",
      "source": "...",
      "target": "..."
    }
  ]
}
