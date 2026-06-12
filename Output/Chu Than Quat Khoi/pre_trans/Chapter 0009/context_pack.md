# Translation Context Pack

## Project
- Branch: Chu Than Quat Khoi
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

## Chapter 0001 - Chương 1: Xuyên không

### Summary
Chapter 1 completed via pipeline.

## Chapter 0002 - Chương 2: Bàn tay vàng của ta ở đâu

### Summary
Chapter 2 completed via pipeline.

## Chapter 0003 - Chương 3: Xuyên không? Vô hạn?

### Summary
Chapter 3 completed via pipeline.

## Chapter 0004 - 0004 队友（求收藏！！！）

### Summary
Chapter 4 completed via pipeline.

## Chapter 0005 - 0005 任务（求推荐！）

### Summary
Chapter 5 completed via pipeline.

## Chapter 0006 - Chương 6: Bất ngờ

### Summary
Chapter 6 completed via pipeline.

## Chapter 0007 - Chương 7: Tát Mãn Vu

### Summary
Chapter 7 completed via pipeline.

## Chapter 0008 - Chương 8: Kiến bám

### Summary
Chapter 8 completed via pipeline.


## Source Chapter 9 - 0009 火攻（求推荐！）
```json
[
  {
    "segment_id": "0001",
    "text": "# 第9章 火攻（求推荐！）"
  },
  {
    "segment_id": "0002",
    "text": "在萨满巫的巫术之下，原本已经士气倾颓，负伤累累的胡人铁骑，赫然再次发起了冲锋！"
  },
  {
    "segment_id": "0003",
    "text": "血与火！生与死！乃至不同种族间的存亡之战，在大青庄的土围上再次展开！"
  },
  {
    "segment_id": "0004",
    "text": "与之前不同的是，萨满巫的出现，令胡人一方的士气、战力提升到巅峰，而大青庄一方则是跌落到低谷。"
  },
  {
    "segment_id": "0005",
    "text": "残阳如血当中，胡人几次冲锋，险些击破防线，全靠王印、吴明等一帮武者拼死才抵挡下来。"
  },
  {
    "segment_id": "0006",
    "text": "结果到了星光灿烂，胡人退去的时候，吴明与王印面上都是难掩疲惫之色，身上盔甲伤痕累累。"
  },
  {
    "segment_id": "0007",
    "text": "“呼……”"
  },
  {
    "segment_id": "0008",
    "text": "王印在两个乡勇的帮助下，好不容易才将布满血肉，几乎与身体粘连一起的铁甲脱下，苦笑着对吴明道：“无名公子，我今日真气损耗甚巨，恐怕需要调养一夜，才能继续上战场，此处就拜托你了……”"
  },
  {
    "segment_id": "0009",
    "text": "“放心，本人也不想胡人入侵，死无葬身之地的！”"
  },
  {
    "segment_id": "0010",
    "text": "今日王印奋勇作战在第一线，冲得比吴明还猛，甚至接下了最多的敌人，乃是人所共见的，吴明当即笑着道。"
  },
  {
    "segment_id": "0011",
    "text": "“甚好……等到胡人退去，本人要好好交一交你这个朋友才是！”"
  },
  {
    "segment_id": "0012",
    "text": "王印对吴明的态度倒是十分友善，不知道其中有没有黄莺的影响。"
  },
  {
    "segment_id": "0013",
    "text": "而看到王印离开，秦虎却是上前：“今日你也出力不小，趁早去休息吧！莫要让佳人久候了……”"
  },
  {
    "segment_id": "0014",
    "text": "说着，脸上又带着几分男人都懂的笑容，显然是误会了什么。"
  },
  {
    "segment_id": "0015",
    "text": "实际上，吴明貌似神勇，但与王印目的不同，还是暗暗保留了三分气力。"
  },
  {
    "segment_id": "0016",
    "text": "此时见到秦虎要来主动揽下守夜之职，心里一动，面上却是露出感激之色：“多谢！”"
  },
  {
    "segment_id": "0017",
    "text": "也不多话，直接下了土围。"
  },
  {
    "segment_id": "0018",
    "text": "只是……秦虎却没有发现，吴明下了围墙之后，脸上一闪而逝的阴冷。"
  },
  {
    "segment_id": "0019",
    "text": "……"
  },
  {
    "segment_id": "0020",
    "text": "“我们的任务只是生存……因此，可以选择大青庄一边，自然也可以选择胡人一边！”"
  },
  {
    "segment_id": "0021",
    "text": "黑暗的阁楼之上，吴明与黄莺并肩，看着似一片平静的庄子，忽然道。"
  },
  {
    "segment_id": "0022",
    "text": "“你……难道是说，秦虎他想……”黄莺捂着红唇，虽然隐隐有着猜测，但真正听到，还是有些难以相信：“他就不怕……”"
  },
  {
    "segment_id": "0023",
    "text": "“每个人总以为自己是特别的……或许，他以为自己有功，就可以被胡人高看一眼了呢！”"
  },
  {
    "segment_id": "0024",
    "text": "吴明的嘴角带起一丝讥讽的笑容：“胡人强而大青庄弱，若非机缘巧合，今日就有可能破庄，绝无可能撑到七天，敌人又有萨满巫之助……此人性格崇拜力量，服从强者，你觉得，在这种情况下，对方会怎么选择？”"
  },
  {
    "segment_id": "0025",
    "text": "“你知道他要献庄？为什么不拿下……？”"
  },
  {
    "segment_id": "0026",
    "text": "黄莺说到一半，却是住口不言，脸上露出苦笑。"
  },
  {
    "segment_id": "0027",
    "text": "毕竟，她们与秦虎一样，可都是外人啊！就算揭破了秦虎的阴谋，恐怕也会更受猜忌。"
  },
  {
    "segment_id": "0028",
    "text": "更何况，甚至就是除掉了内患，对于大青庄能否守到第七日，两人也是毫无信心。"
  },
  {
    "segment_id": "0029",
    "text": "“因此……必须行险了！”"
  },
  {
    "segment_id": "0030",
    "text": "吴明忽然侧耳倾听，就发现土围处隐隐有着骚乱，外面马蹄的规律震动传来，不由对黄莺道：“开始了，我们依计行事！”"
  },
  {
    "segment_id": "0031",
    "text": "“妾身知晓了！”"
  },
  {
    "segment_id": "0032",
    "text": "黄莺面色复杂地看了吴明一眼，没入黑暗当中。"
  },
  {
    "segment_id": "0033",
    "text": "……"
  },
  {
    "segment_id": "0034",
    "text": "“秦大人，你……你做什么？”"
  },
  {
    "segment_id": "0035",
    "text": "看着秦虎忽然发难，将旁边两人砍瓜切菜般剁死，周围的乡勇一副吓傻了的表情。"
  },
  {
    "segment_id": "0036",
    "text": "“做什么？嘿嘿……自然是投降啊！”"
  },
  {
    "segment_id": "0037",
    "text": "秦虎舔了舔刀锋上的鲜血，表情疯狂而凶残。"
  },
  {
    "segment_id": "0038",
    "text": "忽然狂扑而上，刀光闪现，他乃肉身境三重的高手，对付一般乡勇，当真如猛虎入羊群一般，刹那间将守门的杀尽。"
  },
  {
    "segment_id": "0039",
    "text": "“杀人啦！”"
  },
  {
    "segment_id": "0040",
    "text": "“外人杀人啦！”"
  },
  {
    "segment_id": "0041",
    "text": "……"
  },
  {
    "segment_id": "0042",
    "text": "尖叫声，还有锣鼓声响起，秦虎脸上却是冷笑：“嘿嘿……吴明、黄莺，你们这对狗男女自求多福吧！”"
  },
  {
    "segment_id": "0043",
    "text": "却是扳动机括，缓缓打开大门。"
  },
  {
    "segment_id": "0044",
    "text": "外面，早已准备好的胡人当即发起冲锋，数骑仿佛风一样杀入进来。"
  },
  {
    "segment_id": "0045",
    "text": "胡人本来就是马背种族，一人一马，才能发挥最大战力，这几日在外面，只能舍弃最长处，以短攻长，早已憋了一肚子邪火，此时驰马飞入，当真犀利无比，神挡杀神，佛挡杀佛！"
  },
  {
    "segment_id": "0046",
    "text": "“诸位大人，我乃……”"
  },
  {
    "segment_id": "0047",
    "text": "秦虎看着此幕，脸色却迅速转化，带着笑容，迎了上去。"
  },
  {
    "segment_id": "0048",
    "text": "但刹那间，他的脸就变化了。"
  },
  {
    "segment_id": "0049",
    "text": "胡人看到他，非但没有停下，反而快马加鞭，脸带狞笑，冲了上来。"
  },
  {
    "segment_id": "0050",
    "text": "“啊……”"
  },
  {
    "segment_id": "0051",
    "text": "一抹刀光浮现，对方人马合一，借着马力冲锋，一刀砍下的力量，简直堪比真气境高手。"
  },
  {
    "segment_id": "0052",
    "text": "秦虎勉强举起钢刀一挡。"
  },
  {
    "segment_id": "0053",
    "text": "当！"
  },
  {
    "segment_id": "0054",
    "text": "巨响当中，他手臂巨震，虎口裂开，长刀飞出，胸前浮现出一道巨大的创伤，倒在地上，嘴角血沫奔涌，眼睛里面还有着挣扎之色，显然是回光返照。"
  },
  {
    "segment_id": "0055",
    "text": "踏踏！"
  },
  {
    "segment_id": "0056",
    "text": "旋即，大量的马蹄踏过，将他碾成了肉酱。"
  },
  {
    "segment_id": "0057",
    "text": "“杀！”"
  },
  {
    "segment_id": "0058",
    "text": "“杀光汉狗！”"
  },
  {
    "segment_id": "0059",
    "text": "胡骑兴奋嘶吼，一下散开，如同虎入羊群，接连屠戮。"
  },
  {
    "segment_id": "0060",
    "text": "整个大青庄顿时化为人间炼狱。"
  },
  {
    "segment_id": "0061",
    "text": "而原先收容老弱妇孺的祠堂附近，人群从睡梦中惊醒，轰然大乱，王印也是狼狈不堪地跑出：“怎么回事？为何胡人这就进来了？”"
  },
  {
    "segment_id": "0062",
    "text": "这时大乱之下，又有那个来回答他，只能取出蛇矛，猛地一抛，将一名胡人骑兵贯穿。"
  },
  {
    "segment_id": "0063",
    "text": "“王兄！”"
  },
  {
    "segment_id": "0064",
    "text": "吴明穿着皮甲，却是忽然赶到：“胡人夜袭，破门而入，我之过也！此时唯有去杀了胡首，方有一线生机！”"
  },
  {
    "segment_id": "0065",
    "text": "“我也去！”"
  },
  {
    "segment_id": "0066",
    "text": "王印当仁不让。"
  },
  {
    "segment_id": "0067",
    "text": "通过黄莺的打探，吴明早知道此人面冷心热，有着一股憨直之劲，此时整个庄子的性命未来全在他手，更是义不容辞。"
  },
  {
    "segment_id": "0068",
    "text": "“印儿！”"
  },
  {
    "segment_id": "0069",
    "text": "王印当即拔出蛇矛，也不管背后狼狈奔出的王乔一眼，跟着吴明而去。"
  },
  {
    "segment_id": "0070",
    "text": "……"
  },
  {
    "segment_id": "0071",
    "text": "“嗯！很好……有着外面的千人，再加上这满庄的生灵，我的法鼓一定可以淬炼大成！”"
  },
  {
    "segment_id": "0072",
    "text": "此时，戴着鹿角面具的萨满巫不顾兵凶战危，骑着骏马，旁边一支十人小队紧张跟着入庄，却并没有参与到杀戮的盛宴中去。"
  },
  {
    "segment_id": "0073",
    "text": "此人举起手中血红色的法鼓，摇摆拍击不断，嘴里念念有词。"
  },
  {
    "segment_id": "0074",
    "text": "在火光之下，法鼓上的血色鲜艳欲滴，一枚枚古怪的符号仿佛有着自己的生命，活过来一般扭动，带着诡异的味道。"
  },
  {
    "segment_id": "0075",
    "text": "“该死，邪巫师做法！”"
  },
  {
    "segment_id": "0076",
    "text": "王印看到这幕，眼睛却是变红了：“萨满巫的法鼓用白骨做架，人皮为面，又用血染色，能收集冤魂之力……”"
  },
  {
    "segment_id": "0077",
    "text": "古代对于死后极为看重，像萨满巫这种杀了你还要你死后都不得安宁的做法，简直比扒人祖坟还遭恨。"
  },
  {
    "segment_id": "0078",
    "text": "就是吴明，看得都有些头皮发麻。"
  },
  {
    "segment_id": "0079",
    "text": "“跟我冲！”"
  },
  {
    "segment_id": "0080",
    "text": "王印招呼一声，从背上拔出一支短矛，猛地投掷出去，刹那间就将一名胡人骑兵捅成透心凉。"
  },
  {
    "segment_id": "0081",
    "text": "“保护萨满！”"
  },
  {
    "segment_id": "0082",
    "text": "那对胡人骑兵呼啸着，死骑就冲了上来。"
  },
  {
    "segment_id": "0083",
    "text": "“杀！”"
  },
  {
    "segment_id": "0084",
    "text": "王印力贯蛇矛，令长柄都弯成诡异的弧度，猛地一甩。"
  },
  {
    "segment_id": "0085",
    "text": "蓬！"
  },
  {
    "segment_id": "0086",
    "text": "一名胡人骑兵连人带马跌倒，被后续冲上的乡勇乱刀分尸。"
  },
  {
    "segment_id": "0087",
    "text": "“放箭！”"
  },
  {
    "segment_id": "0088",
    "text": "两边拼杀在一起，厮杀极惨。"
  },
  {
    "segment_id": "0089",
    "text": "见到此幕，萨满巫面具之下却是浮现出一缕不屑之色，忽然从怀中摸出一根骨哨，鼓起腮帮子一吹。"
  },
  {
    "segment_id": "0090",
    "text": "咻咻！"
  },
  {
    "segment_id": "0091",
    "text": "刺耳的哨声仿佛无形之箭，一名乡勇捂着脖子，直挺挺地倒了下去，一张脸孔尽成漆黑之色。"
  },
  {
    "segment_id": "0092",
    "text": "萨满巫不断吹哨，每一次都有一人倒下，凶威滔天，而周围的胡人更是渐渐汇聚而来，令王印等人陷入绝对的下风。"
  },
  {
    "segment_id": "0093",
    "text": "“不要站在萨满巫面前，他的哨子里有毒！”"
  },
  {
    "segment_id": "0094",
    "text": "吴明却是一开始就默默缩头，没有被当成第一目标，观察片刻，立即大喊。"
  },
  {
    "segment_id": "0095",
    "text": "“不错，不要被哨口对着！”"
  },
  {
    "segment_id": "0096",
    "text": "王印来去如风，又杀了两名胡人骑兵，也是大叫。"
  },
  {
    "segment_id": "0097",
    "text": "乡勇们纷纷散开，取出弓箭御敌，但萨满巫仍是不慌不忙，以哨声杀人。"
  },
  {
    "segment_id": "0098",
    "text": "熊熊！"
  },
  {
    "segment_id": "0099",
    "text": "忽然间，周围光线越来越亮，恐怖的红黄色火舌不断蔓延。"
  },
  {
    "segment_id": "0100",
    "text": "“走水啦！”"
  },
  {
    "segment_id": "0101",
    "text": "“走水啦！”"
  },
  {
    "segment_id": "0102",
    "text": "……"
  },
  {
    "segment_id": "0103",
    "text": "耀眼的火光几乎照耀天幕，令整个大青庄都在火海中簌簌发抖。"
  },
  {
    "segment_id": "0104",
    "text": "“怎么回事？”王印大急：“胡人放火？”"
  },
  {
    "segment_id": "0105",
    "text": "但此时，对面的萨满巫也有些焦急的模样，大声呼喝着，似要召集、整顿队伍。"
  },
  {
    "segment_id": "0106",
    "text": "毕竟，不断蔓延的火势，令整个胡人骑兵都被分割，甚至有着误伤的可能。"
  },
  {
    "segment_id": "0107",
    "text": "大青庄四面建起土围，里面的空间就不算太大，屋宇连绵，更要命的是，最外围多为木草建筑，连块砖都少见，这烧起来就很要命了。"
  },
  {
    "segment_id": "0108",
    "text": "一个不好，大青庄乡民与胡人都得同归于尽。"
  },
  {
    "segment_id": "0109",
    "text": "“律律！”"
  },
  {
    "segment_id": "0110",
    "text": "此时萨满巫带着最后一个贴身的图鲁勇士，勒转马头，显然有了去意。"
  },
  {
    "segment_id": "0111",
    "text": "但吴明怎么舍得让他离开，当即扯出背负的上好牛角弓，弯弓搭箭，猛地一放。"
  },
  {
    "segment_id": "0112",
    "text": "咻！"
  },
  {
    "segment_id": "0113",
    "text": "狼牙箭直取萨满巫而去，又被马匹挡住，正中脖子，鲜血狂涌。"
  },
  {
    "segment_id": "0114",
    "text": "射人先射马，萨满巫坐骑倒毙，在地上狼狈不堪地滚了滚。"
  },
  {
    "segment_id": "0115",
    "text": "“喝！纳命来！”"
  },
  {
    "segment_id": "0116",
    "text": "见到此时胡人援兵被火势阻挡，虽然心里焦急，但王印又怎么会放过这个擒杀敌酋的天赐良机？大喝一声，蛇矛似灵蛇出洞，将最后一名图鲁勇士从马上挑下，又向萨满巫冲去。"
  }
]
```

## Output Format
CRITICAL INSTRUCTION: You MUST translate the source text EXACTLY paragraph by paragraph, preserving the original order perfectly. DO NOT skip, drop, merge, or reorder any paragraphs. Each paragraph in the source MUST be translated.
Return ONLY valid JSON matching this schema:
{
  "chapter_number": 9,
  "chapter_title_vi": "Chương 9: <Vietnamese title>",
  "segments": [
    {
      "segment_id": "XXXX",
      "source": "...",
      "target": "..."
    }
  ]
}
