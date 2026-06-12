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
ter 0034 - Chương 34: Những hạt giống đầu tiên

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

## Chapter 0055 - Chương 55: Tế đàn tà thần? Có thể phá không?

### Summary
Chapter 55 completed via pipeline.

## Chapter 0056 - Chương 56: Chuyên tinh và kiêm tu

### Summary
Chapter 56 completed via pipeline.

## Chapter 0057 - Chương 57: Trình mô phỏng tu hành đã ra mắt!

### Summary
Chapter 57 completed via pipeline.

## Chapter 0058 - Chương 58: Cấp độ huyền thoại

### Summary
Chapter 58 completed via pipeline.

## Chapter 0059 - Chương 59: Nữ thần Ma pháp, chó cũng không thèm tin

### Summary
Chapter 59 completed via pipeline.

## Chapter 0001 - Chương 1: Xuyên không thành tà thần thì phải làm sao

### Summary
Chapter 1 completed via pipeline.

## Chapter 0002 - Chương 2: Khởi đầu nát bét

### Summary
Chapter 2 completed via pipeline.

## Chapter 0003 - Chương 3: Pete Chinar

### Summary
Chapter 3 completed via pipeline.


## Source Chapter 3 - 0003 培特奇纳尔
```json
[
  {
    "segment_id": "0001",
    "text": "# 第3章 培特奇纳尔"
  },
  {
    "segment_id": "0002",
    "text": "“不对不对，让我好好理顺下这个过程，到底是哪个步骤有问题才产生的异变！”"
  },
  {
    "segment_id": "0003",
    "text": "第一次回应信徒发生了完全没有预料到的意外情况，诺文试图复盘这个过程。"
  },
  {
    "segment_id": "0004",
    "text": "“第一步，信徒向我发出祈祷，我可以选择接听或无视，没问题。”"
  },
  {
    "segment_id": "0005",
    "text": "“第二步，如果接收了信徒传递给我的信息，我就能凭借权能瞬间掌握有关信徒所想要的事物的一切相关信息，这个也没问题。”"
  },
  {
    "segment_id": "0006",
    "text": "“第三步，我可以选择回应信徒，通过消耗神力把相关能力……”"
  },
  {
    "segment_id": "0007",
    "text": "“哎？等等，不对！”"
  },
  {
    "segment_id": "0008",
    "text": "回忆到导致发生异变的步骤时，诺文突然察觉到一个之前被他所忽略掉的问题。"
  },
  {
    "segment_id": "0009",
    "text": "“我原本以为神力赐予的效果是直接将对应的能力传输给信徒，就像灌顶传功一样，能直接让普通人变成绝世高手。”"
  },
  {
    "segment_id": "0010",
    "text": "“但是……实际上的效果，好像并不是让普通人能跟我一样瞬间掌握相关能力，而是给了他们一个可以随时使用的许可！”"
  },
  {
    "segment_id": "0011",
    "text": "“对了！这个过程中信徒需要神力的部分应该并非学习，而是使用！”"
  },
  {
    "segment_id": "0012",
    "text": "诺文顿时豁然开朗。"
  },
  {
    "segment_id": "0013",
    "text": "凭借着前世各种科技产品使用出来的经验，让诺文意识到了两者间的区别。"
  },
  {
    "segment_id": "0014",
    "text": "诺文赐予给信徒的能力，并非面对面快传直接将相关的能力交给信徒，他真正给予信徒的，只是一个允许信徒使用能力的“许可凭证”。"
  },
  {
    "segment_id": "0015",
    "text": "即使信徒自身并没有掌握相关的能力，有了这个许可凭证，就可以通过消耗诺文的神力，来完成对应的施法！"
  },
  {
    "segment_id": "0016",
    "text": "如果打个比方来形容，在诺文以前的世界，普通人并不需要懂得手机的运行原理，但只要按下对应的按键，所有实际的运算实际是由幕后的硬件来完成，呈现在普通人面前的只是最终的结果！"
  },
  {
    "segment_id": "0017",
    "text": "“所以，其实这个世界所谓的神明给凡人赐予力量，或许真相是凡人借助那位神明的神力才临时拥有了使用的权限，并没有真正获得切实的能力……”"
  },
  {
    "segment_id": "0018",
    "text": "“……然后，因为我这种邪神的神力中有大量混乱危险的气息，凡人向我发送借助我的神力完成施法的请求时，我所消耗的神力顺着这一请求影响到了凡人，于是才会导致发生畸变！”"
  },
  {
    "segment_id": "0019",
    "text": "“如果是这样的话，有办法破局了！”"
  },
  {
    "segment_id": "0020",
    "text": "……"
  },
  {
    "segment_id": "0021",
    "text": "一片狼藉的阴森地下洞窟中。"
  },
  {
    "segment_id": "0022",
    "text": "培特·奇纳尔此时的想法就是后悔，非常后悔！"
  },
  {
    "segment_id": "0023",
    "text": "他先前一定是鬼迷了心窍，怎么就想不开，偏偏信了那个黑袍人的邪！"
  },
  {
    "segment_id": "0024",
    "text": "几小时前他还是个卡罗恩学院奥法学派拖低平均水平的吊车尾，为了想办法掌握一个三阶法术而绞尽脑汁，头疼不已。"
  },
  {
    "segment_id": "0025",
    "text": "可是现在怎么就一下卷入到生死存亡的危险境地了呢！"
  },
  {
    "segment_id": "0026",
    "text": "看着眼前这已经靠着不断吞食人类而成长为庞然大物，满是肉瘤、口器和眼球的恐怖血肉怪物正在挥舞着触手，仿佛猫戏老鼠一般，没有直接将剩下的最后几名“食物”卷走撕碎，而是一步步地慢慢压缩着他们的生存空间。"
  },
  {
    "segment_id": "0027",
    "text": "培特没吓的当场失禁已经是他胆子大了！"
  },
  {
    "segment_id": "0028",
    "text": "几天前他在布告板上看到一则消息，说是有办法让人快速掌握三阶法术成为高级施法者，而且最重要的是，上面说了只要条件匹配，即使对魔法女神的亲和度不够也没有关系。"
  },
  {
    "segment_id": "0029",
    "text": "培特也是病急乱投医，还真就信了这上面的鬼话，循着消息留下的联系方式在对应时间来到了接头地点，有个神神秘秘的黑袍人在得知他的来意后，让他也披上黑袍，要带他去所谓的“秘密集会”。      结果现在亲眼目睹那个给他领路的黑袍人已经变成了那只可怕畸变怪的“身体组成部分”，培特哪里还不知道他是上了贼船！"
  },
  {
    "segment_id": "0030",
    "text": "“魔法女神在上！不对，管他哪个神也行，谁能来救救我啊！”"
  },
  {
    "segment_id": "0031",
    "text": "培特对他自己是个什么水平有着清晰的认知，让他去当个学院派法师糊弄糊弄考核，装模作样搞个魔法研究还行，真要让他去实战？快别开玩笑了！"
  },
  {
    "segment_id": "0032",
    "text": "他可能连个一阶水平的小魔物都打不过，更何况眼前这个光凭气势压制培特感觉就少说得有三阶的畸变怪！"
  },
  {
    "segment_id": "0033",
    "text": "一阶评级的职业者通常就可以轻松撂倒正常体格的健壮成年人，更不用说三阶评级，若是在一些普通人生活的小村子，这种级别的怪物是有屠村威胁的，必须要筹集重金请动附近的教会或者高阶职业者来讨伐才有可能消灭。"
  },
  {
    "segment_id": "0034",
    "text": "就在培特·奇纳尔已然心如死灰，准备想个还算体面的姿势闭眼等死的时候，他的脑海中忽然响起一道清脆的声音："
  },
  {
    "segment_id": "0035",
    "text": "【叮！】"
  },
  {
    "segment_id": "0036",
    "text": "【检测到信徒正面临巨大危险，正在查找解决方案。】"
  },
  {
    "segment_id": "0037",
    "text": "【查找完成，任务已发布。】"
  },
  {
    "segment_id": "0038",
    "text": "【任务目标："
  },
  {
    "segment_id": "0039",
    "text": "学习法术[哈达之饥渴]（当前进度：0%）"
  },
  {
    "segment_id": "0040",
    "text": "消灭神孽畸变怪（当前进度：0/1）】"
  },
  {
    "segment_id": "0041",
    "text": "脑海里突然冒出的信息，先是让培特大喜过望，以为是哪位特别的神明真的收到他的求助，又看他顺眼，打算赐下力量帮他度过危机，结果等看完实际内容，培特心直接凉了半截。"
  },
  {
    "segment_id": "0042",
    "text": "“不是？我？让我现在当场学三阶法术？”"
  },
  {
    "segment_id": "0043",
    "text": "培特从来没有如此因为他和魔法女神的亲和度太低而感到后悔，他虽然是魔法女神的浅信徒没错，但从魔法学徒开始，他花了将近三年时间，最高也才堪堪学会释放几个二阶魔法，还都是些类似【秘法锁】、【侦测思想】之类的辅助魔法。"
  },
  {
    "segment_id": "0044",
    "text": "唯一能称得上可以用于战斗的只有个【蛛网术】，可是这法术也仅仅只有限制敌人的效果，几乎没有攻击性。"
  },
  {
    "segment_id": "0045",
    "text": "在这个世界，对正常的凡人来说，想要学习各种魔法，需要向传说中的魔法女神献上信仰，信徒与魔法女神的亲和度越高，越容易清晰地调动魔网来释放法术，反之，倘若亲和度不够高，那魔网在信徒的感知里就会模模糊糊，难以捉摸，越高阶复杂的法术便越难以成型。"
  },
  {
    "segment_id": "0046",
    "text": "培特就是个亲和度不够的典型，他想成功释放出一个二阶魔法都得花费好几个月的时间才能勉强摸到方法，三阶更是直接毫无头绪，根本不知从何尝试。"
  },
  {
    "segment_id": "0047",
    "text": "结果眼下这位不知名的神明发来的信息，却试图让他现在掌握一个真正的三阶攻击性魔法！"
  },
  {
    "segment_id": "0048",
    "text": "“不知道哪位神明大人在上！我也很想照您说的去自救，可我真的做不到！能不能请您换个方法啊！”培特绝望地在脑海中呐喊。"
  },
  {
    "segment_id": "0049",
    "text": "下一瞬间，更多的信息涌现在培特的脑海。"
  },
  {
    "segment_id": "0050",
    "text": "“这是？！”"
  },
  {
    "segment_id": "0051",
    "text": "……"
  },
  {
    "segment_id": "0052",
    "text": "可以投推荐票吗，那对我真的很重要，谢谢！"
  }
]
```

## Output Format
CRITICAL INSTRUCTION: You MUST translate the source text EXACTLY paragraph by paragraph, preserving the original order perfectly. DO NOT skip, drop, merge, or reorder any paragraphs. Each paragraph in the source MUST be translated.
Return ONLY valid JSON matching this schema:
{
  "chapter_number": 3,
  "chapter_title_vi": "Chương 3: <Vietnamese title>",
  "segments": [
    {
      "segment_id": "XXXX",
      "source": "...",
      "target": "..."
    }
  ]
}
