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


## Source Chapter 6 - 0006 未来的路，会很精彩
```json
[
  {
    "segment_id": "0001",
    "text": "# 第六节：未来的路，会很精彩"
  },
  {
    "segment_id": "0002",
    "text": "空窍玄妙异常，虽然寄托在方源体内，但是却不和五脏六腑同处一个空间。你可以说它无限大，又可以说它无限小。"
  },
  {
    "segment_id": "0003",
    "text": "有人称之为紫府，有人称之为华池。不过更多人称之为元海空窍。"
  },
  {
    "segment_id": "0004",
    "text": "整个空窍呈球形，空窍表面流动着白光，是一层光膜。就是先前的希望蛊炸裂开来，凝聚的一层光。"
  },
  {
    "segment_id": "0005",
    "text": "正是因为有了这层光膜，才支撑着空窍，不会塌陷。"
  },
  {
    "segment_id": "0006",
    "text": "空窍之中，自然就是元海。"
  },
  {
    "segment_id": "0007",
    "text": "海水平滑如镜，呈现一片碧青之色，却又浓稠无比，带着铜的光泽。"
  },
  {
    "segment_id": "0008",
    "text": "这是一转蛊师才有的青铜真元凝结，俗称青铜海。"
  },
  {
    "segment_id": "0009",
    "text": "海面不到空窍的一半高度，只有四成四。这也是丙等资质的局限。"
  },
  {
    "segment_id": "0010",
    "text": "每一滴的海水，都是真元，代表着方源精气神的凝结，象征着他十五年来积蓄出来的生命潜能。"
  },
  {
    "segment_id": "0011",
    "text": "蛊师就是用这真元来催动蛊虫，也就是说，从此刻起，方源就正式迈入一转蛊师的行列。"
  },
  {
    "segment_id": "0012",
    "text": "空窍已开，再没有希望蛊汇入方源体内。"
  },
  {
    "segment_id": "0013",
    "text": "方源收起心神，只觉得前方的压力坚厚如壁，也不能再进一步。"
  },
  {
    "segment_id": "0014",
    "text": "“一如前世啊。”对这个结果他淡然一笑。"
  },
  {
    "segment_id": "0015",
    "text": "“不能再走了吗？”学堂家老抱着万分之一的希望，隔岸喊道。"
  },
  {
    "segment_id": "0016",
    "text": "方源直接转身往回走，以实际行动回答了他。"
  },
  {
    "segment_id": "0017",
    "text": "这下子，就连那些少年们也反应过来了。"
  },
  {
    "segment_id": "0018",
    "text": "顿时，就听嗡的一声，人群炸开了锅。"
  },
  {
    "segment_id": "0019",
    "text": "“什么？方源走了二十七步？”"
  },
  {
    "segment_id": "0020",
    "text": "“原来他只有丙等资质？！”"
  },
  {
    "segment_id": "0021",
    "text": "“难以置信，他这么天才，只是个丙等？”"
  },
  {
    "segment_id": "0022",
    "text": "人群中掀起轩然大波。"
  },
  {
    "segment_id": "0023",
    "text": "“哥哥……”在人群中，古月方正抬起头来，震惊地看着趟河回来的方源。他不敢相信眼前的一幕，自己的哥哥居然只是一个丙等？"
  },
  {
    "segment_id": "0024",
    "text": "他一直认为，哥哥会是个甲等资质。"
  },
  {
    "segment_id": "0025",
    "text": "不，不仅是他，舅父舅母还有族中的许多人都这么认为着。"
  },
  {
    "segment_id": "0026",
    "text": "但是现在，结果居然是这样！"
  },
  {
    "segment_id": "0027",
    "text": "“可恶，居然只是个丙等！”古月族长暗捏双拳，深深地叹了一口气，失望之情溢于言表。"
  },
  {
    "segment_id": "0028",
    "text": "暗中关注的家老们，有的皱起眉头，有的低头谈论，有人仰天长叹。"
  },
  {
    "segment_id": "0029",
    "text": "“会不会测试有误？”"
  },
  {
    "segment_id": "0030",
    "text": "“怎么可能？这方法准确无比，况且有我们一直盯着，作弊都难。”"
  },
  {
    "segment_id": "0031",
    "text": "“可是，那他先前的表现和才情，又怎么解释呢？”"
  },
  {
    "segment_id": "0032",
    "text": "“元海资质越高的少年，的确会表现出超越常人的特性。比如聪颖、悟性、记忆力、力量、敏捷等等。但是反过来，这些特性并不代表资质一定就高，一切还得以测试结果为准。”"
  },
  {
    "segment_id": "0033",
    "text": "“唉，希望越大失望越大。古月一族是一代不如一代了。”"
  },
  {
    "segment_id": "0034",
    "text": "……"
  },
  {
    "segment_id": "0035",
    "text": "冰凉的河水，浸湿了足袜，冷得有些刺骨。"
  },
  {
    "segment_id": "0036",
    "text": "方源依旧面无表情地走着，距离越来越近，他可以清晰地看到学堂家老沉重的表情，可以敏锐地觉察到上百位少年投来的目光。"
  },
  {
    "segment_id": "0037",
    "text": "这目光中有惊诧，有震动，有嘲讽，有幸灾乐祸，有恍然，有冷漠。"
  },
  {
    "segment_id": "0038",
    "text": "一模一样的情境，让方源不由地想到了前世。"
  },
  {
    "segment_id": "0039",
    "text": "那时自己感觉天都塌下来了，过河时失足摔了一跤，浑身湿透，失魂落魄。却没有一个人搀扶自己。"
  },
  {
    "segment_id": "0040",
    "text": "这些失望、冷漠的表情和眼神，像是尖刀凌迟着自己的心。思绪纷乱无比，胸口更是隐隐作痛。"
  },
  {
    "segment_id": "0041",
    "text": "就好像是从云端摔到地上，站得越高，摔得越狠。"
  },
  {
    "segment_id": "0042",
    "text": "不过，今生。"
  },
  {
    "segment_id": "0043",
    "text": "重临这样的场景，方源的心却平静无比。"
  },
  {
    "segment_id": "0044",
    "text": "他想到了那个传说，当困境来临时，要把心交给希望。"
  },
  {
    "segment_id": "0045",
    "text": "如今这个希望，就在自己的体内。虽然这希望不大，但已经好过那些毫无修行资质的人。"
  },
  {
    "segment_id": "0046",
    "text": "别人因此而失望，那就失望吧，又能如何呢？"
  },
  {
    "segment_id": "0047",
    "text": "别人的失望与我何干？重要的是自己心存希望！"
  },
  {
    "segment_id": "0048",
    "text": "五百年的生涯，让他明白了一个道理：人的一生之精彩，在于自己追逐梦想的过程。不必苛求旁人的不失望或者喜欢。"
  },
  {
    "segment_id": "0049",
    "text": "走自己的路，让旁人失望和不喜欢去吧！"
  },
  {
    "segment_id": "0050",
    "text": "“唉……”学堂家老深深地叹了一口气，又喊道，“下一位，古月方正。”"
  },
  {
    "segment_id": "0051",
    "text": "却无人应答。"
  },
  {
    "segment_id": "0052",
    "text": "“古月方正！”家老大喝，声音在溶洞中嗡嗡回响。"
  },
  {
    "segment_id": "0053",
    "text": "“啊？我在，我在！”方正从震惊的情绪中挣脱，连忙跑出，不幸脚下一个踉跄，顿时摔了个跟头，噗通一声，恰巧滚落到河里。"
  },
  {
    "segment_id": "0054",
    "text": "顿时，哄堂大笑。"
  },
  {
    "segment_id": "0055",
    "text": "“方家兄弟，不过如此。”古月族长冷哼一声，对古月方正也产生了一种厌烦。"
  },
  {
    "segment_id": "0056",
    "text": "“这下丢人丢大了！”方正在河水中奋力扑腾了几下，奈何这河底甚滑，根本站不起来。努力的结果，反而显得他更加笨手笨脚。耳中听到一阵阵的哄笑声，这让他心中越加慌乱。"
  },
  {
    "segment_id": "0057",
    "text": "但就在这时，他忽然感觉一股大力把他拽住，脑袋终于脱离了水面，身体也重新掌握了平衡。"
  },
  {
    "segment_id": "0058",
    "text": "狼狈地抹了一把脸，再定睛一看，却是哥哥方源提着自己的衣领，将自己提了起来。"
  },
  {
    "segment_id": "0059",
    "text": "“哥……”他张口欲言，换来的却是水呛到的结果，继而又引发了一阵剧烈的咳嗽。"
  },
  {
    "segment_id": "0060",
    "text": "“哈哈，方家的难兄难弟！”岸上有人嘲笑出声。"
  },
  {
    "segment_id": "0061",
    "text": "哄笑声愈加响亮，学堂家老也没有站出来阻止，他深皱着眉头，心中充满了失望。"
  },
  {
    "segment_id": "0062",
    "text": "方正手足无措，就听到耳边传来哥哥的声音：“去吧，未来的路，会很精彩呢。”"
  },
  {
    "segment_id": "0063",
    "text": "方正不由地惊讶地张开嘴，此时方源背对着众人，因此岸上的人都看不清楚。但是方正却清楚地感觉到方源的平静，说话的时候嘴角甚至都微微翘起，流露出一抹玩味深沉的笑意。"
  },
  {
    "segment_id": "0064",
    "text": "“明明只是个丙等资质，为什么哥哥还这么平静？”不由地，方正的心中充满了疑惑。"
  },
  {
    "segment_id": "0065",
    "text": "方源再没有多说，拍拍方正的背，转身就走。"
  },
  {
    "segment_id": "0066",
    "text": "方正表情愣愣的，走向花海。"
  },
  {
    "segment_id": "0067",
    "text": "“想不到哥哥竟然这么平静，要是我的话，恐怕……”他低着头，无意识地向前走着。却并不知道自己正上演着一场奇迹式的表演。"
  },
  {
    "segment_id": "0068",
    "text": "等到他惊醒的时候，他已经站在花海的深处，一个先前并未有人达到的距离。"
  },
  {
    "segment_id": "0069",
    "text": "四十三步！"
  },
  {
    "segment_id": "0070",
    "text": "“天呐，甲等资质！！！”学堂家老失态地大叫着。"
  },
  {
    "segment_id": "0071",
    "text": "“甲等，竟是甲等？！”"
  },
  {
    "segment_id": "0072",
    "text": "“三年了，古月一族终于又出现了甲等资质的天才！”"
  },
  {
    "segment_id": "0073",
    "text": "暗中关注的家老们，也同时叫喊着，大失风范。"
  },
  {
    "segment_id": "0074",
    "text": "“嗯，方之一脉本来就是从我们赤脉分出去的，这个古月方正就由我赤之一脉收养了。”古月赤练当即宣布道。"
  },
  {
    "segment_id": "0075",
    "text": "“怎么可能？你赤练老鬼何德何能，误人子弟的本事倒是不错。这个孩子还不如交给我古月漠尘抚养。”古月漠尘像触电一般，立即咆哮起来。"
  },
  {
    "segment_id": "0076",
    "text": "“谁都别争了。这个孩子谁栽培，都没有本族长亲自栽培的好。谁有异议，就是反对我古月博！”古月族长双眼赤红，一扫先前的失望颓废，整个人都癫狂了。"
  },
  {
    "segment_id": "0077",
    "text": "(ps:新书真心需要大家鼎力支持啊，多点击一下，都是好的。虽然说隔了两个月才开新书，人气有点断，随着时间流逝，人气就会回升。但是……目前在冲新书榜的说，急需大家支持呀。混贴吧的同学都来起点支持一下，公众章节是不收费的。)"
  }
]
```

## Output Format
CRITICAL INSTRUCTION: You MUST translate the source text EXACTLY paragraph by paragraph, preserving the original order perfectly. DO NOT skip, drop, merge, or reorder any paragraphs. Each paragraph in the source MUST be translated.
Return ONLY valid JSON matching this schema:
{
  "chapter_number": 6,
  "chapter_title_vi": "Chương 6: <Vietnamese title>",
  "segments": [
    {
      "segment_id": "XXXX",
      "source": "...",
      "target": "..."
    }
  ]
}
