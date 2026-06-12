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

## Chapter 0005 - Chương 5: Thi thử đại học

### Summary
Chapter 5 completed via pipeline.

## Chapter 0006 - Chương 6: Thời đại Đại Hắc Ám

### Summary
Chapter 6 completed via pipeline.


## Source Chapter 7 - 0007 二中女神
```json
[
  {
    "segment_id": "0001",
    "text": "# 第7章 二中女神"
  },
  {
    "segment_id": "0002",
    "text": "“嗡……”"
  },
  {
    "segment_id": "0003",
    "text": "老旧的考试舱缓缓打开，李耀迈步而出，甩了甩脑袋，隐隐有些头痛，这是在太虚幻境中过度透支心神的副作用。"
  },
  {
    "segment_id": "0004",
    "text": "“脑袋好痛，真该死，就我们这些‘杂鱼班’的学生还在用这种垃圾货色，重点班和平行班的学生，都换上了最新一代的灵能考试舱，再怎么透支都不会有副作用的！”孟江在他身边大声抱怨，随后捅了捅他的腰眼，“小妖，这次模拟考难度好高，我大概又考砸了，回去肯定要吃一顿‘竹笋炒肉’，你怎么样？”"
  },
  {
    "segment_id": "0005",
    "text": "“一般般吧。”李耀摸了摸鼻子，这次考试的难度确实有点高，不过他的基础比较扎实，心态也够冷静，自我感觉已经发挥到极限了。"
  },
  {
    "segment_id": "0006",
    "text": "“赶紧看看！”孟江凑到他的考试舱旁边操作起来，考试舱中都安装有超高速晶脑，可以实时计算成绩，考试一结束，成绩就出来了。"
  },
  {
    "segment_id": "0007",
    "text": "“哇，525分，好高的分数，足够上重点大学了，还说一般般？过分的谦虚就是骄傲，你个死小妖！”孟江惊呼。"
  },
  {
    "segment_id": "0008",
    "text": "李耀扫了一眼光幕，心中却是暗叹一声，525分这个分数确实不算低，勉强够得上联邦几所知名的重点大学分数线了，不过紧随其后的一个数值，却红得有些扎眼。"
  },
  {
    "segment_id": "0009",
    "text": "“灵根开发度，35%。”"
  },
  {
    "segment_id": "0010",
    "text": "灵根，是位于人类大脑前额“松果体”部位的一个神秘器官，说神秘，是因为从解剖学的角度来说，这个器官根本就不存在，千百年来都没有人能找到一个货真价实的“灵根标本”。"
  },
  {
    "segment_id": "0011",
    "text": "但是在修真世界中，这又是一个真实存在的器官，而且是修真者最重要的器官，是沟通人类和天地灵气、宇宙灵能的关键所在！"
  },
  {
    "segment_id": "0012",
    "text": "只有灵根开发度达到100%，“灵根觉醒”，才能踏上修真之路！"
  },
  {
    "segment_id": "0013",
    "text": "一般大学在招生时，是不看灵根开发度这一项数值的，哪怕是1%也没有关系，反正一般大学培养的都是普通人。"
  },
  {
    "segment_id": "0014",
    "text": "可是专门培养修真者的“九大精英联校”在招生时，却会把考生成绩和灵根开发度相乘，当成最终分数——自然，灵根开发度越高越占便宜。"
  },
  {
    "segment_id": "0015",
    "text": "李耀的灵根开发度低得可怜，五百多分乘以35%之后，只剩下不到两百分。"
  },
  {
    "segment_id": "0016",
    "text": "而重点班的天之骄子，普遍拥有超过60%的灵根开发度，也就是说人家只要考三百多分，就能轻松碾压李耀。"
  },
  {
    "segment_id": "0017",
    "text": "更何况，灵根开发度越高，人的思维就越敏捷，五感越敏锐，对身体掌控度越高，成绩怎么也不会比他们这些普通班的“杂鱼”差了。"
  },
  {
    "segment_id": "0018",
    "text": "李耀不是没想过下苦功提升灵根开发度，可这玩意儿和学习不同，书本知识可以死记硬背，体能和武技可以疯狂修炼，灵根开发度却是实打实要靠资源堆出来的。"
  },
  {
    "segment_id": "0019",
    "text": "比如重点班的天之骄子们，每天服用各种天材地宝和强化药剂，还在家里添置“灵根开发仪”或者去专门的“冥修馆”特训，每个月花在灵根开发上的钱，少则数万、多则几十上百万都有，金山银山砸下去，才能将灵根开发度艰难地提升“1%”。"
  },
  {
    "segment_id": "0020",
    "text": "而李耀在法宝坟墓拾荒，一个月最多也就赚万把块，支付房租、生活费和学费之后，就剩不下三瓜两枣了，肚皮都填不饱，哪里有闲钱去开发灵根？"
  },
  {
    "segment_id": "0021",
    "text": "总而言之一个字——他娘的穷啊！"
  },
  {
    "segment_id": "0022",
    "text": "心里正犯愁呢，就听到孟江又用杀猪般的声音嚎叫起来：“哇，两个691分！司佳雪和赫连烈这两个家伙，又是这次模拟考的并列第一！”"
  },
  {
    "segment_id": "0023",
    "text": "这一次模拟考，是整个高三年级组同时举行，教室前方的光幕上，飞快浮现出了全校前十名的学生信息。"
  },
  {
    "segment_id": "0024",
    "text": "其中并列第一的，是一名清冷如雪的美少女，和一名英姿勃发、目光慑人的高大少年。"
  },
  {
    "segment_id": "0025",
    "text": "他们的分数，并没有让李耀动容，可是跟在分数后面的灵根开发度，令他嫉妒得眼里喷火。"
  },
  {
    "segment_id": "0026",
    "text": "司佳雪，灵根开发度71%；赫连烈，灵根开发度72%！"
  },
  {
    "segment_id": "0027",
    "text": "孟江兀自聒噪：“啧啧啧啧，真不愧是咱们赤霄二中的风云人物，校花校草，重点班几十个精英中的精英！你看看，这两个家伙不但男的帅，女的靓，而且出身富豪家庭，据说家族里都出现过好几名修真者，成绩又好，灵根开发度又高，是这一次咱们学校冲击高考的秘密武器！据说他们考上九大精英联校是十拿九稳的事，学校专程请妖刀彭海来给他们特训，也有一层意思，是希望他们能冲击浮戈城的高考状元，至少是全市前十名！”"
  },
  {
    "segment_id": "0028",
    "text": "说着说着，孟江很夸张地叹了口气：“唉，货比货得扔，人比人要死啊，大家平平都是高中生，现在都在一个学校里厮混，可是经过高考，恐怕他们就要一飞冲天，踏入修真者圈子，过上纸醉金迷，腐朽没落的生活了，而咱们这样的穷小子，就只有当一辈子的打工者，工薪族，想想真是心凉！”"
  },
  {
    "segment_id": "0029",
    "text": "说了半天，没见反应，孟江扭头一看，却见李耀双眼发直，盯着司佳雪的照片，目光幽深，不知在琢磨什么，连忙在死党脑袋上敲了一下：“喂，你小子不会是看上司佳雪了吧？我好心好意提醒你，这女人可是咱们碰不得的，她和赫连烈是世交，据说两大家族颇有联姻的意思，赫连烈对她也是志在必得——你别看这小子长得高大威猛，心眼却是最小，从来见不得别人亲近司佳雪，上次有个转校生初来乍到，不知深浅，放出话来要追求司佳雪，结果在‘武技课’上被赫连烈打断了三根骨头，至于我们这种杂鱼，赫连烈一个喷嚏，我们就内伤吐血了！”"
  },
  {
    "segment_id": "0030",
    "text": "“废话。”"
  },
  {
    "segment_id": "0031",
    "text": "李耀收回目光，似乎下了什么决心，“赫连烈先不提，就说这个司佳雪，整天摆出一张冷冰冰的死人脸，十有八九是性冷淡，我怎么会喜欢这一型？”"
  },
  {
    "segment_id": "0032",
    "text": "……"
  },
  {
    "segment_id": "0033",
    "text": "学校的大部分资源都向重点班和平行班倾斜，对普通班的管理十分宽松，模拟考结束之后，普通班的学生就针对各自缺陷，进行专项训练，一天很快过去，下午四点，就要放学了。"
  },
  {
    "segment_id": "0034",
    "text": "“等会儿一起走，我刚找到一家煎饼摊，老板的三大爷是‘火神派’的烧火杂役，老板也间接学到一手‘火云掌’，炮制出来的‘赤焰大手印鸡蛋饼’绝对一流，今天我请客，怎么样？”孟江豪气万千地拍着胸脯。"
  },
  {
    "segment_id": "0035",
    "text": "“不了，今天有事，还是明天我请你吧！”不等死党回答，李耀飞快窜出了教室。"
  },
  {
    "segment_id": "0036",
    "text": "他贼头贼脑地左右打量一阵，绕着校园兜了大半圈，穿过两处食堂，在校园后面一片小树林里停了十几分钟，又折返回来，蹑手蹑脚地摸进了老教学楼底层的一间杂物室。"
  },
  {
    "segment_id": "0037",
    "text": "轻轻关上门，就嗅到了一股若有若无，空谷幽兰般的香气。"
  },
  {
    "segment_id": "0038",
    "text": "一双清泉般的冷冽美眸，正在黑暗中有些不耐地瞪着他，眸子下方，是挺翘的鼻尖和抿紧的薄唇。"
  },
  {
    "segment_id": "0039",
    "text": "如果孟江在这里，一定会发出标志性的杀猪嚎叫：“好你个死小妖，居然真的和‘二中女神’司佳雪勾搭上了！你，你真是色胆包天！”"
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
