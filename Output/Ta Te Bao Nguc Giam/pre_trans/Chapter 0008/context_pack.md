# Translation Context Pack

## Project
- Branch: Ta Te Bao Nguc Giam
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

## Chapter 0001 - Chương 1: Tất cả tà thuật được ghi chép trong chương một, bao gồm luyện thành cơ thể người, hiến tế tà pháp, trận pháp ô nhiễm, v.v., đều là một số yếu lĩnh cơ bản.

### Summary
Chapter 1 completed via pipeline.

## Chapter 0002 - Chương 2: Sự phát hiện của Hàn Đông

### Summary
Chapter 2 completed via pipeline.

## Chapter 0001 - 0001 神秘的监狱

### Summary
Chapter 1 completed via pipeline.

## Chapter 0001 - Chương 1: Nhà giam thần bí

### Summary
Chapter 1 completed via pipeline.

## Chapter 0002 - Chương 2: Sự phát hiện của Hàn Đông

### Summary
Chapter 2 completed via pipeline.

## Chapter 0003 - Chương 3: Bắt đầu lại từ đầu

### Summary
Chapter 3 completed via pipeline.

## Chapter 0004 - Chương 4: Thanh niên treo cổ

### Summary
Chapter 4 completed via pipeline.

## Chapter 0005 - Chương 5: Nhà giam di động

### Summary
Chapter 5 completed via pipeline.

## Chapter 0006 - Chương 6: Quảng trường Tế Điển

### Summary
Chapter 6 completed via pipeline.

## Chapter 0007 - Chương 7: Không gian Vận Mệnh

### Summary
Chapter 7 completed via pipeline.


## Source Chapter 8 - 0008 六人小队
```json
[
  {
    "segment_id": "0001",
    "text": "# 第8章 六人小队"
  },
  {
    "segment_id": "0002",
    "text": "卷发小哥的激励性话语起了一定的作用。"
  },
  {
    "segment_id": "0003",
    "text": "首先有所反应的就是手持十字架的黑发女性。"
  },
  {
    "segment_id": "0004",
    "text": "“没错！伟大的库兰团长可是连五星难度的诅咒类事件都顺利度过，而且还带着小队里的大部分人活了下来。"
  },
  {
    "segment_id": "0005",
    "text": "我们的决心一定会被主所发现，主会引领我们走出这片危险的黑森林。”"
  },
  {
    "segment_id": "0006",
    "text": "就在这时，一阵声音回荡于每个人的脑海中。"
  },
  {
    "segment_id": "0007",
    "text": "『事件尚未开启，你们的身份为大学生拍摄团队，请在一小时内与事件主要人物‘王婆’正面接触，一同前往事件发生地【废弃山庄】。"
  },
  {
    "segment_id": "0008",
    "text": "若在规定时间内未与‘王婆’接触，干扰或是拒绝乘坐前往事件发生地的车辆，个体将遭到强制抹除。』"
  },
  {
    "segment_id": "0009",
    "text": "一小时的准备时间。"
  },
  {
    "segment_id": "0010",
    "text": "卷发小哥试着将大家组织起来，以增加存活概率。"
  },
  {
    "segment_id": "0011",
    "text": "“时间充裕，大家互相介绍一下吧！我叫爱德华.默里……我父亲是一位小有名气的作家，家庭条件还算不错。"
  },
  {
    "segment_id": "0012",
    "text": "儿时因出了点事故，右手变成了这样。”"
  },
  {
    "segment_id": "0013",
    "text": "小哥主动脱去白手套并挽起衣袖。"
  },
  {
    "segment_id": "0014",
    "text": "一条融合着机械美学的金属义肢显露而出。"
  },
  {
    "segment_id": "0015",
    "text": "手肘、手腕以及手指节点处，均由大量精密的齿轮与微型螺栓构成……不仅能实现关节间的正常弯曲活动，甚至能作出常人无法达到的弯曲动作。"
  },
  {
    "segment_id": "0016",
    "text": "多流线型的金属手臂中，隐藏着小型蒸汽液压装置，赋予义肢强大的力量。"
  },
  {
    "segment_id": "0017",
    "text": "“蒸汽义肢！！”"
  },
  {
    "segment_id": "0018",
    "text": "颇有姿色的金发碧眼女生仿佛抓住救民稻草，尽可能显露出自身美貌的一面，将身子靠向这位小哥。"
  },
  {
    "segment_id": "0019",
    "text": "蒸汽义肢这可不是平民能够接触到的东西，哪怕是圣城的中产阶级家庭想要购买这样的义肢，也得花费掉大量资产。"
  },
  {
    "segment_id": "0020",
    "text": "金发小姐姐的目光全然投向卷发小哥默里，紧跟着进行自我介绍：“我叫霍尔.莫妮卡……母亲在‘餐厅’里工作。”"
  },
  {
    "segment_id": "0021",
    "text": "卷发小哥默里微微一笑，并未接受此女的投怀送抱，也没有排斥，保持着约两拳的距离。"
  },
  {
    "segment_id": "0022",
    "text": "既然有人起了头，自我介绍也就顺利进行了下去。"
  },
  {
    "segment_id": "0023",
    "text": "队伍中体型最为强壮、年龄最大的光头白人男子一脸不屑地说着："
  },
  {
    "segment_id": "0024",
    "text": "“德里昂，零件工厂的普通工人。比较擅长……揍人。"
  },
  {
    "segment_id": "0025",
    "text": "该死！如果是异变类或是怪物类的事件，我还能正面对抗！这种摸不到的恶灵，真是恶心……我的运气怎么会这么差。”"
  },
  {
    "segment_id": "0026",
    "text": "德里昂一想到事件问题，直接一拳砸在路旁的围墙上……当然，限于普通人体质的他，只是砸出声响，墙面纹丝不动。"
  },
  {
    "segment_id": "0027",
    "text": "手中紧抓着十字架的黑发女生缓慢起身。"
  },
  {
    "segment_id": "0028",
    "text": "“我叫格林.阿卡曼，我在教堂里做义工……神父大人许诺我，待我下半年成年时，就能留在教堂正式工作。"
  },
  {
    "segment_id": "0029",
    "text": "神父大人对我很好……义工期间，只要夜晚在教堂里加班一段时间，就能得到十便士的奖励。”"
  },
  {
    "segment_id": "0030",
    "text": "这句话里有着明显的问题。"
  },
  {
    "segment_id": "0031",
    "text": "教堂是不会在也夜晚开门的，所谓的夜晚加班，就有些蹊跷了。"
  },
  {
    "segment_id": "0032",
    "text": "紧跟着，一位假装镇定，实则内心十分慌张的青年站了出来。"
  },
  {
    "segment_id": "0033",
    "text": "看样貌也就二十岁上下，亚麻衬衣外还搭配着一件粗布小马甲，戴着一顶有着毛边的报童帽。"
  },
  {
    "segment_id": "0034",
    "text": "“彼得斯.赫伯特……大家叫我伯特就行。"
  },
  {
    "segment_id": "0035",
    "text": "我跟着父亲做卖报工作，没有特别擅长的，也就跑得比较快，能看出什么人会愿意买报纸。      我会努力的，希望大家都能活下来。”"
  },
  {
    "segment_id": "0036",
    "text": "这位报童，算得上是队伍中最为乐观的一人。"
  },
  {
    "segment_id": "0037",
    "text": "最后，自然而然就轮到韩东了……一行人中，韩东这身体素质恐怕与那位瘦弱的信徒女生并列排在倒数第一。"
  },
  {
    "segment_id": "0038",
    "text": "亚麻衬衣下，如柴瘦般的躯干给人一种风吹即倒的感觉。"
  },
  {
    "segment_id": "0039",
    "text": "“瓦伦.尼古拉斯……先天身体不太好，留在家里无所事事。不过，平时无聊的时候，对语言学有一定的了解，应该能担当翻译。”"
  },
  {
    "segment_id": "0040",
    "text": "韩东故意给出一个‘特长’。"
  },
  {
    "segment_id": "0041",
    "text": "如果让自己显得太没用，必将遭到队友的嫌弃。"
  },
  {
    "segment_id": "0042",
    "text": "在很多情报暂不清楚，且肉体偏弱的情况下，韩东必须让自己显得有点‘作用’而与队友平等共处，至少不能成为最差的一员。"
  },
  {
    "segment_id": "0043",
    "text": "“你会九州的汉语？”有着蒸汽义肢的青年-爱德华.默里一脸诧异。"
  },
  {
    "segment_id": "0044",
    "text": "“嗯……基本的沟通没问题。”"
  },
  {
    "segment_id": "0045",
    "text": "“很好！待会儿就由你担当翻译，与重要人物‘王婆’接触，让我们全员顺利前往事件发生地。”"
  },
  {
    "segment_id": "0046",
    "text": "“嗯。”韩东接下这份差事，实现自己的队内价值。"
  },
  {
    "segment_id": "0047",
    "text": "爱德华转向全员而说道："
  },
  {
    "segment_id": "0048",
    "text": "“大家不介意我来担任队长吧？"
  },
  {
    "segment_id": "0049",
    "text": "希望在接下来的事件行动中，大家能服从我的指示与要求，我会尽全力增加大家的存活率。"
  },
  {
    "segment_id": "0050",
    "text": "大家有什么意见都可以向我或者全小队提出，只要合理，一定会采纳的。”"
  },
  {
    "segment_id": "0051",
    "text": "“我赞成！”金发女霍尔.莫妮卡第一个赞成。"
  },
  {
    "segment_id": "0052",
    "text": "紧跟着，韩东也举手。"
  },
  {
    "segment_id": "0053",
    "text": "这样的团体行动，有一个领导者是必须的。"
  },
  {
    "segment_id": "0054",
    "text": "从目前的情况看来，爱德华有这个资格。"
  },
  {
    "segment_id": "0055",
    "text": "就在大家相继举手时，光头男德里昂则是一脸不屑，“我会跟着你们前往事件发生地，我想要做什么就做什么，不会听任何人的意见。”"
  },
  {
    "segment_id": "0056",
    "text": "爱德华一脸微笑地回应着，“表示理解，德里昂朋友，只要你不作出有害于团队的行为，你想做什么都行。”"
  },
  {
    "segment_id": "0057",
    "text": "随后，爱德华转向韩东，“尼古拉斯朋友，我们出发吧？”"
  },
  {
    "segment_id": "0058",
    "text": "“好。”"
  },
  {
    "segment_id": "0059",
    "text": "就这样，全员六人介绍完毕并基本统一战线，正式踏上恐怖之旅。"
  },
  {
    "segment_id": "0060",
    "text": "为方便记忆。"
  },
  {
    "segment_id": "0061",
    "text": "韩东将这五位队友分别贴上一个标签。"
  },
  {
    "segment_id": "0062",
    "text": "【义肢】、【信徒】、【金发妹】、【光头哥】、【报童】"
  },
  {
    "segment_id": "0063",
    "text": "另外，一道来自于「无面者的头颅」的信息打消掉韩东打算投机取巧的做法。"
  },
  {
    "segment_id": "0064",
    "text": "『检测到主体目前置身于特别的空间区域，开启监狱将消耗大量的空间能源……便携式监狱仅会在收容外物时短暂开启，主体无法自主进入便携式监狱。』"
  },
  {
    "segment_id": "0065",
    "text": "“果然没这么简单……”"
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
