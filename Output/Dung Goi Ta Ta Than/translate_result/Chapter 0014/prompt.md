# Translation Task

## Context
- Project: Đừng Gọi Ta Tà Thần (Đừng Gọi Ta Tà Thần)
- Author: Thủy Quả Trung Đích Đồng Thần
- Genre: Fantasy phương Tây (isekai)
- Chapter: 14 - Thay đổi tâm lý
- Source: Chapter 0014 心态转变.md
- Target language: Vietnamese (tiếng Việt)

## Plot summary (Chapter 14)
Pete và Lena đến quán rượu nhà Lena ở Khu Hạ Thành, Green Port. Họ thấy một nhóm côn đồ đang đe dọa Old Moni (cha Lena) đòi bồi thường cho Dussley. Lena muốn bỏ trốn nhưng Pete — sau khi trải qua sự thay đổi tâm lý — quyết định ở lại đối đầu. Cậu cầu nguyện Norven (Thần Tri Thức) và nhận nhiệm vụ học 【O Thuật Phi Đạn】 (Arcane Missiles), một pháp thuật cấp 1. Pete thành công xây dựng mô hình pháp thuật và bắn ba viên đạn ma thuật về phía tên cầm đầu.

## Character references
- 培特 = Pete (Pete Chinar): học viên Học viện Caroen, Thi Pháp Giả nhị giai. Trong chương này cậu thay đổi tâm lý từ sợ hãi sang tự tin.
- 蕾娜 = Lena (Lena Monia): thiếu nữ khoảng 18-20, con gái chủ quán rượu Moni Brotherhood.
- 诺文 = Norven: Thần Tri Thức, thần của Pete.
- 巴哈姆特 = Bahamut: pháp sư cấp 5, người xuyên không.
- 德思礼 = Dussley: kẻ sai côn đồ đến đòi bồi thường.
- 老莫尼 = Old Moni: cha của Lena, chủ quán rượu.

## Place references
- 格林港 = Green Port
- 上城区 = Khu Thượng Thành
- 下城区 = Khu Hạ Thành
- 卡罗恩学院 = Học viện Caroen

## Term mapping (MANDATORY)
| Source | Target | Notes |
|--------|--------|-------|
| 魔网 | Ma Võng | KHÔNG dịch là Ma Lưới |
| 施法者 | Thi Pháp Giả | |
| 法师 | Pháp Sư | |
| 大法师 | Đại Pháp Sư | |
| 魔法学徒 | Ma Pháp Học Đồ | |
| 职业者 | Chức Nghiệp Giả | |
| 法术位 | Pháp thuật vị | |
| 戏法 | Hí pháp | |
| 奥术飞弹 | 【O Thuật Phi Đạn】 | giữ nguyên 【】 |
| 奥术能量 | năng lượng O Thuật | |
| 法术模型 | mô hình pháp thuật | |
| 神谕 | thần dụ | |
| 畸变怪 | quái vật dị biến | |
| 地精 | tinh linh | |
| 大地精 | đại tinh linh | |
| 精灵 | tinh linh (chủng tộc) | |
| 半精灵 | bán tinh linh | |
| 矮人 | người lùn | |
| 祷告 | cầu nguyện | |
| 混混 | côn đồ / lưu manh | |

## Narrator style
- Dùng "hắn" cho Pete (giọng người dẫn chuyện).
- Pete tự xưng "ta", Lena xưng "em" với Pete.
- Lena gọi Pete là "Pete" hoặc "anh".
- Côn đồ gọi Old Moni là "lão" (thô tục).
- Giọng văn: tự nhiên, mạch lạc, có chút hài hước nhẹ ở suy nghĩ của Pete.

## Rules
1. Dịch sát nghĩa, tự nhiên, KHÔNG tóm tắt.
2. Không thêm chú thích, giải thích hay bình luận.
3. KHÔNG để sót chữ Hán/CJK trong target (trừ tên giữ Latin).
4. Giữ đúng segment_id và cấu trúc JSON.
5. Tiêu đề chương: # Chương 14: Thay đổi tâm lý

## Input segments
```json
{
  "chapter_number": 14,
  "segments": [
    {
      "segment_id": "0001",
      "type": "title",
      "source": "# 第14章 心态转变"
    },
    {
      "segment_id": "0002",
      "type": "dialogue_intro",
      "source": "没来得及询问蕾娜发生了什么事，培特便见到领头的壮汉拎着根粗木棒，气势汹汹地咣咣砸着酒馆的木门，朝酒馆里面叫嚣："
    },
    {
      "segment_id": "0003",
      "type": "dialogue",
      "source": "\"老莫尼，说了给你三天时间考虑，考虑的怎么样了！\"\n\"说话啊！当初跟你朋友们去闹事的时候，你声音不是挺大的吗！现在怎么连出来都不敢了！\"\n\"德思礼大人可是给我们下了死命令，赔偿大人这段时间的全部损失，否则的话，你别想再格林港再混下去！\""
    },
    {
      "segment_id": "0004",
      "type": "paragraph",
      "source": "木门在壮汉的用力击打下摇摇欲坠，蕾娜见状表情更加难看，低声咕哝道：\"法……\"\n培特似乎隐约听到少女骂了一个F开头的单词。"
    },
    {
      "segment_id": "0005",
      "type": "dialogue",
      "source": "\"这些人都什么来头？\""
    },
    {
      "segment_id": "0006",
      "type": "paragraph",
      "source": "培特在卡罗恩学院的朋友跟他提过，说格林港的上城区和下城区几乎就是两个世界，差距可谓天壤之别。\n上城区居住的基本都是有钱的大商人、大地精或者高阶职业者，享受着奢华而舒适的生活，住所周围有着精心打理的花园和庭院，各种的奇珍异宝作为装饰，来自大陆各地的美食美酒任其享用，几乎每天都有各种各样的交谊舞会或酒宴。\n下城区则是格林港的普通人聚集的地方，居住在简陋的木质或石质房屋里，因为港口渔船晒鱼而吹来的鱼腥味长年不散，环境就是脏乱差的代名词。\n而且各种黑帮势力在下城区横行，再加上格林港警署懒散的工作效率，治安情况更是混乱的一塌糊涂。\n这才刚到蕾娜家的酒馆门口，培特就亲自感受到了下城区的混乱程度。"
    },
    {
      "segment_id": "0007",
      "type": "dialogue_intro",
      "source": "蕾娜蹙着眉，愁苦地叹了口气："
    },
    {
      "segment_id": "0008",
      "type": "dialogue",
      "source": "\"这事说来话长，现在不是解释的时候，可能没机会请你喝一杯了，真是不走运，怎么又撞上这些可恶的家伙！\"\n\"总之，趁他们没发现我，我们赶紧离开这里，他们知道我是老莫尼的女儿，要是落到他们手里就麻烦了。\""
    },
    {
      "segment_id": "0009",
      "type": "paragraph",
      "source": "培特本想下意识答应蕾娜跟着她离开，却突然心中一动。"
    },
    {
      "segment_id": "0010",
      "type": "dialogue",
      "source": "\"不对啊！\"\n\"如果放在过去，在格林港这地方遇到这种事情，我肯定是多一事不如少一事，能躲就躲。\"\n\"毕竟以前的我虽然是职业者，实际上根本没有战斗能力，真要打起来我肯定是挨打的那个。\"\n\"问题是，现在有求知之神罩着我，连3阶的畸变怪我都能干掉了，为什么还要怕下城区的几个流氓混混？\"\n\"他们再能打，还能比那畸变怪更强？\"\n\"看那几个人的样子也不是什么职业者，应该就是普通人里比较强壮的家伙而已。\"\n\"求知之神没来的时候，我怕遇上类似的事情是因为我打不过，现在求知之神已经来了，我也能学会强力的法术了，我要是还怕，那求知之神岂不是白来了？\""
    },
    {
      "segment_id": "0011",
      "type": "paragraph",
      "source": "培特的心态在悄然间发生了些许改变。\n以前他对自己的职业者水分含量有多高心知肚明，格林港不是他家乡的男爵庄园，没有侍卫能让他狐假虎威。\n可是在被卷入那些黑袍人的祭祀仪式，经历了真正的战斗，亲手消灭掉强大的怪物后，培特发现他开始变得不一样了。\n在格林港警署的时候，他被那个叫巴哈姆特的神秘人的气场所震慑，下意识地按着过去的心态，第一反应是求饶。\n离开警署后，培特逐渐回过味儿来。\n有了击杀3阶畸变怪的战绩打底，他头一次产生了\"我很强\"的感觉。\n更何况，现在罩着的他可不是那个高冷无比、对他爱答不理的魔法女神，而是求知之神诺文！\n求知之神给他的知识可比魔法女神的那套好用多了！"
    },
    {
      "segment_id": "0012",
      "type": "dialogue",
      "source": "\"蕾娜，我们不用走！\"\n\"区区几个混混罢了，交给我吧。\""
    },
    {
      "segment_id": "0013",
      "type": "paragraph",
      "source": "心态转变过后，培特的胆子也变大了。"
    },
    {
      "segment_id": "0014",
      "type": "dialogue",
      "source": "\"伟大的求知之神在上，我需要您的帮助，请教给我能够教训这些家伙的法术吧！！\""
    },
    {
      "segment_id": "0015",
      "type": "paragraph",
      "source": "下一瞬间，熟悉的声音在培特耳畔响起："
    },
    {
      "segment_id": "0016",
      "type": "system",
      "source": "【叮！】\n【收到信徒祈祷！任务已发布】\n【任务：学习法术[奥术飞弹]（1阶），当前进度：0%】\n【任务：击败混混0/5】"
    },
    {
      "segment_id": "0017",
      "type": "dialogue",
      "source": "\"你先在旁边稍微躲一下，别忘了你说过的，我可是大法师，收拾他们几个不过是简简单单的事情罢了。\""
    },
    {
      "segment_id": "0018",
      "type": "dialogue",
      "source": "\"那……培特先生，一定要注意安全，千万别被他们伤到。\""
    },
    {
      "segment_id": "0019",
      "type": "paragraph",
      "source": "培特比了个妥当的手势，稳定心神，开始照着诺文神谕中的信息，着手构建法术模型。\n调动魔网的步骤他已经相当熟练，仅仅只花了数秒时间便成功地又一次勾搭上了魔网。"
    },
    {
      "segment_id": "0020",
      "type": "dialogue",
      "source": "\"啧，还是求知之神的方法好，我以前根本不敢想，原来与魔网沟通会是这么简单的事情。\""
    },
    {
      "segment_id": "0021",
      "type": "paragraph",
      "source": "培特在搭建【奥术飞弹】法术模型的时候忍不住感叹。\n如果说以前他用向魔法女神祈祷的方式调动魔网是低声下气地去申请、求着魔网回应他的诉求，能使用多少奥术能量全看魔网的心情。\n那么现在的培特就仿佛是在向魔网发号施令一般，只要他心意一动，流动的奥术能量就会排布成他需要的样子。"
    },
    {
      "segment_id": "0022",
      "type": "paragraph",
      "source": "【奥术飞弹】只是个基础的1阶攻击型法术，需要搭建的法术模型并不复杂，何况还有诺文给予的现成模型可以照着\"临摹\"，更是大幅度降低了难度。"
    },
    {
      "segment_id": "0023",
      "type": "paragraph",
      "source": "关键的节点布置完成后，培特便能清楚地感觉到奥术能量在他的手中逐渐汇聚。\n这道法术的具体效果培特在卡罗恩学院查阅资料的时候了解过。\n奥术会被约束成三颗明亮而小巧的紫色飞弹，随着施法者指定目标，飞弹会以惊人的速度冲向目标，并且会通过多变的飞行轨迹避开路上可能存在的障碍物。\n飞弹中蕴含的魔法能量在命中目标爆发时会形成强大的冲击力，其强度足以当场打翻一名普通成年人。\n毫无疑问，【奥术飞弹】算是法师最基础也是最好用的1阶攻击魔法。"
    },
    {
      "segment_id": "0024",
      "type": "dialogue",
      "source": "\"Arcane Missiles！\""
    },
    {
      "segment_id": "0025",
      "type": "paragraph",
      "source": "培特念动咒语，精神集中于那个拎着粗木棒砸门的带头壮汉，猛一抬手，三颗散发着亮丽紫光的飞弹便发出尖锐的呼啸声，划破空气朝着对方快速飞去！"
    },
    {
      "segment_id": "0026",
      "type": "author_note",
      "source": "更新掉落完成，小飞弹来啦，求推荐票月票，如果有的话，谢谢您哦~"
    }
  ]
}
```

## Output
Return ONLY valid JSON (no markdown, no explanation). Each segment has "source", "target", "notes".
DO NOT wrap in ```json.
DO NOT include any text before or after the JSON.
