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

## Chapter 0004 - Chương 4: Cổ Nguyệt Phương Nguyên!

### Summary
Chapter 4 completed via pipeline.

## Chapter 0005 - Chương 5: Nhân Tổ tam cổ, hy vọng khai khiếu

### Summary
Chapter 5 completed via pipeline.

## Chapter 0006 - 0006 未来的路，会很精彩

### Summary
Chapter 6 completed via pipeline.

## Chapter 0006 - Chương 6: Con đường tương lai sẽ rất đặc sắc

### Summary
Chapter 6 completed via pipeline.

## Chapter 0007 - Chương 7: Cổ sư chia cửu chuyển, Hoa Tửu lưu di tàng

### Summary
Chapter 7 completed via pipeline.

## Chapter 0008 - Chương 8: Vật thị nhân phi

### Summary
Chapter 8 completed via pipeline.

## Chapter 0009 - 0009 渐行渐远

### Summary
Chapter 9 completed via pipeline.

## Chapter 0010 - Chương 10: Trời có lúc gió mây bất trắc, luyện Cổ muôn vàn gian nan

### Summary
Chapter 10 completed via pipeline.


## Source Chapter 9 - 0009 渐行渐远
```json
[
  {
    "segment_id": "0001",
    "text": "# 第九节：渐行渐远"
  },
  {
    "segment_id": "0002",
    "text": "红日西沉，但还未完全落下。"
  },
  {
    "segment_id": "0003",
    "text": "天空还有着光，只是所有的事物都像是被蒙上了一层灰色。透过窗户远眺，远处的山，正渐渐地向沉重的黑色靠拢。"
  },
  {
    "segment_id": "0004",
    "text": "客厅内光线暗淡，舅父舅母高座在主位上，面目表情都笼罩着一层阴影，看不大分明。"
  },
  {
    "segment_id": "0005",
    "text": "看到方源随身带来的那两坛酒，舅父古月冻土的眉头拧成了疙瘩，他开口道：“时间一晃，你们已经十五岁了。竟然都有蛊师资质，尤其是方正，舅父舅母都替你们感到骄傲。我给你们每人六块元石，你们兄弟俩拿去。炼化蛊虫，极耗真元，这些元石你们需要。”"
  },
  {
    "segment_id": "0006",
    "text": "说着，就有奴仆过来，交给方源方正两兄弟每人一个小袋子。"
  },
  {
    "segment_id": "0007",
    "text": "方源收起袋子，沉默不语。"
  },
  {
    "segment_id": "0008",
    "text": "方正则立即展开袋口一看，只见里面装着六块椭圆的灰白色元石。顿时脸色涌现出感激之色，从座位上站起来，对舅父舅母行礼道：“谢谢舅父舅母，侄儿正需要元石来补充真元呢。你们把侄儿养这么大，养育之恩侄儿铭记在心，永生不忘！”"
  },
  {
    "segment_id": "0009",
    "text": "舅父笑着点点头。"
  },
  {
    "segment_id": "0010",
    "text": "舅母则连忙摆手，对方正温言道：“快坐下，快坐下。你们兄弟俩虽然不是我们亲生的，但我们一直都把你们当做亲生儿子抚养。你们能有出息，我们也感到骄傲。唉，我们膝下无子，有时候在想你们真能成为我们的孩子，就好了。”"
  },
  {
    "segment_id": "0011",
    "text": "这话说的大有深意，方正没听出来，方源却微微皱起眉头。"
  },
  {
    "segment_id": "0012",
    "text": "果然舅父接着就道：“我和你们舅母商量过，想把你们过继到我们家来，成为真正的一家人。方正，不知道你愿不愿意？”"
  },
  {
    "segment_id": "0013",
    "text": "方正楞了一下，但他很快脸上就涌现出欣喜之色，一口应承下来：“说实在话，自从双亲死后，侄儿就很渴望一家团圆的日子。能和舅父舅母成为一家人，这太好不过了！”"
  },
  {
    "segment_id": "0014",
    "text": "舅母神情一松，笑起来：“那你就是我们的乖儿子了，还叫舅父舅母么？”"
  },
  {
    "segment_id": "0015",
    "text": "“父亲，母亲。”方正恍然，连忙改口。"
  },
  {
    "segment_id": "0016",
    "text": "舅父舅母都哈哈一笑。"
  },
  {
    "segment_id": "0017",
    "text": "“好儿子，不枉费我们夫妻从五岁就抚养你，可养了你整整十年啊。”舅母抹着泪。"
  },
  {
    "segment_id": "0018",
    "text": "舅父则看向沉默不语的方源，温和地说着：“方源，我的意向呢？”"
  },
  {
    "segment_id": "0019",
    "text": "方源摇头不语。"
  },
  {
    "segment_id": "0020",
    "text": "“哥哥。”古月方正想劝，却被舅父阻止。"
  },
  {
    "segment_id": "0021",
    "text": "舅父语气不变，又道：“既然如此，方源侄儿，我们也不会勉强你。只是你已经十五岁了，也该独立门户，这样一来也方便继承你方家支脉。舅父这里为你准备了两百块元石，算是给你的资助。”"
  },
  {
    "segment_id": "0022",
    "text": "“两百块元石！”方正顿时瞪圆了眼睛，他从未见过这么多的元石，不禁流露出羡慕的神情。"
  },
  {
    "segment_id": "0023",
    "text": "哪知方源却仍旧摇头。"
  },
  {
    "segment_id": "0024",
    "text": "方正大惑不解，舅父的面色却微微一变，舅母的脸也阴沉下来。"
  },
  {
    "segment_id": "0025",
    "text": "“舅父舅母，若没其他事情，侄儿就先告辞了。”方源没有给他们再说话的机会，丢下这句话，拎起酒坛，直接就出了厅堂。"
  },
  {
    "segment_id": "0026",
    "text": "方正起身：“父亲，母亲，哥哥是一时想不通，不如让我来劝劝他？”"
  },
  {
    "segment_id": "0027",
    "text": "舅父摆手，故意长叹：“唉，这事不能强求，你有这个心，为父已经很欣慰了。来人，把方正少爷待下去，好生安住着。”"
  },
  {
    "segment_id": "0028",
    "text": "“那儿子告退了。”方正退下，客厅便陷入了沉寂。"
  },
  {
    "segment_id": "0029",
    "text": "太阳彻底落下山去，客厅中越加昏暗。"
  },
  {
    "segment_id": "0030",
    "text": "半晌，昏暗中传来舅父冷冷的声音：“看来方源这个小兔崽子，已经看破了我们的谋算。”"
  },
  {
    "segment_id": "0031",
    "text": "古月一族的族规中，有明文规定：十六岁的长子，有继承家产的资格。"
  },
  {
    "segment_id": "0032",
    "text": "方源的双亲，已经亡故，留下一笔不菲的遗产，都被舅父舅母“保管”着。"
  },
  {
    "segment_id": "0033",
    "text": "这笔遗产的价值，可不是区区两百块元石可比的。"
  },
  {
    "segment_id": "0034",
    "text": "若是方源也像方正一样过继给舅父舅母，那就没有资格继承这笔遗产。若是方源今年十五岁就独立门户，也不符合族中继承家产的规定。"
  },
  {
    "segment_id": "0035",
    "text": "“幸亏啊，我们笼络住了方正，而方源只有丙等资质。”舅父又叹一声，感到庆幸无比。"
  },
  {
    "segment_id": "0036",
    "text": "“那老爷，方源摆明了是要在十六岁独立出去，我们该怎么办呢？”舅母一想到那笔遗产，语气就急了。"
  },
  {
    "segment_id": "0037",
    "text": "“哼，他既然心怀不轨，也就怪不得我们了。只要我们在他独立出去之前，抓住他的大错，将他逐出家门，也就剥夺了他继承遗产的资格。”舅父冷哼道。"
  },
  {
    "segment_id": "0038",
    "text": "“可是方源这小兔崽子，聪明得很，怎么会犯错呢？”舅母不解。"
  },
  {
    "segment_id": "0039",
    "text": "舅父顿时翻了个白眼，低声呵斥：“你真是蠢笨！他不会犯错，难道我们就不能陷害么？就让沈翠那个丫头先去勾引方源，然后再大叫非礼，我们当场人赃俱获，再栽赃他个酒后乱性，丧心病狂的罪名，还怕逐不出方源？”"
  },
  {
    "segment_id": "0040",
    "text": "“老爷还是你有办法，妙计啊！”舅母顿时大喜过望。"
  },
  {
    "segment_id": "0041",
    "text": "浓郁的夜色铺盖下来，漫天的繁星被飘来的阴云遮挡住大半。山寨中各家各户渐渐亮起了灯火。"
  },
  {
    "segment_id": "0042",
    "text": "古月方正被领进一间房内。"
  },
  {
    "segment_id": "0043",
    "text": "“方正少爷，这可是老爷亲自叮嘱老奴，特意为您整理，专门腾出来的房间。”沈嬷嬷殷勤地介绍着，她弓着腰，脸上堆满了谄媚的笑容。"
  },
  {
    "segment_id": "0044",
    "text": "方正环视一周，眼睛发亮。这房间比他原先住的还要大上两倍，中央是宽大的床铺，窗台一侧是檀木书桌，摆着精致的笔墨纸砚，四周墙壁是精美的挂饰。甚至脚下也不是普通的地板，而是覆盖了一层柔软的手工地毯。"
  },
  {
    "segment_id": "0045",
    "text": "从小到大，方正还从未住过这样的房间。当即连连点头：“这很好，真是不错。谢谢沈嬷嬷了。”"
  },
  {
    "segment_id": "0046",
    "text": "这沈嬷嬷是舅母最器重的人，管理着家里上下的奴仆，是名副其实的管家。"
  },
  {
    "segment_id": "0047",
    "text": "方源的贴身丫鬟沈翠，就是她的女儿。"
  },
  {
    "segment_id": "0048",
    "text": "沈嬷嬷呵呵地笑起来：“奴婢哪里敢当得起少爷您的谢，应该的，应该的！少爷您尽管吃好睡好，想要什么就摇摇床边的铃铛，立即就会有下人上来听候吩咐。老爷吩咐了，这些日子少爷您就一门心思的修行，其他的琐事都交给我们下人们办理。”"
  },
  {
    "segment_id": "0049",
    "text": "方正心中再度涌出一股感激之情，他没有再说什么，只在心中默默下定决心：这一次一定要夺得第一，不让舅父舅母失望！"
  },
  {
    "segment_id": "0050",
    "text": "……"
  },
  {
    "segment_id": "0051",
    "text": "天空中的阴云越来越重，夜色也因此越发深沉。夜空中的星辰几乎都被云翳遮蔽，只余下几颗闪着微弱的光芒，在天空中挣扎着。"
  },
  {
    "segment_id": "0052",
    "text": "“舅父舅母应该在合计着，怎么将我逐出家门吧。前世是暗中唆使下人挑衅我，然后栽赃我，最后把我逐出家门，不知道这一世会有什么变化。”方源走在街道上，心中冷笑不止。"
  },
  {
    "segment_id": "0053",
    "text": "对于舅父舅母的真面目，他早就看清了。"
  },
  {
    "segment_id": "0054",
    "text": "不过也能理解。"
  },
  {
    "segment_id": "0055",
    "text": "人为财死鸟为食亡，不管是地球还是这个世界上，总有那么多的人为了利益而践踏亲情、友情、爱情。"
  },
  {
    "segment_id": "0056",
    "text": "事实上，亲情根本就没有。当初舅父舅母收养方源方正，根本目的就是贪图遗产。只是方源方正两兄弟频频让他们意外。"
  },
  {
    "segment_id": "0057",
    "text": "“万事开头难，对我而言，更是如此。我一没有过人资质，二没有师长关照，等于是白手起家。双亲的遗产，可以说是我的一个大跳板。前世遗产被舅父舅母夺去，害得自己整整耗费了两年，才修行到一转巅峰。这一世，这个错误不能再犯了。”"
  },
  {
    "segment_id": "0058",
    "text": "方源就这样一边走，一边思考着。"
  },
  {
    "segment_id": "0059",
    "text": "他没有在居所待着，而是提着两坛酒，方向直指寨外。"
  },
  {
    "segment_id": "0060",
    "text": "夜空越来越阴沉，乌云遮蔽了星光，山风呼呼的吹着，有渐渐增强的趋势。"
  },
  {
    "segment_id": "0061",
    "text": "山雨欲来啊。"
  },
  {
    "segment_id": "0062",
    "text": "不过还是要探索。双亲遗产要夺回来，那也得等到他明年十六岁。而花酒行者遗藏，才是近期就可能得手的东西。"
  },
  {
    "segment_id": "0063",
    "text": "街道上，行人很少。路边房屋中透出昏暗的光，一些琐碎的生活垃圾，以及树叶尘土，被风卷吹，随意飘零。"
  },
  {
    "segment_id": "0064",
    "text": "方源单薄的衣服，有些挡不住这山风，不由地感到一阵冷意。"
  },
  {
    "segment_id": "0065",
    "text": "他索性将拎着的酒坛打开，小小的喝了一口。虽是浊酒，但是咽下去后，就有一股暖意升腾上来。"
  },
  {
    "segment_id": "0066",
    "text": "这还是他这些天，第一次真的饮酒。"
  },
  {
    "segment_id": "0067",
    "text": "越要出山寨，路边的房屋就越稀疏，灯火就越昏暗。"
  },
  {
    "segment_id": "0068",
    "text": "前方，更是黑暗重重。风吹压着山林，夜色中树枝摇曳，呼呼作响，像是群兽在咆哮。"
  },
  {
    "segment_id": "0069",
    "text": "方源的步伐没有半点迟疑，出了山寨大门，在黑暗的路中渐行渐远。"
  },
  {
    "segment_id": "0070",
    "text": "而在他的背后，是明媚辉煌的万家灯火。"
  },
  {
    "segment_id": "0071",
    "text": "在这灯火中，有个温暖的角落。"
  },
  {
    "segment_id": "0072",
    "text": "弟弟古月方正坐在书桌前，温习着课上记下的笔记。房屋中灯火明亮，坚实的墙壁阻挡了冷风，在他的手边摆着一杯温热的参茶，热气袅袅地升腾着。"
  },
  {
    "segment_id": "0073",
    "text": "“方正少爷，洗澡的热水已经为您准备好了。”门外，沈翠的声音轻轻传来。"
  },
  {
    "segment_id": "0074",
    "text": "方正心中一动：“那就拿进来吧。”"
  },
  {
    "segment_id": "0075",
    "text": "沈翠带着一脸的媚意，扭着腰走进了房间。"
  },
  {
    "segment_id": "0076",
    "text": "“奴婢见过方正少爷。”她满眼秋波地向方正望过去。方源只是个丙等，方正可是甲等资质。能攀上他，才是真正的大富贵！"
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
