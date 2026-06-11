# Translation Context Pack

## Project
- Branch: Dung Goi Ta Ta Than
- Title: Đừng Gọi Ta Tà Thần
- Author: Thủy Quả Trung Đích Đồng Thần
- Genre: fantasy / western_fiction
- Source language: zh
- Target language: vi

## Translation Rules
- Dịch đúng theo ngữ cảnh, tự nhiên như truyện tiếng Việt.
- Đặc biệt chú ý xưng hô của người dẫn truyện: bối cảnh phương Tây fantasy, giọng kể hiện đại, tự nhiên, có chút hài hước và mỉa mai nhẹ.
- Xưng hô giữa các nhân vật: Norven là thần, Pete là tín đồ — Norven dùng "ta", Pete dùng "cậu" hoặc gọi tên. Khi Norven tự độc thoại nội tâm, dùng "hắn" hoặc "Norven".
- Các tên riêng phương Tây giữ nguyên Latin (Norven, Pete Chinar, Hada, Caroen).
- Thuật ngữ Trung/Hán dùng Hán Việt khi phù hợp (thần lực, thần dụ, tín ngưỡng, dị biến).
- KHÔNG để sót chữ Hán/CJK trong bản dịch, trừ tên riêng được phép (Hada).
- KHÔNG tóm tắt thay cho dịch.
- KHÔNG thêm bình luận ngoài truyện.
- KHÔNG thêm giải thích tiếng Anh trong ngoặc.

## Forbidden
- Không để sót chữ Hán trong bản dịch, trừ proper name được phép.
- Không thêm giải thích tiếng Anh trong ngoặc.
- Không đổi segment_id.
- Không tóm tắt thay cho dịch.
- Không bỏ sót hoặc gộp segment.
- Không viết lại bố cục hoặc layout.

## Character Table
| Name | Source | Target | Type | Note |
|---|---|---|---|---|
| Norven | 诺文 | Norven | MC | Tà thần tri thức, xuyên không, giọng nội tâm hài hước |
| Pete Chinar | 培特·奇纳尔 | Pete Chinar | disciple | Học viên Học viện Caroen, tín đồ đầu tiên |
| Người áo choàng đen | 黑袍人 | Người áo choàng đen | group | Kẻ môi giới lừa người đến ổ dị biến |
| Nữ thần Ma pháp | 魔法女神 | Nữ thần Ma pháp | deity | Thần ma pháp chính thống |

## Glossary
| Term | Source | Target | Note |
|---|---|---|---|
| Thần quốc | 神国 | thần quốc | Không gian thần minh ngự trị |
| Thần lực | 神力 | thần lực | Năng lượng thần minh |
| Thần dụ | 神谕 | thần dụ | Lời chỉ dẫn từ thần |
| Mô hình ma pháp | 法术模型 | mô hình ma pháp | Cấu trúc ma pháp |
| Nhân quả luật | 因果律 | nhân quả luật | Luật nhân quả |
| Tín ngưỡng chi lực | 信仰之力 | tín ngưỡng chi lực | Sức mạnh từ lòng tin |
| Ban phúc | 赐福 | ban phúc | Thần ban ơn |
| Dị biến | 畸变 | dị biến | Biến dạng do thần lực hỗn loạn |
| Quái vật dị biến | 畸变怪 | quái vật dị biến | Quái vật do thần lực hỗn loạn |
| Cây công nghệ | 科技树 | cây công nghệ | Technology tree |
| Cân bằng thu chi | 收支平衡 | cân bằng thu chi | Balance income/expense |
| Tín đồ nông cạn | 浅信徒 | tín đồ nông cạn | Người mới tin, chưa sâu sắc |
| Ma lưới | 魔网 | Ma lưới | Mạng lưới ma pháp |
| 【Cơn Đói Khát của Hada】 | 【哈达之饥渴】 | 【Cơn Đói Khát của Hada】 | Ma pháp cấp ba |

## Previous Story Timeline (up to Chapter 4)
- Norven xuyên không thành tà thần trong thế giới fantasy phương Tây.
- Thần lực của Norven có vấn đề: ban thần lực trực tiếp sẽ làm tín đồ biến thành quái vật dị biến.
- Pete Chinar, học viên Học viện Caroen, bị lừa đến ổ dị biến, được Norven cứu.
- Norven đã thử nghiệm cơ chế ban thần lực qua Pete, phát hiện ra phương pháp "hack" Ma lưới.
- Pete đã thành công thi triển ma pháp cấp ba 【Cơn Đói Khát của Hada】 và tiêu diệt quái vật.

## IMPORTANT: Output Title Instruction
Tiêu đề chương trong bản dịch PHẢI là tiếng Việt tự nhiên. Tiêu đề gốc là "授人以渔", thành ngữ Trung Quốc. Hãy dịch tiêu đề chương này sang tiếng Việt tự nhiên, ngắn gọn, dùng cho filename và toc.title.

## Segments to Translate
```json
{
  "chapter_number": 5,
  "segments": [
    {"segment_id": "0001", "type": "title", "source": "# 第5章 授人以渔"},
    {"segment_id": "0002", "type": "paragraph", "source": "与此同时，远在神国的诺文也长长的舒了一口气。"},
    {"segment_id": "0003", "type": "paragraph", "source": ""果然，我的判断是正确的。""},
    {"segment_id": "0004", "type": "paragraph", "source": "培特·奇纳尔脑海凭空中出现的信息自然是由诺文亲手编写提供，目的则是为了验证诺文的一个推测。"},
    {"segment_id": "0005", "type": "paragraph", "source": "至于为什么要弄成一条条任务指引的样子，甚至还像模像样了搞一声"叮"，则是诺文临时想到的预防手段。"},
    {"segment_id": "0006", "type": "paragraph", "source": "毕竟他这明显邪神的神力画风，如果打算正经传教收集信徒的话，最好还是在外面包装一层看起来比较正常的皮肤，让自己在凡人眼里看起来像是个正经的神明。"},
    {"segment_id": "0007", "type": "paragraph", "source": "不然人家还以为自己是被某个邪神盯上了，万一搞个宁死不屈之类的操作，那诺文哭都没地方哭去。"},
    {"segment_id": "0008", "type": "paragraph", "source": "好吧，虽然从某种意义上来说，被诺文选中的凡人确实是被邪神盯上没错；"},
    {"segment_id": "0009", "type": "paragraph", "source": "但诺文觉得他自己应该不算邪神，至少他在尽可能地让自己不那么像个邪神。"},
    {"segment_id": "0010", "type": "paragraph", "source": "在培特身上进行的测试，最终也取得了让诺文相当满意的成果。"},
    {"segment_id": "0011", "type": "paragraph", "source": ""确认了！即便是所谓的神明伟力，在这个世界也要遵循某些规律，或者说，规则！""},
    {"segment_id": "0012", "type": "paragraph", "source": ""一开始我以为所谓的神力会直接将施放法术的能力给予信徒，他们不需要明白这个法术究竟是如何构筑、如何生效，只要消耗加持的神力就能成功释放出来，相当于因果律概念级的力量。""},
    {"segment_id": "0013", "type": "paragraph", "source": ""但从测试来看，情况恰恰相反，这个世界其实相当严谨。""},
    {"segment_id": "0014", "type": "paragraph", "source": ""施法的过程并没有消失，而是在神明响应信徒的请求后，以消耗自身的神力为代价，替代信徒完成了法术。""},
    {"segment_id": "0015", "type": "paragraph", "source": ""在我的视角里，施法的过程其实是完全透明的，每个步骤需要进行的特定动作、咒语，乃至法术模型的形状细节，如何将魔法能量按照对应的规则进行排布，甚至还有各种各样的进阶性知识。""},
    {"segment_id": "0016", "type": "paragraph", "source": ""这些东西完全与神力无关，它们是最基础的，整个世界都通用的知识！""},
    {"segment_id": "0017", "type": "paragraph", "source": ""如果一个凡人能够学会这些知识，那么他完全可以绕过向神明献上信仰，接收神力的步骤，凭借自己的努力来施法。""},
    {"segment_id": "0018", "type": "paragraph", "source": ""培特成功释放出了【哈达之饥渴】就能证明这一点！""},
    {"segment_id": "0019", "type": "paragraph", "source": ""但——正是因为有了向神明祈祷这种简单便捷的办法，导致凡人根本不需要付出多少努力！""},
    {"segment_id": "0020", "type": "paragraph", "source": ""毕竟他们遇到困难的时候，只要呼唤自己所信仰的神明，然后就能等待神明显灵，去帮他们解决掉困难。""},
    {"segment_id": "0021", "type": "paragraph", "source": "诺文意识到了这个世界在发展上和他前世出现巨大差别的关键。"},
    {"segment_id": "0022", "type": "paragraph", "source": "凡人文明的发展本来会遇到许多困难，最早期的部落时代面临的各种自然灾害、凶猛野兽、病毒瘟疫，乃至缺衣少食，这些都是可能给弱小的凡人招致灭顶之灾的严重问题，一个不慎可能就会导致整个部落的灭亡。"},
    {"segment_id": "0023", "type": "paragraph", "source": "在诺文原本的世界中，无数前人付出巨大的代价，努力发挥出属于凡人的聪明才智，一点点地总结规律、制造工具，最终才点出了繁茂的科技树，文明得以存续和发展。"},
    {"segment_id": "0024", "type": "paragraph", "source": "可是在诺文穿越到这个世界里，凡人的发展路线一开始就跑偏了！"},
    {"segment_id": "0025", "type": "paragraph", "source": "因为遇到任何困难都可以直接求助神明。"},
    {"segment_id": "0026", "type": "paragraph", "source": "而且神明有事是真上！"},
    {"segment_id": "0027", "type": "paragraph", "source": "那么凡人文明想要发展壮大，最值得研究的，无疑就是如何去更高效、更稳定地获得神明的回应了。"},
    {"segment_id": "0028", "type": "paragraph", "source": "至于研究知识，认识世界？"},
    {"segment_id": "0029", "type": "paragraph", "source": "明明有捷径可以走，为什么还要费时费力地去做"吃力不讨好"的事情呢？"},
    {"segment_id": "0030", "type": "paragraph", "source": ""啧……很难评价两种文明的发展模式究竟谁更优越，不过既然来到了这个世界，而且我的神力有这么大的问题，凡人向我祈祷获得的力量只会让他们被污染成畸变怪，那么留给我的选项也就只有一个了。""},
    {"segment_id": "0031", "type": "paragraph", "source": "诺文确定了他的思路。"},
    {"segment_id": "0032", "type": "paragraph", "source": ""没法授人以鱼，但我可以授人以渔！""},
    {"segment_id": "0033", "type": "paragraph", "source": ""只要有信徒向我祈祷，我能获得他们需要的事物的相关知识和信息，然后我可以通过神谕之类的形式，指引凡人，让他们一步步地凭借着自己的努力来亲手完成。""},
    {"segment_id": "0034", "type": "paragraph", "source": ""而且，我还有一个独特的优势。""},
    {"segment_id": "0035", "type": "paragraph", "source": ""神力！""},
    {"segment_id": "0036", "type": "paragraph", "source": ""即使是神明也不能无代价无条件地回应每一位祂的信徒的诉求，毕竟神迹需要支付神力才能展现，而神力是凡人的信仰转化而成。""},
    {"segment_id": "0037", "type": "paragraph", "source": ""凡人在祈祷时能提供的信仰，往往又比神赐时消耗的要少得多。""},
    {"segment_id": "0038", "type": "paragraph", "source": ""所以其他神明为了保持一定的'收支平衡'，祂们没法有求必应，必然要在信徒中划分出三六九等，这才能维持神力和信仰转化的稳定。""},
    {"segment_id": "0039", "type": "paragraph", "source": ""而我不一样！""},
    {"segment_id": "0040", "type": "paragraph", "source": ""我所要做的仅仅只是将相关的知识以神谕的形式包装好传达下去，再关注着信徒的状态，根据他们的进展，随时更新神谕的信息。""},
    {"segment_id": "0041", "type": "paragraph", "source": ""这个过程需要消耗的神力比起神赐来说要少的多！""},
    {"segment_id": "0042", "type": "paragraph", "source": "诺文能明确地感知到两者的区别。"},
    {"segment_id": "0043", "type": "paragraph", "source": "如果把洞窟里那些黑袍人们一开始集体向他祈祷时提供的信仰之力传化出的神力算作10个单位。"},
    {"segment_id": "0044", "type": "paragraph", "source": "那么第一次降下赐福导致黑袍人畸变的时候就消耗掉了最少30个单位的神力！"},
    {"segment_id": "0045", "type": "paragraph", "source": "换言之，这次赐予对诺文来说就是纯纯的负收益，信徒祈祷赚来的神力不够，他还得自己往里搭上不少，而且仅仅只让一名凡人获得了"力量"。"},
    {"segment_id": "0046", "type": "paragraph", "source": "可后来给培特·奇纳尔提供有关【哈达之饥渴】法术知识的神谕时，整个过程则仅仅只消耗了大概1点神力，理论上来讲，诺文甚至还有净赚！"},
    {"segment_id": "0047", "type": "paragraph", "source": ""虽然我的信徒没法像其他神明的信徒那样快速获得力量，但我也有自己的独特优点嘛，"诺文满意地点了点头，"我跟其他那些画饼神明不一样，只要信徒们愿意按照我提供的方法去努力，那么他们最终一定会有所回报！""},
    {"segment_id": "0048", "type": "paragraph", "source": ""其他神明是靠着大量祈祷获取信仰，但最终肯定只能从中培养出几个高质量的信徒，因为祂们的神力有限，支撑不起培养更多信徒的消耗，大部分信徒都只能捡点边角料，没法享受到神明的特别关爱。""},
    {"segment_id": "0049", "type": "paragraph", "source": ""我完全可以开辟一条不同的新赛道！""},
    {"segment_id": "0050", "type": "paragraph", "source": ""主打以量取胜！""},
    {"segment_id": "0051", "type": "paragraph", "source": ""只要愿意为我提供信仰的，都能从我这里得到他们应得的奖励！""},
    {"segment_id": "0052", "type": "paragraph", "source": ""虽然一开始的效果不像其他神明那么立竿见影，但胜在量大管饱，还足够持久！""},
    {"segment_id": "0053", "type": "paragraph", "source": ""至于该如何找到更多的信徒嘛……""},
    {"segment_id": "0054", "type": "paragraph", "source": "诺文缓缓将目光投向了他目前唯一的浅信徒——培特·奇纳尔。"},
    {"segment_id": "0055", "type": "paragraph", "source": "推荐票对我真的很重要，如果觉得不错请投个票吧，谢谢您~！"}
  ]
}
```

## Required Output Format
Return valid JSON only with this schema:
```json
{
  "chapter_number": 5,
  "chapter_title_vi": "...",
  "segments": [
    {
      "segment_id": "0001",
      "source": "...",
      "target": "...",
      "notes": ""
    }
  ]
}
```

IMPORTANT:
- `chapter_title_vi` MUST be the Vietnamese title used for filename and toc.title. Translate the chapter title naturally to Vietnamese. Do NOT keep "授人以渔" as-is.
- Each segment MUST have the correct segment_id matching the input. Do not skip any segment.
- Do NOT add or remove segments.
- Do NOT include CJK characters in target text except for allowed proper names in 【】 brackets like 【Hada】.
