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

## Chapter 0003 - Chương 3: Đỉnh Hồ phái

### Summary
Chapter 3 completed via pipeline.

## Chapter 0004 - Chương 4: Bán bộ vô địch thần công

### Summary
Chapter 4 completed via pipeline.


## Source Chapter 5 - 0005 道果之器
```json
[
  {
    "segment_id": "0001",
    "text": "# 第5章 道果之器"
  },
  {
    "segment_id": "0002",
    "text": "虽然姜离帅气又全能，符法、武功、卜算无一不精，但由于他比较能藏，平日里就算接追缉任务也是专挑软柿子，这使得知晓他真正实力的人屈指可数。"
  },
  {
    "segment_id": "0003",
    "text": "就说卜算，除了姜离自己以外，无人知晓他的造诣如何，否则的话，周明云也不会想着埋伏姜离，甚至失败了六次还不罢休。"
  },
  {
    "segment_id": "0004",
    "text": "那么问题来了，一个除了帅以外其余地方都不上不下的少年，有何资格让人对他产生杀意，并且如此殷切地下手？总不可能真就为了一千五善功吧。"
  },
  {
    "segment_id": "0005",
    "text": "排除那人脑袋有坑的可能，就只剩下出身了。"
  },
  {
    "segment_id": "0006",
    "text": "‘姜家的政敌？仇人？难道是未婚妻？’"
  },
  {
    "segment_id": "0007",
    "text": "贵族子弟落魄之后惨遭嫌弃，未婚妻意图以谋杀手段来摆脱婚约？"
  },
  {
    "segment_id": "0008",
    "text": "如果是这样的话就好了，妥妥的主角待遇，可惜姜离并没有未婚妻。"
  },
  {
    "segment_id": "0009",
    "text": "‘从当下情况来看，还是仇人的概率更大。’"
  },
  {
    "segment_id": "0010",
    "text": "姜离心中思索，表面上则是毫无异色地走到了距离武曲坪不远的弟子寮舍，进入自己的房间。"
  },
  {
    "segment_id": "0011",
    "text": "关上了的房门隔开了远方窥伺的视线，同时有淡淡的光泽在房梁、地面、门窗等地方出现，一道道符箓亮起又隐去。"
  },
  {
    "segment_id": "0012",
    "text": "‘没人进过我的房间，也就是说······单纯只想要我的命。’"
  },
  {
    "segment_id": "0013",
    "text": "姜离见状，得出得出一个不太好的结论。"
  },
  {
    "segment_id": "0014",
    "text": "不进他的房间，说明敌人对外物不感兴趣，否则绝对是要进姜离房间搜寻一番的。"
  },
  {
    "segment_id": "0015",
    "text": "他，或者他们，只想要姜离的命。"
  },
  {
    "segment_id": "0016",
    "text": "这就没得缓解了。"
  },
  {
    "segment_id": "0017",
    "text": "【一想到这里，姜离就目露寒光，杀机闪烁。"
  },
  {
    "segment_id": "0018",
    "text": "你们这是取死有道！】"
  },
  {
    "segment_id": "0019",
    "text": "因果集适时显现出一句话，姜离见到后杀心一顿，突然有种尬意袭上心头。"
  },
  {
    "segment_id": "0020",
    "text": "这破书哪都好，就是这记录想法的功能有时候会尬住自己。"
  },
  {
    "segment_id": "0021",
    "text": "自己怎么想是一回事，看到自己的想法，又是另一回事了。尤其是一些话语，想想还好，真要是写出来，简直就像是在看中二日记，妥妥的黑历史。"
  },
  {
    "segment_id": "0022",
    "text": "这么一打岔，姜离心中的杀意反倒是渐渐平息了下来，摇头失笑。"
  },
  {
    "segment_id": "0023",
    "text": "他走到不远处的书桌后坐下，将能增长实力的物事一一拿出。"
  },
  {
    "segment_id": "0024",
    "text": "六丁六甲护身符法、楼观剑法、容纳“长蛇”道果的蛇牙匕首，还有一枚玉符。"
  },
  {
    "segment_id": "0025",
    "text": "玉符和蛇牙匕首一样，都是储纳道果的载体。"
  },
  {
    "segment_id": "0026",
    "text": "按照外门长老所说，道果乃是强者遗留在世间的痕迹，是其力量的投影，会自动依附到和道果契合的物体当中。"
  },
  {
    "segment_id": "0027",
    "text": "这些被道果依附的物体，统称为道器。"
  },
  {
    "segment_id": "0028",
    "text": "前五品的道果之器甚至拥有一些特殊能力，哪怕不被容纳，也可给拥有者带来极强的臂助，而后四品的道果之器就有些拉胯了，一般只有让载体难以毁坏的作用。"
  },
  {
    "segment_id": "0029",
    "text": "之所以如此，乃是因为后四品的道果非是真正的强者痕迹，而是人为的产物。"
  },
  {
    "segment_id": "0030",
    "text": "就姜离所知，“道人”便是复制五品道果·天师的部分能力，然后加工炼制出来的。"
  },
  {
    "segment_id": "0031",
    "text": "其余的人属、仙属、佛属、神属道果也基本都是如此，都是人工量产的。"
  },
  {
    "segment_id": "0032",
    "text": "至于魔、妖、鬼、怪的低级道果，则是打杀妖魔鬼怪，取其精粹炼制而成。"
  },
  {
    "segment_id": "0033",
    "text": "也正是因此，各门各派才会有大量的低级道果供弟子们容纳，没让修行者彻底成为少数群体。"
  },
  {
    "segment_id": "0034",
    "text": "而真正的妖魔鬼怪则是都快死光了，现在各地流传的各种妖怪奇闻，九成九是容纳妖属道果之人所造成的。      话归正题，姜离手上的两件道器，蛇牙匕首硬又锐，可以作防身之用。而玉符在没了道果之后，已经不算是道器了，但它却是极好的符箓载体。"
  },
  {
    "segment_id": "0035",
    "text": "相较于匕首而言，玉符的作用反倒更大。"
  },
  {
    "segment_id": "0036",
    "text": "它可以用来制作六丁六甲护身符。"
  },
  {
    "segment_id": "0037",
    "text": "姜离将玉符放到符法书册上面。"
  },
  {
    "segment_id": "0038",
    "text": "然后再看楼观剑法，同时，因果集上也显示出那部半步无敌神功。"
  },
  {
    "segment_id": "0039",
    "text": "楼观，为“结草为楼，观星望气”之意，乃是末法前一大派之名。楼观剑法正是楼观派之法，是一门料敌机先、后发先至的武功。"
  },
  {
    "segment_id": "0040",
    "text": "这门剑法需要修炼者具备一定的术算造诣，正好适合姜离，且威能也是不俗，在九品中堪称顶尖。"
  },
  {
    "segment_id": "0041",
    "text": "至于折花手，它的厉害，懂的都懂。"
  },
  {
    "segment_id": "0042",
    "text": "姜离稍作思索，便直接拿起了符法书册翻开。"
  },
  {
    "segment_id": "0043",
    "text": "保命第一，还是先学符箓。"
  },
  {
    "segment_id": "0044",
    "text": "末法之前的符法，被视为沟通天地、使役鬼神的妙法，其类别也大致分为连接天地和沟通鬼神两种。"
  },
  {
    "segment_id": "0045",
    "text": "不过在末法之后，灵机都化为五浊恶气，神灵估计也都成道果了，旧有的符法体系全废了。"
  },
  {
    "segment_id": "0046",
    "text": "末法后的符法体系，就只有一种沟通对象——自己。"
  },
  {
    "segment_id": "0047",
    "text": "以符箓为媒介，以气为源，化出风火雷电等奇能，也可显化出各种神形，具现出各种请神符箓的作用。"
  },
  {
    "segment_id": "0048",
    "text": "符箓就等同于使用者的外置经脉，其复杂程度不下于同品级的心法，无论是笔画和力度，皆有大讲究，还需一气呵成。"
  },
  {
    "segment_id": "0049",
    "text": "而六丁六甲护身符按品级算，是七品，也就是说，姜离绘制此符的难度相当于跨级运行七品心法，甚至更大。"
  },
  {
    "segment_id": "0050",
    "text": "以普遍理性来讲，能在九品就制出此符的人，不是绝世天才，就是有深蓝可以加点。"
  },
  {
    "segment_id": "0051",
    "text": "万长老认为姜离能够画出此符，实际上是高看他了。"
  },
  {
    "segment_id": "0052",
    "text": "姜离不是绝世天才，哪怕他有道果加持悟性暂时也不太行，毕竟他的三教底蕴还不算太深，也没有修改器，但是······"
  },
  {
    "segment_id": "0053",
    "text": "“我可以肝。”"
  },
  {
    "segment_id": "0054",
    "text": "姜离深吸一口气，从桌下拿出厚厚一叠黄纸。"
  },
  {
    "segment_id": "0055",
    "text": "因果集固化因果的能力让姜离的努力不会白费，如今他刚容纳道果，潜力大增，正是大肝特肝之时。"
  },
  {
    "segment_id": "0056",
    "text": "一次不行就十次，十次不行就百次，只要肝不死，就往死里肝。"
  },
  {
    "segment_id": "0057",
    "text": "姜某人能有今日的成就，全凭自己的努力，全凭足够肝。"
  },
  {
    "segment_id": "0058",
    "text": "“决定了，在肝出十张···不，五十张六丁六甲护身符之前，绝不出门！”"
  },
  {
    "segment_id": "0059",
    "text": "“不对，我还要吃喝拉撒。可恶！为什么现在的修行者还要为吃喝拉撒烦恼。那就绝对不出门派！”"
  },
  {
    "segment_id": "0060",
    "text": "宗门里倒是有可以用善功兑换的辟谷丹，可惜太贵了。现在这时代，第一珍贵的是道果，第二就是丹药了。"
  },
  {
    "segment_id": "0061",
    "text": "以姜离如今的资产，辟谷丹就是一遥远的梦，还是老老实实吃喝拉撒吧。"
  },
  {
    "segment_id": "0062",
    "text": "总而言之，就是先稳健发育一波，护身符肝好，武功学好，要是能一路肝到八品，那自然是更好了。"
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
