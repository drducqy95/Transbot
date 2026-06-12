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

## Chapter 0003 - Chương 3: Xin cứ ra một góc mà chơi đi

### Summary
Chapter 3 completed via pipeline.


## Source Chapter 4 - 0004 古月方源！
```json
[
  {
    "segment_id": "0001",
    "text": "# 第四节：古月方源！"
  },
  {
    "segment_id": "0002",
    "text": "朝阳升起来，霞光烂漫。"
  },
  {
    "segment_id": "0003",
    "text": "山雾不是很浓，被利剑般的阳光轻易洞穿。"
  },
  {
    "segment_id": "0004",
    "text": "一百多位十五岁的少年，此刻汇集在家主阁前。"
  },
  {
    "segment_id": "0005",
    "text": "家主阁就处在山寨的正中央，高达五层，飞檐翘角，重兵把守。阁前就是广场，阁内供奉着古月先人的牌位。每代族长也都生活起居在这里面，每逢重大典礼，或者有突发大事，也会在这里召集家老们商讨议论。这是整个山寨的权利中枢。"
  },
  {
    "segment_id": "0006",
    "text": "“很好，都准时来了。今天是开窍大典，是你们人生的重大转折点。闲话不多说了，随我来吧。”负责此行的，是学堂家老。他须发皆白，精神矍铄地领着少年们进入家主阁。"
  },
  {
    "segment_id": "0007",
    "text": "不过却没有上楼，而是通过一层大堂的入口，往下走。"
  },
  {
    "segment_id": "0008",
    "text": "顺着打造好的石梯，就进入地下溶洞。"
  },
  {
    "segment_id": "0009",
    "text": "少年们纷纷发出惊叹之声。地下溶洞美轮美奂，钟乳石散发着赤橙黄绿青蓝紫七色光华，这光彩映照在少年们的脸上，霓虹般绚烂。"
  },
  {
    "segment_id": "0010",
    "text": "方源混杂在人群中央，静静地审视这一切，心中暗暗思量：“数百年前，古月一族从中土迁徙到南疆，在这青茅山驻扎下来。就是看中了这里地下溶洞的一口灵泉。这灵泉产出大量元石，可以说是古月山寨的根基。”"
  },
  {
    "segment_id": "0011",
    "text": "行了数百步，却是越来越暗，并且依稀听到了水声。"
  },
  {
    "segment_id": "0012",
    "text": "转过转角，一条宽三丈有余的地下河，就展现在众人眼前。"
  },
  {
    "segment_id": "0013",
    "text": "此地钟乳石的彩光，已经彻底消失了。"
  },
  {
    "segment_id": "0014",
    "text": "但是黑暗中，河水却散发着淡淡的幽蓝之光，好像是夜空中的星河。"
  },
  {
    "segment_id": "0015",
    "text": "河水从溶洞的黑暗深处流淌过来，清澈无比，甚至可以看到里面的游鱼，水草，以及河底的沙石。"
  },
  {
    "segment_id": "0016",
    "text": "在河的对岸，是一片花海。"
  },
  {
    "segment_id": "0017",
    "text": "这是古月一族有意栽培的月兰花，花瓣如月牙，呈现出清丽淡雅的蓝粉色。花茎如玉，花心闪耀着，好像是珍珠在光下的折射出来的温润光华。"
  },
  {
    "segment_id": "0018",
    "text": "乍一眼看上去，在黑暗的背景中，河畔花海就好像是一大片的蓝绿地毯，点缀着数不清的珍珠。"
  },
  {
    "segment_id": "0019",
    "text": "“月兰花，是很多蛊虫的食材。这片花海，可以说是家族最大的培养基地了。”方源对此心知肚明。"
  },
  {
    "segment_id": "0020",
    "text": "“好美。”"
  },
  {
    "segment_id": "0021",
    "text": "“真是漂亮呀。”"
  },
  {
    "segment_id": "0022",
    "text": "少年们算是开了眼界，一个个双眼放光，既兴奋又紧张。"
  },
  {
    "segment_id": "0023",
    "text": "“好了，下面听我报名，叫到的人穿过这河，到对岸去。能走多远，就走多远，当然越远越好。都听清楚了吗？”家老此刻说着。"
  },
  {
    "segment_id": "0024",
    "text": "“清楚了。”少年们纷纷应是。其实来之前，都听家人或者前辈们讲过，知道走的越远，代表资质越好，日后的成就也就越大。"
  },
  {
    "segment_id": "0025",
    "text": "“古月陈博。”家老拿着名单点出第一人。"
  },
  {
    "segment_id": "0026",
    "text": "河水虽宽却并不深，只及少年膝盖。陈博一脸的严肃，踏上河畔花海。"
  },
  {
    "segment_id": "0027",
    "text": "顿时他就感觉到一股隐形的压力，好像面前有一面看不见的墙，在阻挡他前进。"
  },
  {
    "segment_id": "0028",
    "text": "正举步维艰之时，脚畔的花海中忽然浮起一蓬光点，光点很稀薄，呈现素白之色。"
  },
  {
    "segment_id": "0029",
    "text": "光辉向陈博汇集过去，并投入到他的体内。"
  },
  {
    "segment_id": "0030",
    "text": "陈博瞬间感觉到压力剧减。那堵无形的墙壁，忽然变得柔软起来。"
  },
  {
    "segment_id": "0031",
    "text": "他咬牙用力向前走，硬生生的挤进去。走了三步之后，前方的压力又大增，一如之前如墙壁一样，不能再进分毫。"
  },
  {
    "segment_id": "0032",
    "text": "见到此景，家老一叹，当场一边记录，一边道：“古月陈博，三步，没有蛊师资质。下一个，古月藻榭。”"
  },
  {
    "segment_id": "0033",
    "text": "陈博脸色顿时苍白，咬着牙，穿过河水，回到原处。没有资质，今后就只能作为一个凡人活着，在家族中也只能是最底层的地位。"
  },
  {
    "segment_id": "0034",
    "text": "他身躯摇摇欲坠，打击太大了，等于是扼杀了一生的希望。"
  },
  {
    "segment_id": "0035",
    "text": "很多人都向他投来怜悯的目光，更多的人则关注着第二位登上彼岸的少年。"
  },
  {
    "segment_id": "0036",
    "text": "可惜这个少年，也只能前进四步，同样没有资质。"
  },
  {
    "segment_id": "0037",
    "text": "并非所有人都有修行的资质，一般而言，十个人中有五人能修行，就已经不错了。在古月家族里，这个比例还要高一些，达到六人的程度。"
  },
  {
    "segment_id": "0038",
    "text": "这是因为古月先祖，也就是一代族长，是一位大名鼎鼎的传奇强者，因为修行的缘故导致他的血脉中隐藏着承载力量的基因。古月族人因为有着他的血脉，因此资质普遍较高。"
  },
  {
    "segment_id": "0039",
    "text": "连续两个没有资质的情况，让暗中关注的其他家老们都脸色难看起来，就是老成持重的古月族长，也微微蹙眉。"
  },
  {
    "segment_id": "0040",
    "text": "就在这时，学堂家老喊出第三个名字：“古月漠北。”"
  },
  {
    "segment_id": "0041",
    "text": "“在！”一个身穿麻布衣衫的马脸少年，轻喝一声，越众而出。"
  },
  {
    "segment_id": "0042",
    "text": "他身材高大，比同龄人要粗壮得多，透着一丝彪悍气息。"
  },
  {
    "segment_id": "0043",
    "text": "三两步过了河，踏上对岸。"
  },
  {
    "segment_id": "0044",
    "text": "十步，二十步，三十步，陆续有微光投入到他的体内。"
  },
  {
    "segment_id": "0045",
    "text": "一直走到三十六步，终于走不动了。"
  },
  {
    "segment_id": "0046",
    "text": "少年们隔岸看得目瞪口呆，学堂家老欢喜得大叫起来：“好，古月漠北，乙等资质，来这里，让我看看你的元海。”"
  },
  {
    "segment_id": "0047",
    "text": "古月漠北便又回到学堂家老的身边，后者伸出手，搭在少年的肩膀，闭目凝神探查了一番，便收回手，点点头，在纸上记录起来：“古月漠北，元海六成六，可大力栽培。”"
  },
  {
    "segment_id": "0048",
    "text": "这资质从上到下，分甲乙丙丁四等。"
  },
  {
    "segment_id": "0049",
    "text": "一位丁等资质的少年，培养个三年，就能晋升成一转的资深蛊师，成为家族的基石。"
  },
  {
    "segment_id": "0050",
    "text": "一位丙等资质的少年，培养两年，大多都能成为二转的蛊师，成为家族的中坚存在。"
  },
  {
    "segment_id": "0051",
    "text": "一位乙等资质，就要呵护了。往往要作为未来的家老培养，六七年的功夫，能成为三转蛊师。"
  },
  {
    "segment_id": "0052",
    "text": "至于甲等资质，哪怕出现一位，都是整个家族的幸运。要细心关照，倾斜资源，十年左右就能成为四转蛊师，到那时便能竞争族长之位！"
  },
  {
    "segment_id": "0053",
    "text": "也就是说，这古月漠北只要成长起来，就是今后古月一族的家老。难怪学堂长老喜得哈哈一笑，而暗中关注的众家老们都统统舒了一口气，而后又纷纷向其中一位家老投去羡慕的目光。"
  },
  {
    "segment_id": "0054",
    "text": "这家老也是一副马脸，正是古月漠北的爷爷古月漠尘。他脸上早已经荡漾起笑意，又挑衅地看了一眼自己的老对头：“怎么样，我的孙儿不差吧，古月赤练。”"
  },
  {
    "segment_id": "0055",
    "text": "家老古月赤练一头红发，此时冷哼一声，并未答话，脸色阴沉得很是难看。"
  },
  {
    "segment_id": "0056",
    "text": "半个时辰之后，已有一半少年踏足过花海，涌现了不少丙等、丁等的资质，当然毫无资质的占了几乎一半。"
  },
  {
    "segment_id": "0057",
    "text": "“唉，血脉越来越稀薄，加上这些年来，家族也没有出现几位四转强者，来增强血脉。四代族长是唯一的五转强者，结果却和花酒行者同归于尽，没有留下血脉后裔。古月一族后辈的资质是越来越弱了。”族长深深的叹息着。"
  },
  {
    "segment_id": "0058",
    "text": "就在这时，学堂家老喊道：“古月赤城。”"
  },
  {
    "segment_id": "0059",
    "text": "听到这个名字，家老们纷纷看向古月赤练，这是古月赤练的孙子。"
  },
  {
    "segment_id": "0060",
    "text": "古月赤城身材矮小，满脸麻子，捏着拳头，满脸出汗，显得特别的紧张。"
  },
  {
    "segment_id": "0061",
    "text": "他踏上对岸，光点纷纷投入他的体内，一连走到三十六步，这才停步。"
  },
  {
    "segment_id": "0062",
    "text": "“又一个乙等！”学堂家老叫喊着。"
  },
  {
    "segment_id": "0063",
    "text": "少年们骚动起来，纷纷向古月赤城投来羡慕的目光。"
  },
  {
    "segment_id": "0064",
    "text": "“哈哈哈，三十六步，三十六步！”古月赤练大叫着，示威地瞪着古月漠尘。"
  },
  {
    "segment_id": "0065",
    "text": "这次轮到古月漠尘脸色铁青了。"
  },
  {
    "segment_id": "0066",
    "text": "“古月赤城么……”人群中，方源若有所思的摩挲着下巴。"
  },
  {
    "segment_id": "0067",
    "text": "记忆中，他因为在开窍大典中作弊，而受到了族中的严厉惩罚。"
  },
  {
    "segment_id": "0068",
    "text": "事实上，他的资质只有丙等，但是他的爷爷古月赤练为他作假，因此有了乙等资质的假象。"
  },
  {
    "segment_id": "0069",
    "text": "其实要作弊，方源心中有数十种方案，有些方案比古月赤城的更加完美。若是表现出乙等，或者甲等的资质，必然受到家族的大力栽培。"
  },
  {
    "segment_id": "0070",
    "text": "但是一来，方源重生的时间太短，以他的境况难以准备作弊手段。"
  },
  {
    "segment_id": "0071",
    "text": "二来，就算是作弊成功，日后修行时的速度是掩盖不住的，照样会露相。"
  },
  {
    "segment_id": "0072",
    "text": "而这个古月赤城却不一样，他的爷爷就是古月赤练，是家族中权势最重的两个家老之一，能够为他遮掩。"
  },
  {
    "segment_id": "0073",
    "text": "“古月赤练一直和古月漠尘敌对，这两个家老是家族中最大的两派势力。为了打压对手，他需要自己的孙子资质出众。也正是因为他在背后掩护，古月赤城才能够隐瞒一时。记忆中要不是那场意外，也不会暴露。”"
  },
  {
    "segment_id": "0074",
    "text": "方源眼中闪烁着精芒，思量着该怎么利用这点来谋夺最大的利益呢？"
  },
  {
    "segment_id": "0075",
    "text": "当场揭露，虽然会得到家族的一点奖赏，但是却会得罪位高权重的古月赤练，绝不可取。"
  },
  {
    "segment_id": "0076",
    "text": "短时间之内，也不能敲诈勒索。因为实力太低，反而会自取其祸。"
  },
  {
    "segment_id": "0077",
    "text": "正思量着，忽然听到学堂家老叫出自己的名字：“古月方源！”;"
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
