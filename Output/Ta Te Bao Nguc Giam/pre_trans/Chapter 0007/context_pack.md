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


## Source Chapter 7 - 0007 命运空间
```json
[
  {
    "segment_id": "0001",
    "text": "# 第7章 命运空间"
  },
  {
    "segment_id": "0002",
    "text": "在黑蔷薇骑士团的监督下。"
  },
  {
    "segment_id": "0003",
    "text": "约有1/3的民众湿润着眼眶，与依恋不舍的亲人分离……眼里透出的悲伤似乎有些过头，有一种送亲人去火葬场的古怪感觉。"
  },
  {
    "segment_id": "0004",
    "text": "在这种古怪气氛的烘托下，广场一大部分人的情绪有些失控。"
  },
  {
    "segment_id": "0005",
    "text": "就在这时，覆盖整座广场的声音再次传来："
  },
  {
    "segment_id": "0006",
    "text": "“恐惧，只会让你们变得更加弱小而已。"
  },
  {
    "segment_id": "0007",
    "text": "而弱小者是没有资格活在当前的世界下。"
  },
  {
    "segment_id": "0008",
    "text": "要知道，你们以及你们的家人之所以能活着，全部依靠十三骑士团的精英成员，拼死在‘命运空间’中获取独一无二的黄铜材料，打造出这一座能庇护百万人的【圣城-诺因忒纳】。"
  },
  {
    "segment_id": "0009",
    "text": "现在，则是证明你们价值的时刻！"
  },
  {
    "segment_id": "0010",
    "text": "前往命运世界，抵抗住从未经受过的恐惧，在生死边缘挣扎并存活下来，成为‘返回者’。"
  },
  {
    "segment_id": "0011",
    "text": "记住，理性与勇气是你们的唯一‘兵器’。"
  },
  {
    "segment_id": "0012",
    "text": "活下来，你们将受到嘉奖，你们的亲人也将为你们而自豪，过上更好的生活。”"
  },
  {
    "segment_id": "0013",
    "text": "骑士的发言回荡在每一个人的脑海间。"
  },
  {
    "segment_id": "0014",
    "text": "虽不是什么振奋人心的话语，但却让大部分人的畏惧感消退大半。"
  },
  {
    "segment_id": "0015",
    "text": "没错，既然已经走到这一步，为何不去拼一拼？就算不是为了人类，也要为了自己与家人努力拼搏而活下来。"
  },
  {
    "segment_id": "0016",
    "text": "就在广场里的青年们，试图结成团队互相加油打气时。"
  },
  {
    "segment_id": "0017",
    "text": "韩东却选择在人多的地方，找了块空地坐下来，思考着骑士发言中所提及的一些信息。"
  },
  {
    "segment_id": "0018",
    "text": "“命运空间？”"
  },
  {
    "segment_id": "0019",
    "text": "骑士的说词中，这一新颖的词汇让韩东很感兴趣。"
  },
  {
    "segment_id": "0020",
    "text": "“活下来而成为‘返回者’？"
  },
  {
    "segment_id": "0021",
    "text": "这些身体素质远超普通人的骑士，难不成就是经历过当前的仪式而存活下来的精英？"
  },
  {
    "segment_id": "0022",
    "text": "话说，到底是个什么地儿呢？死亡率会这么高？”"
  },
  {
    "segment_id": "0023",
    "text": "韩东并不害怕。"
  },
  {
    "segment_id": "0024",
    "text": "他已经是死过一次的人，他并不认为还有什么能比死亡更加恐怖的。"
  },
  {
    "segment_id": "0025",
    "text": "反倒觉得所谓的‘命运空间’很有意思。"
  },
  {
    "segment_id": "0026",
    "text": "静静等待着，就这么盯着手腕上的发条装置，倒计时即将结束。"
  },
  {
    "segment_id": "0027",
    "text": "10、9、8……"
  },
  {
    "segment_id": "0028",
    "text": "最后十秒。"
  },
  {
    "segment_id": "0029",
    "text": "韩东也变得紧张起来，深呼吸一口气，尽可能平复内心。"
  },
  {
    "segment_id": "0030",
    "text": "3、2、1……"
  },
  {
    "segment_id": "0031",
    "text": "噗通！"
  },
  {
    "segment_id": "0032",
    "text": "地面竟化作一滩粘稠而淤黑的液体。"
  },
  {
    "segment_id": "0033",
    "text": "数千位聚集在广场上的民众一同落入其中。"
  },
  {
    "segment_id": "0034",
    "text": "由于身体被粘稠流质所包裹，呼吸困难的同时无法做出太多的挣扎动作。"
  },
  {
    "segment_id": "0035",
    "text": "与此同时，某种提示音，通过粘稠液体传入每一人的耳中。"
  },
  {
    "segment_id": "0036",
    "text": "『进入者身份信息已确认-新人。』"
  },
  {
    "segment_id": "0037",
    "text": "『随机场景生成中……』"
  },
  {
    "segment_id": "0038",
    "text": "前面这两段声音是针对于所有人的。"
  },
  {
    "segment_id": "0039",
    "text": "就在大部分人因窒息而快要坚持不住时，针对于不同进入者的提示音，在各自的脑海中产生。      韩东收到的信息是——"
  },
  {
    "segment_id": "0040",
    "text": "『场景已生成，背景采用九州电影《中邪（导演修订版）》"
  },
  {
    "segment_id": "0041",
    "text": "类型：恶灵类事件"
  },
  {
    "segment_id": "0042",
    "text": "难度（新人）：★★★★"
  },
  {
    "segment_id": "0043",
    "text": "主线要求：在不离开废弃山庄的情况下，存活三天。"
  },
  {
    "segment_id": "0044",
    "text": "奖励：命运点【1】、低概率获得「命运卡牌（新手级）」』"
  },
  {
    "segment_id": "0045",
    "text": "随着提示声的结束，包裹着身体的粘附感也随之消失。"
  },
  {
    "segment_id": "0046",
    "text": "韩东以及另外五名来自于圣城的普通人，出现在一处乡间小道上。"
  },
  {
    "segment_id": "0047",
    "text": "泥泞小径、低矮平房、贴瞒着‘办证’的电线杆。"
  },
  {
    "segment_id": "0048",
    "text": "这个地方对于韩东来说再熟悉不过，这不就是祖国的农村吗？"
  },
  {
    "segment_id": "0049",
    "text": "一看这农院门口的尾巴翘得贼高、血统纯正的中华田园犬就能完全确认。"
  },
  {
    "segment_id": "0050",
    "text": "再通过一些自建的精美小别墅、安装在电线杆上的网线端口，以及坐在门口躺椅上刷着短视频的老大爷，这时间线也一下理清了。"
  },
  {
    "segment_id": "0051",
    "text": "应该就是韩东生前所处的年代。"
  },
  {
    "segment_id": "0052",
    "text": "而且，韩东还发现，自己的服装发生了改变，换了一身契合当代大学生身份的简易服装。"
  },
  {
    "segment_id": "0053",
    "text": "“所谓的命运空间竟然以我原来世界中的电影为背景？”"
  },
  {
    "segment_id": "0054",
    "text": "就在韩东惊诧于环境之逼真，人物之真实时……一旁的五名队友已经完全慌了神。。"
  },
  {
    "segment_id": "0055",
    "text": "并不是因为来到建筑风格完全不同的陌生环境，而是因为收到的‘系统信息’。"
  },
  {
    "segment_id": "0056",
    "text": "一位身材消瘦的黑发女性跪倒在地，紧紧抓住胸前的十字架，瑟瑟发抖。"
  },
  {
    "segment_id": "0057",
    "text": "“主啊！为什么？为什么我会遭受如此苦难！！”"
  },
  {
    "segment_id": "0058",
    "text": "一名年纪稍微偏大，约有25岁的光头白人，垂头顿足、咬牙切齿。“恶灵类……四颗星难度！完蛋了，我们都得死在这里，不可能有活着离开的机会。"
  },
  {
    "segment_id": "0059",
    "text": "该死的骑士团，我诅咒你们！”"
  },
  {
    "segment_id": "0060",
    "text": "一名颇有姿色的长发碧眼女生，不停转动着视线，在同行者的身上寻找‘生机’，“请问，这里有骑士团的候选者吗？能不能想办法带着我活下去……我愿意献出一切。”"
  },
  {
    "segment_id": "0061",
    "text": "这位女生的目光停留在比较镇定的韩东身上，但立即就判断出韩东的瘦弱身板根本就不可能是骑士团的候选者。"
  },
  {
    "segment_id": "0062",
    "text": "很快，这位女生因没有找到‘可依靠者’，立马因绝望而双眼无神，傻傻站在原地。"
  },
  {
    "segment_id": "0063",
    "text": "就在大部分人意志消沉时。"
  },
  {
    "segment_id": "0064",
    "text": "六人之中，一位比较特殊的小哥站了出来。"
  },
  {
    "segment_id": "0065",
    "text": "金色卷发、戴有一副较为精致的铜片护目镜。"
  },
  {
    "segment_id": "0066",
    "text": "韩东还注意到，此人右臂的动作显得不太自然……所戴的白手套与袖口间，可见些许金属光泽。"
  },
  {
    "segment_id": "0067",
    "text": "因服装的更变，大家都穿着符合当前背景下的大学生装束，但此人的气质一看就与普通平民不同。"
  },
  {
    "segment_id": "0068",
    "text": "似乎来自于圣城中的中产阶级，甚至更高。"
  },
  {
    "segment_id": "0069",
    "text": "“朋友们，现在可不是恐惧与害怕的时候，还记得刚不久，伟大的黑蔷薇骑士所告诫我们的话语吗？"
  },
  {
    "segment_id": "0070",
    "text": "恐惧只会让我们失败。"
  },
  {
    "segment_id": "0071",
    "text": "只有理性与勇气，才是我们唯一的‘兵器’，唯一能战胜‘恶灵’的兵器。"
  },
  {
    "segment_id": "0072",
    "text": "伟大的黑蔷薇骑士团长，他曾经可在新人时期通过了五星难度的事件！我们面对的只不过是四星难度的事件，并不是毫无生机。"
  },
  {
    "segment_id": "0073",
    "text": "大家团结起来，一定能找到活下去的机会！”"
  }
]
```

## Output Format
CRITICAL INSTRUCTION: You MUST translate the source text EXACTLY paragraph by paragraph, preserving the original order perfectly. DO NOT skip, drop, merge, or reorder any paragraphs. Each paragraph in the source MUST be translated.
Return ONLY valid JSON matching this schema:
{
  "chapter_number": 7,
  "chapter_title_vi": "Chương 7: <Vietnamese title>",
  "segments": [
    {
      "segment_id": "XXXX",
      "source": "...",
      "target": "..."
    }
  ]
}
