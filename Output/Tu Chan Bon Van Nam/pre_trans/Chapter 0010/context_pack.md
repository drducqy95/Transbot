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

## Chapter 0007 - Chương 7: Nữ thần Nhị Trung

### Summary
Chapter 7 completed via pipeline.

## Chapter 0008 - Chương 8: Sửa chữa tinh não

### Summary
Chapter 8 completed via pipeline.

## Chapter 0002 - 0002 光幕仪

### Summary
Chapter 2 completed via pipeline.

## Chapter 0002 - Chương 2: Quang mạc nghi

### Summary
Chapter 2 completed via pipeline.

## Chapter 0002 - Chương 2: Quang mạc nghi

### Summary
Chapter 2 completed via pipeline.

## Chapter 0009 - Chương 9: Cá muối và giày

### Summary
Chapter 9 completed via pipeline.


## Source Chapter 10 - 0010 阴魂入体
```json
[
  {
    "segment_id": "0001",
    "text": "# 第10章 阴魂入体"
  },
  {
    "segment_id": "0002",
    "text": "超高速晶轨列车飞驰而过，“波”一声，好似鸡蛋碎裂，神秘老者被撞了个正着，在千分之一秒内就四分五裂，汹涌澎湃的灵能轰击之下，残肢断臂瞬间气化，连最基本的细胞都灰飞烟灭，荡然无存！"
  },
  {
    "segment_id": "0003",
    "text": "李耀只看到红光一闪，神秘老者就彻底消失！"
  },
  {
    "segment_id": "0004",
    "text": "他心中有些无奈地叹了口气。"
  },
  {
    "segment_id": "0005",
    "text": "在法宝坟墓那种危机四伏的恐怖地域长大，死人是家常便饭，更何况在异梦中他也无数次亲身经历死亡，所以对于死亡，李耀倒是没有常人那种极度恐惧和不适应的感觉。"
  },
  {
    "segment_id": "0006",
    "text": "不过，终究是一条鲜活的生命，却以这样一种惨烈的方式消逝在自己面前，心里多少有些异样。"
  },
  {
    "segment_id": "0007",
    "text": "“这个老头大概是走火入魔的修真者，发了疯，才会干出这样的怪事。”李耀暗自思量。"
  },
  {
    "segment_id": "0008",
    "text": "晶轨列车并没有被这场小小的意外干扰，仍旧高速疾驰，一去不复返，很快消失在视野中。"
  },
  {
    "segment_id": "0009",
    "text": "李耀却知道，列车上的警卫肯定把这件事通知了本地的警察部门，甚至还有军方，很快就会有大批军警赶来。"
  },
  {
    "segment_id": "0010",
    "text": "作为在法宝坟墓中拾荒的垃圾虫，他的行为可以说游走在法律边缘，一向很忌讳和军警打交道，李耀不想惹上麻烦，紧了紧衣服，加快脚步，穿过了涵洞。"
  },
  {
    "segment_id": "0011",
    "text": "他却不知，在他看不见的层面，晶轨大桥上，刚才神秘老者站立的地方，浮现出了一个和神秘老者一模一样的透明水晶人形，有些疑惑地打量了一下四周，最后眼前一亮，锁定住了生气焕发的他。"
  },
  {
    "segment_id": "0012",
    "text": "透明水晶人形骤然迸裂，化作万千无影无形的水晶碎片，折射着皎洁的月华，如同上万头斑斓的蝴蝶，振翅高飞，无声无息地没入李耀体内！"
  },
  {
    "segment_id": "0013",
    "text": "“好冷！”"
  },
  {
    "segment_id": "0014",
    "text": "李耀觉得阴风刺骨，好似有什么东西在他耳边轻声呢喃，用十分古老玄妙的语言，诉说着难以言喻的恐怖，不由自主地打了个寒颤。"
  },
  {
    "segment_id": "0015",
    "text": "古怪，实在太古怪了，他有些毛骨悚然，紧了紧校服，干脆一路小跑起来。"
  },
  {
    "segment_id": "0016",
    "text": "按理说，人一旦跑动起来，四肢都活动开了，身体应该发热，可是无论李耀怎么跑，甚至将速度飙至极限，跑得都要呕吐，那股冻彻心扉的凉意却始终如影随形，如跗骨之蛆，一寸一寸将他吞噬！"
  },
  {
    "segment_id": "0017",
    "text": "当他跌跌撞撞扑进家门时，整个人已经冻成了冰坨，可是从外表看起来，却是面色潮红，满头大汗，周身白雾缭绕，热气蒸腾，说不出的诡异！"
  },
  {
    "segment_id": "0018",
    "text": "“小黑，小黑，我好像是生病了，快扶我上床，再从药箱里找点退烧的药用灵符来！”李耀含含糊糊地说着，眼前却是一阵一阵地发黑，上下眼皮不住打架，不等黑翼剑飞来，腿一软，他已经瘫倒在了地上，打起了呼噜，彻底睡死过去。"
  },
  {
    "segment_id": "0019",
    "text": "仿佛陷入一团幽深的沼泽，五感都被剥夺殆尽，他在绝对的黑暗中不断**，**，永无止境地**。"
  },
  {
    "segment_id": "0020",
    "text": "终于，在他就要发疯，就要祈求九天十地无穷世界亿万神佛干脆给他一个了断之时，周身一松，黑暗如潮水般退去，他又一次呼吸到了新鲜的空气——比他曾经呼吸到过，更新鲜百倍的空气！"
  },
  {
    "segment_id": "0021",
    "text": "“这是什么地方？”李耀有些迷惘的打量着四周。"
  },
  {
    "segment_id": "0022",
    "text": "潜意识里他知道自己正陷入一场凶险的“梦魇”，不过和他过去所做的“异梦”不同，这是一处明显带有浓烈古典风格的梦境。"
  },
  {
    "segment_id": "0023",
    "text": "他正站在一片无比辽阔的大校场之上，四周矗立着无数高耸入云的巨大兵刃和法宝铜像，而占地超过一百亩的巨大校场，竟然是平铺在一座浮空山头之上。"
  },
  {
    "segment_id": "0024",
    "text": "下面，是一眼望不到边，巨浪翻滚的黑色海洋！"
  },
  {
    "segment_id": "0025",
    "text": "熏人的汗臭味和阳刚血气在鼻腔里横冲直撞，差点没把李耀熏死过去，在他周围站着好几千名四肢发达，肌肉贲张，满脸横肉的壮汉，每一条壮汉肩膀上都扛着一柄看似足有千斤的巨锤，卖力操练着。"
  },
  {
    "segment_id": "0026",
    "text": "轰！轰！轰！"
  },
  {
    "segment_id": "0027",
    "text": "数千柄巨锤一起砸向地面，整座浮空山都微微震荡。"
  },
  {
    "segment_id": "0028",
    "text": "随即，李耀吃惊地发现，自己竟然也变成了一条身高九尺的彪形大汉，连容貌都发生了彻底改变，用手一摸，下巴上胡子拉碴，钢针也似！"
  },
  {
    "segment_id": "0029",
    "text": "他手里同样攥着一柄栲栳大的铁锤，握把的缠绳都被他磨破掌心的鲜血*******大校场前方，一条比所有巨汉都要庞大一轮，简直不似人类的“巨灵神”，瞪着铜铃大眼，如雷暴喝：“你们这三千五百二十七个废物，已经正式拜入‘百炼宗’门下，成为百炼宗的低级杂役，这是你们祖上积德，三生修来的福气！我们百炼宗，是‘洪荒大世界’中最强的炼器宗派，门规森严，即便门下一名小小的低级杂役，也要豁出命去修炼！”"
  },
  {
    "segment_id": "0030",
    "text": "“身为低级杂役，你们每天都要挑三千斤水，砍五十棵树，去下面的‘无渊海’里猎杀至少十条‘脊刺鲨’，那就是你们的食物！”"
  },
  {
    "segment_id": "0031",
    "text": "“不过最最重要的，就是要练好咱们百炼宗的基础功法《一百零八手披风乱锤法》！都给我听好了，你们这些废物，每天都要挥舞铁锤一万下，一下都不准少，什么时候能把面前这块用‘金精石’炼制的地板轰出一尺深的窟窿，就能提升成‘打铁杂役’，修炼更上乘的功法！”"
  },
  {
    "segment_id": "0032",
    "text": "“练！练！都给我玩命练！欧冶明，你傻愣愣站着干什么，为什么不练？”"
  },
  {
    "segment_id": "0033",
    "text": "李耀还没搞清楚怎么回事，却发现所有壮汉都用万分怜悯的眼神打量着自己，心中顿时大寒，面前扑来一股猛恶的旋风，百丈开外的巨灵神，一眨眼功夫就出现在他面前，居高临下，恶狠狠地瞪着他。"
  },
  {
    "segment_id": "0034",
    "text": "“欧冶明，昨天吃饭时胡言乱语，说什么将来一定要当‘百炼宗宗主’的狂徒也是你，怎么，是否觉得《披风乱锤法》太过低级，不适合你这个‘未来宗主’修炼？好，我今天就让你见识一下，一百零八手披风乱锤法的厉害，哇杀！”"
  },
  {
    "segment_id": "0035",
    "text": "巨灵神双手一摊，手中黑气凝结，幻化出一柄比李耀脑袋还大的巨锤，舞得虎虎生风，劈头盖脑砸了过来，李耀还没反应过来，就觉得自己肋生双翅，腾空而起，而脑袋好似变成了十个那么大，心中不住惨叫：“这，这他娘的究竟是怎么回事啊！”"
  }
]
```

## Output Format
CRITICAL INSTRUCTION: You MUST translate the source text EXACTLY paragraph by paragraph, preserving the original order perfectly. DO NOT skip, drop, merge, or reorder any paragraphs. Each paragraph in the source MUST be translated.
Return ONLY valid JSON matching this schema:
{
  "chapter_number": 10,
  "chapter_title_vi": "Chương 10: <Vietnamese title>",
  "segments": [
    {
      "segment_id": "XXXX",
      "source": "...",
      "target": "..."
    }
  ]
}
