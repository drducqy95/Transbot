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


## Source Chapter 2 - 0002 天地初开有貔貅()
```json
[
  {
    "segment_id": "0001",
    "text": "# 第一章 天地初开有貔貅()"
  },
  {
    "segment_id": "0002",
    "text": "“我这是在哪里……”罗帆从混混沌沌的迷糊状态之中渐渐清醒过来，睁开好似山一样沉重的眼皮，脑海之中出现这么一个念头。"
  },
  {
    "segment_id": "0003",
    "text": "刺目的光芒刺入他的双眼之中，让他不由得将刚刚睁开的双眼再度闭上，等了许久，刺痛减弱方才缓缓睁开。"
  },
  {
    "segment_id": "0004",
    "text": "这么一睁开，他便知道自己已经不在地球上了。"
  },
  {
    "segment_id": "0005",
    "text": "因为，地球上绝对不可能有那么高、那么大的山！"
  },
  {
    "segment_id": "0006",
    "text": "在他的前方不知道多远的地方，模模糊糊的，有一座好似天柱一般，拔地而起，直插云端的巨山！即使距离过远，此时远望那座山已经觉得其模模糊糊了，但罗帆却依然看不到这座山的山顶，即使将脑袋仰成和地面平行，也只看到那不断向上延伸的山体！"
  },
  {
    "segment_id": "0007",
    "text": "“我是做梦了？……还是穿越了？……”又有一个念头在他的脑海中泛出。"
  },
  {
    "segment_id": "0008",
    "text": "随着这个念头出现，他猛然感到自己的脑袋受到了无数铁锤在疯狂的捶打，轰轰轰轰轰轰的声响伴随着无穷的剧痛。无数千奇百怪的图像、声音等种种信息从他的脑海深处不断翻出来，好似吹气球一般，将他的脑袋涨得几乎要炸开。"
  },
  {
    "segment_id": "0009",
    "text": "“吼！”一声无比巨大的兽吼猛然从他的口中爆发出来，这一声兽吼好似晴天霹雳，好似天地反复……"
  },
  {
    "segment_id": "0010",
    "text": "接着，很自然的，罗帆十分幸福的晕了过去……"
  },
  {
    "segment_id": "0011",
    "text": "不知过了多久，罗帆再度从混混沌沌迷迷糊糊的状态之中清醒过来。"
  },
  {
    "segment_id": "0012",
    "text": "清醒过来之后，还没有睁开双眼，他便完全明白了自己此时此刻的处境。"
  },
  {
    "segment_id": "0013",
    "text": "“原来，我已经穿越了……”"
  },
  {
    "segment_id": "0014",
    "text": "在他的脑海之中，此时多了一大片量无比巨大，但又无比单调的记忆。"
  },
  {
    "segment_id": "0015",
    "text": "“浑浑噩噩的状态出现在这个世界，浑浑噩噩的四处游荡，吃饱了睡，睡饱了吃，这个过程持续了不知多少千年，亦或是多少万年，在某一天，他来到了一个让他感觉无比舒服的地方，就地睡倒，直到完全失去意识……再接着，罗帆的意识，便出现了……”"
  },
  {
    "segment_id": "0016",
    "text": "“吃饱了睡，睡饱了吃……这种生活真是让人向往啊……”罗帆苦笑着抖抖自己的身躯。"
  },
  {
    "segment_id": "0017",
    "text": "他现在已经变成了一头龙头、马身、麟脚，状如狮子，毛色灰白的怪兽，这种怪兽有着一个举世闻名的名字“貔貅”（音：皮休）。"
  },
  {
    "segment_id": "0018",
    "text": "而这里有着这种传说中的貔貅，自然不可能还是地球。这里，是洪荒！"
  },
  {
    "segment_id": "0019",
    "text": "没错，就是那个盘古所开辟出来的那个洪荒天地，而现在的时间，只是盘古开天陨落之后不到十万年时间。"
  },
  {
    "segment_id": "0020",
    "text": "他最开始看到的那一座言语无法形容其高大的山，正是洪荒的西北天柱，那盘古的脊梁，不周山。《淮南子天文训》有言，“昔者，共工与颛顼（音，专需）争为帝，怒而触不周之山。天柱折，地维绝，天倾西北，故日月星辰移焉，地不满西南，故水潦尘埃归焉。”不周山被撞断了，天就往西北倾倒，那岂不是说明不周山应当就是在西北方向撑住天，也就该是西北的天柱。"
  },
  {
    "segment_id": "0021",
    "text": "罗帆那他完全陌生的龙头上牵扯出一个无奈的苦笑。"
  },
  {
    "segment_id": "0022",
    "text": "对于如何穿越的，为什么会穿越，他虽然惊讶，但却没有一般人经历这种事之时的那种喜悦、痛苦、惊慌。"
  },
  {
    "segment_id": "0023",
    "text": "因为，相比于这具身体所带来的不知几千还是几万年的记忆，他在地球上那二十多年的记忆简直就如沧海一粟一般不值一提。虽然他并没有因此而忘记地球上的那些经历，甚至记得前所未有的清楚，但那原本刻骨铭心的种种情感，在这貔貅无比单调的记忆之中，却被不断的消磨，稀释。这让他的心情已经变得极其平静……"
  },
  {
    "segment_id": "0024",
    "text": "再度向那不周山望过去，罗帆忽然感受到一种无以伦比的震撼。"
  },
  {
    "segment_id": "0025",
    "text": "一股苍茫不屈的意志从不周山上不断散发出来，虽然此地离那不周山还有不知几百几千万里之遥，但那一股苍茫不屈的意志依然没有减弱分毫，即使相隔如此之远，却也依然在不断的影响着罗帆周围的万事万物！"
  },
  {
    "segment_id": "0026",
    "text": "望着这高不可测，时刻散发着慑人气息的不周山，罗帆心中不知不觉起了一种难以名状的感觉。"
  },
  {
    "segment_id": "0027",
    "text": "这种感觉就好似自己已经变为了眼前这不知多少千万里之外的那座山，四脚踩着无比广阔，无比稳固的大地，头顶着那无比悠远，无比神秘的天空！"
  },
  {
    "segment_id": "0028",
    "text": "一股顶天立地，永不屈服，永不放弃的感觉瞬间充满了他的整个内心！"
  },
  {
    "segment_id": "0029",
    "text": "噗……"
  },
  {
    "segment_id": "0030",
    "text": "一声轻响忽然在罗帆的脑袋之中爆出。"
  },
  {
    "segment_id": "0031",
    "text": "这轻响虽然只是轻轻的，但却好似开天辟地一般，瞬间将罗帆从那种难以名状的感觉之中惊醒过来。"
  },
  {
    "segment_id": "0032",
    "text": "“这是怎么回事？”罗帆心中惊疑不定。"
  },
  {
    "segment_id": "0033",
    "text": "他感到自己的体内，多了一种以前所不存在，或者他所感知不到的东西！"
  },
  {
    "segment_id": "0034",
    "text": "细细感知那东西一番，忽然一阵天旋地转，他的意念已经进入了一个莫名的所在。"
  },
  {
    "segment_id": "0035",
    "text": "周围灰蒙蒙的，宛如混沌一般。而他自身，却变成了一个十分怪异的存在。低头一看，一个拳头大小，活灵活现的小貔貅就是他此时的身躯。这小貔貅全身混混沌沌，似虚似实的半透明形态，十分灵活，十分可爱。"
  },
  {
    "segment_id": "0036",
    "text": "“神魂……元神？”罗帆心中惊讶万分。"
  },
  {
    "segment_id": "0037",
    "text": "无论在地球上的那二十多年记忆，还是这貔貅多年的记忆都告诉他，他根本就没有任何修行功法！罗帆在地球上自然不用说，这貔貅上万年的的经历一直是浑浑噩噩的，虽然因为是天生天养，记忆之中有一些关于这个世界的信息，但关于修行之类的知识却是完全没有，他所与众不同的，也就只是这具身体自发本能的吸收先天元气罢了。"
  },
  {
    "segment_id": "0038",
    "text": "而以他浑浑噩噩只知吃了睡，睡了吃的心智，内视自身自然也是不可能。"
  },
  {
    "segment_id": "0039",
    "text": "所以这灰蒙蒙好似混沌一般的空间，却是罗帆，也是貔貅第一次到来的地方，让罗帆根本无法在貔貅的记忆之中寻找到关于这个地方的消息。"
  },
  {
    "segment_id": "0040",
    "text": "意念在这不知神魂还是元神里面的感觉十分奇妙，好似脱去了一切束缚一般，变得无比轻松，无比自在。"
  },
  {
    "segment_id": "0041",
    "text": "抖抖身体，周围灰蒙蒙的空间一阵抖动，渐渐退散。"
  },
  {
    "segment_id": "0042",
    "text": "没多久，便空出了一个一米直径的球形虚无区域出来。"
  },
  {
    "segment_id": "0043",
    "text": "活动一下身躯来到这球形区域的边缘，往外走出去，似乎碰到了一堵无法抵挡的墙壁一般。"
  },
  {
    "segment_id": "0044",
    "text": "猛撞上去，一股玄妙的信息忽然涌入罗帆的意念之中。"
  },
  {
    "segment_id": "0045",
    "text": "伴随这股玄妙的信息，罗帆瞬间明白自己此时所在的位置，也明白自己此时的状态是什么状态。"
  },
  {
    "segment_id": "0046",
    "text": "“原来，这里是我的识海，而我现在是神魂状态。”他心中暗自想着。心中明白了这么一个小小的球形区域就是他此时识海所能够开辟的范围，再往外便不是他所能够涉足的区域。"
  },
  {
    "segment_id": "0047",
    "text": "暗叹了口气，罗帆心神微微一动，这拳头大小，混混沌沌的小貔貅往一个莫名的方向一冲，便好似突破了一种无比强大的无形桎梏一般，突入了一个光彩夺目，精彩万分，又充满了一股无尽苍茫与不屈气息的空间。"
  },
  {
    "segment_id": "0048",
    "text": "低头一看，他的身躯正趴在下方，神色安详，好似睡着。"
  },
  {
    "segment_id": "0049",
    "text": "在身体周围雾气弥漫，那下方的山石只透出些微轮廓。前方不知多远之处有着一个拔地而起，高耸入云，看不见顶的高山在散发着无比强大的气息……"
  },
  {
    "segment_id": "0050",
    "text": "赫然已经到了身体之外……"
  },
  {
    "segment_id": "0051",
    "text": "微风吹过，身体飘飘欲仙，没有了身体的束缚，他和天地的距离前所未有的靠近。整个世界变得前所未有的绚丽，前所未有的清晰。周围那种苍茫、不屈的气息似乎也变得更加明显，更加强烈。"
  },
  {
    "segment_id": "0052",
    "text": "笼罩在这一股气息之中，罗帆忽然觉得就算天塌下来，也无法让他屈服，无法让他放弃。"
  },
  {
    "segment_id": "0053",
    "text": "此时乃是盘古开天不到十万年，整个洪荒天地的演化并没有稳定下来，整个洪荒世界除了无尽的先天元气之外，在许许多多的特殊位置还有着无量的混沌元气。"
  },
  {
    "segment_id": "0054",
    "text": "就比如，貔貅在不知多少年前所找到的这么一个地穴，便是一个在时时刻刻散发着浓郁混沌元气的地穴。"
  },
  {
    "segment_id": "0055",
    "text": "也正是因为其在散发混沌元气，方才会让从天地初开之时随着出生的貔貅感到舒服，并在这里停留下来。"
  },
  {
    "segment_id": "0056",
    "text": "那一股从不周山所发出来的苍茫、不屈气息虽然让罗帆感觉很好，但这一股气息实在是太强了。强到他这具刚刚成型的神魂也无法承受太久的地步。"
  },
  {
    "segment_id": "0057",
    "text": "神魂在外面停留了不到十分钟，罗帆便感到一股股刺痛从神魂的各处传来。那原本半透明，混混沌沌的身躯变得更加的透明了。"
  },
  {
    "segment_id": "0058",
    "text": "知道这神魂依然脆弱，不可在身体之外停留太久，罗帆心神一动，控制那神魂往自己身躯的天灵盖一钻，便钻了进去。"
  },
  {
    "segment_id": "0059",
    "text": "一进入身躯，没有经历任何过程的，这身躯便重新回归了那一个一米直径的球形虚无区域。"
  },
  {
    "segment_id": "0060",
    "text": "那种在外面被气息侵蚀而产生的剧痛，困苦转眼消失无踪，神魂各处变得暖融融的舒适。"
  },
  {
    "segment_id": "0061",
    "text": "“果然，在神魂不够壮大之前身体是决不能抛弃的啊。”罗帆心中感叹一声，意念一动，已经脱离了神魂，重新回归了自己的身体。"
  },
  {
    "segment_id": "0062",
    "text": "迷迷糊糊的睁开双眼，周围灰蒙蒙的混沌元气映入眼帘，刚才所发生的那一切似乎都是他在做梦一样，感觉十分的奇妙。"
  }
]
```

## Output Format
CRITICAL INSTRUCTION: You MUST translate the source text EXACTLY paragraph by paragraph, preserving the original order perfectly. DO NOT skip, drop, merge, or reorder any paragraphs. Each paragraph in the source MUST be translated.
Return ONLY valid JSON matching this schema:
{
  "chapter_number": 2,
  "chapter_title_vi": "Chương 2: <Vietnamese title>",
  "segments": [
    {
      "segment_id": "XXXX",
      "source": "...",
      "target": "..."
    }
  ]
}
