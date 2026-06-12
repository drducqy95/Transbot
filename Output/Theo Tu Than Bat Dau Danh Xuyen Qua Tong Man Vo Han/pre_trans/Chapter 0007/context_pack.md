# Translation Context Pack

## Project
- Branch: Theo Tu Than Bat Dau Danh Xuyen Qua Tong Man Vo Han
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
| Chinese | Vietnamese | Type |
| --- | --- | --- |
| 产地：衍生 | Sản địa: Phái sinh | term |
| 天赋评级： | Đánh giá thiên phú: | term |
| 天赋：限制器 | Thiên phú: Bộ hạn chế | term |
| 浅打 | Thiển Đả | term |


## Story Timeline (latest)

## Chapter 0001 - Chương 1: Ta Có Một Vẻ Đẹp Trị Số

### Summary
Chapter 1 completed via pipeline.

## Chapter 0002 - Chương 2: Không Gian Chung Yên

### Summary
Chapter 2 completed via pipeline.

## Chapter 0003 - Chương 3: Hóa Ra Ta Đang Cười

### Summary
Chapter 3 completed via pipeline.

## Chapter 0004 - Chương 4: Unohana (Truyện mới cầu cất chứa)

### Summary
Chapter 4 completed via pipeline.

## Chapter 0005 - Chương 5: Bạn Cùng Phòng Của Ta Là Aizen? (Ba canh cầu phiếu)

### Summary
Chapter 5 completed via pipeline.

## Chapter 0006 - Chương 6: Bài kiểm tra nhập học

### Summary
Chapter 6 completed via pipeline.


## Source Chapter 7 - 0007 剑道？我没学过啊
```json
[
  {
    "segment_id": "0001",
    "text": "# 第7章 剑道？我没学过啊"
  },
  {
    "segment_id": "0002",
    "text": "轰——"
  },
  {
    "segment_id": "0003",
    "text": "在剧烈的撞击声中，陆离倒飞了出去，他在空中调整身形，落地后连续撤步卸力，最后在地板上划出一段距离才停了下来。"
  },
  {
    "segment_id": "0004",
    "text": "他看了眼手中已经断成两截的竹剑，将其扔在地上，活动了下被震得生疼的手臂，咧嘴笑道：“老师，这可不是十七等灵威吧？”"
  },
  {
    "segment_id": "0005",
    "text": "藤本柱神情有些尴尬，是的，方才的那一瞬，他本能的防御要害，动用了自己的灵压力量防御，这才将陆离震飞了出去。"
  },
  {
    "segment_id": "0006",
    "text": "而他此时惊觉，他的后背已经被汗浸湿了，刚才短暂的交锋，仿佛像是在生死线上走了一遭。"
  },
  {
    "segment_id": "0007",
    "text": "明明对方真正的实力很弱，却让他在那一瞬间感到有种压迫感，正是那种要压倒他的狂气，摧毁了他的神经，让他人体的自我防御机制启动了。"
  },
  {
    "segment_id": "0008",
    "text": "“陆君，你很出色，以前是接受过剑道相关的训练吗？”"
  },
  {
    "segment_id": "0009",
    "text": "藤本柱调整心态后好奇的问道，他毕竟是真央灵术院的老师，也不至于因为这件事就恼羞成怒，反而对于有着出众剑道水平的陆离很欣赏。"
  },
  {
    "segment_id": "0010",
    "text": "“剑道？没学过。”"
  },
  {
    "segment_id": "0011",
    "text": "陆离摇头道，他说的是实话，他可从来没学过这个世界的‘剑道’，但刀术他确实略知一二。"
  },
  {
    "segment_id": "0012",
    "text": "哦，按照终焉空间菜单中关于专精的评价，他是大师级刀术专精，貌似还可以的样子。"
  },
  {
    "segment_id": "0013",
    "text": "在他原有的世界中，练武的人已经很少了。"
  },
  {
    "segment_id": "0014",
    "text": "尽管他不愿意承认，但悲哀的事实是，那些被他杀死的人，已经在某种意义上代表了那个时代武学的巅峰了。"
  },
  {
    "segment_id": "0015",
    "text": "可即便是带着外骨骼辅助提升了身体机能，被誉为刀王的王落，在自己手中也只走了十招罢了。"
  },
  {
    "segment_id": "0016",
    "text": "王落拿着公司定制的亚利钢刀，而自己杀对方的时候，只用了一把普通的杀猪刀。"
  },
  {
    "segment_id": "0017",
    "text": "所以他在杀掉那群所谓的武学宗师后，对那个世界有些绝望。"
  },
  {
    "segment_id": "0018",
    "text": "此时，道场内小声讨论声不绝，显然都被这场切磋的结果惊到了。"
  },
  {
    "segment_id": "0019",
    "text": "而人群中的蓝染，黑框眼镜下的那双眸子也闪烁着某种光，他感觉自己的室友好像很有意思，看来在真央灵术院的这几年不会无聊了。"
  },
  {
    "segment_id": "0020",
    "text": "“你是说……你从没学过剑道？”"
  },
  {
    "segment_id": "0021",
    "text": "藤本柱对陆离的答案很吃惊，不过细想，对方只是一个流民，也确实没什么正规渠道能学习剑道。"
  },
  {
    "segment_id": "0022",
    "text": "可这么一来，岂不是更能说明陆离的天赋吗？"
  },
  {
    "segment_id": "0023",
    "text": "从未接受过正规教育，却能在‘同灵威’等级下正面战胜自己这个剑道老师，卯之花队长这次带回来的孩子，可能是百年难见的超级天才！"
  },
  {
    "segment_id": "0024",
    "text": "见陆离面无表情的点了点头，藤本柱更兴奋了，可随后又有些失落。"
  },
  {
    "segment_id": "0025",
    "text": "兴奋是因为他发现了一个超级天才，失落是因为他发现自己好像……教不了陆离。"
  },
  {
    "segment_id": "0026",
    "text": "是的，他得承认，恐怕他刚刚就算没有掉以轻心，和陆离同灵压切磋的话，最终输的人也还是他。"
  },
  {
    "segment_id": "0027",
    "text": "真正令他惊艳的不是陆离的第一刀，而是陆离的第二刀，那第二刀借助反震力量收刀、卸力，又在卸力过程中如引导水流般引导力量回转，最终以一个刁钻的角度重新出刀。"
  },
  {
    "segment_id": "0028",
    "text": "这种对力量的把控，精湛的技艺根本不是他能做到的，不如说，任何剑道流派都不会有这种技艺传授，这种技巧的理论或许有，但能做到的，都是万中无一的天赋者。"
  },
  {
    "segment_id": "0029",
    "text": "这就是卯之花队长看重他的原因吗……      “陆君，你先入座吧，今天要先讲一会儿理论课，然后才是对练。”"
  },
  {
    "segment_id": "0030",
    "text": "藤本树平复自己复杂的心情，课还是要上的。"
  },
  {
    "segment_id": "0031",
    "text": "陆离在诸多或吃惊或好奇或崇拜的目光中走入人群，来到蓝染身边坐下。"
  },
  {
    "segment_id": "0032",
    "text": "“陆君真的很强啊，我还从没见过能在剑道课上战胜藤本老师的人呢。”"
  },
  {
    "segment_id": "0033",
    "text": "蓝染感慨般的说道。"
  },
  {
    "segment_id": "0034",
    "text": "陆离笑问蓝染：“惣右介也做不到吗？”"
  },
  {
    "segment_id": "0035",
    "text": "蓝染的神情自然，“陆君在说什么呢，我的剑道成绩虽然不错，但也还远远不到能跟藤本老师过招的程度，以后还要请你多多指教了。”"
  },
  {
    "segment_id": "0036",
    "text": "陆离心中有些腻歪，他是不太能理解蓝染扮猪吃老虎的愉悦感的，也不知道蓝染现在隐藏实力的目的是什么，难道从这个时候就已经在谋算着要登上王座了吗？"
  },
  {
    "segment_id": "0037",
    "text": "恐怕是为了照顾说从没学过剑道的陆离，接下来的时间，藤本柱老师讲的都是一些剑道的基本知识。"
  },
  {
    "segment_id": "0038",
    "text": "陆离也没有心不在焉，而是仔细听了一遍，他发现这里所谓的剑道也不是完全没有可取之处的，弱的是藤本柱，并不是剑道。"
  },
  {
    "segment_id": "0039",
    "text": "他不禁去想，据说掌握了尸魂界所有流派的卯之花八千流的剑道会有多强，只是想想，就让他有些兴奋。"
  },
  {
    "segment_id": "0040",
    "text": "当然，他也不会作死到去挑战卯之花队长，对方和自己的灵压等级天差地别，用空间面板来说，恐怕属性差了几十乃至上百点都是有可能的。"
  },
  {
    "segment_id": "0041",
    "text": "他现在要做的是变强，然后才能挑战那些高手，享受战斗的愉悦。"
  },
  {
    "segment_id": "0042",
    "text": "如今他的主线任务第一环已经完成了，第二环任务已经派发。"
  },
  {
    "segment_id": "0043",
    "text": "【主线任务第二环：速通真央灵术院】"
  },
  {
    "segment_id": "0044",
    "text": "任务内容：探索者需在三个自然月内完成真央灵术院的所有课程，并进行跳级毕业，完成目前真央灵术院历史上未曾有人达成的最速成就。"
  },
  {
    "segment_id": "0045",
    "text": "任务难度：困难～噩梦"
  },
  {
    "segment_id": "0046",
    "text": "任务奖励：3000终焉币、浅打、回归资格"
  },
  {
    "segment_id": "0047",
    "text": "失败惩罚：抹杀"
  },
  {
    "segment_id": "0048",
    "text": "这个任务的难度上限就有点高了，陆离也是接触过游戏的，‘噩梦’两个字看上去就像是很有挑战性的。"
  },
  {
    "segment_id": "0049",
    "text": "直观分析的话，在真央灵术院他貌似不会遇到什么危险，但要是想提前毕业，多半是走不了寻常路的。"
  },
  {
    "segment_id": "0050",
    "text": "尸魂界这么大的地方，真央灵术院成立这么多年来出现的天才还少吗？既然任务描述中说这是从未有人达成的成就，那恐怕想要“极速”提前毕业没这么容易。"
  },
  {
    "segment_id": "0051",
    "text": "一般的护庭队士的确只有20等灵威那样，可这不意味着你有了20等灵威及以上的水平，就可以直接从真央灵术院毕业了。"
  },
  {
    "segment_id": "0052",
    "text": "如果一个人很天才，那么真央灵术院便会更想细心栽培，而不是拔苗助长，所以即便有哪个学员天赋很好，也会被压在学院内接受教育，让他的实力变得更强后再加入护庭十三队。"
  },
  {
    "segment_id": "0053",
    "text": "陆离看着那些已经开始对练的同学们陷入了沉思，他在想，自己要想完成这个任务，最大的阻碍究竟会是什么？"
  },
  {
    "segment_id": "0054",
    "text": "还有"
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
