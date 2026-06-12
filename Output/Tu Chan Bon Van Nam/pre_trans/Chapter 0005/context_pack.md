# Translation Context Pack

## Project
- Branch: Tu Chan Bon Van Nam
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

## Chapter 0001 - Chương 1: Nghĩa địa pháp bảo

### Summary
Chapter 1 completed via pipeline.

## Chapter 0002 - Chương 2: Quang mạc nghi

### Summary
Chapter 2 completed via pipeline.

## Chapter 0003 - Chương 3: Dị mộng

### Summary
Chapter 3 completed via pipeline.

## Chapter 0004 - Chương 4: Yêu Đao Bành Hải

### Summary
Chapter 4 completed via pipeline.

## Chapter 0001 - Chương 1: Nghĩa địa pháp bảo

### Summary
Chapter 1 completed via pipeline.

## Chapter 0002 - 0002 光幕仪

### Summary
Chapter 2 completed via pipeline.

## Chapter 0003 - Chương 3: Dị mộng

### Summary
Chapter 3 completed via pipeline.


## Source Chapter 5 - 0005 模拟高考
```json
[
  {
    "segment_id": "0001",
    "text": "# 第5章 模拟高考"
  },
  {
    "segment_id": "0002",
    "text": "作为冲刺高考的高三生，该学的课程早就学完了，最后这一百天主要是查漏补缺和各种考试，每周一上午，都有一场非常重要的模拟考。"
  },
  {
    "segment_id": "0003",
    "text": "在老师不耐烦的催促下，李耀深吸一口气，踏入标注着自己学号的“考试舱”，舱门封闭，整个世界一片死寂。"
  },
  {
    "segment_id": "0004",
    "text": "“就算没有‘彭海’亲自指点，我也要考上‘九大精英联校’，我拼命，我怕谁？”李耀狠狠攥紧了拳头。"
  },
  {
    "segment_id": "0005",
    "text": "“滴！滴！滴！”考试舱内侧的一块光幕上，数字跳动，正在倒计时，当数字变成“零”时，一道古井无波的冰冷声音响起：“考试开始，考生准备！”"
  },
  {
    "segment_id": "0006",
    "text": "考试舱内侧镌刻的上万道灵符同时闪亮，李耀只觉得眼前一花，斗转星移，已经出现在一片红褐色的荒漠中央。"
  },
  {
    "segment_id": "0007",
    "text": "地面炙热，双脚仿佛针扎；空气粘稠到近乎凝固，就像湿毛巾缠在身上，怎么都挣脱不开；偶尔刮来的热风中夹杂着浓烈的血腥气息，四面八方隐约传来鬼哭狼嚎。"
  },
  {
    "segment_id": "0008",
    "text": "五感如此真切，仿佛脚踏实地，置身修罗杀场。"
  },
  {
    "segment_id": "0009",
    "text": "李耀却知道，这是考试舱幻化出来的“太虚幻境”，时间紧迫，他定了定神，朝着天空中一个透明箭头指引的方向疾驰而去。"
  },
  {
    "segment_id": "0010",
    "text": "五十公里长途越野跑，是联邦高考的基础科目，为了遴选出有希望成为修真者的精英少年，一路上都是危机四伏，陷阱重重。"
  },
  {
    "segment_id": "0011",
    "text": "果然，当李耀路过一处微微隆起的土包时，土包忽然爆裂，射出无数碎石，从碎石中窜出一头土黄色的双头沙狼！"
  },
  {
    "segment_id": "0012",
    "text": "这种妖兽比普通野狼要大上一轮，脊背高高鼓起，上面还长着一个畸形的小脑袋，是低阶妖兽“沙狼”的变种，除了擅长蛰伏在沙地中之外，还拥有极高的智慧，对高中生而言，是极为难缠的对手。"
  },
  {
    "segment_id": "0013",
    "text": "可是对李耀这头在法宝坟墓中生存了十八年的“秃鹫”来说，观察每一寸环境变化早就成为本能，双头沙狼的伪装未免有些拙劣，早就被他看穿。"
  },
  {
    "segment_id": "0014",
    "text": "“巨熊靠！”"
  },
  {
    "segment_id": "0015",
    "text": "不等双头沙狼完全窜出，李耀双腿弹射，身体缩成一团，肩膀一沉，恍若一头狂暴的巨熊，狠狠撞了过去！"
  },
  {
    "segment_id": "0016",
    "text": "他选的时机非常巧妙，正是双头沙狼窜出的最高点，旧力已尽，无处借力，更无法变向，被他撞个正着。"
  },
  {
    "segment_id": "0017",
    "text": "“咔嚓！”"
  },
  {
    "segment_id": "0018",
    "text": "双头沙狼阴险狡诈，体质却弱，只喜偷袭，不擅正面对抗，被他一记“巨熊靠”撞断了脊椎骨，朝沙坑反弹回去。"
  },
  {
    "segment_id": "0019",
    "text": "李耀冷笑一声，蛇步上前，伸爪如刃，狠狠抓向双头沙狼脊背上的小脑袋。"
  },
  {
    "segment_id": "0020",
    "text": "“铁鹰爪！”"
  },
  {
    "segment_id": "0021",
    "text": "狼头瞬间碎裂，双头沙狼惨叫一声，死得不能再死。"
  },
  {
    "segment_id": "0022",
    "text": "虚空中传来一阵悦耳的“叮叮”声，是考试舱正在计算李耀这次击杀的分数。"
  },
  {
    "segment_id": "0023",
    "text": "李耀心中窃喜，这套源自基础武学《战兽十三势》的连续技，起码能为自己加上十分。"
  },
  {
    "segment_id": "0024",
    "text": "他也不急着赶路，而是把双头沙狼的尸体拖出沙坑，找了块边缘还算锋利的石头，将妖兽开膛破肚。"
  },
  {
    "segment_id": "0025",
    "text": "片刻之后，四根肋骨打磨成了四柄骨刃，狼皮勉强扎成一个水袋，装满了狼血。"
  },
  {
    "segment_id": "0026",
    "text": "在炙热的荒漠中，一袋狼血是能救命的。"
  },
  {
    "segment_id": "0027",
    "text": "全副武装，略加休整之后，李耀继续前进，不过一个钟头，他已经扛过一场黑风暴，击杀了四头低阶妖兽，不过考试才刚刚开始，这还只是热身而已，接下来才是叫每一名联邦考生最痛不欲生的环节。"
  },
  {
    "segment_id": "0028",
    "text": "天空中，绿色的符文如暴雨般倾盆直下，组成了一道问题："
  },
  {
    "segment_id": "0029",
    "text": "“肖明是一名炼气期修真者，身怀5500晶的灵力，在一次修炼中不小心中了诡异的‘噬心虫’，每秒钟被吞噬48晶灵力，肖明的师父在1分13秒之后发现，为了救他，每秒钟向他体内渡入55晶灵力，并且在两分钟之后提升到每秒钟渡入59晶灵力，问——”"
  },
  {
    "segment_id": "0030",
    "text": "“一，肖明要多久才能恢复正常灵力水平？”"
  },
  {
    "segment_id": "0031",
    "text": "“二，请简述‘噬心虫’的炼制方法，以及中了噬心虫之后的症状及治疗步骤。”"
  },
  {
    "segment_id": "0032",
    "text": "“三，请说出‘噬心虫’最早由哪一个门派炼制成功？列举至少五名该门派的宗主，并简述该门派的灭亡原因。”"
  },
  {
    "segment_id": "0033",
    "text": "李耀轻轻拍了拍脸颊，没想到一上来就是难度这么高的“综合题”，糅合了数学、历史学、药理学、战场急救学等多学科的知识，不愧是完全仿真的“模拟高考”！"
  },
  {
    "segment_id": "0034",
    "text": "凝神静气，仔细思索，脑海中浮现出无数平时积累的知识，李耀聚精会神，飞快作答，一小题一小题地“攻克”，很快，一道道用神念书写的淡蓝色答案，出现在绿色的题目下方。"
  },
  {
    "segment_id": "0035",
    "text": "解答完成，下一题！"
  },
  {
    "segment_id": "0036",
    "text": "“一位正道‘灵山宗’修真者脚踩飞剑，从东方以每秒钟247米的速度向一处山谷飞去，而另一位邪道‘血杀堡’修真者脚踏黑云，从西方以每秒239秒的速度相对而行，目前两人之间相距122.5公里，问他们将在多久之后相遇？”"
  },
  {
    "segment_id": "0037",
    "text": "“假设两人修为相当，均采用各自宗门基础功法和法宝，请结合灵山宗和血杀堡的特点，推演两人的战斗过程——至少推演七个回合，不得少于五百字。”"
  },
  {
    "segment_id": "0038",
    "text": "这道题明显比上一道要简单许多，不过当李耀正欲答题时，前方再度传来熏人的妖兽气息，焦躁的低吼声越来越近。"
  },
  {
    "segment_id": "0039",
    "text": "——在腥风血雨中计算、答题，比的是考生的体能、武技、意志、计算力和思维敏捷力，所有能力综合起来全都出类拔萃的人，才能在联邦高考中脱颖而出，走上修真之路！"
  },
  {
    "segment_id": "0040",
    "text": "李耀双手交叉，拔出两柄白森森的骨刃，舔了舔嘴唇，正面迎上，而大脑中上万道念头不住翻滚，高速计算着……"
  },
  {
    "segment_id": "0041",
    "text": "偌大的校园鸦雀无声，每一个教室里都摆放着几十台考试舱，在太虚幻境里，一名名高三生，都在疯狂地奋斗、拼搏，干掉一头头妖兽和一道道题目。"
  },
  {
    "segment_id": "0042",
    "text": "不知不觉，太虚幻境中的时间已经过去了四个多小时，考试接近尾声。"
  },
  {
    "segment_id": "0043",
    "text": "李耀周身布满了大大小小的七八十处伤口，不少地方的鲜血都流干了，特别是腹部还插着一枚妖兽断齿不敢拔出，手中的骨刃也几乎磨凸。"
  },
  {
    "segment_id": "0044",
    "text": "只有那对亮晶晶的大眼睛，依旧保持清澈，毫不掩饰地喷涌着**的光芒。"
  },
  {
    "segment_id": "0045",
    "text": "“应该是最后一题了……”"
  },
  {
    "segment_id": "0046",
    "text": "当天空中滚落八角垂芒，金光闪闪的符文时，李耀凭借丰富的考试经验判断出，是最后一道价值一百分的大题“综述题”。"
  },
  {
    "segment_id": "0047",
    "text": "果然，题目不长，却一字千钧：“请综述‘大黑暗时代’。”"
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
