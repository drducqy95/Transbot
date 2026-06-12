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

## Chapter 0005 - Chương 5: Xuất sơn (Cầu đề cử)

### Summary
Chapter 5 completed via pipeline.


## Source Chapter 6 - 0006 遭贼
```json
[
  {
    "segment_id": "0001",
    "text": "# 第6章 遭贼"
  },
  {
    "segment_id": "0002",
    "text": "“那是什么人？”"
  },
  {
    "segment_id": "0003",
    "text": "看着兄妹二人离开的背影，方元一边整理着上品雄黄粉，一边随口问道。"
  },
  {
    "segment_id": "0004",
    "text": "“他们啊……可是县城大户，周家之人，今日你算运气好，遇到了周家二公子出来，否则若单独是他家的刁蛮小姐，那真是……”"
  },
  {
    "segment_id": "0005",
    "text": "掌柜的摇了摇头，显然对此了解颇深。"
  },
  {
    "segment_id": "0006",
    "text": "“要红山参，治病么？周家老爷染疾了？”"
  },
  {
    "segment_id": "0007",
    "text": "“哪有那么简单，周家背靠归灵宗，周家老爷也是一名执事，据说是受了伤！内伤！因此才要诸多草药大补元气，可惜……若你那株红参有着一百年！不……五十年份，说不定就可试试去揭榜文了！”"
  },
  {
    "segment_id": "0008",
    "text": "“榜文？”"
  },
  {
    "segment_id": "0009",
    "text": "方元来了兴趣：“掌柜的你给我说说呗。”"
  },
  {
    "segment_id": "0010",
    "text": "“嗨……那有什么？左右不过是周家见老爷子迟迟未愈，发出榜文，招募良医，声明只要能妙手回春，什么条件都可答应……”"
  },
  {
    "segment_id": "0011",
    "text": "掌柜的叹息一声，显然对那位周家老爷的未来不甚看好了。"
  },
  {
    "segment_id": "0012",
    "text": "方元听了，却是下意识地瞥了一眼自己的属性栏，里面的医术明晃晃地杵在那里。"
  },
  {
    "segment_id": "0013",
    "text": "能被这个系统看上并且收录的内容，那都是入了品阶的。"
  },
  {
    "segment_id": "0014",
    "text": "方元虽然掌握了不少技能，但真正被收录的，仍旧只有被问心居士点拨过的医术与种植。"
  },
  {
    "segment_id": "0015",
    "text": "因此，比起那些普通医生而言，方元自觉也算得上良医了。"
  },
  {
    "segment_id": "0016",
    "text": "只是他天性懒散，对那周家小姐的脾性也不怎么喜欢，半点都没有毛遂自荐的心思。"
  },
  {
    "segment_id": "0017",
    "text": "‘倒是周家也是归灵宗之人，说不定就有着武功秘籍什么的……不过这条路还是有些危险，放弃吧……’"
  },
  {
    "segment_id": "0018",
    "text": "那周家兄妹虽然有些无礼，但财大气粗，价钱给得很足，令方元不仅购置了大批雄黄粉，甚至手上还有着余钱。"
  },
  {
    "segment_id": "0019",
    "text": "出了商铺，当即又在街上闲逛，左顾右盼，自得其乐。"
  },
  {
    "segment_id": "0020",
    "text": "‘说起来，这次的事情，应该就是归灵宗底下某个人的自作主张，并且能量也不是很大……’"
  },
  {
    "segment_id": "0021",
    "text": "到了正午，方元蹲在街角，一边啃着自己带来的饭团，一边思索着。"
  },
  {
    "segment_id": "0022",
    "text": "这是个好消息，代表着自己暂时不用背井离乡，仓惶逃离了。"
  },
  {
    "segment_id": "0023",
    "text": "对方断了自己的供应，未尝也没有逼迫自己离开的打算，只是如今不识趣，后面会如何，可就当真不好说了。"
  },
  {
    "segment_id": "0024",
    "text": "‘或许……应该去找本武功秘籍什么的练练？传说归灵宗有武宗坐镇，武宗是什么？很厉害么？还有武功，不知道系统认不认啊……’"
  },
  {
    "segment_id": "0025",
    "text": "饭团用的是珍珠玉晶米所做，中间包了酸梅，散发着阵阵食物香气。"
  },
  {
    "segment_id": "0026",
    "text": "在他周围，则是聚集了几个乞丐，目光炯炯，狂咽着口水，显然也是被香味吸引过来的。"
  },
  {
    "segment_id": "0027",
    "text": "看样子，若不是在人来人往的大街上，恐怕早就要过来直接抢了。"
  },
  {
    "segment_id": "0028",
    "text": "“呵呵……小乞丐，你原来在这里？”"
  },
  {
    "segment_id": "0029",
    "text": "就在方元被那些可怜巴巴的眼神盯得受不了，想着是不是施舍几个的时候，一个有些熟悉的声音在旁边响了起来。"
  },
  {
    "segment_id": "0030",
    "text": "他抬起头，顿时就看到了那位周家小姐，正趾高气昂地看着他。"
  },
  {
    "segment_id": "0031",
    "text": "“小乞丐？我么？”"
  },
  {
    "segment_id": "0032",
    "text": "方元有些愕然地指了指自己的鼻子。"
  },
  {
    "segment_id": "0033",
    "text": "“你跟乞丐挤在一堆，不是小乞丐又是什么？”"
  },
  {
    "segment_id": "0034",
    "text": "周家小姐笑嘻嘻地道，一边掏出绣着金丝银线的荷包：“怎么样？要不要大小姐打赏你几个小钱，好进饭馆享用一顿？”"
  },
  {
    "segment_id": "0035",
    "text": "方元顿时无语了，又看了看自己。"
  },
  {
    "segment_id": "0036",
    "text": "没办法，乡下人进城，不都是这幅模样么？"
  },
  {
    "segment_id": "0037",
    "text": "他翻了翻白眼，干脆不理不睬，直接啃着自己的饭团。"
  },
  {
    "segment_id": "0038",
    "text": "“呵呵……也就你这种乡下人，才将饭团当宝，本小姐可是刚刚从富贵楼……咦，什么这么香？”"
  },
  {
    "segment_id": "0039",
    "text": "周家大小姐琼鼻动了动，忽然间看向方元手里的饭团。"
  },
  {
    "segment_id": "0040",
    "text": "那一粒粒珍珠般的玉晶米，晶莹剔透，宛若水晶一般，与中间的梅子红白相称，完全不像是乡下人的东西。"
  },
  {
    "segment_id": "0041",
    "text": "当然，最关键的，还是那纯粹的米香。"
  },
  {
    "segment_id": "0042",
    "text": "她刚刚就在富贵楼用饭，吃的同样是玉晶米，但这种纯粹的香气，实在……实在是……不能忍了啊……"
  },
  {
    "segment_id": "0043",
    "text": "周家大小姐无限怨念地发现，自己刚刚吃过的肚子又咕咕叫了起来。"
  },
  {
    "segment_id": "0044",
    "text": "不，这并非单纯的肚子饿，而是吸引！美食的吸引！"
  },
  {
    "segment_id": "0045",
    "text": "她喉咙滚动，感觉方元正在吃着的饭团仿佛变成了一个黑洞，吸引着她的目光，怎么也摆脱不了。"
  },
  {
    "segment_id": "0046",
    "text": "不行了，再这样下去，口水都要流出来了！"
  },
  {
    "segment_id": "0047",
    "text": "周家大小姐明智地决定转身就走。"
  },
  {
    "segment_id": "0048",
    "text": "“那个……你要么？”"
  },
  {
    "segment_id": "0049",
    "text": "方元正好看见这姑娘的目光，感觉对方也是可怜，将最后一个饭团拿出来：“给你！”"
  },
  {
    "segment_id": "0050",
    "text": "“咕噜！”"
  },
  {
    "segment_id": "0051",
    "text": "周家小姐喉咙滚动，白玉般的脸庞却是变得涨红，手指发抖，一副想伸又不想伸的纠结模样，最后转为浓烈的气场爆发了：“开……开什么玩笑，我堂堂周家大小姐周文馨，又怎么……又怎么会……”"
  },
  {
    "segment_id": "0052",
    "text": "她说着，脚步却是不自觉地上前。"
  },
  {
    "segment_id": "0053",
    "text": "“哦，你不要啊！”"
  },
  {
    "segment_id": "0054",
    "text": "方元感觉听懂了，直接将饭团给旁边的一名小乞丐：“拿去吃吧！”"
  },
  {
    "segment_id": "0055",
    "text": "“谢谢大爷！”“谢谢大爷！”"
  },
  {
    "segment_id": "0056",
    "text": "这小乞丐之前就对着方元不停流口水，这时喜从天降，当即连连道谢，美滋滋地吃了起来。"
  },
  {
    "segment_id": "0057",
    "text": "看着他黑乎乎的小手一抓，饭团上就浮现出清晰的爪印，纵然周文馨都产生出暴殄天物的感觉。"
  },
  {
    "segment_id": "0058",
    "text": "“呜呜……好吃……好吃！”"
  },
  {
    "segment_id": "0059",
    "text": "小乞丐狼吞虎咽，三两口就将饭团啃完，最后更是连嘴角与发丝上的米粒都不放过，吃完之后，意犹未尽地舔着嘴唇手指。"
  },
  {
    "segment_id": "0060",
    "text": "“你……”"
  },
  {
    "segment_id": "0061",
    "text": "周文馨一下呆滞，面皮从白转红，又从红转白，突然‘哇’的一声哭了出来：“你欺负我！呜呜……”"
  },
  {
    "segment_id": "0062",
    "text": "也不知道为什么，心里就是觉得委屈非常，转身跑了。"
  },
  {
    "segment_id": "0063",
    "text": "周围认识她的人，纷纷向方元投来敬佩的目光。"
  },
  {
    "segment_id": "0064",
    "text": "竟然能将周家小辣椒都气哭了？嗯，小伙子人不可貌相！前途无量啊！"
  },
  {
    "segment_id": "0065",
    "text": "“这……”"
  },
  {
    "segment_id": "0066",
    "text": "方元摸了摸脑袋，感觉自己非常无辜，这姑娘自己哭了，关他鸟事？不得不说，有时候，智商并不等于情商。"
  },
  {
    "segment_id": "0067",
    "text": "但他情商再不正常，也知道再不跑的话，等到给小姑娘出头的人来了，那就是想跑都跑不了了。"
  },
  {
    "segment_id": "0068",
    "text": "当即转身就进入街道拐角，开溜去也。"
  },
  {
    "segment_id": "0069",
    "text": "……"
  },
  {
    "segment_id": "0070",
    "text": "方元的预感果然无比正确。"
  },
  {
    "segment_id": "0071",
    "text": "过了没有多久，一帮气势汹汹的家丁就飞扑而来，就差封闭四门，全城大索了。"
  },
  {
    "segment_id": "0072",
    "text": "可惜这时候，他早就悠哉悠哉地出了城，在回山的路上。"
  },
  {
    "segment_id": "0073",
    "text": "而整个县城中，又有几个认得他这个陌生人，知道他老窝在那里？"
  },
  {
    "segment_id": "0074",
    "text": "连那小浑蛋姓名都没问清楚的周家大小姐周文馨闹得鸡飞狗跳之后，也只能恹恹离去，倒是传闻越传越广，在诸多八卦与好事之人的流传下，最后竟然变成周家刁蛮小姐在一个山野穷小子面前吃了大亏，其中颇多喜闻乐见，不可描述之事，将周文馨气得七窍生烟，却又无处发泄。"
  },
  {
    "segment_id": "0075",
    "text": "“嗯……原来武宗，就是武者中的一个境界，觉醒元力，能以一敌百，万夫莫当……整个归灵宗，也只有一位……”"
  },
  {
    "segment_id": "0076",
    "text": "此时的方元，拿着随手花了几个铜板，从地摊上淘来的书册，却是看得津津有味。"
  },
  {
    "segment_id": "0077",
    "text": "这应该是某个读书人的笔记，上面写了许多见闻，看来他应当很喜欢游历，其中就有关于武宗的描述，方元看了之后，见猎心喜，当即买了下来。"
  },
  {
    "segment_id": "0078",
    "text": "“而我所在的山脉，被称为清灵山，这里是清河郡，刚才的县城是青叶城……”"
  },
  {
    "segment_id": "0079",
    "text": "令方元欣喜的是，通过对游记的解读，令他对这附近地域，乃至自己所处的世界，都有了一点了解。"
  },
  {
    "segment_id": "0080",
    "text": "“这个大陆似乎面积很广，纵然我所在的国度，也只是一个小国而已，与整个大陆相比，根本算不得什么，当然，对普通人而言，还是庞然大物一般了……”"
  },
  {
    "segment_id": "0081",
    "text": "从这部游记里面，方元知晓外面的世界很大，也非常精彩。"
  },
  {
    "segment_id": "0082",
    "text": "“纵然武宗，也不过能在附近百里称雄一时，并且除了武道之外，还应该有着其它的体系……”"
  },
  {
    "segment_id": "0083",
    "text": "方元将本子收进竹篓，起身开始继续跋涉。"
  },
  {
    "segment_id": "0084",
    "text": "“可惜，此时的我，连最基本的一本武功秘籍都弄不到，就根本不用考虑其它的东西了……”"
  },
  {
    "segment_id": "0085",
    "text": "回到幽谷之中，立即就有一种安心感传来。"
  },
  {
    "segment_id": "0086",
    "text": "“到底还是自己的狗窝最舒坦啊……”"
  },
  {
    "segment_id": "0087",
    "text": "虽然离开的时间不是很久，但方元还是不由生出一种游子归乡的情绪。"
  },
  {
    "segment_id": "0088",
    "text": "等到放下东西之后，他几乎是迫不及待地来到了种植园内。"
  },
  {
    "segment_id": "0089",
    "text": "“咦？”"
  },
  {
    "segment_id": "0090",
    "text": "只是来到路口，他的脸色就顿时变化了：“这脚印，有兽害？”"
  },
  {
    "segment_id": "0091",
    "text": "深山之中开辟种植园，鸟兽之类的侵害绝对是个大问题，好在问心居士于此道有着专长，能调配辟兽散。"
  },
  {
    "segment_id": "0092",
    "text": "猛虎、暴狼之类的猛兽，会用尿液标记领地，百兽莫敢相犯，辟兽散理论相同，实际上，就是用药材配置出类似东西，洒在周围，给其它动物造成此地已经有着‘领主’的错觉，就不敢冒然前来。"
  },
  {
    "segment_id": "0093",
    "text": "再有那么几只生冷不忌的，几个兽夹与陷阱也足以解决问题。"
  },
  {
    "segment_id": "0094",
    "text": "但现在，种植园里面的陷阱却是被一起破坏，里面的诱饵却消失得无影无踪，仿佛窃贼发出了无声的嘲笑。"
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
