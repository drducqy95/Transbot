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

## Chapter 0009 - Chương 9: Đè Yoruichi xuống đất ma sát

### Summary
Chapter 9 completed via pipeline.


## Source Chapter 10 - 0010 大鬼道长
```json
[
  {
    "segment_id": "0001",
    "text": "# 第10章 大鬼道长"
  },
  {
    "segment_id": "0002",
    "text": "“妙啊！”"
  },
  {
    "segment_id": "0003",
    "text": "就连观战的老师也惊叹出声，因为夜一的应对方式堪称完美，在被压到地板上的时候，她现在唯一能翻盘的就是寝技，而她居然真的能找到那微小的空隙！"
  },
  {
    "segment_id": "0004",
    "text": "夜一的速度极快，双腿发力间紧紧的夹住陆离，随后如同柔软的藤蔓一样缠了上去。"
  },
  {
    "segment_id": "0005",
    "text": "陆离眼神一凌，他没有大意，但夜一的这一招确实是抓到了他的破绽，在所有的格斗对手中，他认为最难缠的就是擅长寝技的敌人。"
  },
  {
    "segment_id": "0006",
    "text": "他在原本的世界中战胜过几位此道高手，但他不认为是寝技不行，而是因为他的力量远超对方，以力破巧获得了胜利。"
  },
  {
    "segment_id": "0007",
    "text": "而现在的情况不一样，夜一的灵体力量此时和自己差不多，而原本她还会更强，自己毫无以前力大砖飞的优势，若是被缠上锁住，输的人就是自己了。"
  },
  {
    "segment_id": "0008",
    "text": "刹那间，仿佛是本能，陆离猛地起跳后空翻，让已经缠向他脖颈的那双长腿动作一滞，而情况便再次翻转了。"
  },
  {
    "segment_id": "0009",
    "text": "若夜一不调整身形，她的脑袋会率先砸在地板上，可若是她要调整身形，她的腿就锁不住陆离。"
  },
  {
    "segment_id": "0010",
    "text": "只是一瞬的犹豫，便决定了胜负。"
  },
  {
    "segment_id": "0011",
    "text": "任谁也没有想到，陆离在半空中探手撑地，并未有夜一预想中的撞击，在她调整身形的时候陆离变招了，他腰身发力将夜一甩了出去。"
  },
  {
    "segment_id": "0012",
    "text": "夜一还未起身，一击冲拳便已经停在了她的面庞前，劲风吹起她的发梢，额前的汗珠滑落在橙色的瞳孔内，那双眸子中的惊异还未褪去。"
  },
  {
    "segment_id": "0013",
    "text": "陆离自半屈膝状态缓缓起身，“承让。”"
  },
  {
    "segment_id": "0014",
    "text": "最后关头收力并非是他怜香惜玉，只是他想起了和藤本老师切磋的事，这一拳要真砸下去，受伤的恐怕不会是夜一，而是他自己。"
  },
  {
    "segment_id": "0015",
    "text": "道场内安静的可怕，过了几息，才有一阵阵倒吸凉气的声音响起。"
  },
  {
    "segment_id": "0016",
    "text": "“女魔头居然输了！？”"
  },
  {
    "segment_id": "0017",
    "text": "“四枫院家的白打……居然输给了一个插班生？”"
  },
  {
    "segment_id": "0018",
    "text": "“夜一不是四枫院家的天才吗？她怎么可能会输……”"
  },
  {
    "segment_id": "0019",
    "text": "“我记得……夜一还在白打切磋中赢过老师吧？”"
  },
  {
    "segment_id": "0020",
    "text": "“……”"
  },
  {
    "segment_id": "0021",
    "text": "在轰动的人群中，蓝染面无表情的站在那，但他的内心远不如表面那般平静，一双眸子紧紧的跟随陆离的背影。"
  },
  {
    "segment_id": "0022",
    "text": "居然能胜过四枫院夜一……连白打，也这么强悍吗？"
  },
  {
    "segment_id": "0023",
    "text": "到底还有什么，是你不擅长的？"
  },
  {
    "segment_id": "0024",
    "text": "“你真的没学过白打？”"
  },
  {
    "segment_id": "0025",
    "text": "夜一起身后神情复杂的看向陆离，通过周遭人的对话，她大概知道了陆离的情况，对方之前只是一个流魂街的流民啊。"
  },
  {
    "segment_id": "0026",
    "text": "“在流魂街没人会教我白打，我不过是自己琢磨出来了些拳脚功夫罢了。”"
  },
  {
    "segment_id": "0027",
    "text": "陆离解释道，他当然不能暴露自己异世界人的身份，所以也只能含糊过去。"
  },
  {
    "segment_id": "0028",
    "text": "而他若是想要提前毕业，就不可能像蓝染那样扮猪吃老虎隐藏实力，他必须全力的发光发热，才能达成提前毕业的成就。"
  },
  {
    "segment_id": "0029",
    "text": "“哼，你别得意，刚刚是我开始有点大意了，下次我一定赢你！”"
  },
  {
    "segment_id": "0030",
    "text": "夜一冷哼一声说道，似乎不太信陆离的说辞，在她看来，陆离的战斗方式尽管看起来很狂暴，像是在凭借战斗本能打，但其实是有章法的，对方绝对接受过系统性的训练。"
  },
  {
    "segment_id": "0031",
    "text": "看着夜一的神态，陆离觉得有些好笑，没想到原著中成熟撩人的夜一也有这样的少女时代，就像是孩子一样，“等你赢了我再说吧。”"
  },
  {
    "segment_id": "0032",
    "text": "说着他走向蓝染，“惣右介，咱们练练？”"
  },
  {
    "segment_id": "0033",
    "text": "夜一看着陆离的背影，气的牙痒痒，她开局的确是大意了，但她也不敢说一开始就拿出全力就能稳赢陆离，这个插班生的确是个白打高手。"
  },
  {
    "segment_id": "0034",
    "text": "从小到大她在白打领域就没输给过任何人，不行，她一定要赢，不是为了四枫院家的荣誉，她只是咽不下这口恶气。"
  },
  {
    "segment_id": "0035",
    "text": "想起陆离那朝着下三路的腿法，她就气的牙痒痒，发誓下次一定要踢爆对方的卵蛋！"
  },
  {
    "segment_id": "0036",
    "text": "正跟蓝染对练的陆离忽然感到一阵恶寒，以至于动作都慢了半分，被蓝染漫不经心的拳头打到了胸口。      蓝染也是有些奇怪的看了一眼陆离，心想陆君难道在照顾我面子，放水了？"
  },
  {
    "segment_id": "0037",
    "text": "后半堂课陆离都是在和蓝染对练，而蓝染也虚心向陆离请教了不少白打方面的问题。"
  },
  {
    "segment_id": "0038",
    "text": "当然，陆离根本不会这个世界的白打，但他教了蓝染一些他理解中的实用格斗技巧，只是在对练中蓝染表现一般，陆离也不好判断对方究竟有没有学会。"
  },
  {
    "segment_id": "0039",
    "text": "陆离好几次都差点忍不住问蓝染你这样伪装到底累不累啊，能不能好好打？"
  },
  {
    "segment_id": "0040",
    "text": "“陆君或许会是个好老师呢，这堂课我获益匪浅。”"
  },
  {
    "segment_id": "0041",
    "text": "下课后蓝染夸赞道，他的确有不少收获，只是没有在切磋中表现出来。"
  },
  {
    "segment_id": "0042",
    "text": "陆离的那种天马行空的战斗思路，他感觉很有必要学习一番，或许将来对自己的事业会有大用。"
  },
  {
    "segment_id": "0043",
    "text": "“对了，陆君，你以前接触过鬼道吗？”"
  },
  {
    "segment_id": "0044",
    "text": "蓝染问道，下一堂课是鬼道课。"
  },
  {
    "segment_id": "0045",
    "text": "…………"
  },
  {
    "segment_id": "0046",
    "text": "陆离看着眼前十分高大，戴反光眼镜，有着奇怪牛角发型、穿着深蓝色长袍的中年男子，感觉这个世界还真是奇妙。"
  },
  {
    "segment_id": "0047",
    "text": "好家伙，这不是大鬼道长握菱铁斋吗，这个时候居然还在真央灵术院教课吗？"
  },
  {
    "segment_id": "0048",
    "text": "“陆君，这堂课你可不能走神，握菱老师可是大鬼道长，每年只在学院带一个月课的。”"
  },
  {
    "segment_id": "0049",
    "text": "蓝染提醒道。"
  },
  {
    "segment_id": "0050",
    "text": "陆离听了心中直呼好家伙，没想到这位后世在浦原店长那打工的大叔居然这么早就是大鬼道长了。"
  },
  {
    "segment_id": "0051",
    "text": "看在场的学员崇敬的态度就知道，一个个都挺直腰板聚精会神的，生怕错过了什么‘鬼道真理’，就可以看出握菱铁斋在众人心中的地位了。"
  },
  {
    "segment_id": "0052",
    "text": "“听说今天来了位插班生，我先简单讲一下鬼道的基本原理，已经听过的同学也不必失望，因为真理往往就蕴含在基础之中……”"
  },
  {
    "segment_id": "0053",
    "text": "握菱铁斋在讲话时目光在陆离身上停顿过一瞬，显然陆离虽然才是第一天入学，但已经是学院内的风云人物了，他也有所耳闻。"
  },
  {
    "segment_id": "0054",
    "text": "其他同学倒也没有不耐烦的，认真听握菱铁斋讲着基础。"
  },
  {
    "segment_id": "0055",
    "text": "陆离也是听得津津有味，毕竟这还是初次接触“超自然”能力，他虽然是武道的狂热者，但对死神世界内的鬼道能力也不是毫无兴趣，若是鬼道运用的好，或许会对战斗有奇效。"
  },
  {
    "segment_id": "0056",
    "text": "这位装扮奇特的大叔讲课意外的有一套，深入浅出下，陆离很快就理解了什么是鬼道。"
  },
  {
    "segment_id": "0057",
    "text": "首先鬼道分为破道、缚道和回道三种。"
  },
  {
    "segment_id": "0058",
    "text": "简单来说，通过吟唱这一举动来操控体内的灵力，进而构成各种各样的鬼道。"
  },
  {
    "segment_id": "0059",
    "text": "吟唱并非是释放鬼道的必要条件，吟唱最大的作用就像是构建一个模具，可以协助死神为鬼道‘塑形’，如果对某一鬼道非常熟练，也就可以破弃吟唱，实现瞬发的效果。"
  },
  {
    "segment_id": "0060",
    "text": "只不过一般的死神没那么高的灵力操控天赋，多半是没法瞬发鬼道的，优秀一些的也只能破弃吟唱一些低级的鬼道，只有在鬼道方面天赋很变态的人才能破弃吟唱释放高级鬼道。"
  },
  {
    "segment_id": "0061",
    "text": "嗯，就比如他身边的这位看似人畜无害的蓝染惣右介同学。"
  },
  {
    "segment_id": "0062",
    "text": "“蓝染同学，你好像和新同学关系比较好，就由你来指导他进行低阶鬼道的释放吧。”"
  },
  {
    "segment_id": "0063",
    "text": "课程进行的差不多时，握菱铁斋在台上开口，指名了蓝染。"
  },
  {
    "segment_id": "0064",
    "text": "蓝染似乎并不意外，他的确在所有的课程中都藏拙了，但即便如此，他的鬼道成绩也名列前茅。"
  },
  {
    "segment_id": "0065",
    "text": "而他也十分好奇，陆离的鬼道天赋究竟如何，这次他可以亲手测试一番。"
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
