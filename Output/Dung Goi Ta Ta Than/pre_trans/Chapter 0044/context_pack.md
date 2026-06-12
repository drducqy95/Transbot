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
p ba: thừa kế tước vị.
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


## Source Chapter 44 - 0044 诱敌深入！
# 第44章 诱敌深入！

势大力沉的一拳带着呼啸的破风声袭来，蕾娜躲闪不及，勉强微侧了下身子避开要害部位。
“嘭！”
遭到重击的蕾娜眼冒金星，脑子里嗡嗡作响，剧烈的疼痛让她根本没法再集中起精神。
“咳……咳咳……”
蕾娜接连咳嗽几声，还没来得及恢复，又是迎面一拳砸来！
“嘭！”
这回蕾娜没能闪开，当场被打飞出去，砸碎了张酒馆的木桌，身上的粗布短衫胸口位置都被划出几道口子，露出里面的一抹白嫩。
领头的混混却对其视若无睹，因为自从在血色轮盘接受了那股燥动的能量后，他就感觉自己的脾气变得越发暴躁，越来越不愿意动脑思考。
而且只要动起手来，就会有一种想要将面前一切都毁掉的冲动感。
……
血牙帮混混的实力突然大幅变强，直接导致蕾娜的计划出现了巨大问题。
她本想靠偷袭解决一人后，将其他几人引诱出去，然后甩开他们或利用潜行的隐匿能力逐个击破。
然而现在她却自身难保。
敌人超过普通人的身体素质，成了计划中的变数。
5名敌人数量，更是让本就不平衡的局面雪上加霜！
以蕾娜现在的状态，别说5个人了，哪怕让她一对一的应付其中一人都相当困难。
因为严格意义上来说，蕾娜虽然通过诺文给予的知识，快速学会了【潜行】战技，可以被认为1阶潜行者。
但她目前的真实实力还远远算不上1阶的水准。
实力的构成，分为“基础”和“技巧”两个部分。
基础部分，对战士、潜行者、游侠这些职业路线来说，代表着身体的综合素质，比如体格是否强健、动作是否灵巧、反应是否快速；
当然，如果法师、术士、牧师这些，还需要考察精神是否充裕，脑子是否聪明。
技巧部分才是考验对各种战技、魔法、神术的掌握情况。
诺文给予信徒们的知识让他们能够快速达成对其他人来说最难的“技巧”部分。
只要照着知识的引导便能一步步上手掌握。
但基础的部分却是诺文现在暂时没法改变的硬伤！
这些东西，要么靠神明的神力赐福，要么靠凡人自己长期的锻炼。
前者诺文做不了，后者不存在难度门槛，但却需要时间去积累！
空有技巧，没有基础，遇到血牙帮混混这种“基础牢固”的敌人时，就会出现攻击不破防的尴尬情况。
亲眼看见女儿受到伤害，老莫尼藏不下去了。
担心女儿被打出事来，老莫尼本能地决定要靠着牺牲自己来吸引几名混混注意。
“别伤害我女儿！有什么事都冲我来！不然我跟你们拼……”
老莫尼话没说完，千钧一发之际，酒馆外突然传来一声爆喝：
“Arcane Missiles！！！”
三颗散发着明亮紫光的梭形飞弹在空中划过优美的弧形曲线，同时命中那正步步朝着蕾娜逼近的领头混混。
“蕾娜别怕，我们来帮你了！！！”
赶到酒馆的培特和盖尔两人，刚好碰上正在爆发的冲突。
培特当时便是眼冒精光。
这不就是限定活动要求里的“犯罪行为”吗？
二话不说，吟唱出一发【奥术飞弹】直接招呼上去！
旁边的盖尔看到培特那熟练的施法动作，羡慕的眼神都快拉丝了！
他也想掌握攻击魔法，挥挥手就能放出强大的攻击，轻松写意地击败敌人。
苦于天赋有限，以前的他跟培特一样，顶多学会些简单的辅助向、生活向的魔法，根本研究不明白攻击向的魔法。
虽然现在他也成了求知之神诺文的信徒，但手头只有新人福利的10知识点数，想兑换1阶魔法却需要足足15知识点数。
想起限定活动的相关奖励。      盖尔看向血牙帮混混们的眼神顿时也变得火热起来。
这哪里是敌人，这分明是行走的正义点数啊！
不过，领头的混混在硬挨了一记【奥术飞弹】的冲击后，虽然被巨大的冲击力打得踉跄了好几步，身形不稳，但没有像上回那样直接被击倒失去战斗能力，反倒是面露凶光，气势更胜。
培特顿觉不妙。
情况跟他预想的好像不太一样！
上回他收拾这些混混时，【奥术飞弹】挨个点名，一下一个。
可这次对方的实力却变强了许多！
普通人被奥术能量凝聚成的飞弹打中，最少也是当场被击晕。
现在他们却能硬挨一记法术还有战斗能力，意味着对方的身体强度少说也是1阶的水平！
“哼哼……我记得你！上回就是你这个法师坏了我们好事！”
领头混混的暴虐气息越发严重，只觉腹中那股燥动的能量越来越难以压抑，将对方撕碎的念头更是越来越强烈。
没法思考，失去理智，只想着把眼前的敌人给撕碎毁灭。
之前那次冲突的时候，他们就跟培特结下了梁子。
这回再度碰上，自然是冤家路窄！
“就你是法师是吧？就你会魔法是吧？再放一个试试啊？”
领头混混用力拍着自己的脑壳，凶神恶煞地威胁道。
酒馆里，蕾娜努力吸了口气，大声提醒道：
“培特先生，他们现在很强，小心！”
她连续遭到几次攻击，现在浑身跟散架了一样，五脏六腑都在传来剧痛，连站起来都很困难，只能将希望寄托于培特身上。
这几天经历了不少事情的培特也算有了些成长，现在已经不会再慌张到六神无主，能维持足够理智去冷静地寻找破局的办法。
思维急转。
“用那个3阶法术？”
“不行，那个法术的吟唱时间太长，根本来不及释放怕是就会被他们贴身打断。”
“这些混混不知怎的实力暴涨！”
“距离太近，正面跟他们对拼的话，我可能顶多解决2、3个！”
对比双方的实力，手头可用的办法似乎都无法破局。
若是换了一般人，可能这时候已经在想该用什么姿势求饶比较好了。
培特……自然不是一般人。
他选择果断开祷！
……
“伟大的求知之神！”
“请告诉您忠实的信徒，我该怎么做才能解决眼前的麻烦！”
早在当初审讯室里的时候，培特就已经发现：求知之神的力量不但能给予知识，还能给予信徒需要的信息！
当他遇到麻烦的时候，解决方案同样是一种“信息”。
收到“需求1知识点数”的提醒后，培特毫不犹豫地消耗点数将其兑换！
【建议方案：诱敌深入！】
快速看完神谕的内容，培特心中大定。
“不愧是求知之神！”
有办法了！
……
感谢：路过看看000，Hank2016，冷蚕投出的1张月票，感谢恋心C投出的2张月票，感谢各位投出推荐票的书友，蟹蟹支持。


## Output Format
Return ONLY valid JSON matching this schema:
{
  "chapter_number": 44,
  "chapter_title_vi": "Chương 44: <Vietnamese title>",
  "segments": [
    {
      "segment_id": "XXXX",
      "source": "...",
      "target": "..."
    }
  ]
}
