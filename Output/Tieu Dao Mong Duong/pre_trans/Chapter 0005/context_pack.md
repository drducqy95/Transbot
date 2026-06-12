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
N/A

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


## Source Chapter 5 - 0005 出山（求推荐）
```json
[
  {
    "segment_id": "0001",
    "text": "# 第5章 出山（求推荐）"
  },
  {
    "segment_id": "0002",
    "text": "“是谁让你如此做的？”"
  },
  {
    "segment_id": "0003",
    "text": "趁着对方痛哭流涕的时候，方元赶紧问着。"
  },
  {
    "segment_id": "0004",
    "text": "这问心茶最多只有洗涤心灵之功，可没有让人弃恶从善之效。"
  },
  {
    "segment_id": "0005",
    "text": "田老汉本来就心地不坏，又有愧于心，这才在灵茶效果之下幡然悔悟，若是本性邪恶，那最多觉得茶叶很好，味道绝佳，却根本不会有着如此效果。"
  },
  {
    "segment_id": "0006",
    "text": "“老汉不是人啊……呜呜……”"
  },
  {
    "segment_id": "0007",
    "text": "地上，田老汉仍涕泪横流：“老汉算是看透了，我这一生过得实在窝囊，到老了勉强有点地位，还是得在人家压力之下构害救命恩人的弟子，我不是人……老汉想清楚了，去他的狗屁归灵宗，老汉纵然洗手不干，也不能让恩人受委屈啊……”"
  },
  {
    "segment_id": "0008",
    "text": "“归灵宗？”"
  },
  {
    "segment_id": "0009",
    "text": "方元听了，却是蓦然一个激灵。"
  },
  {
    "segment_id": "0010",
    "text": "‘莫非他们还不肯罢休？等一等！不对！若真的不肯罢休，就直接来做掉我了，如此不干不脆的，反倒像是下面人自作主张，小孩子恶作剧一般了……’"
  },
  {
    "segment_id": "0011",
    "text": "想到这里，他接着问道：“是归灵宗唆使的么？谁来恐吓你的？”"
  },
  {
    "segment_id": "0012",
    "text": "“一个外门执事，也不知道从哪里听到的消息，知晓小老儿与你们有着来往……小居士，要不咱们离开吧，纵然归灵宗在百里之内一手遮天，但出去几百里之后，谁还认它啊！小老儿还有着一点积蓄，也曾经见过世面，一路绝对无虞的……”"
  },
  {
    "segment_id": "0013",
    "text": "田老汉良心发现之后，又积极劝着方元，寻找退路。"
  },
  {
    "segment_id": "0014",
    "text": "看着他这幅要毁家纾难的样子，方元却是无语了：“不急！不急！再等等……”"
  },
  {
    "segment_id": "0015",
    "text": "说完，他就盘膝坐下，自顾自地品茶。"
  },
  {
    "segment_id": "0016",
    "text": "“咦？”"
  },
  {
    "segment_id": "0017",
    "text": "片刻之后，田老汉心头热血散去，圆滑性格又浮现出来，顿时后悔不已：‘我是怎么了？为何连基业都不要，就要帮小居士与归灵宗对上？’"
  },
  {
    "segment_id": "0018",
    "text": "此时扪心自问，要他通风报信，让方元尽快离开，倒是有着可能。"
  },
  {
    "segment_id": "0019",
    "text": "但将自己身家全部压上去，一同逃命？田老汉摸了摸自己的脑袋，感觉也没有被驴踢过。"
  },
  {
    "segment_id": "0020",
    "text": "这时看到方元目光望过来，更是叫苦不迭，生怕方元真的意动，要拉他一起跑路。"
  },
  {
    "segment_id": "0021",
    "text": "方元看着他坐立不安，尴尬异常的模样，也是暗暗好笑。"
  },
  {
    "segment_id": "0022",
    "text": "‘此人本心不坏，奈何世俗中牵挂太多，容易优柔寡断，迟疑不定……’"
  },
  {
    "segment_id": "0023",
    "text": "心里默道一句，方元直接开口：“田老你放心，我并没有逃走的打算，也不必劳烦你帮忙！”"
  },
  {
    "segment_id": "0024",
    "text": "“这怎么成呢？”"
  },
  {
    "segment_id": "0025",
    "text": "田老汉弱弱回了一句，心里却着实松了一口长气。"
  },
  {
    "segment_id": "0026",
    "text": "虽然诧异自己今天怎么良心发现，但既然已经说了，就提醒道：“自古民不与官斗，归灵宗虽然不是官，但比官更加厉害，小居士不知如何得罪了他们？若有得回转，还是尽快找中人相助，若无法回转，那就赶紧走吧！”"
  },
  {
    "segment_id": "0027",
    "text": "“多谢田老好意，只是我舍不得这里……”"
  },
  {
    "segment_id": "0028",
    "text": "方元吐出口气，这说得是实话。"
  },
  {
    "segment_id": "0029",
    "text": "他从小就在这里长大，情感投注，可不是那么容易消除的。"
  },
  {
    "segment_id": "0030",
    "text": "并且，还有灵茶与灵米，仓促之间，更不可能长途转移。"
  },
  {
    "segment_id": "0031",
    "text": "再说，方元也相信自己的判断，自己婚书都退了，又收了赔礼，伏低做小，对方根本没有必要赶尽杀绝。"
  },
  {
    "segment_id": "0032",
    "text": "这件事情，八成还是某个下面人自作主张，为讨欢心罢了。"
  },
  {
    "segment_id": "0033",
    "text": "‘莫非又是蕾月惹出来的什么祸患？’"
  },
  {
    "segment_id": "0034",
    "text": "方元感觉心里囧了一下，记忆中，那妮子似乎也没有多么漂亮，脸庞都有些模糊了。"
  },
  {
    "segment_id": "0035",
    "text": "倒是梦中世界里面，很多小说都有这个套路，特别是一堆莫名其妙的情敌，简直就是天生的龙套备选啊。"
  },
  {
    "segment_id": "0036",
    "text": "“再说，禁运物资，也并非什么大事！”"
  },
  {
    "segment_id": "0037",
    "text": "他笑了笑：“以后田老就不必如此辛苦了！”"
  },
  {
    "segment_id": "0038",
    "text": "“咦？”"
  },
  {
    "segment_id": "0039",
    "text": "田老汉看着方元，有些惊疑不定。"
  },
  {
    "segment_id": "0040",
    "text": "“我孤身一人，无牵无挂，也没有什么，倒是田老你，只要按照他们所说做了，他们也没有理由来找你麻烦！”"
  },
  {
    "segment_id": "0041",
    "text": "方元冷静分析道，又端出一盘药材：“这是这次的药材，钱货两清了。”"
  },
  {
    "segment_id": "0042",
    "text": "“唉……小居士，你多保重啊！”"
  },
  {
    "segment_id": "0043",
    "text": "田老汉长吁短叹，但见方元意思甚为坚定，只能无奈离开。"
  },
  {
    "segment_id": "0044",
    "text": "……"
  },
  {
    "segment_id": "0045",
    "text": "“谷内物资，倒是足够使用，盐油之类也不缺少……”"
  },
  {
    "segment_id": "0046",
    "text": "送走田老汉之后，方元翻了翻地上的竹篓。"
  },
  {
    "segment_id": "0047",
    "text": "这次老汉准备的物资份量很是充足，再加上储备，想必足够接下来几个月的生活所需。"
  },
  {
    "segment_id": "0048",
    "text": "“只是还火液需要的材料，有一味必须到外界收购，原本这次还想请田老汉代劳的……现在看来，也只有我亲自跑一趟了！”"
  },
  {
    "segment_id": "0049",
    "text": "方元轻叹口气：“还有这故意针对之事，也必然要查个清楚的……”"
  },
  {
    "segment_id": "0050",
    "text": "说实在话，他辟居幽谷之中，甚少出山，如今对于外面的世界，还当真有着几分向往之心。"
  },
  {
    "segment_id": "0051",
    "text": "既然决定外出，自然要有着准备。"
  },
  {
    "segment_id": "0052",
    "text": "方元首先挑了几株比较珍贵，有一定年份的炮制药材，作为这次的花费，又换了一身衣服鞋袜，当然，最关键的还是带够干粮。"
  },
  {
    "segment_id": "0053",
    "text": "外界的普通大米，哪里有他亲手培植的珍珠玉晶米好吃？"
  },
  {
    "segment_id": "0054",
    "text": "吃惯了自己培育出的蔬菜谷物，再吃外面的普通食物，就简直跟猪食没什么两样了。"
  },
  {
    "segment_id": "0055",
    "text": "准备完毕之后，再在腰间悬挂一柄柴刀，略作防身，方元当即施施然上路。"
  },
  {
    "segment_id": "0056",
    "text": "……"
  },
  {
    "segment_id": "0057",
    "text": "清灵山地域广泛，绵延数个郡县。"
  },
  {
    "segment_id": "0058",
    "text": "距离幽谷最近的，还是清河郡。"
  },
  {
    "segment_id": "0059",
    "text": "方元纵然甚少离开深山，但也曾经跟随问心居士出来过几次，暗中记下路径，不会有错。"
  },
  {
    "segment_id": "0060",
    "text": "一路过了几个村镇，又进入县城之后，方元心里一松：‘若真是归灵宗要对付我，以对方庞大的能量，我现在早就寸步难行了……现在看起来，我的猜测应该是真的，某个下面人的警告？’"
  },
  {
    "segment_id": "0061",
    "text": "一想到自己被当成潜在情敌，甚至对方手下的狗腿子迫不及待地跳出来找麻烦之场景，方元的脸色顿时有些发囧。"
  },
  {
    "segment_id": "0062",
    "text": "“实在不行，干脆去找林员外，这归根结底，还是对方惹出来的麻烦，总不好意思袖手不理的吧？”"
  },
  {
    "segment_id": "0063",
    "text": "交了入门钱之后，方元在县城的街道上漫无目的地行走着，心里则是默默思索。"
  },
  {
    "segment_id": "0064",
    "text": "对于他而言，只要能少些麻烦，面子当真不算什么。"
  },
  {
    "segment_id": "0065",
    "text": "不过经常劳烦人家，也不是长久之计，更何况两相见面，都有些尴尬，因此能自己解决，还是要尽量自己解决。"
  },
  {
    "segment_id": "0066",
    "text": "“炊饼！”"
  },
  {
    "segment_id": "0067",
    "text": "“胭脂水粉！”"
  },
  {
    "segment_id": "0068",
    "text": "“上好的金银首饰……”"
  },
  {
    "segment_id": "0069",
    "text": "……"
  },
  {
    "segment_id": "0070",
    "text": "纵然只是一个小县城，主干道上的店铺也很多，各种吆喝声此起彼伏，很是热闹，令方元看得津津有味，当然，也少不了被投几个看到乡巴佬进城的鄙视目光，只是他丝毫不以为意。"
  },
  {
    "segment_id": "0071",
    "text": "“调配还火液，需要离火木、无根水、还有雄黄粉……前两样我自己谷内就有出产，关键就是雄黄粉，得大大购置一批！”"
  },
  {
    "segment_id": "0072",
    "text": "方元心里盘算着，来到一家杂货铺前。"
  },
  {
    "segment_id": "0073",
    "text": "“客官需要什么？”"
  },
  {
    "segment_id": "0074",
    "text": "掌柜的是一名中年胖子，笑得很是和气。"
  },
  {
    "segment_id": "0075",
    "text": "“嗯，我需要上好的雄黄粉！另外……你这里收不收药材？”"
  },
  {
    "segment_id": "0076",
    "text": "上次林员外给了些金银，但方元下意识地还是想用自己的东西，那些金银直接窖藏，留作储备，日后再用。"
  },
  {
    "segment_id": "0077",
    "text": "毕竟，万一情况真的坏到了无与伦比的地步，需要跑路的时候，带金银当然比带着其它杂物方便多了。"
  },
  {
    "segment_id": "0078",
    "text": "方元纵然舍不得幽谷，却也不是傻子，关键时刻自然知道应该怎么选择。"
  },
  {
    "segment_id": "0079",
    "text": "“收！收！”"
  },
  {
    "segment_id": "0080",
    "text": "掌柜一怔，旋即笑呵呵地道：“小兄弟有着什么山药，尽管带来！”"
  },
  {
    "segment_id": "0081",
    "text": "“嗯！”"
  },
  {
    "segment_id": "0082",
    "text": "方元也知晓，别看这掌柜笑眯眯的，一旦自己拿出之物太过珍贵，八成就要动什么不好心思了。"
  },
  {
    "segment_id": "0083",
    "text": "反正自己一看就是山里穷小子，又有什么后台？"
  },
  {
    "segment_id": "0084",
    "text": "思虑之下，取出一个布包，立即引起了掌柜的注意，但一层层打开，看到是一株红参之后，脸上又浮现出失望之色。"
  },
  {
    "segment_id": "0085",
    "text": "“红山参，二十年份，品相倒是不错！让我再看看……”"
  },
  {
    "segment_id": "0086",
    "text": "方元拿出来的东西，算不上多么珍惜，但也还不错，掌柜下意识地就要找些破绽，狠狠压价，但仔细看后，又是有些倒吸凉气。"
  },
  {
    "segment_id": "0087",
    "text": "因为这株红参从品相、保存、色泽……各方面来看，都几乎找不出破绽，最后只能道：“可惜……还是年份太浅，我只能给个……”"
  },
  {
    "segment_id": "0088",
    "text": "“等一等，这东西我要了！”"
  },
  {
    "segment_id": "0089",
    "text": "他话还没有说完，旁边一只手掌就直接将红参取过，仔细看了看：“可惜……年份不足！”"
  },
  {
    "segment_id": "0090",
    "text": "这声音如同黄莺一般，空灵娇嫩，而方元则是转过头，看着这名穿着鹅黄色长衫的少女，脸上带着不悦：“这位姑娘，这株红参，还是我的东西！”"
  },
  {
    "segment_id": "0091",
    "text": "“你要多少银两？”"
  },
  {
    "segment_id": "0092",
    "text": "那姑娘大概十七八岁，与方元差不多大，直接问道。"
  },
  {
    "segment_id": "0093",
    "text": "“这并非银钱的问题，而是在下正准备拿它跟掌柜换取其它货物，姑娘此举，却是有着巧取豪夺之嫌了！”"
  },
  {
    "segment_id": "0094",
    "text": "方元摇摇头，将那个少女气得脸色涨红：“你！”"
  },
  {
    "segment_id": "0095",
    "text": "“这位小兄弟，在下妹妹也是心忧家父病情，这才心急失礼，还请小兄弟与掌柜的莫怪！”"
  },
  {
    "segment_id": "0096",
    "text": "这时候，从这姑娘身后，一名穿着青衫的少年就走了出来，赔礼说道。"
  },
  {
    "segment_id": "0097",
    "text": "“哪里，哪里，令妹一片纯孝，定能感动上天的！”"
  },
  {
    "segment_id": "0098",
    "text": "对方似乎在这里势力颇大，掌柜的连连搓手赔笑道。"
  }
]
```

## Output Format
CRITICAL INSTRUCTION: You MUST translate the source text EXACTLY paragraph by paragraph, preserving the original order perfectly. DO NOT skip, drop, merge, or reorder any paragraphs. Each paragraph in the source MUST be translated.
Return ONLY valid JSON matching this schema:
{
  "chapter_number": 5,
  "chapter_title_vi": "Chương 5: <Vietnamese title>",
  "segments": [
    {
      "segment_id": "XXXX",
      "source": "...",
      "target": "..."
    }
  ]
}
