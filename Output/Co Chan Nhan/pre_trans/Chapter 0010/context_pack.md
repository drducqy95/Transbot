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


## Source Chapter 10 - 0010 天有不测风云，炼蛊别具艰辛
```json
[
  {
    "segment_id": "0001",
    "text": "# 第十节：天有不测风云，炼蛊别具艰辛"
  },
  {
    "segment_id": "0002",
    "text": "啪啪啪……"
  },
  {
    "segment_id": "0003",
    "text": "豆大的雨点，密集地下着。打在苍翠的竹楼上，发出脆响。"
  },
  {
    "segment_id": "0004",
    "text": "楼前池塘中，水面被雨点激打着，鱼儿在水里快活地穿梭着，水草在池底摇曳。"
  },
  {
    "segment_id": "0005",
    "text": "阴云密布，整个视野都被一层浓密厚重的雨帘遮挡起来。"
  },
  {
    "segment_id": "0006",
    "text": "在有些昏暗的房间里，窗户开着，方源静静地看着这场大雨，心中幽幽一叹：“已经三天三夜了。”"
  },
  {
    "segment_id": "0007",
    "text": "三天前的那晚，他拎着两坛酒，出了山寨，在周边继续探索。"
  },
  {
    "segment_id": "0008",
    "text": "但到了深夜就下起了瓢泼大雨。"
  },
  {
    "segment_id": "0009",
    "text": "被淋成落汤鸡且不去谈他，关键是如此情况下，就再也不能四处探索了。"
  },
  {
    "segment_id": "0010",
    "text": "雨水能将酒气迅速地冲刷掉，同时若顶着雨强行探索，只怕会引起怀疑。"
  },
  {
    "segment_id": "0011",
    "text": "先前是伪装成失意酗酒的样子，来遮掩真正的动机。但千万不要低估旁人的智慧，往往只有蠢材才会认为别人愚蠢。"
  },
  {
    "segment_id": "0012",
    "text": "所以无奈之下，方源就只能终止了探索。"
  },
  {
    "segment_id": "0013",
    "text": "而这场雨下起来，就一直持续着，期间或大或小，或稀或密，却没有停止过。"
  },
  {
    "segment_id": "0014",
    "text": "“这样一来，酒虫短时间之内就寻不到了。保险起见，只能先着手炼化月光蛊。在这炼化的过程中，能寻到酒虫最好，得不到也只好这样将就了。不过此事也很平常，天有不测之风云。这世间哪有人做事能一直顺风顺水，尽善尽美的？”方源心境很平稳，五百年的经历，早就洗去了他性情中本来就少的浮躁。"
  },
  {
    "segment_id": "0015",
    "text": "他关上窗户和门，趺坐到床榻之上。缓缓闭上双眼，呼吸调匀后，便将心神一沉。"
  },
  {
    "segment_id": "0016",
    "text": "下一刻，脑海中就展现出自身空窍的景象。"
  },
  {
    "segment_id": "0017",
    "text": "空窍虽然寄托在体内，但是玄妙异常，无限大，又无限小。"
  },
  {
    "segment_id": "0018",
    "text": "空窍外侧，是一层光膜。白色的光膜给人很纤薄的感觉，但是却实实在在地支撑着空窍。"
  },
  {
    "segment_id": "0019",
    "text": "空窍中，是一片真元海洋。"
  },
  {
    "segment_id": "0020",
    "text": "海水呈青铜色，海面平静如镜，水位差不多是空窍的一半高。整个元海体积，占据空窍的四成四。"
  },
  {
    "segment_id": "0021",
    "text": "这就是一转蛊师的青铜元海，每一滴海水，都是真元。是方源的生命元力，是方源的精气神的凝结。"
  },
  {
    "segment_id": "0022",
    "text": "每一滴真元都是宝贵的，因为它是一个蛊师的根本，是力量之源。就是靠着真元，蛊师才能炼化和催动蛊虫。"
  },
  {
    "segment_id": "0023",
    "text": "心神从元海中退出来，方源睁开双眼，从怀中取出那只月光蛊。"
  },
  {
    "segment_id": "0024",
    "text": "月光蛊静静地躺在方源的掌心中，就好像一个弯弯的蓝色月亮，小巧玲珑，晶莹剔透。"
  },
  {
    "segment_id": "0025",
    "text": "方源心念一动，顿时空窍中的元海翻滚起来，一股真元水流冲破海面，调动到体外，尽数涌入到月光蛊之中。"
  },
  {
    "segment_id": "0026",
    "text": "月光蛊猛地绽放出幽蓝的光辉，在方源的手掌中微微地颤动，抗拒着方源真元的涌入。"
  },
  {
    "segment_id": "0027",
    "text": "蛊是天地之精华，大道之密码，法则之载体。它也是生灵，天生自由自在，存在着本身的意志。现在方源要炼化它，就是要抹去它的意志，感应到这股危机，月光蛊自然要反抗。"
  },
  {
    "segment_id": "0028",
    "text": "炼化的过程十分艰难。"
  },
  {
    "segment_id": "0029",
    "text": "月光蛊就像是一片弯弯的月牙，青铜色的真元注入到月牙当中，首先就将月牙两个尖端染绿。"
  },
  {
    "segment_id": "0030",
    "text": "随后这股青铜绿意，开始向月牙中段蔓延。"
  },
  {
    "segment_id": "0031",
    "text": "不到三分钟，方源的脸上就呈现出一抹苍白。大量的真元不断地涌入到月光蛊中，导致一股股抽经伐髓的虚弱感，连绵不绝地向他心头袭来。"
  },
  {
    "segment_id": "0032",
    "text": "一分、两分、三分……八方、九分、一成。"
  },
  {
    "segment_id": "0033",
    "text": "十分钟后，方源元海就消耗掉了整整一成真元。但是蓝水晶一样的月光蛊表面，处在月牙尖端的两点青铜绿意，却只向中段扩张了一丁点的面积。"
  },
  {
    "segment_id": "0034",
    "text": "月光蛊的反抗力，十分顽强。"
  },
  {
    "segment_id": "0035",
    "text": "好在方源对此早有预料，也不意外，坚持向月光蛊中灌输真元。"
  },
  {
    "segment_id": "0036",
    "text": "一成，两成，三成。"
  },
  {
    "segment_id": "0037",
    "text": "又过了二十分钟，方源体内的元海只剩下一成四分，月光蛊上青铜绿意扩张了一丝，两片绿意若叠加起来算，大约有整个月光蛊表面的十二分之一。"
  },
  {
    "segment_id": "0038",
    "text": "至于其余部分，还是月光蛊本身的淡蓝之色。"
  },
  {
    "segment_id": "0039",
    "text": "“炼蛊艰难呐。”看到此景，方源暗叹一声，断了真元供给，不再继续炼化这月光蛊。"
  },
  {
    "segment_id": "0040",
    "text": "到此刻，炼蛊整整半小时，空窍元海已经消耗了一大半，只剩下一成四的真元残留着。而月光蛊才刚刚炼化了十二分之一。"
  },
  {
    "segment_id": "0041",
    "text": "而且，更叫人难以接受的是，月光蛊仍旧散发着幽蓝的光晕。方源虽然停止了炼化，但是它却没有停止反抗，仍旧在驱逐方源的青铜真元。"
  },
  {
    "segment_id": "0042",
    "text": "方源可以清晰地感到，汇入到月光蛊中的真元，正在一点点被月光蛊驱除出去，逸散到体外。月光蛊表面，两个月牙尖端的青铜绿意也在慢慢地缩小。"
  },
  {
    "segment_id": "0043",
    "text": "照这减少的速度估算，大约六个小时之后，月光蛊就能将方源的真元全部驱除。到那时再来炼化这蛊虫，和重头祭炼没有分别。"
  },
  {
    "segment_id": "0044",
    "text": "“每一次炼蛊，就像是两军交战，打阵地战，消耗战。蛊虫只祭炼了十二分之一，而我的真元却消耗了整整三成。蛊师炼蛊就必须一边补充元海真元，一边持续不断地祭炼，巩固胜利成果。炼蛊考较的不仅是调动真元的技巧，还有持久战的耐心。”"
  },
  {
    "segment_id": "0045",
    "text": "方源一边想着，一边从钱袋中取出一块元石。"
  },
  {
    "segment_id": "0046",
    "text": "蛊师要补充消耗掉的真元，通常有两种方法。"
  },
  {
    "segment_id": "0047",
    "text": "一种是自然恢复。每过一段时间，元海就会自动补充真元。像方源这种丙等资质，大约一个小时补充四分真元。六个小时，就能恢复二成四分的真元总量。"
  },
  {
    "segment_id": "0048",
    "text": "第二种方法，就是汲取元石中的自然元力。"
  },
  {
    "segment_id": "0049",
    "text": "元石是大自然的瑰宝，凝聚着天然真元，可以被蛊师吸收。"
  },
  {
    "segment_id": "0050",
    "text": "方源手握元石，从里面源源不断地汲取出天然真元，汇入到自己的空窍元海之中。"
  },
  {
    "segment_id": "0051",
    "text": "元石表面的细腻光华，慢慢地暗淡下去，方源的元海水位却以肉眼可见的速度，不断攀升。"
  },
  {
    "segment_id": "0052",
    "text": "大约半个小时之后，元海重新恢复到四成四的体积。到了这程度，海面增高的趋势，就戛然而止。虽然空窍中还有空间，但是方源却再也存储不了更多真元。这就是他丙等资质的局限了。"
  },
  {
    "segment_id": "0053",
    "text": "由此，就可体现出修行资质的重要作用了。"
  },
  {
    "segment_id": "0054",
    "text": "资质越高，空窍中存储的真元就越多，并且真元自然恢复的速度也越快。"
  },
  {
    "segment_id": "0055",
    "text": "对于方源来讲，要炼化蛊虫，巩固成果，必须得吸收元石，因为他真元自然恢复的速度，比不上月光蛊驱逐真元的速度。"
  },
  {
    "segment_id": "0056",
    "text": "但是对于甲等资质的方正来讲，他每小时能补充八分真元。六个小时，就能恢复四成八分的真元总量，而月光蛊在同样的六个小时内，只能驱逐三成真元。"
  },
  {
    "segment_id": "0057",
    "text": "他甚至不需要元石这样的外力帮助，就这样一直炼化，期间休息几次，过个几天，就能将月光蛊成功炼化。"
  },
  {
    "segment_id": "0058",
    "text": "所以，方源从一开始就知道，在这场炼化月光蛊的考核中，自己根本就没可能夺得第一。这无关实力，而是资质才是此中的第一因素。"
  },
  {
    "segment_id": "0059",
    "text": "第二因素则是元石。"
  },
  {
    "segment_id": "0060",
    "text": "若是元石充沛，不惜损耗，乙等资质的人，也可能超越甲等，夺得第一。"
  },
  {
    "segment_id": "0061",
    "text": "“我手中只有六块元石，比不上古月漠北，古月赤城这种背后有长辈支持的人。我资质只有丙等，也比不上甲等资质的古月方正。这场考核本来就没有一丁点胜算，还不如分散精力，去寻找酒虫。若是能将酒虫炼成本命蛊，可比月光蛊要好多了。嗯？窗外的雨声小了，似乎有停息的迹象。这场大雨已经连下了三天三夜，也该停了。”"
  },
  {
    "segment_id": "0062",
    "text": "方源收起月光蛊，下了床榻，正要打开窗，此时却有敲门声响起。"
  },
  {
    "segment_id": "0063",
    "text": "门外传来贴身丫鬟沈翠的声音：“方源少爷，是奴婢。这三天雨连下着，奴婢这就给您带来了一些酒菜，少爷吃喝一些，也能解些乏闷。”"
  },
  {
    "segment_id": "0064",
    "text": "（ps：感谢粉丝789、蓝浪魔、颓废wudi、甜甜圈现象、q62552217几位同学的打赏。感谢粉丝789、蓝浪魔等同学们的满分评价票。感谢一直投着推荐票的朋友们。人气在回归，老朋友们也越来越多，我们的力量在慢慢回复。新书就像婴儿、幼草，需要点击、收藏和推荐票的灌溉，这样才能茁壮成长。请诸君努力灌溉和支持啊！）"
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
