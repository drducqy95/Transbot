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


## Source Chapter 5 - 0005 便携式监狱
```json
[
  {
    "segment_id": "0001",
    "text": "# 第5章 便携式监狱"
  },
  {
    "segment_id": "0002",
    "text": "『【无面者的头颅】相关能力已激活。』"
  },
  {
    "segment_id": "0003",
    "text": "韩东思索着：“头颅所具备的能力是「模仿」与「便携式监狱」……第一个能力很容易理解，也就是相当于‘易容术’。”"
  },
  {
    "segment_id": "0004",
    "text": "先前，韩东在夺取头颅后，便自动根据他的潜意识变化为韩东生前的模样。"
  },
  {
    "segment_id": "0005",
    "text": "占据肉身后，也是完美模仿出青年的容貌。"
  },
  {
    "segment_id": "0006",
    "text": "“第二项能力……量子技术与某种魔法手段的结合吗？”"
  },
  {
    "segment_id": "0007",
    "text": "就在肉身占据成功时，韩东意识中出现了一扇铁门。"
  },
  {
    "segment_id": "0008",
    "text": "试着通过意识去触碰这扇铁门时。"
  },
  {
    "segment_id": "0009",
    "text": "嗡！"
  },
  {
    "segment_id": "0010",
    "text": "耳鸣声并伴随着短暂的意识放空。"
  },
  {
    "segment_id": "0011",
    "text": "重新睁眼时，韩东已置身于一间狭小、阴森而黑暗的监狱之中。"
  },
  {
    "segment_id": "0012",
    "text": "是切切实实存在的监狱，并非单纯的意识图像。"
  },
  {
    "segment_id": "0013",
    "text": "监狱规模较小，仅由一条走廊、一间牢房与一间密室所构成……与之前寻找肉体的监狱完全不同。"
  },
  {
    "segment_id": "0014",
    "text": "除去密室，整体还不到三十平米。"
  },
  {
    "segment_id": "0015",
    "text": "“这就是所谓的‘亚空间收容技术’？通过大脑主观意识干预形成的内部空间……真是神奇啊。”"
  },
  {
    "segment_id": "0016",
    "text": "过道普通，没有值得注意的地方。"
  },
  {
    "segment_id": "0017",
    "text": "韩东首先跨入一侧由铁栏封闭的牢房，当即发现了‘怪异之物’。"
  },
  {
    "segment_id": "0018",
    "text": "第一眼扫去，牢房似乎就是由普通的黑石材质构成。"
  },
  {
    "segment_id": "0019",
    "text": "如若仔细观察，会发现在这些黑石岩块的缝隙间，隐隐浮动着些许触须。"
  },
  {
    "segment_id": "0020",
    "text": "“之前，依靠着头颅进行移动时，脖颈处也是长出类似的触须，不过，在形态上更加类似于菌丝体……但牢房避免里的这些触须不同。”"
  },
  {
    "segment_id": "0021",
    "text": "但凡有缝隙的地方，均都能看见深色触须来回蠕动……长时间的凝视会让韩东很不舒服。"
  },
  {
    "segment_id": "0022",
    "text": "就在这时，一阵提示传来。"
  },
  {
    "segment_id": "0023",
    "text": "【无面者的监狱】"
  },
  {
    "segment_id": "0024",
    "text": "个体匹配性：完美（个体可完美驾驭监狱，不会因使用过度而遭到反噬）"
  },
  {
    "segment_id": "0025",
    "text": "规模：极小，可收纳生物数量：1（升级【无面者的头颅】将增加监狱规模）"
  },
  {
    "segment_id": "0026",
    "text": "使用方法：目标生命体陷入虚弱状态时，与其接触并启动便携式监狱，即可进行收容。"
  },
  {
    "segment_id": "0027",
    "text": "注："
  },
  {
    "segment_id": "0028",
    "text": "①.【无面者的头颅】升级后，会增加负重需求，请提前预留至少50点负重值，否则将导致升级失败。"
  },
  {
    "segment_id": "0029",
    "text": "②.请不要尝试收容状态良好的生物，一旦收容失败，将对本体造成极大伤害，监狱也将受到一定破坏。"
  },
  {
    "segment_id": "0030",
    "text": "③.在特殊环境下或主体正遭受其他生物的攻击时，将无法将自身传送到「便携式监狱」』"
  },
  {
    "segment_id": "0031",
    "text": "…………"
  },
  {
    "segment_id": "0032",
    "text": "“无面者的监狱？能收容生命体？”"
  },
  {
    "segment_id": "0033",
    "text": "韩东第一时间想到的是这个世界里追赶金属马车的‘异变体’。"
  },
  {
    "segment_id": "0034",
    "text": "至于收容普通人类，韩东是不会考虑的……收容人类既属于犯罪行为，也触及到韩东做人的底线。"
  },
  {
    "segment_id": "0035",
    "text": "如果真能收容一只异变体或是什么魔法生物，就能进行生物学层面的研究了。"
  },
  {
    "segment_id": "0036",
    "text": "韩东暂时退出这间让他感到毛骨悚然的牢房，转而前往隔壁的【密室】。"
  },
  {
    "segment_id": "0037",
    "text": "完全密封的房间，透过外层黑石缝隙，甚至能窥见内在的白色金属墙面。"
  },
  {
    "segment_id": "0038",
    "text": "密室正门为一扇厚重铁门所密封，需转动门上的液压阀来开启。"
  },
  {
    "segment_id": "0039",
    "text": "韩东本以为凭借这般弱小的肉身很难转动这种阀门。"
  },
  {
    "segment_id": "0040",
    "text": "谁知道，在手掌落于圆盘状的阀门表面时，就好像识别了韩东的生物信息，阀门自行转动。"
  },
  {
    "segment_id": "0041",
    "text": "嘎吱！"
  },
  {
    "segment_id": "0042",
    "text": "厚重的金属门也向外开启。      跨入密室的那一刻，由监狱本身带来的危险与压抑感瞬间消失。"
  },
  {
    "segment_id": "0043",
    "text": "掀开一帘防菌薄膜并穿过一道狭窄的缓冲间。"
  },
  {
    "segment_id": "0044",
    "text": "一间韩东无比熟悉的无菌实验室出现在眼前……洁净的白色墙面、事宜的温度与湿度、可调节的光照强度。"
  },
  {
    "segment_id": "0045",
    "text": "这与外面的监狱形成鲜明对比。"
  },
  {
    "segment_id": "0046",
    "text": "不过，相比于韩东生前所用的实验室……这间无菌室相对较小而且器材并不那么齐全。"
  },
  {
    "segment_id": "0047",
    "text": "内部仅有一台靠着墙壁的超净工作台与一道立于房间正中央的展览台。"
  },
  {
    "segment_id": "0048",
    "text": "前者用于菌体接种实验。"
  },
  {
    "segment_id": "0049",
    "text": "后者的玻璃展柜里，放置着一道特殊的注射器。"
  },
  {
    "segment_id": "0050",
    "text": "“这……为什么在监狱里会多出一间无菌实验室？难道说，与‘细胞团’有关？”"
  },
  {
    "segment_id": "0051",
    "text": "绕过展览台，韩东先行来到超净工作台前。"
  },
  {
    "segment_id": "0052",
    "text": "意外发现了栖息于培养皿内的细胞团，约手指头大小、正是韩东重生时的体征表象。"
  },
  {
    "segment_id": "0053",
    "text": "直觉告诉他，若这团细胞死亡，他也将一同殉葬。"
  },
  {
    "segment_id": "0054",
    "text": "就在韩东接触操作台时，一阵提示音传来："
  },
  {
    "segment_id": "0055",
    "text": "『击杀特定生命时，可通过「死尸注射器」抽取‘细胞精华’。"
  },
  {
    "segment_id": "0056",
    "text": "收集到的‘细胞精华’可通过无菌操作注入到‘细胞主体’之中，将根据细胞精华的质量与数量，增加负重上限。"
  },
  {
    "segment_id": "0057",
    "text": "请注意："
  },
  {
    "segment_id": "0058",
    "text": "1.「死尸注射器」可随意取用，遭到破坏也没关系。"
  },
  {
    "segment_id": "0059",
    "text": "2.「死尸注射器」只能对死亡时间不超过五分钟的特殊生物使用，对于活物或死亡时间过长的尸体，无法抽取‘细胞精华’。"
  },
  {
    "segment_id": "0060",
    "text": "3.一具尸体只能抽取一次。』"
  },
  {
    "segment_id": "0061",
    "text": "听闻提示后，韩东连忙扭头看向展览台里的精致注射器。"
  },
  {
    "segment_id": "0062",
    "text": "透明晶体管、黄铜针头并配以金属镶边。"
  },
  {
    "segment_id": "0063",
    "text": "“这就是增加细胞负重上限的方式！！”"
  },
  {
    "segment_id": "0064",
    "text": "韩东很是激动。"
  },
  {
    "segment_id": "0065",
    "text": "一个困扰自己的难题被解开了，接下来只需要确定何为‘特殊生命’即可。"
  },
  {
    "segment_id": "0066",
    "text": "只要能增加负责上限，韩东就能驾驭更强的肉体。"
  },
  {
    "segment_id": "0067",
    "text": "“对于这一世界的了解还是太少……便携式监狱暂时就了解这么多吧。”"
  },
  {
    "segment_id": "0068",
    "text": "韩东退回走廊，推开监狱出口门时，转眼间便回到巨型橡树的下端。"
  },
  {
    "segment_id": "0069",
    "text": "四周无人，韩东试着取用注射器。"
  },
  {
    "segment_id": "0070",
    "text": "果真，随着他意识传递‘取用’的想法，直接在手掌中出现了一道精密的铜制外壳注射器……随着意识传递‘收回’的想法，注射器也就自行没入皮下。"
  },
  {
    "segment_id": "0071",
    "text": "这一过程让韩东的掌心略感酥麻。"
  },
  {
    "segment_id": "0072",
    "text": "“监狱里的秘密还有很多……暂时就这样吧，首先得处理这位青年的事情。"
  },
  {
    "segment_id": "0073",
    "text": "与他相关的基本家庭关系必须搞清楚。"
  },
  {
    "segment_id": "0074",
    "text": "以及他自杀的原因与手腕上正在倒计时的发条装置。”"
  },
  {
    "segment_id": "0075",
    "text": "韩东的思路很清晰。"
  },
  {
    "segment_id": "0076",
    "text": "夺得肉身只是最简单的一步，接下来需要去熟悉与适应他的生活环境，不能让人发现瓦伦.尼古拉斯已经换了一个人。"
  },
  {
    "segment_id": "0077",
    "text": "而且，发条手环的倒计时让韩东十分不安。"
  },
  {
    "segment_id": "0078",
    "text": "新书期间，老样子，每日两更……如果不想追更的可以先屯着，不过记得投个票呀~~"
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
