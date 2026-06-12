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


## Source Chapter 8 - 0008 物是人非
```json
[
  {
    "segment_id": "0001",
    "text": "# 第八节：物是人非"
  },
  {
    "segment_id": "0002",
    "text": "学堂旁设立了一个蛊室。蛊室并不大，只有六十平方米。"
  },
  {
    "segment_id": "0003",
    "text": "蛊师修行，蛊虫就是实力的关键。"
  },
  {
    "segment_id": "0004",
    "text": "课程一结束，兴奋的少年们就向蛊室蜂拥而来。"
  },
  {
    "segment_id": "0005",
    "text": "“排队，一个个的进来。”怒喝声骤起，蛊室门外自然有人把守。"
  },
  {
    "segment_id": "0006",
    "text": "少年们一个个的进去，又出来。"
  },
  {
    "segment_id": "0007",
    "text": "轮到方源走进蛊室。"
  },
  {
    "segment_id": "0008",
    "text": "只见这房间内大有乾坤，四壁都做成隔洞，这些内嵌的方格子一个挨着一个。格子有大有小，大的超不过砂锅，小的小不过拳头。"
  },
  {
    "segment_id": "0009",
    "text": "密密麻麻的格子里，摆放着各式各样的器皿，有的是灰色的石盆，有的是青翠的玉盘，有的是精致的草笼，有的是陶制的暖炉。"
  },
  {
    "segment_id": "0010",
    "text": "这些器皿中就存养着各种各样的蛊虫。"
  },
  {
    "segment_id": "0011",
    "text": "有些蛊虫静默无声，有些蛊虫却吵闹得很，发出吱吱吱、咯咯咯、窸窣窸窣等等各种各样的声音，汇集成一支生命的交响曲。"
  },
  {
    "segment_id": "0012",
    "text": "“蛊虫也分九大层次，照应蛊师九转境界。这些蛊虫都是一转蛊虫。”方源扫视一圈，顿时心知肚明。"
  },
  {
    "segment_id": "0013",
    "text": "一般来讲，一转境界的蛊师，只能用一转层次的蛊虫。若是越级催动高等蛊虫，蛊师往往要付出极其惨重的代价。"
  },
  {
    "segment_id": "0014",
    "text": "而且蛊虫也需要喂养，喂养高等蛊虫所耗费的代价，往往也不是低等蛊师能承受得起的。"
  },
  {
    "segment_id": "0015",
    "text": "对于新人蛊师来讲，不是特殊情况，都会选择一转蛊虫进行首次炼化。"
  },
  {
    "segment_id": "0016",
    "text": "而蛊师炼化的第一只蛊虫，意义重大，称之为本命蛊，性命交修。一旦灭亡，蛊师必定遭受重创。"
  },
  {
    "segment_id": "0017",
    "text": "“唉，原本指望能得到花酒行者的酒虫，炼化它成为我的本命蛊。但是现在，寻找花酒行者尸骨仍旧未见端倪，也不知道什么时候能找到，或者被别人发现。保险起见，还是选一只月光蛊吧。”"
  },
  {
    "segment_id": "0018",
    "text": "方源一边心中暗叹，一边径直走向左手墙侧。"
  },
  {
    "segment_id": "0019",
    "text": "在这面墙洞位置稍稍靠上的其中一层，是一排的白银盘子。每个盘子上都摆放着一只蛊虫。"
  },
  {
    "segment_id": "0020",
    "text": "这蛊虫晶莹剔透，弯弯如月，好像是一块蓝水晶，在白银底盘的映衬下，显现出一股清幽之气。"
  },
  {
    "segment_id": "0021",
    "text": "蛊名月光，是古月一族的镇族蛊虫，绝大多数的族人都选择它成为本命蛊。它并非是天然蛊虫，而是经过古月一族的秘法培育而来，其他地方没有，可以说是古月一族的标志象征。"
  },
  {
    "segment_id": "0022",
    "text": "都是一转的月光蛊，差别极其细微。方源随意挑选了一只，拿在手上。"
  },
  {
    "segment_id": "0023",
    "text": "月光蛊很轻，堪比一张薄纸的重量。只占据掌心一块，如寻常玉坠大小。方源放在手中，能透过它，看到自己被遮掩的掌纹。"
  },
  {
    "segment_id": "0024",
    "text": "最后看了一眼，发现没有什么问题了，方源将其放在口袋中，就出了蛊室。"
  },
  {
    "segment_id": "0025",
    "text": "蛊室外还排着长长的队伍，随后的一个少年见方源走了出来，连忙兴冲冲地跑进蛊室去。"
  },
  {
    "segment_id": "0026",
    "text": "若换做其他人，得了蛊虫，第一反应就是拿回家赶紧炼化。但是方源却没有急着这么做，他的心中还惦记着那只酒虫呢。"
  },
  {
    "segment_id": "0027",
    "text": "酒虫更珍贵，月光蛊虽然是古月山寨的特产，但是却没有酒虫对蛊师的帮助大。"
  },
  {
    "segment_id": "0028",
    "text": "离开了蛊室，方源直接去了酒肆。"
  },
  {
    "segment_id": "0029",
    "text": "“掌柜的，来两坛陈酒。”方源掏掏口袋，将仅剩的元石碎块，放在柜台上。"
  },
  {
    "segment_id": "0030",
    "text": "这些天来，他都会来此买酒，然后再去山寨周边晃荡搜索，意图吸引那只酒虫现身。"
  },
  {
    "segment_id": "0031",
    "text": "掌柜的是个矮矮的中年胖子，满脸油光，经过这些天已经记住了方源。"
  },
  {
    "segment_id": "0032",
    "text": "“客官，你来啦。”打招呼的同时，他伸出又粗又短的胖手，娴熟地将方源的元石碎块抹走。"
  },
  {
    "segment_id": "0033",
    "text": "又放在手中颠了颠，觉得份量不差，掌柜脸上的笑容又亲切几分。"
  },
  {
    "segment_id": "0034",
    "text": "元石是这个世界的货币，用于衡量一切商品的价值。同时它是天地精华的凝练物，自身也能被使用，帮助蛊师更好的修行。"
  },
  {
    "segment_id": "0035",
    "text": "既有货币属性，又有商品属性，极为类似地球上的黄金。地球上有过单一金本位制，这个世界上就是单一元石本位制。"
  },
  {
    "segment_id": "0036",
    "text": "对比一下黄金，因此元石的购买力也相当的惊人。"
  },
  {
    "segment_id": "0037",
    "text": "不过，再多的元石也经不起方源这样连续的消耗。"
  },
  {
    "segment_id": "0038",
    "text": "“每天两坛酒，已经整整七天了。原先积攒的元石，差不多都花完了。”拎着两坛酒出了酒店，方源眉头微微皱着。"
  },
  {
    "segment_id": "0039",
    "text": "一旦成为蛊师，就可以从元石中直接抽取出纯净真元，来补充空窍中的元海。"
  },
  {
    "segment_id": "0040",
    "text": "因此对于蛊师来讲，元石不仅是货币，更是修行的帮手。"
  },
  {
    "segment_id": "0041",
    "text": "有了充足的元石，修行的速度能提升不少，这或多或少能弥补一些资质上的短板。"
  },
  {
    "segment_id": "0042",
    "text": "“明天就没有元石购买酒水了，酒虫却迟迟不现身。难道真的要我把月光蛊炼化成本命蛊？”方源心中有些不甘心。"
  },
  {
    "segment_id": "0043",
    "text": "出了酒肆，方源手中提着两坛酒，一边走路一边思量：“学堂家老说，此次考核第一个炼化本命蛊的人，就有二十块元石的奖励。现在恐怕许多人，都在家卯足劲，炼化蛊虫，争取第一吧。可惜，炼化本命蛊极为考验资质。资质好的人，优势极大。以我丙等资质，有没有其他手段，根本就没有得胜的希望。”"
  },
  {
    "segment_id": "0044",
    "text": "就在这时，身后响起古月方正的声音：“哥哥，你果真又来酒馆买醉！跟我来，舅父舅母要见你。”"
  },
  {
    "segment_id": "0045",
    "text": "方源停下脚步，回身望去。"
  },
  {
    "segment_id": "0046",
    "text": "发现弟弟再没有像从前那般低着头说话。"
  },
  {
    "segment_id": "0047",
    "text": "兄弟俩视线相撞。"
  },
  {
    "segment_id": "0048",
    "text": "一阵风呼啸地吹来，拂起哥哥散乱的黑发，吹起弟弟的衣摆。"
  },
  {
    "segment_id": "0049",
    "text": "短短的一个月，却已物是人非了。"
  },
  {
    "segment_id": "0050",
    "text": "一周前的开窍大典，不管是对于哥哥还是弟弟，都是巨大的改变。"
  },
  {
    "segment_id": "0051",
    "text": "哥哥方源从云端跌下，天才的光环被人无情地剥夺。而弟弟则开始绽放光芒，如一颗新星，冉冉升起。"
  },
  {
    "segment_id": "0052",
    "text": "这种改变对于弟弟古月方正来讲，更是有着一种天翻地覆的意味。"
  },
  {
    "segment_id": "0053",
    "text": "他终于品尝到了哥哥当初的感受，被人寄托着希望，被人用羡慕或者嫉妒的目光看着。"
  },
  {
    "segment_id": "0054",
    "text": "他感觉自己就好像忽然从幽暗的角落里，置身到了充满光的天堂。"
  },
  {
    "segment_id": "0055",
    "text": "每一天醒来，他都感觉自己仿佛在做着一个美梦。天差地别的待遇，让他至今都有些难以置信，同时还有着强烈的不适感。"
  },
  {
    "segment_id": "0056",
    "text": "不适应。"
  },
  {
    "segment_id": "0057",
    "text": "一下子从默默无闻，到被人密切关注，指指点点。"
  },
  {
    "segment_id": "0058",
    "text": "有时候方正走在路上，听到身边路人议论自己、赞叹自己的声音，都会感到脸上发烫，手足无措，眼神躲闪，差点都连路不知道怎么走了！"
  },
  {
    "segment_id": "0059",
    "text": "最初的十几天下来，古月方正莫名其妙的瘦了一圈，不过精气神却越加旺盛。"
  },
  {
    "segment_id": "0060",
    "text": "从他的内心最深处，开始滋生出一种叫做“自信”的东西。"
  },
  {
    "segment_id": "0061",
    "text": "“这就是哥哥以前的感觉啊，真是美妙而又痛苦！”他不可避免地想到自己的哥哥古月方源，面对这样的议论和关注，哥哥他以前是怎么应对的呢？"
  },
  {
    "segment_id": "0062",
    "text": "他下意识地开始模仿方源，装作面无表情，但很快发现自己不是那块料。"
  },
  {
    "segment_id": "0063",
    "text": "有时候在学堂，一声女孩的叫喊，就能让他闹出个大红脸。在路上，大妈大婶的调戏，更让他多次落荒而逃。"
  },
  {
    "segment_id": "0064",
    "text": "他像是一个婴儿学步，跌跌撞撞地适应着新的生活。"
  },
  {
    "segment_id": "0065",
    "text": "在这个过程中，他不可避免地听到有关哥哥的传闻——消沉颓废，变得酗酒，夜不归宿，学堂大睡。"
  },
  {
    "segment_id": "0066",
    "text": "他起先十分震惊，自己的哥哥，那么强大那么天才的存在，竟然变成了这样子？！"
  },
  {
    "segment_id": "0067",
    "text": "但是渐渐的，他开始有点理解了。哥哥也是常人啊，遭遇到这样的挫折和打击，消沉也是必然的。"
  },
  {
    "segment_id": "0068",
    "text": "伴随着这种理解，方正隐隐地感到一阵难以言表的痛快。"
  },
  {
    "segment_id": "0069",
    "text": "这种痛快的情绪，是他极为不想承认的，但的确存在着。"
  },
  {
    "segment_id": "0070",
    "text": "被称赞为天才的哥哥，曾经如阴影般镇压自己的哥哥，如今如此落魄颓丧。这从反面，更见证了自己的成长，不是吗？"
  },
  {
    "segment_id": "0071",
    "text": "自己是优秀的，这才是真相啊！"
  },
  {
    "segment_id": "0072",
    "text": "因此，看到方源拎着酒坛，头发散乱，衣衫不整的模样，古月方正心中狠狠地舒了一口气，呼吸莫名地轻松了许多。"
  },
  {
    "segment_id": "0073",
    "text": "但他嘴上却又说着：“哥哥，你不能再喝酒了，不能再这样下去了。你不知道关心你的人会多么的担心，你要振作起来！”"
  },
  {
    "segment_id": "0074",
    "text": "方源面无表情，没有开口。"
  },
  {
    "segment_id": "0075",
    "text": "兄弟俩四目相对。"
  },
  {
    "segment_id": "0076",
    "text": "弟弟古月方正的眼中闪闪发亮，透出一股锐利之意。而哥哥方源的双眸，却黑的深沉，如幽幽之古潭。"
  },
  {
    "segment_id": "0077",
    "text": "这样的眸子，让方正不由地感到一种莫名其妙的压抑。对视没有多久，他下意识地转移了视线，望向另一侧。"
  },
  {
    "segment_id": "0078",
    "text": "但当他反应过来时，心中瞬间升腾起一股愤怒。"
  },
  {
    "segment_id": "0079",
    "text": "一股对自己的愤怒。"
  },
  {
    "segment_id": "0080",
    "text": "自己这是怎么了？连和哥哥对视的勇气都没有么？"
  },
  {
    "segment_id": "0081",
    "text": "我已经变了，我已经彻底改变了！"
  },
  {
    "segment_id": "0082",
    "text": "这样想着，眼神就锐利起来，重新扫射过去。"
  },
  {
    "segment_id": "0083",
    "text": "但是方源却已不看他，而是一手拎着一坛酒，走过他的身边，平淡的声音传来：“还愣着做什么，走吧。”"
  },
  {
    "segment_id": "0084",
    "text": "方正呼吸一乱，心底积蓄起来的那口气，再没有了发泄的地方，这让他感到一种难以表达的郁闷。"
  },
  {
    "segment_id": "0085",
    "text": "眼看哥哥已经走远，他只好快步跟上去。"
  },
  {
    "segment_id": "0086",
    "text": "只是这一次，他的头不再低着，而是昂起面朝着夕阳。"
  },
  {
    "segment_id": "0087",
    "text": "他的目光则注视着自己的脚，正一步步踩在哥哥方源的影子上。"
  }
]
```

## Output Format
CRITICAL INSTRUCTION: You MUST translate the source text EXACTLY paragraph by paragraph, preserving the original order perfectly. DO NOT skip, drop, merge, or reorder any paragraphs. Each paragraph in the source MUST be translated.
Return ONLY valid JSON matching this schema:
{
  "chapter_number": 8,
  "chapter_title_vi": "Chương 8: <Vietnamese title>",
  "segments": [
    {
      "segment_id": "XXXX",
      "source": "...",
      "target": "..."
    }
  ]
}
