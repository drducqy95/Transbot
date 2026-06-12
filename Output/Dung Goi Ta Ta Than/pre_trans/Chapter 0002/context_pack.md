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
h dùng mới của Điểm Tri Thức

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


## Source Chapter 2 - 0002 天崩开局
```json
[
  {
    "segment_id": "0001",
    "text": "# 第2章 天崩开局"
  },
  {
    "segment_id": "0002",
    "text": "诺文心情复杂地通过神之眼注视着他的这批“信徒”。"
  },
  {
    "segment_id": "0003",
    "text": "他觉得这个世界的凡人似乎对他有什么误会。"
  },
  {
    "segment_id": "0004",
    "text": "通过这些黑袍人们祈祷提供的信仰之力，让诺文搞清楚了他拥有的神职权能。"
  },
  {
    "segment_id": "0005",
    "text": "黑袍人所请求的“哈达的饥渴之力”，实际上是一种通过构筑法术模型而施放的，名为【哈达之饥渴】的强力魔法。"
  },
  {
    "segment_id": "0006",
    "text": "诺文投下注视接收了信徒的祷告，便在一瞬间无师自通地掌握了有关这道法术的全部知识，从其诞生发展到现在的各种变种、优化、进阶等信息全部一清二楚，尽在掌握，无论理解还是熟练度都直接达到冠绝于世的顶级程度。"
  },
  {
    "segment_id": "0007",
    "text": "并且只要他消耗一部分神力，可以直接将知识和力量快速传授给他的信徒。"
  },
  {
    "segment_id": "0008",
    "text": "哪怕信徒是个从未尝试过施法的门外汉，也能通过这种神赐的力量立马成为熟练掌握该法术的顶级大师。"
  },
  {
    "segment_id": "0009",
    "text": "诺文寻思着，他的神职权能简直强的离谱，要知道这对普通的凡人来说，相当于是跳过了原本漫长的研究、学习、熟练的过程，甚至可以无视天赋等各种外界条件限制，只要神明赐下力量，凡人便能直接完全掌握相关的技能。"
  },
  {
    "segment_id": "0010",
    "text": "可问题的关键就在这里。"
  },
  {
    "segment_id": "0011",
    "text": "照理来讲，这种宛若作弊般的神明伟力，明明应该受到大量的凡人追捧才对。"
  },
  {
    "segment_id": "0012",
    "text": "可在诺文的神觉感知里，除了那些可能仅仅只是无意间提起跟他相关的信息才被他接收到的“祈祷声”，此刻只有这群被他投下神之眼注视的，俨然一副邪教徒做派的黑袍人们，在指向性非常明确地向他发出祈祷。"
  },
  {
    "segment_id": "0013",
    "text": "事出反常必有妖，诺文隐隐觉得似乎有哪里不太对，但他一时又说不上来。"
  },
  {
    "segment_id": "0014",
    "text": "……"
  },
  {
    "segment_id": "0015",
    "text": "地下洞窟的仪式现场，为首的黑袍人感受到一阵不同于他们往常祈祷献祭时的神力波动，顿觉激动，惊喊出声："
  },
  {
    "segment_id": "0016",
    "text": "“兄弟姐妹们！伟大的全知之父！祂终于回应了我们！我感觉到了！我感觉到了祂的注视！”"
  },
  {
    "segment_id": "0017",
    "text": "“为了伟大的主，我等愿意献出一切！遵从主的指引！请引领我们，见证世界的真相！”"
  },
  {
    "segment_id": "0018",
    "text": "看着这群黑袍人虔诚的样子，诺文做出了决定："
  },
  {
    "segment_id": "0019",
    "text": "“邪教徒就邪教徒！至少这些人能够为我提供信仰之力！有了更多的信仰来源，才能扩张教派。”"
  },
  {
    "segment_id": "0020",
    "text": "“何况邪教徒又不是不能引导他们去向善，力量本身又没有善恶之分，重要的肯定是如何去使用！”"
  },
  {
    "segment_id": "0021",
    "text": "在这个有神明存在的世界里，信徒和神灵的关系是双向的。"
  },
  {
    "segment_id": "0022",
    "text": "神灵需要信仰来维持存在，凡人则需要神明赐福的力量。"
  },
  {
    "segment_id": "0023",
    "text": "凡人可以选择向对应的不同神明提供信仰，通过虔诚的祈祷或者仪式，有机会得到神明的赐福。"
  },
  {
    "segment_id": "0024",
    "text": "同时，凡人也要遵守神明的指引或戒律，否则的话，神明亦可随时选择收回他给予的神力，不再接受这名凡人的信仰。"
  },
  {
    "segment_id": "0025",
    "text": "当然，在这份双向选择的关系里，毫无疑问，神明会占据更多的主动权。"
  },
  {
    "segment_id": "0026",
    "text": "如果信徒的行事不符合神明的要求，随时可以单方面地将其“拉黑”，神明损失的只是一个信仰之力来源，而信徒则可能会立刻失去大部分的力量。"
  },
  {
    "segment_id": "0027",
    "text": "诺文此刻便是抱了类似的想法。"
  },
  {
    "segment_id": "0028",
    "text": "如果这个世界的凡人真的对他的形象有什么误会，那他大可从接纳这批黑袍人开始，给予他们力量，然后再通过指引他们的行动，来逐渐改善诺文的风评！"
  },
  {
    "segment_id": "0029",
    "text": "“先从这个领头的家伙开始，看看赐予神力的效果。”      诺文尝试着建立起他与信徒间神力通道，一阵虚幻的波动过后，诺文将他的力量灌注入了为首的黑袍人体内。"
  },
  {
    "segment_id": "0030",
    "text": "“我已经看到了！这个世界的真实，是的，我亲眼目睹了一切……呃……呃啊……！”"
  },
  {
    "segment_id": "0031",
    "text": "黑袍人声音中满是狂喜地接收着来自神明的力量时，异变突生。"
  },
  {
    "segment_id": "0032",
    "text": "只见他黑袍下的身体毫无预兆地胀大起来，原本有些瘦削的身形，在短短数秒时间里，膨胀到足足4、5米高，无数凭空快速增生的腐败血块与丑陋的肉瘤撑破了黑袍，伴随着痛苦的惨叫声，血肉层层堆叠，数不清的眼球，口器与触手在它可怖的躯体上生长。"
  },
  {
    "segment_id": "0033",
    "text": "这一刻，诺文的沉默震耳欲聋。"
  },
  {
    "segment_id": "0034",
    "text": "他终于意识到了他先前觉得不对劲的地方究竟是什么："
  },
  {
    "segment_id": "0035",
    "text": "“坏了，不是这个世界对我的认识有误会，而是我好像对自己的认知有误解。”"
  },
  {
    "segment_id": "0036",
    "text": "“难怪只有这些家伙愿意向我献上信仰，合着原来我自己是邪神本神！”"
  },
  {
    "segment_id": "0037",
    "text": "他所谓的知识与启蒙的神职权能，的确可以在得到信徒的相关诉求时，瞬间了解并掌握知识，学会技能。可是伴随着神力的传输，诺文能明显感受到他的力量中还有着一股混乱无序的气息！"
  },
  {
    "segment_id": "0038",
    "text": "诺文身为神灵不会受其影响，但对凡人来说，这股混乱气息的冲击足够瞬间摧毁他们的心智，导致凡人发生严重的畸变，变成失去理智的怪物！"
  },
  {
    "segment_id": "0039",
    "text": "仪式现场的黑袍人们目睹带头人转化成怪物的一幕，产生了截然不同的两种反应。"
  },
  {
    "segment_id": "0040",
    "text": "更靠近祭坛的几个成员情绪变得更加疯狂，纷纷狂热高喊起来："
  },
  {
    "segment_id": "0041",
    "text": "“伟大的主终于苏醒了！”"
  },
  {
    "segment_id": "0042",
    "text": "“回归父神怀抱！”"
  },
  {
    "segment_id": "0043",
    "text": "“所有的未来都将向我们敞开大门！”"
  },
  {
    "segment_id": "0044",
    "text": "几个黑袍人一边声嘶力竭地叫喊着，一边狂热跪拜着那只刚刚完成转化的丑陋畸变体。"
  },
  {
    "segment_id": "0045",
    "text": "甚至还有彻底疯狂的，主动冲进了畸变体的“怀抱”。"
  },
  {
    "segment_id": "0046",
    "text": "一阵让人毛骨悚然的骨骼混合着血肉被压碎、咀嚼的声音响起，新鲜的人体被融入其中，畸变怪的身躯变得更加庞大，更多的触手源源不断地从它体内长出，不断向四周挥舞，尝到甜头让它开始兴奋地寻找着新的原料。"
  },
  {
    "segment_id": "0047",
    "text": "至于那些比较外围的黑袍人则是一片鬼哭狼嚎，吓得瑟瑟发抖，个别胆小的甚至能从黑袍上看到可疑的水渍。"
  },
  {
    "segment_id": "0048",
    "text": "这场面简直包含了一切反派邪神该有的要素。"
  },
  {
    "segment_id": "0049",
    "text": "那些争着抢着要变成怪物的，连自己的命都愿意献祭给神，明显是已经没救了的狂热癫佬；"
  },
  {
    "segment_id": "0050",
    "text": "那些快被吓破胆的，则大概率是一群不知情的倒霉蛋，被骗过来准备连带着一同献祭给诺文。"
  },
  {
    "segment_id": "0051",
    "text": "诺文的传教事业迎来了标准的天崩开局！"
  },
  {
    "segment_id": "0052",
    "text": "……"
  },
  {
    "segment_id": "0053",
    "text": "18:00准时投放更新，改状态前每天1更，改状态后公众章节期间每天2更，上架入V会开始稳定爆更。"
  }
]
```

## Output Format
CRITICAL INSTRUCTION: You MUST translate the source text EXACTLY paragraph by paragraph, preserving the original order perfectly. DO NOT skip, drop, merge, or reorder any paragraphs. Each paragraph in the source MUST be translated.
Return ONLY valid JSON matching this schema:
{
  "chapter_number": 2,
  "chapter_title_vi": "Chương 2: <Vietnamese title>",
  "segments": [
    {
      "segment_id": "XXXX",
      "source": "...",
      "target": "..."
    }
  ]
}
