# Translation Context Pack

## Project
- Branch: Co Chan Nhan
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


## Source Chapter 3 - 0003 请一边玩蛋去
```json
[
  {
    "segment_id": "0001",
    "text": "# 第三节：请一边玩蛋去"
  },
  {
    "segment_id": "0002",
    "text": "邦、邦邦，邦、邦邦。"
  },
  {
    "segment_id": "0003",
    "text": "巡游的更夫，敲着有节奏的梆子。"
  },
  {
    "segment_id": "0004",
    "text": "声音传入高脚吊楼，方源睁开干涩的眼皮，心中暗道：“是五更天了。”"
  },
  {
    "segment_id": "0005",
    "text": "昨夜躺在床上思索了很久，计划安排了一大堆，算起来只睡了一个时辰多丁点。"
  },
  {
    "segment_id": "0006",
    "text": "这个身体还没有开始修行，精力并不旺盛，因此一阵阵的疲累困乏之意，仍旧笼罩着身心。"
  },
  {
    "segment_id": "0007",
    "text": "不过五百多年的经历，早就打造了方源钢铁般深沉的毅志。这点嗜睡之意，根本就算不了什么。"
  },
  {
    "segment_id": "0008",
    "text": "当即便推开身上的薄丝被褥，干净利落地起了身。"
  },
  {
    "segment_id": "0009",
    "text": "推开窗户，春雨已经停了。"
  },
  {
    "segment_id": "0010",
    "text": "混合着泥土、树木和野花的香味的清新湿气，顿时扑面而来。方源顿感头脑一清，昏沉的睡意被驱除了干净。"
  },
  {
    "segment_id": "0011",
    "text": "此时太阳还未升起，天空蓝的深沉，似暗似亮。"
  },
  {
    "segment_id": "0012",
    "text": "放眼望去，用绿竹和树木搭建的高脚吊楼，和群山相衬着，一片幽静苍绿之色。"
  },
  {
    "segment_id": "0013",
    "text": "高脚吊楼至少有两层，是山民居住屋的特有结构。因为山上崎岖不平，因此一楼是巨大的木桩，二楼才是人的居所。"
  },
  {
    "segment_id": "0014",
    "text": "方源和弟弟方正是住在二楼。"
  },
  {
    "segment_id": "0015",
    "text": "“方源少爷，您醒了。奴家这就上楼来，伺候您洗漱。”就在此刻，楼下传来一个少女的声音。"
  },
  {
    "segment_id": "0016",
    "text": "方源低头一看，是自己的贴身丫鬟沈翠。"
  },
  {
    "segment_id": "0017",
    "text": "她姿容只能算上中等，但打扮得好，穿着一身绿衫，长袖长裤，脚下是绣花鞋，黑发上还有一个珍珠簪子，全身上下都散发出青春的活力。"
  },
  {
    "segment_id": "0018",
    "text": "她欢喜地望了一眼方源，端着一盆水，蹬蹬蹬的就上了楼。"
  },
  {
    "segment_id": "0019",
    "text": "水是调好的温水，用来洗脸。漱口则用柳条沾着雪盐，能净齿白牙。"
  },
  {
    "segment_id": "0020",
    "text": "沈翠温柔的伺候着，脸上带着笑颜，眉目含春。而后又为方源穿衣结扣，在这过程中时不时地用丰满的胸脯蹭方源的胳膊，或者后背。"
  },
  {
    "segment_id": "0021",
    "text": "方源面无表情，心如止水。"
  },
  {
    "segment_id": "0022",
    "text": "这个丫鬟不仅是舅父舅母的眼线，而且爱慕虚荣，性情薄凉。上一世曾被其蒙蔽，到了开窍大典之后，自己地位一落千丈，她顿时就翻了脸，没少给过自己白眼。"
  },
  {
    "segment_id": "0023",
    "text": "方正来的时候，正看到沈翠为方源抚平胸口衣衫上的褶皱，眼中不由地闪过一丝羡慕嫉妒的光。"
  },
  {
    "segment_id": "0024",
    "text": "这些年跟着哥哥一起生活，受方源的照顾，他也有个奴仆伺候着。不过却不是沈翠这样的年轻丫鬟，而是个体型肥肿的老妈子。"
  },
  {
    "segment_id": "0025",
    "text": "“若是哪天，沈翠能伺候我这样，该是什么滋味？”方正心中有些想，又有些不敢想。"
  },
  {
    "segment_id": "0026",
    "text": "舅母舅父偏爱方源，这是府上众所周知的事情。"
  },
  {
    "segment_id": "0027",
    "text": "本来他都没有奴仆伺候，还是方源主动为方正要求来的。"
  },
  {
    "segment_id": "0028",
    "text": "虽说有着主仆的身份区别，但是平日里方正也不敢小瞧这个沈翠。皆因沈翠的母亲，就是舅母身边的沈嬷嬷，也是整个府里的管家，深受舅母之信任，有着不小的权柄。"
  },
  {
    "segment_id": "0029",
    "text": "“好了，不用收拾了。”方源不耐地拂开沈翠的柔软小手，衣衫早就平整，沈翠更多的是在引诱。"
  },
  {
    "segment_id": "0030",
    "text": "对她来讲，自己前途光明，甲等资质的可能性极大，若是能成为方源的侧室，就能从奴转为主，可谓一步登天。"
  },
  {
    "segment_id": "0031",
    "text": "上一世方源被蒙蔽过，甚至喜欢上这个婢女。重生之后却是洞若观火，心冷似霜。"
  },
  {
    "segment_id": "0032",
    "text": "“你退下罢。”方源看也不看沈翠，整理着自己的袖口。"
  },
  {
    "segment_id": "0033",
    "text": "沈翠微微撅嘴，为方源今日的不解风情感到有些奇怪和委屈。想要说什么撒娇的话，但是被方源若有若无的莫名气质震慑着，张口几次，最终说了声“是”，乖乖地退下。"
  },
  {
    "segment_id": "0034",
    "text": "“你准备好了？”方源看向方正。"
  },
  {
    "segment_id": "0035",
    "text": "弟弟呆呆地站在门口，低下头看着自己的脚尖，轻轻地嗯了一声。"
  },
  {
    "segment_id": "0036",
    "text": "他其实四更时就醒了，紧张的睡不着，偷偷起床早早就准备好了，两个眼圈都是黑的。"
  },
  {
    "segment_id": "0037",
    "text": "方源点点头，弟弟心中的想法，在前世他并不清楚，不过今生他又怎么不明白？"
  },
  {
    "segment_id": "0038",
    "text": "但此时点破毫无意义，淡淡地吩咐着：“那就走吧。”"
  },
  {
    "segment_id": "0039",
    "text": "于是兄弟俩就走出了居所，一路上，碰到不少的同龄人，三三两两的，显然有着相同的目的地。"
  },
  {
    "segment_id": "0040",
    "text": "“你们看，那是方家两兄弟。”小耳边传来小心翼翼的议论声。"
  },
  {
    "segment_id": "0041",
    "text": "“前面走着的就是那个方源，就是那个作诗的方源。”有人强调着。"
  },
  {
    "segment_id": "0042",
    "text": "“原来是他呀，面无表情、旁若无人的样子，果真和传闻中一样拽。”有人语气酸酸，带着嫉妒和羡慕。"
  },
  {
    "segment_id": "0043",
    "text": "“哼，你要是能像他一样，你也可以这样拽！”有人冷哼着这样回答，隐藏着一种不满。"
  },
  {
    "segment_id": "0044",
    "text": "方正面无表情地听着，这样的议论声他早已习惯了。"
  },
  {
    "segment_id": "0045",
    "text": "他低着头，跟在哥哥的身后，默默走着。"
  },
  {
    "segment_id": "0046",
    "text": "此时天边已经亮起晨光，方源的影子就投在他的脸上。"
  },
  {
    "segment_id": "0047",
    "text": "朝阳在渐渐升起，但是方正却忽然觉得，自己正走向黑暗。"
  },
  {
    "segment_id": "0048",
    "text": "这个黑暗来源于他的哥哥，也许这一辈子，自己都不能挣脱哥哥笼罩自己的巨大阴影。"
  },
  {
    "segment_id": "0049",
    "text": "他感到胸口传来一阵阵的压抑，甚至是呼吸不畅，这该死的感觉让他甚至联想到“窒息”这个词！"
  },
  {
    "segment_id": "0050",
    "text": "“哼，这样的议论，果真是木秀于林风必催之。”听着耳边的议论声，方源心中冷笑着。"
  },
  {
    "segment_id": "0051",
    "text": "难怪在测出自己的丙等资质后，会四面环敌，很长一段时间都受着苛刻、白眼、冷遇。"
  },
  {
    "segment_id": "0052",
    "text": "身后弟弟方正越来越沉闷的喘息声，他也尽收耳底。"
  },
  {
    "segment_id": "0053",
    "text": "前世没有察觉到的，今生则是明察秋毫。"
  },
  {
    "segment_id": "0054",
    "text": "这都是五百年人生经历带来的敏锐洞察力。"
  },
  {
    "segment_id": "0055",
    "text": "他忽然想到舅父舅母，真是有些手段。给自己配了沈翠来贴身监控，给弟弟配的老嬷嬷。其实还有其他生活细节上的差别待遇。"
  },
  {
    "segment_id": "0056",
    "text": "这都是有意为之，就是要挑起弟弟心中的不平之气，挑拨和自己的兄弟情谊。"
  },
  {
    "segment_id": "0057",
    "text": "世人皆不患寡，而患不均。"
  },
  {
    "segment_id": "0058",
    "text": "前世自己经历太少，弟弟又太傻太天真，被舅父舅母挑拨成功。"
  },
  {
    "segment_id": "0059",
    "text": "重生以来，眼看着就要开窍大典，局面看似积重难返，但是以方源魔道巨擘的手段和智慧，也不是不可以改变。"
  },
  {
    "segment_id": "0060",
    "text": "这弟弟完全可以镇压收服，沈翠一个小小的丫头片子，更能提早收入后.宫。还有舅父舅母、族长家老，敲打他们至少有数百种方案。"
  },
  {
    "segment_id": "0061",
    "text": "“但是，我却不想这么做呀……”方源在心中悠然一叹。"
  },
  {
    "segment_id": "0062",
    "text": "就算是亲弟弟又如何，没有亲情可言，只是个外人罢了，舍了也就舍了。"
  },
  {
    "segment_id": "0063",
    "text": "就算是沈翠长得再漂亮又如何，没有爱和忠心，不过是一具肉体。收入后.宫？她还不配。"
  },
  {
    "segment_id": "0064",
    "text": "就算是舅父舅母，族长家老又如何，都是生命中的过客，何必费尽心机，耗散精力，来敲打这些路人？"
  },
  {
    "segment_id": "0065",
    "text": "呵呵。"
  },
  {
    "segment_id": "0066",
    "text": "只要不阻碍我赶路，那就一边玩自己的蛋去，踩都不屑踩。;"
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
