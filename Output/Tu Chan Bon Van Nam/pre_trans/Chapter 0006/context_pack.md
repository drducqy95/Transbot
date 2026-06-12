# Translation Context Pack

## Project
- Branch: Tu Chan Bon Van Nam
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
N/A

## Glossary
N/A

## Story Timeline (latest)

## Chapter 0001 - Chương 1: Nghĩa địa pháp bảo

### Summary
Chapter 1 completed via pipeline.

## Chapter 0002 - Chương 2: Quang mạc nghi

### Summary
Chapter 2 completed via pipeline.

## Chapter 0003 - Chương 3: Dị mộng

### Summary
Chapter 3 completed via pipeline.

## Chapter 0004 - Chương 4: Yêu Đao Bành Hải

### Summary
Chapter 4 completed via pipeline.

## Chapter 0001 - Chương 1: Nghĩa địa pháp bảo

### Summary
Chapter 1 completed via pipeline.

## Chapter 0002 - 0002 光幕仪

### Summary
Chapter 2 completed via pipeline.

## Chapter 0003 - Chương 3: Dị mộng

### Summary
Chapter 3 completed via pipeline.

## Chapter 0005 - Chương 5: Thi thử đại học

### Summary
Chapter 5 completed via pipeline.


## Source Chapter 6 - 0006 大黑暗时代
```json
[
  {
    "segment_id": "0001",
    "text": "# 第6章 大黑暗时代"
  },
  {
    "segment_id": "0002",
    "text": "李耀的睫毛一抖，脸色有些凝重，“大黑暗时代”是修真文明发展过程中最重要的一个时期，甚至可以说正是大黑暗时代划分了“古典修真时期”和“现代修真时期”，这是一道非常经典的问题，人尽皆知，却不容易回答全面。"
  },
  {
    "segment_id": "0003",
    "text": "沉吟片刻，李耀心思电转，神念飞扬："
  },
  {
    "segment_id": "0004",
    "text": "“古代修真者以永生不死为目标，创造出无比辉煌的古修文明，他们建立了从炼气、筑基到结丹、元婴……直至渡劫、真仙、不朽的升级体系，并且沿着这条道路勇往直前，不断开拓生命的极限，迈向无尽的星辰大海。”"
  },
  {
    "segment_id": "0005",
    "text": "“在古修文明的全盛时期，古修们开辟了一处又一处大千世界，构筑了贯穿无尽星海的古传送阵，在星辰和世界之间任意穿梭，甚至开始探索时间的终极奥秘！”"
  },
  {
    "segment_id": "0006",
    "text": "“随着古修文明不断进化，古代修真者变得越来越强大，越来越长寿，强者的数量也越来越多。”"
  },
  {
    "segment_id": "0007",
    "text": "“在古修文明早期，三千世界中只有数百名金丹期修真者，几十名元婴期修真者，至于‘化神老怪’、‘渡劫真君’都是闻所未闻，几十个世界、几千年时间才有可能出现一个，绝对是凤毛麟角的存在！”"
  },
  {
    "segment_id": "0008",
    "text": "“可是到了古修文明后期，如同大爆炸一般，高阶修真者以几何级数倍增——在当时，有‘元婴多如狗，化神满地走’的说法。”"
  },
  {
    "segment_id": "0009",
    "text": "“如此之多的高阶修真者，都需要庞大的资源来修炼，再加上越来越多的修真者达到了近乎永生不朽，他们对资源的渴求也达到了——无穷无尽！”"
  },
  {
    "segment_id": "0010",
    "text": "“一开始，还可以通过开发新的大千世界来满足贪婪的高阶修真者，可是经过上万年的开发，发现了将近五千个世界之后，有整整一千年，古修文明没能再发现哪怕一个新的大千世界。"
  },
  {
    "segment_id": "0011",
    "text": "“世界是有限的，而修真者的索求是无限的——古修们用一千年时间，明白了这个真理，顺理成章，为了争夺有限的资源，内战立刻爆发。”"
  },
  {
    "segment_id": "0012",
    "text": "“三千年的内战席卷了全部大千世界，可以呼风唤雨、移山倒海的古修在每一颗星辰上互相厮杀！星球在燃烧、古传送阵被毁灭、晶石战舰连环爆炸、号称‘不朽’的高阶修真者纷纷陨落，而‘结丹强者’、‘元婴老怪’更是像他们曾经视若蝼蚁的凡人一样，变成了毫无价值的炮灰，在足以毁灭星球的攻击下灰飞烟灭。”"
  },
  {
    "segment_id": "0013",
    "text": "“内战后期，超过七成大千世界都被毁灭，更有无数大千世界切断了和主世界的联系，超过九成的高阶修真者化作灰灰，剩下的低阶修真者也在废墟中苟延残喘。”"
  },
  {
    "segment_id": "0014",
    "text": "“战争似乎难以维系，和平的曙光依稀出现——直到在一处不知名的大千世界，一名无知的修炼天才，发明了一个‘小玩意’。”"
  },
  {
    "segment_id": "0015",
    "text": "“这名修炼天才的名字和宗派已经不可考证，他的炼制过程也早已随风而逝，现代人将他创造的东西称之为——妖神病毒！”"
  },
  {
    "segment_id": "0016",
    "text": "“或许他的想法非常简单：既然没有足够的战士，为什么不发明一种东西，全面提升灵兽的战斗力，代替修真者来战斗——毕竟，灵兽的数量是近乎无穷的！”"
  },
  {
    "segment_id": "0017",
    "text": "“他成功了，经过‘妖神病毒’的催化，无数温驯的灵兽被调制成了可怕的杀戮工具，号称‘妖兽’的战争机器，不知疲倦、不会犹豫、不死不休！”"
  },
  {
    "segment_id": "0018",
    "text": "“短短十年，这名修炼天才就凭借妖兽大军统一了他所在的大千世界，妖兽大军的数量也达到了上亿头，其余世界的修真者发现了他的所作所为，也纷纷开始炼制自己的‘妖兽’。”"
  },
  {
    "segment_id": "0019",
    "text": "“百年时间，妖兽成为了修真界内战的主力，出现在星辰大海的各个角落。”"
  },
  {
    "segment_id": "0020",
    "text": "“只不过，所有修真者都没有发现两件事。”"
  },
  {
    "segment_id": "0021",
    "text": "“第一，‘妖神病毒’拥有极强的自我复制能力和传染性。”"
  },
  {
    "segment_id": "0022",
    "text": "“第二，‘妖神病毒’在提升妖兽战斗力的同时，也在潜移默化之中，不断提升妖兽的智能，而在上百年的残酷血战中，在庞大基数的催化下，数以万亿计算的妖兽中，诞生了智能堪比人类的‘妖族’！”"
  },
  {
    "segment_id": "0023",
    "text": "“终于，在三千年的内战最后一日——妖族觉醒了！”"
  },
  {
    "segment_id": "0024",
    "text": "“仿佛是受到某个恐怖存在的指挥，星辰大海中所有世界的妖兽，几乎在同一时间起来反抗他们的主宰，已经躲在山门中养尊处优了数百年的修真者根本不是久经沙场的妖兽的对手——更何况还有掌握了人类修真技术的妖族！”"
  },
  {
    "segment_id": "0025",
    "text": "“一座又一座灵山被夷为平地，一个又一个宗派被满门屠灭，百年时间里，妖族在星辰大海中疯狂追逐每一名漏网的修真者，昔日高高在上的修真者就像是丧家之犬，藏匿于星海的暗域和时空的缝隙之中，惶惶不可终日。”"
  },
  {
    "segment_id": "0026",
    "text": "“此后整整三万年，都是人类的‘大黑暗时代’，在无穷无尽的黑暗中，妖族建立起了庞大的‘妖兽王朝’，而人类则沦为卑贱的奴隶，丧失了尊严，丧失了骄傲，也丧失了最宝贵的——修真炼气的权力！”"
  },
  {
    "segment_id": "0027",
    "text": "“三万年，整整三万年！昔日灿烂辉煌，统治无尽星海的古修文明，就如黄沙之塔，被惊涛骇浪摧毁，没有留下半点印记！昔日里‘永生不朽’的高阶修真者的后裔们，只能凭借最原始的强大繁殖力，以庞大的数量，艰难维持着种族的延续！”"
  },
  {
    "segment_id": "0028",
    "text": "“直到三万年后，大黑暗时代末期，妖族内部争权夺利，矛盾不断尖锐，人类才得到了一丝喘息的机会，在无数修真天才的不懈努力之下，人类在暗中发动了三次‘修真革命’，建立起了和古修文明截然不同的‘现代修真文明体系’，才重新走上波澜壮阔的修真之路，复兴之路！”"
  },
  {
    "segment_id": "0029",
    "text": "“在绝世强者‘帝皇’的带领下，人类发掘大量古修文明的遗迹，重新创立了二十个‘元始宗派’，经过千年血战，人道大昌，人类重新成为无尽星海的主宰，现代修真文明也焕发出了勃勃生机！”"
  },
  {
    "segment_id": "0030",
    "text": "“距离‘大黑暗时代’结束已经有一万年，而距离古修文明崩溃已经有整整四万年，现在，是最好的修真世纪，是魅力无穷的修真40000年代！”"
  },
  {
    "segment_id": "0031",
    "text": "李耀思考最后一个段落时，天空中出现了代表考试即将结束的倒计时，他只好放弃继续阐述“帝皇”生平的念头，随口说了几句套话，匆匆结尾。"
  },
  {
    "segment_id": "0032",
    "text": "几乎就在最后一个字浮出脑海的刹那，整个世界轰然倒塌，化作朵朵蝴蝶般的碎片，李耀被一股大力强行推了出去，眼前一花，意识回到了教室中。"
  }
]
```

## Output Format
CRITICAL INSTRUCTION: You MUST translate the source text EXACTLY paragraph by paragraph, preserving the original order perfectly. DO NOT skip, drop, merge, or reorder any paragraphs. Each paragraph in the source MUST be translated.
Return ONLY valid JSON matching this schema:
{
  "chapter_number": 6,
  "chapter_title_vi": "Chương 6: <Vietnamese title>",
  "segments": [
    {
      "segment_id": "XXXX",
      "source": "...",
      "target": "..."
    }
  ]
}
