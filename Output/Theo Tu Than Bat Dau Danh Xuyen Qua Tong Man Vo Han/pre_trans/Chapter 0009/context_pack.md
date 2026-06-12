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

## Chapter 0007 - Chương 7: Kiếm đạo? Ta chưa từng học nha

### Summary
Chapter 7 completed via pipeline.

## Chapter 0008 - Chương 8: Bạch Đả, Yoruichi (Ba canh cầu phiếu)

### Summary
Chapter 8 completed via pipeline.


## Source Chapter 9 - 0009 把夜一按在地上摩擦
```json
[
  {
    "segment_id": "0001",
    "text": "# 第9章 把夜一按在地上摩擦"
  },
  {
    "segment_id": "0002",
    "text": "作为一个老师他当然不喜欢有人在他的课上睡觉，但这个问题少女在白打上的天赋简直堪称妖孽，他确实没什么能教对方的了。"
  },
  {
    "segment_id": "0003",
    "text": "他知道上午的剑道课中，陆离击败了藤本老师，就是不清楚陆离白打的水平如何。"
  },
  {
    "segment_id": "0004",
    "text": "不亲自出手教陆离并非是他不喜欢这个新生或是有轻视，而是他在心里得承认，四枫院家的这个孩子，在白打的造诣上比自己更高。"
  },
  {
    "segment_id": "0005",
    "text": "“哦？新生啊……”"
  },
  {
    "segment_id": "0006",
    "text": "夜一顺着众人的目光转身，看向陆离，擦去嘴角午睡的痕迹后，露出了小恶魔一般的表情，让周围的几名学员不禁躲得远远的。"
  },
  {
    "segment_id": "0007",
    "text": "一年级的学生都知道，这个贵族家的大小姐简直就是混世小魔女，就没有她不敢干的事，而在白打课上，在场的所有人，包括蓝染都被她揍过。"
  },
  {
    "segment_id": "0008",
    "text": "“陆君，她是四枫院家的人，白打说是学员中最强也不为过，你要小心点。”"
  },
  {
    "segment_id": "0009",
    "text": "蓝染提醒道，但他嘴角的笑容却暴露了些许内心的想法，他觉得眼前的局面很有趣。"
  },
  {
    "segment_id": "0010",
    "text": "是的，他也被夜一揍过，而且他得承认，在不仗着灵压欺人的情况下，纯靠白打，就算他使出全力，如今也还不是夜一的对手。"
  },
  {
    "segment_id": "0011",
    "text": "那么陆君，你还能带给我更多惊喜吗？"
  },
  {
    "segment_id": "0012",
    "text": "“最强？”"
  },
  {
    "segment_id": "0013",
    "text": "陆离和夜一对视时微微侧了侧头，咧嘴露出一口森白的牙齿，“所谓白打，我可以理解为不用兵器的无限制搏杀吧？”"
  },
  {
    "segment_id": "0014",
    "text": "“你这么说也没错。”"
  },
  {
    "segment_id": "0015",
    "text": "回话的是这堂课的老师。"
  },
  {
    "segment_id": "0016",
    "text": "而夜一见陆离毫不畏惧，也感觉颇为有趣，迈步朝陆离走近，“怎么，你很擅长拳脚吗？”"
  },
  {
    "segment_id": "0017",
    "text": "仿佛有火花在空气中碰撞，原本站在夜一和陆离之间的学员们都向两侧退去，大多眼中带着看热闹的亢奋。"
  },
  {
    "segment_id": "0018",
    "text": "陆离活动了下躯体，骨骼发出一阵爆响声，“很擅长不敢当，只能说是略知一二。”"
  },
  {
    "segment_id": "0019",
    "text": "他当然有练过拳脚，不如说师父收集的古籍中一切的格斗技巧他都有学过，只可惜他所在的那个世界武学失传了太多，所以他认为从广义角度来说，算上他们世界被埋没的武学历史的话，他的确只能算得上是略知一二。"
  },
  {
    "segment_id": "0020",
    "text": "“哈哈，你真有意思，看你的站姿、架势就知道，你是白打的高手，却只说自己是略知一二吗？”"
  },
  {
    "segment_id": "0021",
    "text": "夜一笑着说道，眼睛笑着笑着就眯了起来，“你这么自谦，可是会让姐姐想要欺负你一下呢。”"
  },
  {
    "segment_id": "0022",
    "text": "“你看起来比我要小。”"
  },
  {
    "segment_id": "0023",
    "text": "陆离笑着说，这是实话，夜一和蓝染应该都是尸魂界内出生的，他们会在这个世界自然生长，此时的蓝染看上去接近青年，而夜一像是十六岁少女那样。"
  },
  {
    "segment_id": "0024",
    "text": "顶着这样的面孔，即便她的胸前再波涛汹涌，自称姐姐也总让人感觉奇怪，或许这个学院内的混世小魔女天生有一颗御姐心吧。"
  },
  {
    "segment_id": "0025",
    "text": "“呵，等下我就打的你喊姐。”"
  },
  {
    "segment_id": "0026",
    "text": "夜一冷笑一声，左右手互相活动着手腕，她和平常学员不同，并非穿着宽大的道服，而是量身定做了颜色风格和校服相近的白色紧身衣，手腕上方还缠着布条，给人一种干练的感觉。"
  },
  {
    "segment_id": "0027",
    "text": "腰间一条束带，将她的小蛮腰收紧，贴身的衣物让在其行走中隐约可见那健康的马甲线，她毫不在乎的展示着她的身材，展示着她的灵体爆发力。"
  },
  {
    "segment_id": "0028",
    "text": "“四枫院同学，记得控制自己的灵威，要和陆同学一样，是十七等。”"
  },
  {
    "segment_id": "0029",
    "text": "老师提醒道，他倒不是想要看什么公平的决斗，而是怕夜一这小魔女失手直接把陆离打死了……"
  },
  {
    "segment_id": "0030",
    "text": "“呦，十七等，不赖嘛。”      夜一说道，像是在称赞，但语气很微妙。"
  },
  {
    "segment_id": "0031",
    "text": "作为四枫院家的传人，她当然从小就有着最好的资源，在入学时就已经有九等灵威了，这还是因为她不怎么喜欢关于灵压的修行，更喜欢练习白打的缘故。"
  },
  {
    "segment_id": "0032",
    "text": "入学时有十七等灵威不算什么，她只对陆离的白打水平感兴趣。"
  },
  {
    "segment_id": "0033",
    "text": "她控制好自己的灵威，然后朝陆离勾了勾手指，“上吧。”"
  },
  {
    "segment_id": "0034",
    "text": "陆离并不因为对方的挑衅而动怒，只是抱拳行了一礼，“请赐教。”"
  },
  {
    "segment_id": "0035",
    "text": "在夜一和其他同学古怪的目光中，陆离动了，势如奔雷！"
  },
  {
    "segment_id": "0036",
    "text": "数米距离在他脚下掠过，一记冲拳直击夜一面门，快、狠、准！"
  },
  {
    "segment_id": "0037",
    "text": "夜一在瞬间就收起了轻视之心，连忙双臂回防挡在了面门前。"
  },
  {
    "segment_id": "0038",
    "text": "在那一拳落下后，她身形借力后撤，可陆离就像是紧咬猎物喉咙的恶狼一般欺身而上，第二拳击向她的小腹。"
  },
  {
    "segment_id": "0039",
    "text": "夜一不愧是四枫院家千年一出的白打天才，她霎时间就做出了判断，借助身躯柔软的优势上半身极速向后翻去，让陆离的那一拳只是擦着她的紧身衣过去，并未造成伤害。"
  },
  {
    "segment_id": "0040",
    "text": "紧接着，她单手支撑地板，一腿横扫而出，要抓住陆离进攻后下盘不稳的机会将陆离扫倒。"
  },
  {
    "segment_id": "0041",
    "text": "可陆离就像是已经预判了她的动作一般提前起跳了，更让夜一讶异的是，陆离跳的不高，只是堪堪躲过她那一腿的高度，在和夜一的长腿错过后，他起跳时就抬起的右脚迅速的下劈，直指夜一的下阴。"
  },
  {
    "segment_id": "0042",
    "text": "夜一有些狼狈的翻滚躲开，羞恼中又有些后怕，她想要反攻，但已经在战斗初期被压制，现在陆离根本就不给她起身的机会。"
  },
  {
    "segment_id": "0043",
    "text": "此时周围观战的同学都已经看呆了，说时迟那时快，转眼间陆离和夜一便已经过了许多招，而他们心中白打无敌的夜一居然正被陆离这个插班新生按在地上摩擦！"
  },
  {
    "segment_id": "0044",
    "text": "陆离不觉得在战斗中朝下三路去有什么不对的，武术是杀人技，战斗中对敌人的怜悯就是对自己的残忍。"
  },
  {
    "segment_id": "0045",
    "text": "尽管只是切磋，面对夜一这样的高手他也不准备放水，何况有藤本柱前车之鉴，真到了能伤到夜一的时候，对方的灵威恐怕就压不住了，自己其实根本破不了夜一的防。"
  },
  {
    "segment_id": "0046",
    "text": "夜一可是五大贵族之一的四枫院家的继承人，她现在的灵威等级恐怕在十等以上，简单来说，就算她不用灵压攻击自己，她自身的‘灵魂密度’也是远高于自己的。"
  },
  {
    "segment_id": "0047",
    "text": "从属性点方面换算，夜一的肉身远比自己抗打，他若是再不进攻夜一的要害，那还怎么赢？"
  },
  {
    "segment_id": "0048",
    "text": "是的，陆离喜欢战斗，但他讨厌输。"
  },
  {
    "segment_id": "0049",
    "text": "就算是对方的真实综合实力要远高于他，在武学的领域，他也不想败北。"
  },
  {
    "segment_id": "0050",
    "text": "轰——"
  },
  {
    "segment_id": "0051",
    "text": "又是一记势大力沉的下劈，他的右腿如同战斧一般落在夜一双腿之间。"
  },
  {
    "segment_id": "0052",
    "text": "得说夜一不愧是白打天才，尽管开局不利落入下风，但每次陆离的“致命攻击”她都躲开了。"
  },
  {
    "segment_id": "0053",
    "text": "可夜一夜明白久守必失的道理，尤其是面对陆离这样的白打高手，若是不能找到翻盘点，那她被击中要害败北也只是时间问题。"
  },
  {
    "segment_id": "0054",
    "text": "剧烈的运动让她额头布满了细密的汗珠，而她也在大脑中飞速思考破局的方式。"
  },
  {
    "segment_id": "0055",
    "text": "久违的，四枫院家的白打天才认真了起来，时间在夜一眼中都仿佛变慢了。"
  },
  {
    "segment_id": "0056",
    "text": "终于，她抓到了一丝机会，在陆离那一脚落空后，猛然腰身发力，一双长腿如同水蛇一般缠了上去。"
  },
  {
    "segment_id": "0057",
    "text": "感谢Grand、BB打赏的3000点币，感谢黄不谷打赏的1000点币，浅梦U墨溪打赏的600点币，感谢武祖顾少伤打赏的500点币，感谢掉在盐里的愚者打赏的500点币，感谢大侦探皮卡丘打赏的100点币"
  }
]
```

## Output Format
CRITICAL INSTRUCTION: You MUST translate the source text EXACTLY paragraph by paragraph, preserving the original order perfectly. DO NOT skip, drop, merge, or reorder any paragraphs. Each paragraph in the source MUST be translated.
Return ONLY valid JSON matching this schema:
{
  "chapter_number": 9,
  "chapter_title_vi": "Chương 9: <Vietnamese title>",
  "segments": [
    {
      "segment_id": "XXXX",
      "source": "...",
      "target": "..."
    }
  ]
}
