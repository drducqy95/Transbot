import json

data = {
  "chapter_number": 17,
  "chapter_title_vi": "Chương 17: Nghệ thuật chính là vụ nổ",
  "segments": [
    {
      "segment_id": "0001",
      "source": "# 第17章 艺术就是爆炸",
      "target": "# Chương 17: Nghệ thuật chính là vụ nổ"
    },
    {
      "segment_id": "0002",
      "source": "三皇之书，伏羲、神农、黄帝之书，谓之《三坟》，言大道也。",
      "target": "Sách của Tam Hoàng, sách của Phục Hy, Thần Nông, Hoàng Đế, gọi là 《Tam Phần》, bàn về đại đạo."
    },
    {
      "segment_id": "0003",
      "source": "此三书乃是有史以来最古老的书籍，虽说时代是向前发展的，但不得不承认，今时修行者的实力不如古，《气坟》之强，也当的上炁道本源之名。",
      "target": "Ba cuốn sách này là những bộ sách cổ xưa nhất từ khi có lịch sử ghi chép lại, tuy nói thời đại luôn phát triển về phía trước, nhưng không thể không thừa nhận, thực lực của người tu hành thời nay không bằng thời cổ, sự cường đại của 《Khí Phần》 cũng hoàn toàn xứng với cái tên khởi nguồn của khí đạo."
    },
    {
      "segment_id": "0004",
      "source": "哪怕只是一点皮毛。",
      "target": "Cho dù chỉ là một chút da lông."
    },
    {
      "segment_id": "0005",
      "source": "真气之墙倾轧而至，神威如潮水般蜂拥而来，吞没四方。",
      "target": "Bức tường chân khí dồn ép kéo đến, thần uy như thủy triều tuôn trào ập tới, nuốt chửng bốn phương."
    },
    {
      "segment_id": "0006",
      "source": "姜离的神态首度变化，第一次察觉到逼命的威胁，他立时取出最大底牌，体内真气顿时空了四成。",
      "target": "Thần thái của Khương Ly lần đầu tiên biến đổi, cũng là lần đầu tiên hắn sát giác được uy hiếp bức mạng, hắn lập tức lấy ra con át chủ bài lớn nhất, chân khí trong cơ thể tức khắc vơi đi bốn phần."
    },
    {
      "segment_id": "0007",
      "source": "“丁丑延我寿，丁亥拘我魂。",
      "target": "“Đinh Sửu diên ngã thọ, Đinh Hợi câu ngã hồn."
    },
    {
      "segment_id": "0008",
      "source": "丁酉制我魄，丁未却我灾。",
      "target": "Đinh Dậu chế ngã phách, Đinh Mùi khước ngã tai."
    },
    {
      "segment_id": "0009",
      "source": "丁巳度我危，丁卯度我厄。",
      "target": "Đinh Tị độ ngã nguy, Đinh Mão độ ngã ách."
    },
    {
      "segment_id": "0010",
      "source": "甲子护我身，甲戌保我形。",
      "target": "Giáp Tý hộ ngã thân, Giáp Tuất bảo ngã hình."
    },
    {
      "segment_id": "0011",
      "source": "甲申固我命，甲午守我魂。",
      "target": "Giáp Thân cố ngã mệnh, Giáp Ngọ thủ ngã hồn."
    },
    {
      "segment_id": "0012",
      "source": "甲辰镇我灵，甲寅育我真。”",
      "target": "Giáp Thìn trấn ngã linh, Giáp Dần dục ngã chân.”"
    },
    {
      "segment_id": "0013",
      "source": "六丁六甲神咒迅速念诵，十二道金光骤然升空，在姜离头顶勾勒出巨大的符箓。",
      "target": "Lục Đinh Lục Giáp thần chú được nhanh chóng đọc lên, mười hai đạo kim quang đột ngột bay vút lên không trung, phác họa ra một tấm bùa chú khổng lồ trên đỉnh đầu Khương Ly."
    },
    {
      "segment_id": "0014",
      "source": "“赦！”",
      "target": "“Sắc!”"
    },
    {
      "segment_id": "0015",
      "source": "符箓降身，金光覆体，连同手上长剑都被包裹，整个人都成了一尊小金人。",
      "target": "Bùa chú giáng xuống người, kim quang bao phủ cơ thể, ngay cả thanh trường kiếm trên tay cũng bị bao bọc lại, cả người hắn biến thành một bức tượng vàng nhỏ."
    },
    {
      "segment_id": "0016",
      "source": "此前仅是催动符箓，就能让一干挑战者无力施为，现在姜离全力运用六丁六甲护身符，金光遍体，充盈内外，令他的筋力和体魄不下于修炼浑元功的张振阳，在防御上更是远远超过。",
      "target": "Trước đó chỉ là thôi động bùa chú đã có thể khiến đám người khiêu chiến vô lực thi triển, bây giờ Khương Ly dốc toàn lực vận dụng Lục Đinh Lục Giáp Hộ Thân Phù, kim quang phủ khắp toàn thân, tràn ngập từ trong ra ngoài, khiến cho gân cốt và thể phách của hắn không hề thua kém Trương Chấn Dương tu luyện Hồn Nguyên Công, về mặt phòng ngự lại càng vượt xa."
    },
    {
      "segment_id": "0017",
      "source": "甚至连心神都受到护持，和道果能力叠加，扛住了那窒息般的威压。",
      "target": "Thậm chí ngay cả tâm thần cũng được bảo vệ, xếp chồng cùng với năng lực của đạo quả, gánh vác được thứ uy áp khiến người ta hít thở không thông kia."
    },
    {
      "segment_id": "0018",
      "source": "“开。”",
      "target": "“Khai.”"
    },
    {
      "segment_id": "0019",
      "source": "长剑出鞘，姜离的双眼中倒映出无数真气流动的轨迹，剑刃携金光于气墙上疾走，如龙蛇行陆，每一次转折变化都切中真气流转之轨迹。",
      "target": "Trường kiếm xuất vỏ, trong đôi mắt Khương Ly phản chiếu quỹ tích lưu động của vô số luồng chân khí, lưỡi kiếm mang theo kim quang lao vút đi trên bức tường khí, như rồng rắn lướt trên đất liền, mỗi một lần chuyển hướng biến hóa đều chém trúng quỹ tích lưu chuyển của chân khí."
    },
    {
      "segment_id": "0020",
      "source": "吕忘机可说是姜离所遭遇的最强之敌，面对此人，姜离不敢有丝毫保留，符法、剑法，还有望气之术，都被他发挥到极限。",
      "target": "Lã Vong Cơ có thể nói là kẻ địch mạnh nhất mà Khương Ly từng gặp phải, đối mặt với người này, Khương Ly không dám giữ lại chút nào, bùa pháp, kiếm pháp, còn có thuật vọng khí, đều được hắn phát huy đến mức tận cùng."
    },
    {
      "segment_id": "0021",
      "source": "刃光和真气碰撞，发出不绝声响，只见一道如电剑光疾走而过，倾轧而至的气墙竟是被分裂成两截。",
      "target": "Ánh kiếm quang cùng chân khí va chạm, phát ra tiếng vang không ngớt, chỉ thấy một đạo kiếm quang như ánh chớp xẹt qua, bức tường khí đang dồn ép tới dĩ nhiên lại bị chia cắt thành hai nửa."
    },
    {
      "segment_id": "0022",
      "source": "“噌！”",
      "target": "“Keng!”"
    },
    {
      "segment_id": "0023",
      "source": "剑鸣铮铮，姜离一手负于背后，一手持剑踏前，一道道符箓从袖中飞出，缠绕剑身，一剑挥出，爆出重重火光。",
      "target": "Kiếm reo tranh tranh, một tay Khương Ly chắp sau lưng, một tay cầm kiếm bước lên phía trước, từng tấm bùa chú từ trong tay áo bay ra, quấn quanh thân kiếm, một kiếm vung ra, bộc phát từng luồng hỏa quang trùng trùng điệp điệp."
    },
    {
      "segment_id": "0024",
      "source": "“竟然还有余力激发符箓？”",
      "target": "“Vậy mà vẫn còn dư sức để kích hoạt bùa chú ư?”"
    },
    {
      "segment_id": "0025",
      "source": "吕忘机见状，赞声道。",
      "target": "Lã Vong Cơ thấy thế, lên tiếng khen ngợi."
    },
    {
      "segment_id": "0026",
      "source": "符箓若成，则可存储部分真气在载体上，载体越好，则存储真气量越大。激发之时，若只追求最低限度的威能，则只需使用这部分真气即可。",
      "target": "Bùa chú nếu như luyện thành, thì có thể lưu trữ một phần chân khí trên vật dẫn, vật dẫn càng tốt thì lượng chân khí lưu trữ càng lớn. Lúc kích hoạt, nếu chỉ theo đuổi mức uy năng thấp nhất, thì chỉ cần sử dụng bộ phận chân khí này là được."
    },
    {
      "segment_id": "0027",
      "source": "理论上，符箓准备的越多，符法修行者就越强。",
      "target": "Trên lý thuyết, chuẩn bị bùa chú càng nhiều, người tu hành bùa pháp sẽ càng mạnh."
    },
    {
      "segment_id": "0028",
      "source": "但实际上，激发符箓需以精神进行引导，并非拿到就可使用。越是高级的符箓消耗精神越大，且同一时刻激发的符箓越多，就越需要精细控制。",
      "target": "Nhưng trên thực tế, muốn kích hoạt bùa chú cần phải dùng tinh thần để dẫn dắt, chứ không phải cứ cầm lấy là dùng được ngay. Bùa chú cấp bậc càng cao thì tinh thần tiêu hao càng lớn, hơn nữa bùa chú kích hoạt trong cùng một lúc càng nhiều, thì lại càng cần phải khống chế một cách tinh vi."
    },
    {
      "segment_id": "0029",
      "source": "姜离已经使用了六丁六甲护身符这一高级符箓，却还有余力去使用火雷符，他的神元之强，实在是出乎吕忘机之预料。",
      "target": "Khương Ly đã sử dụng Lục Đinh Lục Giáp Hộ Thân Phù - một tấm bùa chú cao cấp như vậy, mà vẫn còn dư lực để sử dụng Hỏa Lôi Phù, thần nguyên của hắn mạnh mẽ tới mức quả thực nằm ngoài dự đoán của Lã Vong Cơ."
    },
    {
      "segment_id": "0030",
      "source": "但也仅是出乎预料。",
      "target": "Nhưng cũng chỉ là vượt ngoài dự đoán mà thôi."
    },
    {
      "segment_id": "0031",
      "source": "“顺逆同流。”",
      "target": "“Thuận Nghịch Đồng Lưu.”"
    },
    {
      "segment_id": "0032",
      "source": "吕忘机双掌相对，掌间有大量真气汇聚，凝成涡旋，吸住挥斩而来的长剑，甚至连剑身上爆出的火光都被强行压了回来，让透明涡旋化成赤色。",
      "target": "Hai lòng bàn tay của Lã Vong Cơ hướng vào nhau, lượng lớn chân khí hội tụ ở giữa hai tay ngưng tụ thành vòng xoáy, hút chặt lấy thanh trường kiếm đang chém tới, thậm chí ngay cả ánh lửa bùng nổ trên thân kiếm cũng bị cưỡng ép đè ngược trở lại, khiến cho vòng xoáy trong suốt hóa thành màu đỏ thẫm."
    },
    {
      "segment_id": "0033",
      "source": "顺逆两股劲力同时出现在涡旋之中，咬着长剑不放，吕忘机右脚后撤，双手侧移，真气涡旋吸附着长剑，也拉着姜离猛地往前一扯。",
      "target": "Hai luồng kình lực thuận và nghịch đồng thời xuất hiện bên trong vòng xoáy, cắn chặt lấy thanh trường kiếm không buông, chân phải của Lã Vong Cơ lùi về sau, hai tay dời sang ngang, vòng xoáy chân khí hút chặt trường kiếm, đồng thời cũng kéo thốc Khương Ly giật mạnh về phía trước."
    },
    {
      "segment_id": "0034",
      "source": "“锵！”      被金光覆盖的精钢长剑竟是被真气涡旋生生绞断，而吕忘机则是双掌一转，和残剑平行，同时印向姜离胸腹。",
      "target": "“Keng!” Trường kiếm tinh cương được bao bọc bởi kim quang dĩ nhiên lại bị vòng xoáy chân khí sống sượng vặn gãy, mà Lã Vong Cơ thì xoay hai bàn tay song song với tàn kiếm, đồng thời ấn thẳng về phía ngực bụng Khương Ly."
    },
    {
      "segment_id": "0035",
      "source": "“嘭！”",
      "target": "“Bành!”"
    },
    {
      "segment_id": "0036",
      "source": "危急关头，姜离果断弃剑，同时左手也不再负于身后，双手拦截，以追风掌阻在胸腹之前，和吕忘机双掌碰撞。",
      "target": "Vào thời khắc nguy cấp, Khương Ly quả quyết bỏ kiếm, đồng thời tay trái cũng không còn chắp sau lưng nữa, hai tay đánh chặn, tung Truy Phong Chưởng chặn ngay trước ngực bụng, va chạm với hai chưởng của Lã Vong Cơ."
    },
    {
      "segment_id": "0037",
      "source": "但一方是蓄势而为，另一方则是仓促防御，加上吕忘机功力远胜姜离，且姜离此刻双臂不便发力，四掌接触，姜离双臂被掌劲推着撞在自己身上，发出闷响，身上金光一阵晃动。",
      "target": "Nhưng một bên là tụ thế mà tung đòn, bên còn lại thì vội vàng phòng ngự, cộng thêm công lực của Lã Vong Cơ vượt xa Khương Ly, lại thêm lúc này hai cánh tay của Khương Ly không tiện phát lực, bốn bàn tay vừa tiếp xúc, hai cánh tay của Khương Ly đã bị chưởng kình đẩy lùi đập mạnh vào cơ thể mình, phát ra tiếng vang trầm đục, kim quang trên người rung lên một trận."
    },
    {
      "segment_id": "0038",
      "source": "若非有六丁六甲符护身，这一击，姜离便要遭受重创。",
      "target": "Nếu không có Lục Đinh Lục Giáp Phù hộ thân, một kích này đã đủ khiến Khương Ly phải chịu trọng thương."
    },
    {
      "segment_id": "0039",
      "source": "姜离遭受重击，向后飞退丈许远，又双足着地，在风云台上飞速向后拖行！",
      "target": "Khương Ly dính đòn trọng kích, bay ngược về phía sau khoảng chừng một trượng, hai chân lại chạm đất, cày nhanh về phía sau trên đài Phong Vân!"
    },
    {
      "segment_id": "0040",
      "source": "“胜负已定！”山崖上的罗仪终是松了一口气，“姜离左手已出，吕忘机绝对不会让他继续使用楼观剑法料敌机先，他就算有六丁六甲符护体，也是难以逆转胜负之势。”",
      "target": "“Thắng bại đã định!” La Nghi đứng trên vách núi rốt cuộc cũng thở phào một hơi, “Tay trái của Khương Ly đã xuất, Lã Vong Cơ tuyệt đối sẽ không để cho hắn tiếp tục sử dụng Lâu Quan Kiếm Pháp tính trước bước đi của địch nữa, hắn cho dù có Lục Đinh Lục Giáp Phù hộ thể, cũng rất khó đảo ngược được thế cục thắng bại.”"
    },
    {
      "segment_id": "0041",
      "source": "果不其然，在姜离退出两丈之际，一声呜然突然响起，吕忘机左掌对向姜离，五指齐张，掌心内陷，真气疾旋，发出呜然之声，一股无形大力扯住急退的姜离，将他再度拉向吕忘机。",
      "target": "Đúng như dự đoán, khi Khương Ly mới lui lại được hai trượng, một tiếng vù vù đột nhiên vang lên, lòng bàn tay trái của Lã Vong Cơ hướng về phía Khương Ly, năm ngón tay xòe rộng, lòng bàn tay hơi lõm vào trong, chân khí xoáy mạnh tạo ra âm thanh vù vù, một cỗ sức mạnh vô hình tóm lấy Khương Ly đang lùi nhanh, một lần nữa kéo hắn về phía Lã Vong Cơ."
    },
    {
      "segment_id": "0042",
      "source": "擒龙功！",
      "target": "Cầm Long Công!"
    },
    {
      "segment_id": "0043",
      "source": "后退的身影如风筝般被拉扯向前，三丈之距飞速缩短。",
      "target": "Bóng người đang lui về sau giống như một con diều bị kéo mạnh lên phía trước, khoảng cách ba trượng bị rút ngắn với tốc độ chóng mặt."
    },
    {
      "segment_id": "0044",
      "source": "姜离人在滑行，双袖齐震，数不尽的火雷符从他袖中飞出，先一步被擒龙功吸摄而去。",
      "target": "Người Khương Ly vẫn đang trượt đi, hai tay áo đồng thời chấn động, vô số Hỏa Lôi Phù từ trong tay áo của hắn bay ra, đi trước một bước bị Cầm Long Công hút tới."
    },
    {
      "segment_id": "0045",
      "source": "每一道符箓都发出灵光，火光重重亮起。",
      "target": "Mỗi một tấm bùa chú đều phát ra linh quang, tầng tầng lớp lớp ánh lửa bừng sáng."
    },
    {
      "segment_id": "0046",
      "source": "“轰轰轰轰······”",
      "target": "“Ầm ầm ầm ầm...”"
    },
    {
      "segment_id": "0047",
      "source": "连环霹雳之声炸响，多达三十张火雷符被激发，姜离的神元之强，着实令人咋舌。",
      "target": "Âm thanh như sấm sét liên hoàn nổ tung, có tới ba mươi tấm Hỏa Lôi Phù được kích hoạt, thần nguyên của Khương Ly mạnh mẽ tới nhường nào, quả thực khiến người ta phải tặc lưỡi."
    },
    {
      "segment_id": "0048",
      "source": "但吕忘机之强，亦是叫人侧目。",
      "target": "Nhưng sự cường đại của Lã Vong Cơ, cũng khiến cho người khác phải ghé mắt nhìn lại."
    },
    {
      "segment_id": "0049",
      "source": "“杂乱混淆。”",
      "target": "“Tạp loạn hỗn hào.”"
    },
    {
      "segment_id": "0050",
      "source": "吕忘机察觉到火雷符虽多，但爆炸却是隐有对冲干扰的迹象，显然是对方被迫出左手，来不及以楼观剑法进行精密计算。",
      "target": "Lã Vong Cơ nhận ra Hỏa Lôi Phù tuy nhiều, nhưng vụ nổ lại có dấu hiệu xung đột và cản trở lẫn nhau, hiển nhiên là đối phương bị ép tung ra tay trái, không kịp dùng Lâu Quan Kiếm Pháp tiến hành tính toán tỉ mỉ."
    },
    {
      "segment_id": "0051",
      "source": "“控鹤。”",
      "target": "“Khống Hạc.”"
    },
    {
      "segment_id": "0052",
      "source": "只见吕忘机右掌前推，身前如有一堵无形墙壁，重重火光撞在上面，成了一个截面，难越雷池半步。",
      "target": "Chỉ thấy bàn tay phải của Lã Vong Cơ đẩy về phía trước, thân trước tựa như có một bức tường vô hình hiện ra chắn ngang, ngập tràn ánh lửa đâm sầm lên đó, tạo thành một mặt cắt, khó lòng vượt qua lằn ranh này được nửa bước."
    },
    {
      "segment_id": "0053",
      "source": "甚至于，一股大力前袭，三十张火雷符所形成的爆炸被一掌轰散。",
      "target": "Thậm chí là, một cỗ cự lực xông đến, vụ nổ hình thành từ ba mươi tấm Hỏa Lôi Phù bị một chưởng đánh cho tan tành."
    },
    {
      "segment_id": "0054",
      "source": "“砰！”",
      "target": "“Bùm!”"
    },
    {
      "segment_id": "0055",
      "source": "爆开的火雨在飞洒，吕忘机大袖飘飘，举步向前，周身真气鼓荡，所过之处火雨皆辟，然而当他身前的火光皆散之时，出现在他眼中的却是万分惊人的一幕。",
      "target": "Mưa lửa nổ tung bay lả tả, hai ống tay áo rộng của Lã Vong Cơ phất phơ trong gió, cất bước tiến về phía trước, chân khí toàn thân cuồn cuộn, đi tới đâu mưa lửa đều dạt ra hai bên tới đó, thế nhưng khi tất cả ánh lửa trước người gã tan hết, cảnh tượng đập vào mắt gã lại là một màn kinh người tột độ."
    },
    {
      "segment_id": "0056",
      "source": "符箓，视线所及都是符箓。",
      "target": "Bùa chú, ngập tràn trong tầm mắt đều là bùa chú."
    },
    {
      "segment_id": "0057",
      "source": "无数的符箓随风乱舞，明黄的颜色充塞视线。",
      "target": "Vô số tấm bùa chú múa lượn cuồng loạn theo gió, màu vàng rực lấp đầy tầm nhìn."
    },
    {
      "segment_id": "0058",
      "source": "借着火光阻碍视线之际，姜离将储物袋里的所有火雷符抛出，飞舞的符箓将他，将吕忘机都包围在内。",
      "target": "Mượn cơ hội ánh lửa che khuất tầm nhìn, Khương Ly đã ném toàn bộ Hỏa Lôi Phù trong túi trữ vật ra ngoài, bùa bay lả tả bao vây chặt cả hắn và Lã Vong Cơ vào bên trong."
    },
    {
      "segment_id": "0059",
      "source": "“你有神功，我有火雷。”",
      "target": "“Ngươi có thần công, ta có hỏa lôi.”"
    },
    {
      "segment_id": "0060",
      "source": "透过飞舞的符箓，姜离对着吕忘机微微一笑，悄然咽下了风紫阳暗送的丹药，同时，附着在符纸上的精神力激发了。",
      "target": "Xuyên qua những tấm bùa bay múa tơi bời, Khương Ly mỉm cười với Lã Vong Cơ, lẳng lặng nuốt viên đan dược mà Phong Tử Dương âm thầm gửi tới xuống bụng, đồng thời, tinh thần lực bám trên giấy bùa cũng được kích hoạt."
    },
    {
      "segment_id": "0061",
      "source": "安拉胡阿克巴，艺术就是爆炸。",
      "target": "Allahu Akbar, nghệ thuật chính là vụ nổ."
    },
    {
      "segment_id": "0062",
      "source": "“轰轰轰轰轰······”",
      "target": "“Ầm ầm ầm ầm ầm...”"
    },
    {
      "segment_id": "0063",
      "source": "火雷符虽然只是不入品的符箓，但量变产生质变，任何东西数量一多，都能产生超越极限的威能。",
      "target": "Hỏa Lôi Phù mặc dù chỉ là loại bùa chú không lọt nổi vào phẩm cấp, nhưng lượng biến thì chất đổi, bất kỳ vật gì cứ hễ số lượng nhiều lên, đều có thể tạo ra uy năng vượt qua giới hạn."
    },
    {
      "segment_id": "0064",
      "source": "就比如吕忘机，他之所以能压着姜离，就是因为他的功力远胜姜离。",
      "target": "Lấy ví dụ như Lã Vong Cơ, nguyên do gã có thể đè ép Khương Ly mà đánh, chính là vì công lực của gã vượt xa Khương Ly."
    },
    {
      "segment_id": "0065",
      "source": "如天雷勾动地火，火光冲天，轰声不绝，烈焰滚滚，席卷四方，转眼间就覆盖了小半风云台。",
      "target": "Giống như thiên lôi gọi địa hỏa, ánh lửa ngút trời, tiếng nổ rền vang không dứt, lửa cháy hừng hực cuồn cuộn càn quét bốn phương, chỉ trong nháy mắt đã che lấp đi non nửa đài Phong Vân."
    }
  ]
}

import re
cjk_chars = []
for seg in data["segments"]:
    target = seg["target"]
    # Look for any CJK character block
    # CJK Unified Ideographs: \u4e00-\u9fff
    # CJK Punctuation: \u3000-\u303f
    # Fullwidth ASCII: \uff00-\uffef
    matches = re.findall(r'[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]', target)
    if matches:
        cjk_chars.append((seg["segment_id"], matches))

print("Found CJK characters:", cjk_chars)

# test
# test
