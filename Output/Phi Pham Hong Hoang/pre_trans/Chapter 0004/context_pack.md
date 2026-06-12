# Translation Context Pack

## Project
- Branch: Phi Pham Hong Hoang
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

## Chapter 0001 - Chương 1: Thiên địa sơ khai có Tỳ Hưu

### Summary
Chapter 1 completed via pipeline.

## Chapter 0002 - Chương 2: Quan Bất Chu ngộ công pháp

### Summary
Chapter 2 completed via pipeline.

## Chapter 0001 - Chương 1: Thiên địa sơ khai có Tỳ Hưu

### Summary
Chapter 1 completed via pipeline.

## Chapter 0002 - Chương 2: Quan Bất Chu ngộ công pháp

### Summary
Chapter 2 completed via pipeline.

## Chapter 0003 - Chương 3: Quan Bất Chu ngộ công pháp

### Summary
Chapter 3 completed via pipeline.


## Source Chapter 4 - 0004 观不周悟功法()
```json
[
  {
    "segment_id": "0001",
    "text": "# 第二章 观不周悟功法()"
  },
  {
    "segment_id": "0002",
    "text": "盘古开天辟地，这天地之中所产生的第一种元气，便是混沌元气。此种混沌元气因乃天地刚生，混沌并未完全分判之时所产生的第一种元气，故包含了混沌之气息，拥有混沌属性，无比暴烈，威能强悍至极，妙用更是无穷无尽。"
  },
  {
    "segment_id": "0003",
    "text": "在混沌元气出现之后，随着时间推移，天地演化渐渐完善，混沌元气再不能稳定存在，于是开始不断演化为可滋养万物的先天元气。如此过程将一直持续下去，直至整个洪荒天地完全稳定，所有混沌元气完全转化为先天元气之后方才停止。"
  },
  {
    "segment_id": "0004",
    "text": "洪荒天地演化完全之后，便要从先天向后天转化，先天元气也开始继续演变，渐渐演变为后天元气。这后天元气，也就是后世修士所言的天地元气了。"
  },
  {
    "segment_id": "0005",
    "text": "当然，这几个演化过程所持续的时间，都是以元会甚至量劫来计算的。几千年几万年对于这个过程来说，粗心一点甚至可以忽略不计。"
  },
  {
    "segment_id": "0006",
    "text": "无论是混沌元气，还是先天元气，都拥有着种种后天元气所没有的功效，对于生命演化有着无穷的妙用。"
  },
  {
    "segment_id": "0007",
    "text": "混沌元气交织演变的过程中，能够凭空产生种种强大的生命，产生先天而生，无父无母的生灵，比如此时洪荒天地之中所游荡的种种生灵，便是此种由混沌元气交织演变而成的生灵。"
  },
  {
    "segment_id": "0008",
    "text": "而先天元气，妙用虽然稍差于混沌元气，但弥漫天地之间，能够补充寿元，只要一直生活在先天元气之间，呼吸先天元气，便寿元无限，不老不死。"
  },
  {
    "segment_id": "0009",
    "text": "正是因为如此，洪荒天地开辟不到十万年时间，在这洪荒天地之中游荡的，还都是由混沌元气所演变而成的天地第一批生灵。"
  },
  {
    "segment_id": "0010",
    "text": "而显然，这些不老不死的天地第一批生灵力量强悍，寿命无穷，皆可称为先天神祇（音：其）！"
  },
  {
    "segment_id": "0011",
    "text": "罗帆所化的貔貅，显然是搭上了这最后一班先天神祇的车。"
  },
  {
    "segment_id": "0012",
    "text": "只是，和想象中不一样的是，他这个先天神祇，只有本能的吸收先天元气，本能的寻找混沌元气让其浸染身躯以壮其身，却并无任何传说中的修炼功法。"
  },
  {
    "segment_id": "0013",
    "text": "强大自身，是任何生命的本能。而作为从混沌元气之中诞生的先天神祇，想要强大自身，光是吸收先天元气显然是不够的。"
  },
  {
    "segment_id": "0014",
    "text": "罗帆虽然已经在这个散发无数混沌元气的地穴上趴了不知多少年时间，但因为他只能凭借混沌元气的侵染身躯方才能够吸收一点点的混沌元气，故而这地穴所散发出来的混沌元气并没有因为他的存在而加快多少。"
  },
  {
    "segment_id": "0015",
    "text": "从貔貅的记忆中知晓混沌元气对自己的好处，罗帆深深的吸入一口混沌元气，这混沌元气十分顺利的顺着鼻孔进入体内，只是，当他呼气的时候，这些混沌元气便再度从他的鼻孔之中出来。其中顶多只是少了微不可察的一丝丝被他所吸收罢了。"
  },
  {
    "segment_id": "0016",
    "text": "这还算他神魂成型之后所得到天大的好处了，在他神魂没有成型之前，他所吸收的混沌元气都不可能达到这一丝丝的量。"
  },
  {
    "segment_id": "0017",
    "text": "这个地穴时刻在散发着混沌元气，灰色的雾气之下，地穴周围三里范围显得格外荒凉。而在三里之外，各种植被却分外茂盛，古木森森，两者形成了极大的反差。"
  },
  {
    "segment_id": "0018",
    "text": "罗帆尝试了一下，发现无论自己如何努力，都拿这混沌元气毫无办法，对混沌元气的吸收没有任何加快的迹象，心中不由无奈起来。"
  },
  {
    "segment_id": "0019",
    "text": "“我之前神魂的出现，似乎是因为我在观察不周山，感受那不周山所散发的气息。会不会我想要吸收混沌元气也要像之前一样？是了！一定可以的！现在天地初开，万事万物依然在演化之中，每一样事物都定然包含了天地演化的某些奥秘，不周山乃是盘古脊梁所化，所包含的天地奥秘定然更多，我观察不周山，感受其散发的气息，定然可以领悟出一些天地奥秘，甚至可能因此而领悟出自己的功法也说不定！”罗帆双眼闪闪发光，心中充满了希望。"
  },
  {
    "segment_id": "0020",
    "text": "想起以前看过的小说中老是说某某前辈观某某现象或某某事物，领悟出某某功法，既然他们可以，自己来到这洪荒天地，还是刚刚开辟出来没多久，依然没有稳定下来，还在演化之中的洪荒天地，那领悟条件更好，没理由不行的！"
  },
  {
    "segment_id": "0021",
    "text": "有了这种自信，罗帆仰天发出一声长吼，“吼！”的一声龙吟有如雷鸣一般激荡周围灰蒙蒙的混沌元气。"
  },
  {
    "segment_id": "0022",
    "text": "罗帆已经下定决心想要从不周山之中领悟出自己的修炼功法自然不会再迟疑，身体挑了个舒服的姿态趴在地穴上，将散发混沌元气的地穴大概的堵在身下，极目远眺那高大至无法形容的不周山，心神放松，极力的感应着那不周山所散发出来的苍茫不屈气息。"
  },
  {
    "segment_id": "0023",
    "text": "在芝兰之室久而不觉其香。"
  },
  {
    "segment_id": "0024",
    "text": "同理，时刻处于那不周山散发的苍茫不屈气息笼罩之中，久了自然也就无法察觉这一股无比玄妙的气息存在了。"
  },
  {
    "segment_id": "0025",
    "text": "此时放松心神，过了良久，他方才再度感受到那一股无法形容其宏大的气息。"
  },
  {
    "segment_id": "0026",
    "text": "被这一股气息笼罩住整个心神，一种与天斗，与地斗，永不屈服，永不放弃的感觉在他心头泛出。"
  },
  {
    "segment_id": "0027",
    "text": "不周山的形象倒影在他的双眸之中，他心神渐渐凝聚，双眼视力渐渐增强，那原本模模糊糊的不周山渐渐变得清晰起来。"
  },
  {
    "segment_id": "0028",
    "text": "不周山乃是盘古脊梁，乃是西北天柱，其本身的功效决定了其定然蕴含了无尽的天地奥秘，甚至，单单其本身的形状，就拥有一股不可思议的威能！"
  },
  {
    "segment_id": "0029",
    "text": "在这一瞬间，罗帆忽然觉得自己已经完全融入了那种苍茫不屈的气息之中，自己似乎再度化身为那拔地而起，高耸入云的天柱，那无比广阔，无比稳固的大地，无比悠远，无比神秘的天空似乎完全和他融为一体。"
  },
  {
    "segment_id": "0030",
    "text": "随着这种感觉的出现，罗帆的身体也渐渐发生了变化。"
  },
  {
    "segment_id": "0031",
    "text": "周围那不断翻涌的，只有微不可察的一丝丝能够被罗帆吸收的混沌元气忽然变成了闻到腥的鲨鱼一般，疯狂的向着罗帆的身体涌过来。"
  },
  {
    "segment_id": "0032",
    "text": "不断的从罗帆身体的各个穴窍冲入罗帆的体内。"
  },
  {
    "segment_id": "0033",
    "text": "这些混沌元气涌入身体之后，在他的身体内部分成数百道，按照数百道玄妙莫测的线路快速的快速的循环运转！这些混沌元气在各自经过一道循环之后，性质产生了种种十分玄妙的变化，被他双眉的中心，那泥丸宫所在的位置吞噬一空。"
  },
  {
    "segment_id": "0034",
    "text": "这个过程随着罗帆那种与天地合一的状态而不断持续着。"
  },
  {
    "segment_id": "0035",
    "text": "罗帆的身体对混沌元气的吸收速度变得越来越快，越来越猛。"
  },
  {
    "segment_id": "0036",
    "text": "……"
  },
  {
    "segment_id": "0037",
    "text": "转眼便是千年时间。"
  },
  {
    "segment_id": "0038",
    "text": "这地穴周围所弥漫的混沌元气已经完全被吸入他的身体内部再经过循环运转发生玄妙的变化被纳入泥丸宫之中。这地穴周围变得一片清明，那原本只在三里之外出现的植被已经布满了地穴周围。"
  },
  {
    "segment_id": "0039",
    "text": "地穴并没有多大改变，依然在不断散发着混沌元气，只是这些混沌元气却已经在没有任何机会向着四面八方散发，而是涓滴不存的涌入罗帆的体内。"
  },
  {
    "segment_id": "0040",
    "text": "经过千年时间，罗帆的身体已经比起千年前大了一倍以上。"
  },
  {
    "segment_id": "0041",
    "text": "千年前的罗帆身体只有三米长，两米高，此时却已经有六米长，四米高。"
  },
  {
    "segment_id": "0042",
    "text": "而他的体内，那混沌元气的循环运转路线已经从原本的数百道渐渐演变成一道，这道循环路线比起之前那数百道循环路线玄妙了千倍以上，包含了那数百种循环的所有优点，所淬炼出来的混沌元气已经完全变成了另一种完全不同，但又无比玄奥的能量，疯狂的涌入泥丸宫之中。"
  },
  {
    "segment_id": "0043",
    "text": "此时的罗帆，双眼之中所见的，依然是那高大至无法想象的不周山，他依然处于那种和大地，和天空融合一体的状态，依然恍如化身那不周山。"
  },
  {
    "segment_id": "0044",
    "text": "千年时光在他感觉之中，却只是一瞬罢了。"
  },
  {
    "segment_id": "0045",
    "text": "这地穴并不大，所蕴含的混沌元气也并不多。罗帆在观察不周山领悟功法的时候吸收的混沌元气比起其自身散发的快了至少千倍。"
  },
  {
    "segment_id": "0046",
    "text": "千年时光的吸收，这地穴早已不堪承受。"
  },
  {
    "segment_id": "0047",
    "text": "终于，在这天，地穴周围的地面发生剧烈的震荡，一大团已经因为浓郁而变成黑色的混沌元气猛然从地穴之中冲出，直轰向罗帆！"
  },
  {
    "segment_id": "0048",
    "text": "“轰！”一声好似天雷轰鸣的巨响响起，那一团混沌元气毫无任何阻碍的轰到了罗帆的腹部！"
  },
  {
    "segment_id": "0049",
    "text": "处于那和天空和大地融合成一体感觉中的罗帆忽然感到全身一阵无法形容的剧痛传入脑海，心神瞬间脱离了那种和天地合一的状态！"
  }
]
```

## Output Format
CRITICAL INSTRUCTION: You MUST translate the source text EXACTLY paragraph by paragraph, preserving the original order perfectly. DO NOT skip, drop, merge, or reorder any paragraphs. Each paragraph in the source MUST be translated.
Return ONLY valid JSON matching this schema:
{
  "chapter_number": 4,
  "chapter_title_vi": "Chương 4: <Vietnamese title>",
  "segments": [
    {
      "segment_id": "XXXX",
      "source": "...",
      "target": "..."
    }
  ]
}
