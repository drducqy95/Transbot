# Translation Context Pack

## Project
- Branch: Thai Nhat Dao Qua
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

## Chapter 0001 - Chương 1: Đạo Quả

### Summary
Chapter 1 completed via pipeline.

## Chapter 0002 - Chương 2: Nhân Quả Tập

### Summary
Chapter 2 completed via pipeline.


## Source Chapter 3 - 0003 鼎湖派
```json
[
  {
    "segment_id": "0001",
    "text": "# 第3章 鼎湖派"
  },
  {
    "segment_id": "0002",
    "text": "去时追追停停花了半个多月，回来时日夜兼程，五天便回到了宗门。"
  },
  {
    "segment_id": "0003",
    "text": "鼎湖派顾名思义，位于一处名为“鼎湖”的湖泊。"
  },
  {
    "segment_id": "0004",
    "text": "纵横三百里的大湖中有或大或小的岛山，其中最大一处名为“乔山”，那便是鼎湖派所在。"
  },
  {
    "segment_id": "0005",
    "text": "巍峨屹立的山岳有七座大殿以及若干楼阁庭院伴山而建，殿以七星命名，从低到高，摇光为尾，天枢为首。"
  },
  {
    "segment_id": "0006",
    "text": "若是从高处往下看去，便能看到七座大殿形成勺形，正合北斗七星之位。"
  },
  {
    "segment_id": "0007",
    "text": "姜离在鼎湖畔换船登岛，直入负责宗门任务的摇光殿，再转进后殿一间小房间，哐的一声将一木匣扔在一张案桌上。"
  },
  {
    "segment_id": "0008",
    "text": "“姜师弟！”"
  },
  {
    "segment_id": "0009",
    "text": "案桌后的青年不悦抬头，看向姜离。"
  },
  {
    "segment_id": "0010",
    "text": "青年身穿代表内门弟子的赤袍，仪表堂堂，一双剑眉扬起，挑起三分凌厉之势。"
  },
  {
    "segment_id": "0011",
    "text": "“罗仪师兄，”姜离道出对方全名，语气生硬，“犯事弟子周明云拒捕抗法，已被我当场毙杀，这是他的头颅。”"
  },
  {
    "segment_id": "0012",
    "text": "说着，他又将蛇牙匕首拍在木匣上，“还有他的道果。”"
  },
  {
    "segment_id": "0013",
    "text": "真气注入匕首，一丝残暴凶戾的气息闪过，姜离冷声道：“要不是师弟临时晋升，说不定现在被割头的就是我了。”"
  },
  {
    "segment_id": "0014",
    "text": "罗仪的脸僵住了。"
  },
  {
    "segment_id": "0015",
    "text": "只是感知气息，就知道这确实是道果无疑，并且还是以凶恶著称的妖属道果。"
  },
  {
    "segment_id": "0016",
    "text": "这件事，摇光殿，或者说他罗仪不在理。"
  },
  {
    "segment_id": "0017",
    "text": "虽然追捕周明云的任务是摇光殿长老定下的，但对任务品级的划分却是他罗仪在调查后裁定的。"
  },
  {
    "segment_id": "0018",
    "text": "他失职了。"
  },
  {
    "segment_id": "0019",
    "text": "这事情要是闹起来，背锅的肯定是他这经手人。"
  },
  {
    "segment_id": "0020",
    "text": "“这是为兄的不是，”罗仪立马换了个脸色，一脸歉意地道，“这样吧，追捕任务五百善功，为兄额外补偿师兄五百善功，以表歉意，如何？”"
  },
  {
    "segment_id": "0021",
    "text": "“不如何。”"
  },
  {
    "segment_id": "0022",
    "text": "姜离一脸冷峻地摇头，吐出三个字：“得加钱。”"
  },
  {
    "segment_id": "0023",
    "text": "听到前一句的时候，罗仪已是要冷脸，但听到后三个字，他立马松了一口气。"
  },
  {
    "segment_id": "0024",
    "text": "“没问题，”罗仪立马拿出弟子玉牌，道，“再加一千善功，这匕首也由师弟处置，怎么样？”"
  },
  {
    "segment_id": "0025",
    "text": "也就是说，此事就当是正常不入品的追捕任务，周明云没有容纳道果。至少在摇光殿的记录中，是如此。"
  },
  {
    "segment_id": "0026",
    "text": "一枚弟子玉牌以迅雷不及掩耳之势贴上，姜离笑得如春风般和煦，斩钉截铁地道：“一言为定。”"
  },
  {
    "segment_id": "0027",
    "text": "因果集也负责地记录着这一幕。"
  },
  {
    "segment_id": "0028",
    "text": "【双方达成了愉快的共识，此事就此了结。"
  },
  {
    "segment_id": "0029",
    "text": "但在姜离转身离去之际，罗仪看着他的身影，眼中闪过一丝不易察觉的寒光。】"
  },
  {
    "segment_id": "0030",
    "text": "‘寒光······’"
  },
  {
    "segment_id": "0031",
    "text": "转身背对罗仪的姜离步履不停，心中留神。"
  },
  {
    "segment_id": "0032",
    "text": "现实中，除非是修炼了瞳术，否则眼睛是绝对不会像闪光灯一样一会儿闪寒光，一会儿又闪锐光的，至少姜离没见过这种情况。"
  },
  {
    "segment_id": "0033",
    "text": "但在因果集的记录中，因为文字描写的关系，对某些不好形容的对象会适当地运用比喻的手法。"
  },
  {
    "segment_id": "0034",
    "text": "根据姜离多年经验和敏锐的直觉，寒光，代表的是恶意，甚至是杀意。"
  },
  {
    "segment_id": "0035",
    "text": "‘是因为这一千五百善功？还是说周明云之事？’"
  },
  {
    "segment_id": "0036",
    "text": "若是前者，只能说明罗仪此人心胸狭窄。姜离多出了一个敌人，但真要说威胁性，还真不大。"
  },
  {
    "segment_id": "0037",
    "text": "若是后者，那水就有点深了。"
  },
  {
    "segment_id": "0038",
    "text": "‘最好是前者，但也不能不考虑后者。而且，周明云这家伙怎么看都不像有被设计的资格，也就是说，要对付的人可能是我？’"
  },
  {
    "segment_id": "0039",
    "text": "一种迫切感油然而生。"
  },
  {
    "segment_id": "0040",
    "text": "要抓紧提升实力了。"
  },
  {
    "segment_id": "0041",
    "text": "姜离不动声色地走出摇光殿，沿着白玉般的石阶拾级而上，来到第六殿开阳。      开阳殿是外门弟子的主要活动场所。"
  },
  {
    "segment_id": "0042",
    "text": "殿外设有武曲坪，乃是弟子们演练武功的地方，弟子寮舍也在周边区域。"
  },
  {
    "segment_id": "0043",
    "text": "殿内，则设讲法堂，每七日都有外门长老在此处讲课。"
  },
  {
    "segment_id": "0044",
    "text": "开阳殿后方院落，还有收藏八品、九品功法的道法阁，姜离的目的地就是此处。"
  },
  {
    "segment_id": "0045",
    "text": "他走入后院，远远地就看见两个老者在阁前对弈。见到姜离走来，其中一个鹤发童颜的老者直接一拂棋盘，高兴地站起，“小姜来了，不下了。”"
  },
  {
    "segment_id": "0046",
    "text": "棋局被打乱，另一老者气得吹胡子瞪眼。"
  },
  {
    "segment_id": "0047",
    "text": "姜离走近，笑道：“云长老又耍赖皮了。”"
  },
  {
    "segment_id": "0048",
    "text": "说着，他走近几步行礼，对着鹤发老者口呼“云长老”，另一个只有几缕发丝雪白的老者则是被称作“万长老”。"
  },
  {
    "segment_id": "0049",
    "text": "二人皆是外门长老，万长老是负责看护道法阁的，而云长老则是他的棋友。"
  },
  {
    "segment_id": "0050",
    "text": "云长老闻言，却是一脸得意地道：“棋场如战场，而战场兵事，正该无所不用其极。”"
  },
  {
    "segment_id": "0051",
    "text": "“呵，下次你敢乱伸手，老夫就把你的手钉在棋盘上。”万长老冷笑道。"
  },
  {
    "segment_id": "0052",
    "text": "“下次的事，下次再说。”云长老浑不在意。"
  },
  {
    "segment_id": "0053",
    "text": "这二位当着姜离的面打嘴仗，显然是和他熟络异常，不摆长老的架子。"
  },
  {
    "segment_id": "0054",
    "text": "这也是姜离在过去两年半里努力的成果。"
  },
  {
    "segment_id": "0055",
    "text": "有因果集帮忙察言观色，再加上前世锻炼出来的职场宫斗术，姜离想要和一个人拉近关系，还是挺容易的。"
  },
  {
    "segment_id": "0056",
    "text": "“懒得和你瞎扯。”"
  },
  {
    "segment_id": "0057",
    "text": "万长老冷哼了一声，看向姜离，突得眉头微皱，鼻翼微动，“你又杀人了？”"
  },
  {
    "segment_id": "0058",
    "text": "姜离身上的血腥气经过连日奔波，早就该散去了，但万长老却是嗅觉灵敏，仅是一接触，就嗅到了那几近于无的气息。"
  },
  {
    "segment_id": "0059",
    "text": "“没办法，”姜离无奈道，“刀剑无眼，这生死搏杀，哪能留得下手？”"
  },
  {
    "segment_id": "0060",
    "text": "“这句话也就你自己信，”万长老有些不满地道，“上一次你用火雷符将人炸得面目模糊，要不是老夫替你担保，你怕是连赏格都拿不到。回去多念几遍静心咒，清清戾气，以后注意点。你这般行事，日后晋升道果时有你后悔的。”"
  },
  {
    "segment_id": "0061",
    "text": "鼎湖派的道果不似妖属道果那般凶戾，甚至不乏对心境、心性有严格要求的。杀心太重，日后晋升时怕是有颇多周折。"
  },
  {
    "segment_id": "0062",
    "text": "姜离也知道这情况，不过他个人的准则是——死掉的敌人才是最好的敌人。"
  },
  {
    "segment_id": "0063",
    "text": "为了防止被反杀、犯人在半路跑了等诸多意外，姜离对敌，一般是能打死就打死，打不死就撤。"
  },
  {
    "segment_id": "0064",
    "text": "他接过七次追捕、剿灭任务，一次主动放弃，六次目标全灭，从无俘虏。"
  },
  {
    "segment_id": "0065",
    "text": "也是得益于这个准则，姜离的任务少有失败之例，积累了不少善功，能够在晋升后的第一时间来道法阁兑换符法、功法。"
  },
  {
    "segment_id": "0066",
    "text": "“弟子领命。”"
  },
  {
    "segment_id": "0067",
    "text": "对于万长老的好意相劝，姜离恭敬应下，保证回去后念上个十来遍静心咒。"
  },
  {
    "segment_id": "0068",
    "text": "至于对敌留手？姜离觉得做人该有原则，当初心不改。"
  },
  {
    "segment_id": "0069",
    "text": "万长老面色稍霁，语气放缓了少许，道：“但愿如此。说吧，这一次来想换点什么？”"
  },
  {
    "segment_id": "0070",
    "text": "“弟子已晋升九品，自是要兑换九品符法，另外，还想学门武功防身。”姜离立马说道。"
  },
  {
    "segment_id": "0071",
    "text": "要是换做他人来，那就只能在道法阁里自己找功法，还不知道是否适合。以外门弟子的阅历，单看简介可没法全面了解功法的底细。"
  },
  {
    "segment_id": "0072",
    "text": "姜离就不一样了，他有人脉。"
  },
  {
    "segment_id": "0073",
    "text": "万长老思索一会儿，便道：“丙区第三个书架，有最全的九品符法图鉴，你可从中择取要兑换的符箓，然后去对应书架找到具体书简。至于武功，道人的能力偏向对真气的控制，当修行擅变化的武功，待老夫想想······”"
  },
  {
    "segment_id": "0074",
    "text": "“老夫倒是知道一门适合小姜你的武功，”云长老突然插言，脸上带着一丝让人捉摸不定的笑，“此功乃是一门绝顶神功，一旦练成，你距离无敌就只差一半，可称半步无敌。小姜你若有兴趣，可去癸区最后一个书架最后一层找寻。”"
  },
  {
    "segment_id": "0075",
    "text": "“最后一区最后一个书架最后一层······我怎么不知道那里有什么绝顶神功？”万长老嘟囔道。"
  },
  {
    "segment_id": "0076",
    "text": "他身为道法阁守阁长老，竟是还没他人了解阁内功法？"
  },
  {
    "segment_id": "0077",
    "text": "沉吟一会儿，万长老对姜离道：“道法阁内藏书甚多，说不定真有什么绝佳功法收藏，你可按这老滑头所言去找一找所谓的神功。若是寻找不到，便去乙区第三、四、五书架找寻吧。”"
  },
  {
    "segment_id": "0078",
    "text": "“多谢长老。”姜离称谢，然后进入道法阁内。"
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
