# Translation Context Pack

## Project
- Branch: Theo Tu Than Bat Dau Danh Xuyen Qua Tong Man Vo Han
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
| Chinese | Vietnamese | Type |
| --- | --- | --- |
| 产地：衍生 | Sản địa: Phái sinh | term |
| 天赋评级： | Đánh giá thiên phú: | term |
| 天赋：限制器 | Thiên phú: Bộ hạn chế | term |
| 浅打 | Thiển Đả | term |


## Story Timeline (latest)

## Chapter 0001 - Chương 1: Ta Có Một Vẻ Đẹp Trị Số

### Summary
Chapter 1 completed via pipeline.

## Chapter 0002 - Chương 2: Không Gian Chung Yên

### Summary
Chapter 2 completed via pipeline.

## Chapter 0003 - Chương 3: Hóa Ra Ta Đang Cười

### Summary
Chapter 3 completed via pipeline.

## Chapter 0004 - Chương 4: Unohana (Truyện mới cầu cất chứa)

### Summary
Chapter 4 completed via pipeline.

## Chapter 0005 - Chương 5: Bạn Cùng Phòng Của Ta Là Aizen? (Ba canh cầu phiếu)

### Summary
Chapter 5 completed via pipeline.

## Chapter 0006 - Chương 6: Bài kiểm tra nhập học

### Summary
Chapter 6 completed via pipeline.

## Chapter 0007 - Chương 7: Kiếm đạo? Ta chưa từng học nha

### Summary
Chapter 7 completed via pipeline.


## Source Chapter 8 - 0008 白打，夜一（三更求票）
```json
[
  {
    "segment_id": "0001",
    "text": "# 第8章 白打，夜一（三更求票）"
  },
  {
    "segment_id": "0002",
    "text": "很快，上午的课程就结束了。"
  },
  {
    "segment_id": "0003",
    "text": "而直到这堂剑道课结束，都没人来找陆离对练，不过陆离倒也不是一直坐在那沉思过去的，他主动找蓝染切磋了一下。"
  },
  {
    "segment_id": "0004",
    "text": "最终的结果是他表面上完胜，实际上如何就难说了，别看蓝染现在还年轻，鬼知道他的战斗造诣达到什么层次了。"
  },
  {
    "segment_id": "0005",
    "text": "“陆君还真是不留情面啊，我还以为能多撑几招的。”"
  },
  {
    "segment_id": "0006",
    "text": "去食堂的路上，蓝染抱怨道，尽管是抱怨的话语，他脸上却带着淡淡的微笑，让人看不透他在想什么。"
  },
  {
    "segment_id": "0007",
    "text": "“可我总觉得惣右介的实力不止于此呢，希望下次能跟状态更好的你切磋。”"
  },
  {
    "segment_id": "0008",
    "text": "陆离也不戳破蓝染的面具，只是表露了自己对强者的渴望。"
  },
  {
    "segment_id": "0009",
    "text": "“那我尽量多从陆君这里学一些剑道技巧吧。”"
  },
  {
    "segment_id": "0010",
    "text": "蓝染笑着说道，在拐角处带路，“陆君还没去过食堂吧，我带你去，灵术院的伙食还是比较丰盛的。”"
  },
  {
    "segment_id": "0011",
    "text": "陆离听后精神一振，他可是好久没吃过东西了，尤其是正常的饭菜。"
  },
  {
    "segment_id": "0012",
    "text": "卯之花昨天带自己来真央灵术院时已经很晚了，所以交代了几句后就让宿舍老师带自己办入住了，而今天早上蓝染提醒自己别吃早饭，直接带着自己去了教室。"
  },
  {
    "segment_id": "0013",
    "text": "蓝染让自己别吃早饭多半是猜到了藤本老师会测验自己的剑道，可他没有猜到结局。"
  },
  {
    "segment_id": "0014",
    "text": "“这么大……”"
  },
  {
    "segment_id": "0015",
    "text": "走进食堂后，陆离吃了一惊，眼睛看着那一排排的打饭窗口，鼻子嗅着空气中饭菜的香气，咽了口口水。"
  },
  {
    "segment_id": "0016",
    "text": "“惣右介……这儿收费吗？”"
  },
  {
    "segment_id": "0017",
    "text": "陆离问道，他昨天还只是个流魂街的流民，身无分环。"
  },
  {
    "segment_id": "0018",
    "text": "蓝染步伐并未停顿，带着陆离朝一处打饭窗口走去，“放心吧，考虑到灵术院内有部分流民出身的学员，这里也是设有不少免费窗口的，而我觉得这里的豆腐还不错。”"
  },
  {
    "segment_id": "0019",
    "text": "“免费？不限量？”"
  },
  {
    "segment_id": "0020",
    "text": "陆离一听免费可就来劲儿了，他可是饿坏了，加上被公司关押的这段时间根本就没吃过人饭，现在只觉得肚子在不争气的叫。"
  },
  {
    "segment_id": "0021",
    "text": "蓝染也听到了陆离肚子的声音，看着陆离的神情心中古怪，他原本还有些怀疑陆离的流民身份，但现在对方看起来的确像是个没吃过饱饭的土狗。"
  },
  {
    "segment_id": "0022",
    "text": "“免费，不限量，你想吃多少就行，但不能浪费，否则这里的打饭阿姨可能会发怒。”"
  },
  {
    "segment_id": "0023",
    "text": "蓝染说道，而此时他已经排到了窗口前，打饭阿姨似乎也认识他，并且对他感官不错，还笑着打了招呼。"
  },
  {
    "segment_id": "0024",
    "text": "“来一份麻婆豆腐。”"
  },
  {
    "segment_id": "0025",
    "text": "“你还真是喜欢豆腐啊。”"
  },
  {
    "segment_id": "0026",
    "text": "打饭阿姨笑着给蓝染打饭，分量不多也不少，显然很清楚蓝染的食量。"
  },
  {
    "segment_id": "0027",
    "text": "到陆离了，陆离的目光扫过窗口内的食物，随后看向阿姨，有些不好意思的开口：“阿姨，请问我能都要一份吗？”"
  },
  {
    "segment_id": "0028",
    "text": "阿姨闻言也愣了下，“都要？我每种给你放一点？”"
  },
  {
    "segment_id": "0029",
    "text": "陆离摇了摇头，在蓝染怪异的目光中说道：“按照惣右介的那份豆腐的分量，每种都来一份，再给我来一盆米……可以吗？”"
  },
  {
    "segment_id": "0030",
    "text": "阿姨懵逼了，她目光在眼前这个阳刚俊朗的小伙子身上扫视，主要是看他的肚子，心说这孩子真能吃这么多吗？"
  },
  {
    "segment_id": "0031",
    "text": "正在场面尴尬时，蓝染居然开口了，“阿姨，陆君是昨天刚到学院的，很长时间没吃饭了，而且饭量比较大，您就先给他打上饭吧，如果吃不完的话我会帮他的。”"
  },
  {
    "segment_id": "0032",
    "text": "陆离有些意外，他没想到蓝染居然会帮他，也不知对方是在维持‘乐于助人’的三好青年形象，还是说有什么别的目的。"
  },
  {
    "segment_id": "0033",
    "text": "但不管怎么说，他现在的确很想饱餐一顿，对方这个情他承了。"
  },
  {
    "segment_id": "0034",
    "text": "“既然惣右介也这么说的话……”"
  },
  {
    "segment_id": "0035",
    "text": "阿姨似乎很喜欢蓝染，语气妥协了下来，开始给陆离打饭，最终盛了好几个铁盘子，另加一大铁盆的米，然后带着怀疑的目光推给了陆离，“……可别浪费啊。”"
  },
  {
    "segment_id": "0036",
    "text": "“谢谢阿姨，我一定吃完。”"
  },
  {
    "segment_id": "0037",
    "text": "陆离感谢道，随后用指头夹着四个铁板，将盘子端起来，正想要将那一盆米饭弄到自己头上顶着时，蓝染已经将那盆米端起来了。"
  },
  {
    "segment_id": "0038",
    "text": "“走吧，那边还有空位，你最好真的能吃完，否则我也帮不了太多忙。”"
  },
  {
    "segment_id": "0039",
    "text": "蓝染看了眼自己端着的那盆米，心说这家伙到底是对自己的胃有多自信啊？"
  },
  {
    "segment_id": "0040",
    "text": "“放心放心。”"
  },
  {
    "segment_id": "0041",
    "text": "陆离端着饭跟蓝染走向餐桌，落座后他就从蓝染手中抢一般的拿过那盆米，在蓝染奇怪的目光中开始风卷残云。      不止是蓝染，附近其他的学员看到陆离抱着个铁盆干饭，也是惊得忘记吞咽。"
  },
  {
    "segment_id": "0042",
    "text": "吃到一半，仿佛是注意到了蓝染的目光，陆离咽下一口饭菜，抬头看向蓝染，“惣右介，你怎么不吃？”"
  },
  {
    "segment_id": "0043",
    "text": "“哦……我刚刚在想事情。”"
  },
  {
    "segment_id": "0044",
    "text": "蓝染回神说道，然后用勺子挖了一口麻婆豆腐送入口中。"
  },
  {
    "segment_id": "0045",
    "text": "他这个人很少吃惊，但今天却三番五次的被惊到，先是陆离那超凡的战斗技艺，后是陆离那超凡的胃口……"
  },
  {
    "segment_id": "0046",
    "text": "他看着埋头干饭的陆离，心说在整个真央灵术院内，陆君恐怕是在免费窗口吃饭最赚的那一个。"
  },
  {
    "segment_id": "0047",
    "text": "不多时，陆离面前的饭菜一扫而空，他满足的摸着微微隆起的肚皮，有一种重生的感觉。"
  },
  {
    "segment_id": "0048",
    "text": "公司关押他的时候只会给他注射营养液，而实际上在那个年代，已经很难找到旧时代的饭菜了，真央灵术院的这顿饭，恐怕是他这辈子吃过最丰盛的一餐了。"
  },
  {
    "segment_id": "0049",
    "text": "吃饱后，他感觉胃部暖洋洋的，能量在不断的传向四肢百骸，这便是尸魂界料理的神奇之处了。"
  },
  {
    "segment_id": "0050",
    "text": "因为这里的一切都是灵子构成的，吃掉这些饭菜，就相当于补充了灵子，是不错的回复手段，长期享用优质食物的话，或许还对灵压的提升有好处。"
  },
  {
    "segment_id": "0051",
    "text": "当然，修炼肯定才是主流的提升灵压方式，只不过他还没上过相关课程，目前还不懂。"
  },
  {
    "segment_id": "0052",
    "text": "回宿舍的路上，蓝染走在陆离身后，一双深邃的眸子里有光在闪烁，就像是一个发现了新玩具的孩子。"
  },
  {
    "segment_id": "0053",
    "text": "他感觉自己的这位室友，很可能在某种意义上，和自己是一样的天才，起码是战斗的天才。"
  },
  {
    "segment_id": "0054",
    "text": "剑道领域如此强大，那么白打呢？瞬步呢？鬼道呢？"
  },
  {
    "segment_id": "0055",
    "text": "蓝染的嘴角在不经意间上扬，又瞬间恢复了原样。"
  },
  {
    "segment_id": "0056",
    "text": "陆君……感觉接下来的这几年，会越来越有趣呢。"
  },
  {
    "segment_id": "0057",
    "text": "…………"
  },
  {
    "segment_id": "0058",
    "text": "“在复杂的战斗情况中，有时我们需要斩魄刀以外的进攻或防御方式……”"
  },
  {
    "segment_id": "0059",
    "text": "讲台上的老师正进行着白打的理论教学，不知是不是有人打了招呼，这堂课前半部分也讲了相当多的基础，这次是真的让陆离听得昏昏欲睡。"
  },
  {
    "segment_id": "0060",
    "text": "反观他身旁的蓝染，倒是一幅很认真的样子，还时不时记一下笔记，完全是老师眼中的三好学生。"
  },
  {
    "segment_id": "0061",
    "text": "“……那么，接下来开始实战演练。”"
  },
  {
    "segment_id": "0062",
    "text": "讲师说话时目光扫视学员，在扫到陆离时顿了下，随后又将目光转移到另一个女生身上，“四枫院同学，你的白打成绩最好，带一下新来的同学。”"
  },
  {
    "segment_id": "0063",
    "text": "陆离也顺着讲师的目光看去，被点到的少女坐在靠窗的位置，皮肤是健康的巧克力色，留着紫色短发，样貌打扮本给人一种青春活力的感觉……"
  },
  {
    "segment_id": "0064",
    "text": "可此时她正懒洋洋的仰着头，双目微闭，嘴角还带着一丝口水，完全就是在午睡，而且像是做了什么好梦，嘴角还带着一丝痴笑。"
  },
  {
    "segment_id": "0065",
    "text": "“四枫院同学！”"
  },
  {
    "segment_id": "0066",
    "text": "讲师的声音高了几个分贝，显然是有些生气，可他也没有下一步动作，其他同学则是见怪不怪，似乎这个上课睡觉的女孩儿本就该有几分‘不认真’的资本。"
  },
  {
    "segment_id": "0067",
    "text": "“啊？到！”"
  },
  {
    "segment_id": "0068",
    "text": "少女终于被讲师的声音惊醒，如同被惊到的猫一般，打了个激灵从原地猛的跳了起来，双脚又轻盈的落地。"
  },
  {
    "segment_id": "0069",
    "text": "陆离看着这一幕目光变化，他感觉事情开始变得有意思了，姓四枫院的巧克力肤色美少女，算算年龄，这莫不是四枫院夜一？"
  },
  {
    "segment_id": "0070",
    "text": "他虽然看过原著，但死神这部漫画对于时间的描述很模糊，关于各队长的年龄也只能预估个大概，从区间计算的话，蓝染和夜一确实算是同代人，只是他没想到他们居然还是同期生。"
  },
  {
    "segment_id": "0071",
    "text": "也怪不得原著中夜一见到蓝染时口气揶揄，合着是老相识了啊。"
  },
  {
    "segment_id": "0072",
    "text": "上午的剑道课陆离没见到夜一，也不知道是不是对方逃课了。"
  },
  {
    "segment_id": "0073",
    "text": "此时老师看着夜一嘴角还没干的痕迹，也是头疼无奈，“今天有插班生，你跟他对练，教他一些白打的基础技巧。”"
  },
  {
    "segment_id": "0074",
    "text": "——————"
  },
  {
    "segment_id": "0075",
    "text": "看着象连续三更的份儿上，读者老爷们追读下吧，如果能有月票就更好啦(ω)"
  },
  {
    "segment_id": "0076",
    "text": "感谢我爱吃象肉打赏的10000点币，感谢无语望天打赏的500点币，感谢无力北归打赏的100点币"
  }
]
```

## Output Format
CRITICAL INSTRUCTION: You MUST translate the source text EXACTLY paragraph by paragraph, preserving the original order perfectly. DO NOT skip, drop, merge, or reorder any paragraphs. Each paragraph in the source MUST be translated.
Return ONLY valid JSON matching this schema:
{
  "chapter_number": 8,
  "chapter_title_vi": "Chương 8: <Vietnamese title>",
  "segments": [
    {
      "segment_id": "XXXX",
      "source": "...",
      "target": "..."
    }
  ]
}
