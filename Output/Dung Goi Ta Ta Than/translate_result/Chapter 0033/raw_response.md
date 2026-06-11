I will start by listing the files in the directory to understand the project structure and look for any existing translations, glossary files, or templates that will help me maintain consistency.
I will list the contents of the `Source` directory to see if there are other chapters, and `$TRANS_DIR` to understand what that directory is for.
I will list the contents of `$TRANS_DIR` and `Global State` to check for translation tools, scripts, or stored reference files like glossaries.
I will list the contents of `$TRANS_DIR` to see what metadata or configuration files are present there.
I will check the `Output` directory to see if there are any previously translated chapters, which can help me align with the formatting and style used so far.
I will list the contents of `Output/Dung Goi Ta Ta Than` to find the existing translation files for this specific project.
I will list the contents of the `translate_result` directory to see the translated files for this project.
I will check what files exist inside the `Chapter 0033` directory to see if a translation already exists there.
I will view the files inside the `Chapter 0032` directory to see how translations were saved previously.
I will view `translated_segments.json` in `Chapter 0032` to understand the JSON schema and how paragraphs/lines are split and ID'd.
I will list the contents of `pre_trans` for Chapter 0033 to check if there is an existing split or source file for it.
I will check `pre_trans/Chapter 0033` to see if there is any pre-processed segment file for Chapter 33.
I will view the `source.md` in `pre_trans/Chapter 0033` to see the exact text content of Chapter 33.
I will check the `ai_review.json` file in `pre_trans/Chapter 0033` to see if there is pre-processed translation data or segment segmentation.
I will run a grep search for the task name "吾主的真理普照" to see its exact translation in previous chapters and maintain consistency.
I will perform a search in `Chapter 0018/translated_segments.json` for "Chân lý" or "Chúa ta" to verify the exact Vietnamese translation of the task "吾主的真理普照大地".
I will verify the translation of this task in Chapter 20 to ensure it is identical.
I will check Chapter 23's translation of the same task name to see which version is used there.
I will view the `state/Glossary.md` file to see the project's glossary.
I will search for "求知之" to see how "求知之神" is translated in the existing Vietnamese chapters.
I will check how "求知之神" was translated in the actual translated files (e.g. Chapter 7 or Chapter 32) to see if "Thần Cầu Tri" or "Thần Tri Thức" is the preferred translation.
I will search for "Thần Tri Thức" to confirm it is the used translation.
I will view `glossary_scan.json` for Chapter 33 to see if it lists terms and their contexts.
I will list the contents of the `pre_trans/Chapter 0032` directory to see if there is a `segments.json` or how segment files were structured there before translation.
I will check the `working` directory to see if there are any working files for Chapter 33.
I will view `pre_trans/Chapter 0032/segments.json` to see the exact structure of segments, particularly if the segment IDs are numbers, and how paragraphs are grouped.
I will list the contents of the `working/pre_trans` directory to see if any segment definitions are located there.
I will view `context_pack.md` in `pre_trans/Chapter 0033` to see if there's any pre-segmented content or additional contextual guidelines.
I will view the rest of `context_pack.md` starting from line 200 to see if it has the segments at the bottom.
I will view `translation_config.json` to check for specific configuration properties, character name mapping, or rules.
I will check how the tavern name "莫尼兄弟酒馆" was translated in the previous chapters.
I will check the `Script` directory to see if there is a validation script or a translation pipeline script, to check if they expect the files to be written in a specific path.
{
  "chapter_number": 33,
  "chapter_title_vi": "Chương 33: Lộ trình Chiến Sĩ",
  "segments": [
    {
      "segment_id": 1,
      "source": "神国的诺文全程关注着他的两名信徒。\n“好家伙，这套路玩的不错啊！”\n诺文没想到，培特居然能无师自通地想出自己当“托”来诱惑其他人加入教会的办法。\n玩套路打配合的自然是培特和蕾娜两人。\n先是通过【真名知晓】跟【潜行】的配合，给目标织造一个第一印象，让对方感觉自己是被人选中的。\n用写有名字的纸条引起对方的好奇心。\n声称说有办法帮助人成为职业者。\n一旦有人因此而有了想法，就算上钩了！",
      "target": "Norven ở Thần quốc theo dõi toàn bộ quá trình của hai tín đồ.\n“Khá thật, màn kịch này diễn hay đấy!”\nNorven không ngờ Pete lại có thể tự thông suốt mà nghĩ ra cách tự mình làm “cò mồi” để lôi kéo người khác gia nhập giáo hội.\nNgười phối hợp diễn kịch tự nhiên là hai người Pete và Lena.\nĐầu tiên là thông qua việc phối hợp giữa 【Biết Tên Thật】 và 【Tiềm Hành】 để tạo ấn tượng ban đầu cho mục tiêu, khiến đối phương có cảm giác mình là người được chọn.\nDùng mảnh giấy viết tên để khơi gợi sự tò mò của đối phương.\nTuyên bố có cách giúp người ta trở thành Chức nghiệp giả.\nMột khi có ai đó nảy sinh ý định vì chuyện này thì coi như đã cắn câu!"
    },
    {
      "segment_id": 2,
      "source": "等到他们来了莫尼兄弟酒馆，培特又装做同样是收到纸条的一员，按着提前设计的“剧本”，跟蕾娜一应一和。\n诺文能想象出来，就算来人原本抱有警惕，亲眼看到有人先去体验了相关的神术，甚至靠着信仰求知之神成为了职业者，警惕心也会被大幅度降低。\n培特和蕾娜计划的套路便是如此，\n人都是从众的，倘若没有个出头鸟，大家可能都不敢相信。\n毕竟嘴上说的和实际做的可能是完全两回事，没有看到真正的仪式和信仰带来的效果，谁也不敢冒然就相信蕾娜说的话。\n可是有培特带头做了表率，而且取得了切实的好处后。\n那情况可就不一样了！",
      "target": "Chờ đến khi họ tới quán rượu Moni Brotherhood, Pete lại đóng giả làm một trong những người nhận được giấy viết tên, tung hứng nhịp nhàng với Lena theo “kịch bản” đã dựng sẵn.\nNorven có thể tưởng tượng ra được, cho dù người đến ban đầu ôm lòng cảnh giác, nhưng khi tận mắt nhìn thấy có người đi trải nghiệm thần thuật liên quan trước, thậm chí nhờ tín ngưỡng Thần Tri Thức mà trở thành Chức nghiệp giả, thì sự cảnh giác cũng sẽ giảm đi đáng kể.\nMàn kịch mà Pete và Lena lên kế hoạch chính là như vậy.\nCon người đều có tâm lý đám đông, nếu không có ai xung phong đi đầu, mọi người có lẽ đều không dám tin tưởng.\nDù sao nói miệng và thực tế làm là hai chuyện hoàn toàn khác nhau, nếu chưa thấy nghi thức và hiệu quả thực sự do tín ngưỡng mang lại, không ai dám mạo muội tin lời Lena nói.\nNhưng một khi đã có Pete đi đầu làm gương, hơn nữa còn đạt được lợi ích thực tế.\nThì tình hình đã hoàn toàn khác!"
    },
    {
      "segment_id": 3,
      "source": "诺文很快收到了数道指向他的信仰来源！\n正是被培特和蕾娜忽悠到莫尼兄弟酒馆的那几位。\n对此，诺文自然是来者不拒！\n他现在正是缺神力的时候，信徒愿意发挥主观能动性，帮他招揽信徒，诺文高兴还来不及呢。\n按照先前发布的那条可重复的任务，【吾主的真理普照大地】，4名新信徒，诺文在接受信仰的同时，分别送出10点知识点数。\n当然，培特和蕾娜应得的奖励也没落下。\n【吾主的真理普照大地】被诺文设定为周常任务，每周只能触发并完成一次，因此两人各自拿到5点知识点数。",
      "target": "Norven nhanh chóng nhận được vài luồng tín ngưỡng hướng về phía mình!\nChính là từ những người bị Pete và Lena dụ dỗ tới quán rượu Moni Brotherhood.\nĐối với việc này, Norven tự nhiên là ai tới cũng không cự tuyệt!\nHiện tại hắn đang rất thiếu thần lực, tín đồ chủ động phát huy tính năng động giúp hắn chiêu mộ thêm người, Norven mừng còn không kịp.\nTheo nhiệm vụ có thể lặp lại đã công bố trước đó là 【Chân lý của Chúa ta soi sáng đại địa】, với 4 tín đồ mới, Norven vừa tiếp nhận tín ngưỡng, vừa gửi đi mỗi người 10 Điểm Tri Thức làm quà gặp mặt.\nDĩ nhiên, phần thưởng xứng đáng của Pete và Lena cũng không bị bỏ sót.\n【Chân lý của Chúa ta soi sáng đại địa】 được Norven thiết lập làm nhiệm vụ hằng tuần, mỗi tuần chỉ có thể kích hoạt và hoàn thành một lần, do đó mỗi người nhận được 5 Điểm Tri Thức."
    },
    {
      "segment_id": 4,
      "source": "新的信徒没法立刻给诺文提供信仰。\n虽然给他们奖励的10知识点数对诺文来说是纯支出，属于他免费送给的新人的“福利”。\n相当于诺文自掏腰包，提前超发。\n但诺文并不担心这部分超发的“福利”会打水漂。\n“知识点数”的本质是信徒从诺文这里换取各种信息的资源。\n而信息是一种可以复用的资源。\n信徒们能直观地得知，他们想从诺文这里得到回应，需要花费多少知识点数。\n初期运行的时候，诺文需要准备一部分神力作为前期成本，用来发动他的权柄，得到信徒们需要的知识。\n不过，等到信徒数量多起来，新信徒需要的知识，很大一部分都会和老信徒重合。\n每一次复用，诺文都能收回一部分他超发的知识点数。\n长远来看，他的收入一定会大于支出。\n至于为什么要给新人提供福利？\n自然是要用这点福利作为甜头，让新的信徒体验到这份信仰的好处！",
      "target": "Tín đồ mới chưa thể lập tức cung cấp đức tin cho Norven.\nMặc dù 10 Điểm Tri Thức thưởng cho họ đối với Norven mà nói là khoản chi thuần túy, thuộc về “phúc lợi” tặng miễn phí cho người mới.\nTương đương với việc Norven tự bỏ tiền túi ra để phát hành vượt mức từ trước.\nThế nhưng Norven không hề lo lắng phần “phúc lợi” phát hành vượt mức này sẽ đổ sông đổ biển.\nBản chất của “Điểm Tri Thức” chính là tài nguyên để tín đồ đổi lấy các loại thông tin từ Norven.\nMà thông tin lại là một loại tài nguyên có thể tái sử dụng.\nCác tín đồ có thể biết một cách trực quan rằng họ cần tiêu tốn bao nhiêu Điểm Tri Thức để nhận được phản hồi từ Norven.\nKhi mới vận hành, Norven cần chuẩn bị một phần thần lực làm chi phí ban đầu, dùng để kích hoạt quyền năng của mình nhằm có được tri thức mà các tín đồ cần.\nTuy nhiên, khi số lượng tín đồ tăng lên, phần lớn tri thức mà tín đồ mới yêu cầu sẽ trùng lặp với tín đồ cũ.\nMỗi lần tái sử dụng như vậy, Norven lại có thể thu hồi một phần Điểm Tri Thức mà hắn đã phát hành vượt mức.\nVề lâu về dài, thu nhập của hắn chắc chắn sẽ lớn hơn chi tiêu.\nCòn về việc tại sao phải cung cấp phúc lợi cho người mới?\nTất nhiên là muốn dùng chút phúc lợi này làm mật ngọt dụ dỗ, để các tín đồ mới trải nghiệm được lợi ích của tín ngưỡng này!"
    },
    {
      "segment_id": 5,
      "source": "……\n布兰登跟着蕾娜念完祷词，瞬间得到了求知之神的回应。\n脑海中突然出现的信息把他给吓了一跳。\n整个人都抖了一下。",
      "target": "……\nBrandon đọc xong lời cầu nguyện theo Lena, lập tức nhận được phản hồi từ Thần Tri Thức.\nLuồng thông tin đột ngột xuất hiện trong đầu làm hắn giật nảy mình.\nCả người run lên một cái."
    },
    {
      "segment_id": 6,
      "source": "毕竟他以前去教会向辉光之神献上信仰的时候，可不会有什么神谕降下，只能感觉身体变得暖洋洋的。\n按照辉光教会 of 教士的说法。\n这是辉光之神赐给信徒的祝福。\n祝福的效果是会让人变得身体强健，不容易被邪恶的气息影响。\n除此之外，没了！\n他每天在家里做日常礼拜，效果也仅仅只是维持祝福不减弱消散罢了。      像他这样的普通信徒，辉光之神根本不会特意投下注视，更别提神谕了。\n结果在求知之神这里，他才刚刚成为信徒，就能直接收到神谕？！",
      "target": "Dù sao trước đây khi hắn tới giáo hội dâng hiến tín ngưỡng cho Thần Huy Quang, làm gì có thần dụ nào giáng xuống, hắn chỉ cảm nhận được cơ thể trở nên ấm áp mà thôi.\nTheo cách nói của các giáo sĩ thuộc Giáo Hội Huy Quang.\nĐây là lời chúc phúc mà Thần Huy Quang ban tặng cho tín đồ.\nHiệu quả của lời chúc phúc là giúp cơ thể tráng kiện hơn, không dễ bị ảnh hưởng bởi những luồng khí tà ác.\nNgoài cái đó ra thì hết!\nMỗi ngày hắn làm lễ bái ở nhà, hiệu quả cũng chỉ là để duy trì lời chúc phúc không bị suy yếu hay tiêu tán mà thôi.\nNhững tín đồ bình thường như hắn, Thần Huy Quang căn bản sẽ không đặc biệt để mắt tới, chứ đừng nói đến việc giáng thần dụ.\nThế mà ở chỗ Thần Tri Thức, hắn mới chỉ vừa trở thành tín đồ đã có thể trực tiếp nhận được thần dụ sao?!"
    },
    {
      "segment_id": 7,
      "source": "“不用紧张，这是正常现象。”\n收到【吾主的真理普照大地】任务完成的信息，蕾娜便知道布兰登已经成为求知之神的信徒。\n就像培特曾经对她做的那样，这回她充当了引路人的身份。\n“放心地向吾主祈祷吧，告诉祂你想知道的事情。”\n“吾主会馈赠你相应的知识，当然，主的真理不是免费的，需要消耗你拥有的知识点数去兑换。”",
      "target": "“Đừng căng thẳng, đây là hiện tượng bình thường.”\nNhận được thông báo hoàn thành nhiệm vụ 【Chân lý của Chúa ta soi sáng đại địa】, Lena liền biết Brandon đã trở thành tín đồ của Thần Tri Thức.\nGiống như việc Pete từng làm với cô trước đây, lần này cô đóng vai trò là người dẫn đường.\n“Hãy yên tâm cầu nguyện với Chúa ta, nói cho Ngài biết điều anh muốn biết.”\n“Chúa ta sẽ ban tặng cho anh tri thức tương ứng. Tất nhiên, chân lý của Ngài không phải là miễn phí, cần phải tiêu hao Điểm Tri Thức mà anh sở hữu để trao đổi.”"
    },
    {
      "segment_id": 8,
      "source": "布兰登思考了一会。\n“求知之神在上，请问，我该怎么做，才能成为一名强大的战士。”\n他刚刚已经做完了天赋检测，结果跟他预料的差不多，他跟几位主神的亲和度都不高。\n这种情况，要么放弃走评级职业者 of 路子，要么……就是开发自己体内的潜能，尝试着激发并驾驭怒气，成为一名战士。",
      "target": "Brandon suy nghĩ một lát.\n“Thần Tri Thức tôn quý, xin hỏi con phải làm thế nào mới có thể trở thành một Chiến Sĩ mạnh mẽ?”\nHắn vừa mới hoàn thành bài kiểm tra thiên phú, kết quả cũng tương tự như hắn dự liệu, độ tương thích của hắn với các vị Chủ Thần đều không cao.\nTrong tình huống này, hoặc là từ bỏ con đường trở thành Chức nghiệp giả có xếp hạng, hoặc là... khai phá tiềm năng bên trong cơ thể, cố gắng khơi gợi và kiểm soát nộ khí để trở thành một Chiến Sĩ."
    },
    {
      "segment_id": 9,
      "source": "布兰登本来就不怎么喜欢那些需要天天做礼拜、认认真真向对应神明祈祷的职业路线。\n因为他觉得神明好像并不怎么关爱他，他能从神明那里得到的只是人人都有的最基础的赐福。\n他的梦想是仗剑走遍大陆，四处冒险，最好能留下属于自己的传说故事，光凭那点神明的基础赐福，肯定不够。",
      "target": "Brandon vốn dĩ chẳng mấy thích thú với những lộ trình nghề nghiệp đòi hỏi phải làm lễ bái hằng ngày, thành kính cầu nguyện trước vị thần tương ứng.\nBởi vì hắn cảm thấy thần linh dường như chẳng hề đoái hoài gì đến mình, thứ hắn có thể nhận được từ thần linh chỉ là chúc phúc cơ bản nhất mà ai ai cũng có.\nƯớc mơ của hắn là mang kiếm đi khắp lục địa, phiêu lưu khắp nơi, tốt nhất là có thể để lại truyền thuyết của riêng mình, mà nếu chỉ dựa vào chút chúc phúc cơ bản của thần linh thì chắc chắn là không đủ."
    },
    {
      "segment_id": 10,
      "source": "战士是大陆上唯一一个不依靠神明力量的评级职业。\n这条路线的修行方式，要学会驾驭怒气的力量，在各种战技中附上怒气，爆发出强横的破坏力。\n虽说战士不要求什么与神明的亲和度，但想成为战士，难度可一点都不低。\n怒气这东西，会就是会，不会就是不会。\n人在极度愤怒的情况下，可以爆发出比平时更强的力量。\n但这不代表成功驾驭了怒气。",
      "target": "Chiến Sĩ là nghề nghiệp có xếp hạng duy nhất trên lục địa không cần dựa vào sức mạnh của thần linh.\nPhương thức tu luyện của lộ trình này là phải học cách kiểm soát sức mạnh của nộ khí, truyền nộ khí vào các loại chiến kỹ, bộc phát ra sức tàn phá mạnh mẽ.\nMặc dù Chiến Sĩ không đòi hỏi độ tương thích với thần linh, nhưng muốn trở thành Chiến Sĩ, độ khó lại chẳng hề thấp chút nào.\nCái thứ gọi là nộ khí này, biết dùng là biết dùng, không biết là không biết.\nCon người trong cơn cực kỳ phẫn nộ có thể bộc phát ra sức mạnh lớn hơn bình thường.\nNhưng điều này không có nghĩa là đã kiểm soát thành công nộ khí."
    },
    {
      "segment_id": 11,
      "source": "想在战士路线上达成1阶评级，最基本的要求就是对怒气的使用收放自如。\n在情绪起伏不大，依然能维持理智的前提下，掌控着怒气的力量，还得加持于战技。\n相比起向神明祈祷获取力量的那些职业者途径，如果亲和度足够高的话，信徒更容易得到对应的神力的回应，等于降低了难度。\n这也是为什么有条件的情况下，最好先做一次天赋检测仪式。可以确认自己跟哪位神明的亲和度更高，哪条路线难度更低。",
      "target": "Muốn đạt được xếp hạng cấp 1 trên lộ trình Chiến Sĩ, yêu cầu cơ bản nhất là phải sử dụng nộ khí thu phát tự nhiên.\nTrong điều kiện cảm xúc không dao động lớn và vẫn duy trì lý trí, người đó phải kiểm soát được sức mạnh của nộ khí, đồng thời gia trì nó vào chiến kỹ.\nSo với những con đường Chức nghiệp giả có được sức mạnh nhờ cầu nguyện thần linh, nếu độ tương thích đủ cao, tín đồ sẽ dễ dàng nhận được phản hồi từ thần lực tương ứng hơn, tương đương với việc giảm bớt độ khó.\nĐây cũng là lý do tại sao nếu có điều kiện, tốt nhất nên làm nghi thức kiểm tra thiên phú trước để xác định bản thân tương thích cao hơn với vị thần nào, lộ trình nào có độ khó thấp hơn."
    },
    {
      "segment_id": 12,
      "source": "战士之道则没有任何投机取巧的办法。\n只能靠自己的努力。\n驾驭不了怒气，那任何战技都是花架子，徒具其表。\n布兰登之前从未听说过有哪位神明能给信徒在战士之路上提供帮助。\n可是在收到求知之神的神谕后，他产生了希望。\n他以前也从来没听说过哪位神明会直接回应某位信徒的祈祷啊！\n或许……求知之神真的跟其他神明不一样？",
      "target": "Con đường Chiến Sĩ thì không có bất kỳ cách nào để giở trò khôn lỏi.\nChỉ có thể dựa hoàn toàn vào sự nỗ lực của chính mình.\nKhông kiểm soát được nộ khí, mọi chiến kỹ chỉ là hoa quyền thêu chân, chỉ có cái mã bên ngoài.\nBrandon trước đây chưa bao giờ nghe nói có vị thần nào có thể giúp đỡ tín đồ trên con đường Chiến Sĩ.\nThế nhưng sau khi nhận được thần dụ của Thần Tri Thức, hắn lại nảy sinh hy vọng.\nTrước đây hắn cũng chưa từng nghe nói vị thần nào sẽ trực tiếp phản hồi lời cầu nguyện của một tín đồ cả!\nCó lẽ... Thần Tri Thức thực sự khác biệt so với các vị thần khác?"
    },
    {
      "segment_id": 13,
      "source": "【检测到信徒诉求】\n【目标：战士修行之路起始，掌控怒气】\n【需求：3知识点数】\n布兰登激动地瞪大了眼睛。\n“真的可以！”\n……",
      "target": "【Phát hiện lời thỉnh cầu của tín đồ】\n【Mục tiêu: Khởi đầu con đường tu luyện Chiến Sĩ, kiểm soát nộ khí】\n【Yêu cầu: 3 Điểm Tri Thức】\nBrandon kích động trợn to hai mắt.\n“Thực sự được kìa!”\n……"
    }
  ]
}