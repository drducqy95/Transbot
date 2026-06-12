# Translation Context Pack

## Project
- Branch: Tieu Dao Mong Duong
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
| 封神演义 | Phong Thần Diễn Nghĩa | term |


## Story Timeline (latest)

## Chapter 0001 - Chương 1: Phương Nguyên

### Summary
Chapter 1 completed via pipeline.

## Chapter 0002 - Chương 2: Thuộc Tính

### Summary
Chapter 2 completed via pipeline.

## Chapter 0001 - Chương 1: Phương Nguyên

### Summary
Chapter 1 completed via pipeline.

## Chapter 0002 - Chương 2: Thuộc Tính

### Summary
Chapter 2 completed via pipeline.

## Chapter 0003 - Chương 3: Linh Trà

### Summary
Chapter 3 completed via pipeline.

## Chapter 0004 - Chương 4: Vấn Tâm (Cầu sưu tầm)

### Summary
Chapter 4 completed via pipeline.

## Chapter 0005 - Chương 5: Xuất sơn (Cầu đề cử)

### Summary
Chapter 5 completed via pipeline.

## Chapter 0006 - Chương 6: Bị trộm

### Summary
Chapter 6 completed via pipeline.

## Chapter 0007 - Chương 7: Linh thú (Cầu ủng hộ!)

### Summary
Chapter 7 completed via pipeline.

## Chapter 0008 - Chương 8: Trao đổi

### Summary
Chapter 8 completed via pipeline.

## Chapter 0009 - Chương 9: Khách tới (Cầu sưu tầm)

### Summary
Chapter 9 completed via pipeline.

## Chapter 0009 - Chương 9: Khách tới

### Summary
Chapter 9 completed via pipeline.

## Chapter 0010 - Chương 10: Giao dịch

### Summary
Chapter 10 completed via pipeline.


## Source Chapter 11 - 0011 秘笈（求支持）
```json
[
  {
    "segment_id": "0001",
    "text": "# 第11章 秘笈（求支持）"
  },
  {
    "segment_id": "0002",
    "text": "林员外倒是个信人，没有多久就让人送来了一个小包裹。"
  },
  {
    "segment_id": "0003",
    "text": "或许是因为心中有愧，又或者这些粗浅的入门武功在林员外看来实在算不得什么，竟一下就送了三本过来，倒是令方元有些小小的惊喜。"
  },
  {
    "segment_id": "0004",
    "text": "此时，他就盘膝坐在青石上，身边跟着花狐貂，小心地翻开了一本秘笈的扉页。"
  },
  {
    "segment_id": "0005",
    "text": "“黑沙掌？”"
  },
  {
    "segment_id": "0006",
    "text": "方元先整体看了看秘笈，就见这书册古旧，上面的字体遒劲有力，又略微有些模糊，边角处带着破损，显然经历了不知道多少代人的研读，蕴含古意，简直就是一件古董了。"
  },
  {
    "segment_id": "0007",
    "text": "“竟然将原本送来了，看来林员外倒是没准备坑我……”"
  },
  {
    "segment_id": "0008",
    "text": "方元见了，心里暗暗点头。"
  },
  {
    "segment_id": "0009",
    "text": "这种武功秘笈什么的，纵然一点小小的差错，结果就有可能天差地别，新抄一部，哪里有原版的好。"
  },
  {
    "segment_id": "0010",
    "text": "他光是抚摸着这古册，就知道当年那位武者，在这上面必然倾注了大量心血。"
  },
  {
    "segment_id": "0011",
    "text": "“也是……即使是最粗浅的武艺，只要能广为流传，必然有着独到之处！”"
  },
  {
    "segment_id": "0012",
    "text": "再看看其它两本，也跟这个类似，方元不由有些汗颜自己的小心思。"
  },
  {
    "segment_id": "0013",
    "text": "他特意要求流传最广的，自然也是为了方便查证。"
  },
  {
    "segment_id": "0014",
    "text": "反正一开始对方所给的秘笈，他是一部都不准备练的。"
  },
  {
    "segment_id": "0015",
    "text": "毕竟，武功可不比其它，另外一个世界中的知识更是告诉他走火入魔的可怕。"
  },
  {
    "segment_id": "0016",
    "text": "“现在看来……似乎有些小人之心了……”"
  },
  {
    "segment_id": "0017",
    "text": "方元沉吟了一下：“再说，我还有着医术傍身，光是研究不练的话，应该也可以看出一点问题。相比较而言，外功之类的，比内功要好点，纵然里面有着陷阱，也不容易出大事……”"
  },
  {
    "segment_id": "0018",
    "text": "虽然这是另外一个世界中的知识，但也不妨碍方元拿来推测。"
  },
  {
    "segment_id": "0019",
    "text": "想到这里，他又放下了手里的秘册，翻了翻另外两本。"
  },
  {
    "segment_id": "0020",
    "text": "“鹰爪功？似乎那个归灵宗的执事，冷面铁鹰也会这样的功夫，但对方会的八成就是秘传，比街面上烂大街的普通版本好得多了……”"
  },
  {
    "segment_id": "0021",
    "text": "三本秘笈当中，有两本都是外功，最后剩下的一本却是无名功法，讲究的也是如何锤炼自身，增加抗打击能力，似乎还有些呼吸技巧，据作者所说，习练到大成，一口气憋住，足以应对普通钝器的打击。"
  },
  {
    "segment_id": "0022",
    "text": "在包裹里面，还有一张小小的纸条，写了三本秘笈的来历。"
  },
  {
    "segment_id": "0023",
    "text": "“黑沙掌，为清河郡拳师大家寇封所著，流传最广，门客献上。”"
  },
  {
    "segment_id": "0024",
    "text": "“鹰爪功，庄客孟元所献，为最普通基础，若要习练至高深境界，需要特定的内功心法！”"
  },
  {
    "segment_id": "0025",
    "text": "“最后这一本是最粗浅的气功，不，根本就只是一些呼吸与挨打技巧的总结，连原著作者都没有起名字，因此就叫硬气功……”"
  },
  {
    "segment_id": "0026",
    "text": "……"
  },
  {
    "segment_id": "0027",
    "text": "方元看到最后也确认了，这三本武功，果然都是最烂大街的货色，没有一本精品。"
  },
  {
    "segment_id": "0028",
    "text": "当然，纵然再粗浅的武功，也是一套传承，千锤百炼，普通人得到其中一门，就勉强可以安身立命，传家糊口，因此还是算比较珍惜的。"
  },
  {
    "segment_id": "0029",
    "text": "用一株六十年的红山参换来这个，只能算不亏不赚。"
  },
  {
    "segment_id": "0030",
    "text": "“并且……没有污秽、破损、涂改……林员外诚意还是有的。”"
  },
  {
    "segment_id": "0031",
    "text": "方元长出口气，开始一本本仔细看了起来。"
  },
  {
    "segment_id": "0032",
    "text": "不知不觉间，小半天的时间过去，夕阳渐渐沉下，橘红色的光辉洒遍大地。"
  },
  {
    "segment_id": "0033",
    "text": "“咯咯！？”"
  },
  {
    "segment_id": "0034",
    "text": "“咯咯？”"
  },
  {
    "segment_id": "0035",
    "text": "旁边的花狐貂，见到方元全神贯注地盯着秘笈，有些好奇地凑过小脑袋，奈何那上面的字符对于它而言就如同天书一般，看得头晕眼花，终于放弃，轻巧地跳入了密林里，没有多久，就拖着一只肥硕的野兔跑了过来，放在方元脚下，眼巴巴地盯着他，黑色的瞳孔里面仿佛冒出了钩子。"
  },
  {
    "segment_id": "0036",
    "text": "“哈哈……就知道吃！”"
  },
  {
    "segment_id": "0037",
    "text": "方元合上最后一本硬气功的秘笈，立即看到这幅模样的花狐貂，不由又哈哈大笑起来。"
  },
  {
    "segment_id": "0038",
    "text": "夜色渐渐朦胧。"
  },
  {
    "segment_id": "0039",
    "text": "火堆旁边，方元将野兔剥皮洗尽，涂上酱料烤了，又扯过一只前腿，将剩下的丢给迫不及待的花狐貂，自己则是默默思索着今天从秘笈上看到的内容。"
  },
  {
    "segment_id": "0040",
    "text": "‘这个世界的武学，似乎比梦中世界要高明不少……并且体系化，规范化……比如黑沙掌与鹰爪功，就是纯粹的外功，利用药物刺激身体，内功则是讲究呼吸法与行气路线，更高级的还有存神观想之类……而不论任何功夫，都有着具体而一致的等级划分，那就是金锁重楼十二关！’"
  },
  {
    "segment_id": "0041",
    "text": "这个名词在三本秘册中都被反复提及，方元细细研究之下，也终于勉强弄懂了其中意思。"
  },
  {
    "segment_id": "0042",
    "text": "“按照此世武道理念，人的身体是一个潜力无穷的大宝藏，只是又有诸多关卡，限制了力量的发挥，武学之道，一开始就是要一重重地冲破这种关卡，不断挖掘自身潜力！”"
  },
  {
    "segment_id": "0043",
    "text": "秘笈中所言，这样的关卡，在人身之内共有十二道，合称为金锁重楼十二关。"
  },
  {
    "segment_id": "0044",
    "text": "武者每破一关，实力都会有着不同程度的提升，越到后期越为恐怖。"
  },
  {
    "segment_id": "0045",
    "text": "而连破十二关之后，便是‘武宗’之境！"
  },
  {
    "segment_id": "0046",
    "text": "此等人物，纵然归灵宗之内，也唯有一人而已。"
  },
  {
    "segment_id": "0047",
    "text": "“身体内部的十二重关卡……听起来倒是与医术中的十二正经，奇经八脉等等的描述有些类似，一开始的武学修习，实际上是冲脉的过程？”"
  },
  {
    "segment_id": "0048",
    "text": "“十二重关卡，就是十二重境界，唯有一一突破之后，方可成就武宗之境！蕾月那丫头，竟然如此天赋异禀么？”"
  },
  {
    "segment_id": "0049",
    "text": "略微理解其中难度之后，方元登时有些疑惑了。"
  },
  {
    "segment_id": "0050",
    "text": "在他印象当中，那丫头的武道天赋，有着这么恐怖？"
  },
  {
    "segment_id": "0051",
    "text": "“不过我当时也看不出来，倒是师父应该察觉了什么，这婚事订得有些蹊跷……”"
  },
  {
    "segment_id": "0052",
    "text": "一想到问心居士，方元就不由幽幽叹息一声。"
  },
  {
    "segment_id": "0053",
    "text": "老家伙对他倒真是相当不错，什么都为他考虑好了，奈何逝去得太早了一点。"
  },
  {
    "segment_id": "0054",
    "text": "若是活到现在，见到林员外的嘴脸，又不知道该是一个怎样的表情？"
  },
  {
    "segment_id": "0055",
    "text": "一念至此，嘴里浓郁的烤兔肉都突然间没了香味。"
  },
  {
    "segment_id": "0056",
    "text": "方元意兴阑珊地起身，又整理了一下，开始就着月色泡茶。"
  },
  {
    "segment_id": "0057",
    "text": "于这坐忘茶道之中，缅怀问心居士，是他独特的纪念方式。"
  },
  {
    "segment_id": "0058",
    "text": "“嘶嘶！？”"
  },
  {
    "segment_id": "0059",
    "text": "旁边的花狐貂看得似懂非懂，但也竟仿佛感受到了方元心中的悲怆情绪，没有一如平日般嬉闹。"
  },
  {
    "segment_id": "0060",
    "text": "……"
  },
  {
    "segment_id": "0061",
    "text": "幽谷深深，山中无日月，转眼就不知道过去了多少时候，一日清晨。"
  },
  {
    "segment_id": "0062",
    "text": "方元照例早早起来，饮完早茶之后，开始下田耕作。"
  },
  {
    "segment_id": "0063",
    "text": "红玉稻田之中，一株株稻苗生长了齐腰高，甚至顶端结出了沉甸甸的稻穗，令稻苗弯下腰来。"
  },
  {
    "segment_id": "0064",
    "text": "方元将灵肥化开，融入山泉水中，倾泻入稻田，顿时波光粼粼，带着一股馨香之气。"
  },
  {
    "segment_id": "0065",
    "text": "“咯咯！”"
  },
  {
    "segment_id": "0066",
    "text": "“咯咯！”"
  },
  {
    "segment_id": "0067",
    "text": "旁边，花狐貂上窜下跳，显得很是兴奋。"
  },
  {
    "segment_id": "0068",
    "text": "它虽然看不上刚刚成长的稻苗，但如今已经快成熟的红玉稻米，却是令它兴奋非常。"
  },
  {
    "segment_id": "0069",
    "text": "“记住，不许偷吃！”"
  },
  {
    "segment_id": "0070",
    "text": "为此，方元不得不郑重警告它，又连连允诺加大每天的茶水份量，才总算勉强安抚下去。"
  },
  {
    "segment_id": "0071",
    "text": "“之前的稻种不多，这次能收获几十斤就相当不错了，不过这次之后，稻种就可以继续种下去，下次就可扩大种植规模……”"
  },
  {
    "segment_id": "0072",
    "text": "方元很是欣喜。"
  },
  {
    "segment_id": "0073",
    "text": "实际上，这批红玉稻谷的长势，简直超出他的预料，生长周期更是短得惊人。"
  },
  {
    "segment_id": "0074",
    "text": "这第一肯定是花狐貂带来的灵肥之功，而第二，也得益于他本身的种植术加成，才造就了如此不可思议的奇迹出现。"
  },
  {
    "segment_id": "0075",
    "text": "“花狐貂，你放心，等到收获之后，肯定要给你一次吃得饱饱的！毕竟这里面也有你的一份功劳！”"
  },
  {
    "segment_id": "0076",
    "text": "方元抚摸着花狐貂毛绒绒的脑袋，安慰道：“还有灵茶，也快第二次长茶叶了……”"
  },
  {
    "segment_id": "0077",
    "text": "他脸上带着微笑，心里充满了丰收的喜悦。"
  },
  {
    "segment_id": "0078",
    "text": "每日例行的巡视过后，方元又来到精舍，看着桌面上并排摆放的秘笈。"
  },
  {
    "segment_id": "0079",
    "text": "“这三本功法，我都已经倒背如流，并且与本身医学与梦中记忆相互论证，似乎并无什么不妥之处……那就练练？”"
  },
  {
    "segment_id": "0080",
    "text": "方元的眸子里闪过一丝跃跃欲试，但旋即还是摇摇头：“不行！不怎么保险！看来我真是个怕死鬼啊，为今之计，只有再去一趟县城，花费代价，收购一本看看，又或者传个人练练……”"
  },
  {
    "segment_id": "0081",
    "text": "武功秘笈不是什么寻常东西，实际操作起来，方元也没有多少把握。"
  },
  {
    "segment_id": "0082",
    "text": "“那小贼就在里面！”"
  },
  {
    "segment_id": "0083",
    "text": "“围住了，不要让他跑了！”"
  },
  {
    "segment_id": "0084",
    "text": "“快，上啊！”"
  },
  {
    "segment_id": "0085",
    "text": "……"
  },
  {
    "segment_id": "0086",
    "text": "突然间，谷外一阵吵杂声传来，令方元不由皱起眉头。"
  },
  {
    "segment_id": "0087",
    "text": "“什么事？”"
  },
  {
    "segment_id": "0088",
    "text": "他打开院门，顿时见到一伙人气势汹汹地从谷口进来，为首者赫然是周文馨那个傲娇大小姐。"
  },
  {
    "segment_id": "0089",
    "text": "“你个小贼！”"
  },
  {
    "segment_id": "0090",
    "text": "见到方元，周文馨新仇旧恨顿时上头，连声音也变得尖锐起来：“你欺辱我在先，用假药害我父亲在后，今日可不能绕了你，给我上！”"
  },
  {
    "segment_id": "0091",
    "text": "一挥手，几个豪仆顿时气势汹汹地上前，将方元团团围住。"
  }
]
```

## Output Format
CRITICAL INSTRUCTION: You MUST translate the source text EXACTLY paragraph by paragraph, preserving the original order perfectly. DO NOT skip, drop, merge, or reorder any paragraphs. Each paragraph in the source MUST be translated.
Return ONLY valid JSON matching this schema:
{
  "chapter_number": 11,
  "chapter_title_vi": "Chương 11: <Vietnamese title>",
  "segments": [
    {
      "segment_id": "XXXX",
      "source": "...",
      "target": "..."
    }
  ]
}
