# Translation Context Pack

## Project
- Branch: Tieu Dao Mong Duong
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

## Chapter 0001 - Chương 1: Phương Nguyên

### Summary
Chapter 1 completed via pipeline.

## Chapter 0002 - Chương 2: Thuộc Tính

### Summary
Chapter 2 completed via pipeline.

## Chapter 0001 - Chương 1: Phương Nguyên

### Summary
Chapter 1 completed via pipeline.

## Chapter 0002 - Chương 2: Thuộc Tính

### Summary
Chapter 2 completed via pipeline.

## Chapter 0003 - Chương 3: Linh Trà

### Summary
Chapter 3 completed via pipeline.


## Source Chapter 4 - 0004 问心（求收藏）
```json
[
  {
    "segment_id": "0001",
    "text": "# 第4章 问心（求收藏）"
  },
  {
    "segment_id": "0002",
    "text": "“这问心茶，纵然冲泡饮用，也有不可思议的效果，但似乎只有与坐忘茶道结合，才有增长神元的奇效！”"
  },
  {
    "segment_id": "0003",
    "text": "方元端坐在桌前，望着其上小半斤不到的茶叶，陷入了沉吟中。"
  },
  {
    "segment_id": "0004",
    "text": "收获这些之后，他按照梦中的习惯，对茶叶实验了几次。"
  },
  {
    "segment_id": "0005",
    "text": "首先，就是直接冲泡，没有坐忘茶道一系列正心诚意、收敛心神的功课，结果味道冲击犹在，并且也有一定洗涤心灵的效果，但那种增长神元的奇效却消失了。"
  },
  {
    "segment_id": "0006",
    "text": "这越发令他觉得，自己的师父问心居士，必然是一位奇人。"
  },
  {
    "segment_id": "0007",
    "text": "而第二点，就更加令方元惋惜了。"
  },
  {
    "segment_id": "0008",
    "text": "“这问心茶，第一次饮用效果最好，其后功效递减……应该有着一个极限，难道是耐受性的问题？”"
  },
  {
    "segment_id": "0009",
    "text": "方元习惯性地将这些记录下来。"
  },
  {
    "segment_id": "0010",
    "text": "通过实验，标准化，数据化，形成日后查验的依据，这也是他从另外一个梦中人生学习到的经验。"
  },
  {
    "segment_id": "0011",
    "text": "纵然只有十八岁，但在那个梦中，他却仿佛经历了一生。"
  },
  {
    "segment_id": "0012",
    "text": "可惜，自从成人之后，那个梦境就消失不见了。"
  },
  {
    "segment_id": "0013",
    "text": "“得此灵物，就已经是侥天之幸，我又有着什么不满足的呢？”"
  },
  {
    "segment_id": "0014",
    "text": "方元安慰着自己，又开始每天的巡视功课。"
  },
  {
    "segment_id": "0015",
    "text": "“嗯，那株问心茶树应该怎么办？移植么？”"
  },
  {
    "segment_id": "0016",
    "text": "他一边走着，眉头一边微微皱起。"
  },
  {
    "segment_id": "0017",
    "text": "幽谷后面的种植园虽然隐蔽，却并非万无一失，纵然通过林员外的关系，方元拿到了幽谷连带附近十里的地契，奈何灵物的诱惑实在太大，他可不想将自己的安全寄托在别人的一念之间。"
  },
  {
    "segment_id": "0018",
    "text": "那株问心茶树的异变实在太过显眼，若被发现，必然引来觊觎，因此还是要转移。"
  },
  {
    "segment_id": "0019",
    "text": "倒是那些红玉稻种，因为是最低级的灵物，来历又较为清白，反倒没有多少可担忧的。"
  },
  {
    "segment_id": "0020",
    "text": "“不知道灵米吃起来，又是何种滋味？”"
  },
  {
    "segment_id": "0021",
    "text": "方元摸了摸下巴，感觉有些迫不及待，来到红玉稻田一看，顿时惊喜交加。"
  },
  {
    "segment_id": "0022",
    "text": "在他面前，一株株火红色的秧苗破土而出，宛若小荷才露尖尖角一般，带着勃勃的生机。"
  },
  {
    "segment_id": "0023",
    "text": "“真的发芽了？”"
  },
  {
    "segment_id": "0024",
    "text": "方元大喜。"
  },
  {
    "segment_id": "0025",
    "text": "毕竟，从问心居士的教导中，他知晓灵种仙种对福地的依赖很大。"
  },
  {
    "segment_id": "0026",
    "text": "其它地方，也只有地气肥沃到极点，钟灵疏秀之处，才勉强有着三分指望，并且能培植的也是最低级的货色。"
  },
  {
    "segment_id": "0027",
    "text": "红玉稻再不堪，那也是灵物！"
  },
  {
    "segment_id": "0028",
    "text": "想不到真的可以被自己培植出来，若能推广开，恐怕归灵宗都没有自己富裕吧？"
  },
  {
    "segment_id": "0029",
    "text": "‘那个什么归灵宗，自以为了不起，但能天天吃灵米么？我就可以！’"
  },
  {
    "segment_id": "0030",
    "text": "方元嘴角带起一丝弧度，眼角余光一瞥，突然间又叫一声糟糕，跑到稻田边缘。"
  },
  {
    "segment_id": "0031",
    "text": "“这……”"
  },
  {
    "segment_id": "0032",
    "text": "他看着眼前一幕，神情略微有些呆滞。"
  },
  {
    "segment_id": "0033",
    "text": "就见在欣欣向荣的稻田边缘处，原本接壤的一块蓝星草坪，茎叶边缘泛黄，部分叶片呈现出枯萎状态，仿佛一下被夺走了生机。"
  },
  {
    "segment_id": "0034",
    "text": "还有黄果树，葛粉藤……只要靠近红玉稻田的，都摆脱不了这个下场。"
  },
  {
    "segment_id": "0035",
    "text": "“不会吧……我为了灵种，种在边上的植株，都是比较易活，还有肥地功效的啊……”"
  },
  {
    "segment_id": "0036",
    "text": "方元看着这一幕，突然若有所悟：“这灵种实在霸道，竟然还能掠夺同类精气……不对，是因为我这里并非灵地福地，它要生长，必须如此！”"
  },
  {
    "segment_id": "0037",
    "text": "一想到这里，方元顿时心急火燎地跑到茶园当中，细细查看问心茶周围。"
  },
  {
    "segment_id": "0038",
    "text": "果然，这株灵植虽然越发生机盎然，但周围的茶树，却是不约而同地出现了萎靡的情况。"
  },
  {
    "segment_id": "0039",
    "text": "“看来……日后培育灵种，要么必须单独种植，要么就必须地力跟上，否则对周围影响实在太大了……”"
  },
  {
    "segment_id": "0040",
    "text": "方元咬着嘴唇：“目前的应急之法也有，左右不过地力不足，营养跟不上，一是加大施肥，还火液一日三次，周围最好再堆些火肥……一些材料有着缺口，正好找田老汉换取！”"
  },
  {
    "segment_id": "0041",
    "text": "田老汉是外界药堂之人，负责收购药材，有时候也亲自入山采药。"
  },
  {
    "segment_id": "0042",
    "text": "有一次被毒蛇咬伤，刚巧被问心居士救下，结下缘分，时常带进来些生活物资，与师徒二人交换药材。"
  },
  {
    "segment_id": "0043",
    "text": "据问心居士所言，这老汉给的价格还算公道，是个实在人，方元也就一直保持着来往。"
  },
  {
    "segment_id": "0044",
    "text": "反正他自己心里清楚，最近几次交易，自己培育的都是品质上乘，药效颇佳的好货，对方应该赚了不少才是。"
  },
  {
    "segment_id": "0045",
    "text": "“小居士！小居士！”"
  },
  {
    "segment_id": "0046",
    "text": "正想着，外面田老汉的声音就飘了进来：“老汉又来了。”"
  },
  {
    "segment_id": "0047",
    "text": "“是田老啊，请进！”"
  },
  {
    "segment_id": "0048",
    "text": "方元来到谷外，笑着将田老汉请入精舍。"
  },
  {
    "segment_id": "0049",
    "text": "这田老汉手长脚长，尖嘴猴腮，仿佛一只大猿猴一般，眼睛里面带着一股山民特有的狡黠之气，背了一个大竹篓进来，气喘吁吁地放下，又搓着双手，赔笑道：“小居士你看看，上次要的东西，都在这里了……”"
  },
  {
    "segment_id": "0050",
    "text": "“嗯，田老辛苦了！”"
  },
  {
    "segment_id": "0051",
    "text": "这山路不近，普通人攀越起来都比较艰难，更别提带着这么多负担了。"
  },
  {
    "segment_id": "0052",
    "text": "“上次的黄果已熟，您等等，我去取！”"
  },
  {
    "segment_id": "0053",
    "text": "方元微笑道。"
  },
  {
    "segment_id": "0054",
    "text": "“唉……”"
  },
  {
    "segment_id": "0055",
    "text": "原本应该笑容满面的田老汉，此时脸上却是带着一丝踌躇之色，蓦然咬了咬牙齿：“这个……小居士，还有一件事老汉要告诉你，这交易，是最后一次了！”"
  },
  {
    "segment_id": "0056",
    "text": "“哦？”"
  },
  {
    "segment_id": "0057",
    "text": "方元眉毛轻轻一挑：“可是田老对上次药材不满意？还是嫌价格太高？这些都可以商量的？”"
  },
  {
    "segment_id": "0058",
    "text": "“不不！问心居士培育的药材那是一等一，小居士你的更不用说，纵然深山老林里面的野生草药，药性都没有你的浓郁，只是……”"
  },
  {
    "segment_id": "0059",
    "text": "田老汉双手乱摇：“总之不成了！”"
  },
  {
    "segment_id": "0060",
    "text": "“好！”"
  },
  {
    "segment_id": "0061",
    "text": "方元试探了一句，心里已经有了点底，又笑道：“既然如此，那至少这次还得钱货两清不是？田老请稍等，如今天色不早，吃过饭，喝完茶再走如何？”"
  },
  {
    "segment_id": "0062",
    "text": "“吃饭？！”"
  },
  {
    "segment_id": "0063",
    "text": "田老汉咽了口唾沫，仿佛又回忆起上次玉晶米的美味，脸上踌躇之意一闪，最终还是被馋虫压倒，嘴上说着：“小居士能舍两个饭团子给老汉，就已经心满意足了……”"
  },
  {
    "segment_id": "0064",
    "text": "双脚却是立地生根，再也不动了。"
  },
  {
    "segment_id": "0065",
    "text": "方元见此，顿时心里暗笑。"
  },
  {
    "segment_id": "0066",
    "text": "玉晶米本来在外界也是小富之家才能吃得起的上佳良种，何况他所培植的珍珠玉晶米更是上品中的极品，前次只是招待了这老头一顿，就让他魂不守舍，找自己讨了点种子去，只可惜，不用看也知道结果。"
  },
  {
    "segment_id": "0067",
    "text": "“田老说笑了，你难得进来一次，我又岂是如此不懂待客之道的人？”"
  },
  {
    "segment_id": "0068",
    "text": "方元淡笑着，转入里屋，没有多久，浓郁的香气就飘了出来。"
  },
  {
    "segment_id": "0069",
    "text": "田老汉伸长脖颈，使劲吸着鼻子，一副抓耳挠腮的猴急之相，看着实在好笑。"
  },
  {
    "segment_id": "0070",
    "text": "“寒舍简陋，怠慢了！”"
  },
  {
    "segment_id": "0071",
    "text": "没有多久，方元就捧着一个木托盘出来，上面是两碗米饭，两个小菜。"
  },
  {
    "segment_id": "0072",
    "text": "菜是新鲜摘的黄瓜，嫩生生的，直接用泉水一洗，就切片上来，水珠犹在，青翠欲滴，玲珑剔透，简直不忍下筷。"
  },
  {
    "segment_id": "0073",
    "text": "还有一叠小菜是酸豆角，小小的一盘，异香扑鼻，只是一闻就令人肚子咕咕直叫。"
  },
  {
    "segment_id": "0074",
    "text": "“好！好！”"
  },
  {
    "segment_id": "0075",
    "text": "当然，最耀眼的还是木碗中颗粒滚圆，珍珠一般的玉晶米，冒着的香气与豆角味道混杂，令田老汉的眼睛都直了。"
  },
  {
    "segment_id": "0076",
    "text": "此时也顾不得客气，直接对着木碗扒饭，不时叫着：“好吃！好吃……呜呜……”"
  },
  {
    "segment_id": "0077",
    "text": "风卷残云一般，直接干了三大碗米饭下去，又将配菜吃净，田老汉才不好意思地笑了：“小居士你的手艺，简直化腐朽为神奇，老汉也是在城里富贵楼吃过宴席的，根本没有一道菜能比得上你这里！”"
  },
  {
    "segment_id": "0078",
    "text": "“来，还请用茶！”"
  },
  {
    "segment_id": "0079",
    "text": "方元神色淡然，又端出一杯清茶。"
  },
  {
    "segment_id": "0080",
    "text": "这茶是问心茶，却并非坐忘茶道，他早就准备拿其他人试试效果，今日田老汉主动送上门来，正当其时也。"
  },
  {
    "segment_id": "0081",
    "text": "“好香！”"
  },
  {
    "segment_id": "0082",
    "text": "纵然未曾经过一番手续，但泡出的茶汤也是宛若一波碧水，带着浓郁香气，消食解暑，令田老汉捧着茶盏的双手都有些颤抖。"
  },
  {
    "segment_id": "0083",
    "text": "“这茶珍贵，老汉见所未见，莫非又是小居士培育出来的什么新品种？”"
  },
  {
    "segment_id": "0084",
    "text": "他问了一句，见方元笑而不答的模样，心里有愧，也不敢再问，直接饮了一口。"
  },
  {
    "segment_id": "0085",
    "text": "轰隆！"
  },
  {
    "segment_id": "0086",
    "text": "茶汤入口，宛若一道玉龙瀑布，从高空冲刷而下，洗涤心灵，又逆流而上，直冲脑门，田老汉顿时想起了自己的一生，幼年贫苦，青年奋斗，到了现在，却还在蝇营狗苟中过活，不由悲从中来，两行清泪不自觉地流下。"
  },
  {
    "segment_id": "0087",
    "text": "前面的方元，顿时就欣赏到了田老汉各种有趣的神态变化。"
  },
  {
    "segment_id": "0088",
    "text": "“呜呜……小居士，我有愧啊！”"
  },
  {
    "segment_id": "0089",
    "text": "突然间，田老汉嚎啕大哭起来，直接跪下：“问心居士救了老汉一条性命，我却被外人收买，要断你生路，老汉简直不是人，猪狗不如！！！”"
  },
  {
    "segment_id": "0090",
    "text": "“这……”"
  },
  {
    "segment_id": "0091",
    "text": "方元有些呆滞，想不到问心茶的效果如此之好。"
  },
  {
    "segment_id": "0092",
    "text": "不过，他细细打量这田老汉，又是摇头：“没错，若无坐忘茶道，并无增长神元之能……否则他根本不会是现在这个神态！”"
  }
]
```

## Output Format
CRITICAL INSTRUCTION: You MUST translate the source text EXACTLY paragraph by paragraph, preserving the original order perfectly. DO NOT skip, drop, merge, or reorder any paragraphs. Each paragraph in the source MUST be translated.
Return ONLY valid JSON matching this schema:
{
  "chapter_number": 4,
  "chapter_title_vi": "Chương 4: <Vietnamese title>",
  "segments": [
    {
      "segment_id": "XXXX",
      "source": "...",
      "target": "..."
    }
  ]
}
