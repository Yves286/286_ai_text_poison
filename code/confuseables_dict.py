confuseables_dict = {
    "a":"⍺ａ𝐚𝑎𝒂𝒶𝓪𝔞𝕒𝖆𝖺𝗮𝘢𝙖𝚊ɑα𝛂𝛼𝜶𝝰𝞪а⍶",
    "A":"Ａ𝐀𝐴𝑨𝒜𝓐𝔸𝖠𝗔𝘈𝘼𝙰Α𝚨𝛢𝜜𝝖𝞐АᎪᗅꓮ𐊠",
    "b":"𝐛𝑏𝒃𝒷𝓫𝔟𝕓𝖇𝖻𝗯𝘣𝙗𝚋ƄЬᏏᖯɓƃƂБƀҍҌѣѢ",
    "B":"Ｂℬ𝐁𝐵𝑩𝓑𝔅𝔹𝕭𝖡𝗕𝘉𝘽𝙱ꞴΒ𝚩𝛣𝜝𝝗𝞑ВᏴᗷꓐ𐊂𐊡𐌁",
    "c":"ｃⅽ𝐜𝑐𝒄𝒸𝓬𝔠𝕔𝖈𝖼𝗰𝘤𝙘𝚌ᴄϲⲥсꮯ𐐽¢ȼçҫ",
    "C":"🝌ＣⅭℂℭ𝐂𝐶𝑪𝒞𝓒𝕮𝖢𝗖𝘊𝘾𝙲ϹⲤСᏟꓚ𐊢𐌂𐐕𐔜₡ÇҪƇ",
    "d":"ⅾⅆ𝐝𝑑𝒅𝒹𝓭𝔡𝕕𝖉𝖽𝗱𝘥𝙙𝚍ԁᏧᑯꓒɗɖƌđ₫ᑻᒇ",
    "D":"Ⅾⅅ𝐃𝐷𝑫𝒟𝓓𝔇𝔻𝕯𝖣𝗗𝘋𝘿𝙳ᎠᗞᗪꓓĐÐƉ",
    "e":"℮ｅℯⅇ𝐞𝑒𝒆𝓮𝔢𝕖𝖊𝖾𝗲𝘦𝙚𝚎ꬲеҽɇҿ",
    "E":"⋿Ｅℰ𝐄𝐸𝑬𝓔𝔼𝖤𝗘𝘌𝙀𝙴Ε𝚬𝛦𝜠𝝚𝞔ЕⴹᎬꓰ𐊆Ɇ",
    "f":"𝐟𝑓𝒇𝒻𝓯𝔣𝕗𝖋𝖿𝗳𝘧𝙛𝚏ꬵꞙſẝƒᵮ",
    "F":"ꞘϜ𝟊ᖴꓝ𐊇𐊥Ƒ",
    "g":"ｇℊ𝐠𝑔𝒈𝓰𝔤𝕘𝖌𝗀𝗴𝘨𝙜𝚐ɡᶃցɠǥ",
    "G":"𝐆𝐺𝑮𝒢𝓖𝔊𝔾𝕲𝖦𝗚𝘎𝙂𝙶ԌᏀᏳꓖǤƓ",
    "h":"ｈℎ𝐡𝒉𝒽𝓱𝔥𝕙𝖍𝗁𝗵𝘩𝙝𝚑հᏂɦꚕ",
    "H":"Ｈℋℌℍ𝐇𝐻𝑯𝓗𝕳𝖧𝗛𝘏𝙃𝙷Η𝚮𝛨𝜢𝝜𝞖ⲎНᎻᕼꓧ𐋏ⱧҢӉӇ",
    "i":"⍳ｉⅰℹⅈ𝐢𝑖𝒊𝒾𝓲𝔦𝕚𝖎𝗂𝗶𝘪𝙞𝚒ı𝚤ɪɩι𝛊𝜄𝜾𝝸𝞲іꙇӏꭵᎥɨᵻᵼ",
    "I":"|𝐈𝐉",
    "j":"ｊⅉ𝐣𝑗𝒋𝒿𝓳𝔧𝕛𝖏𝗃𝗷𝘫𝙟𝚓ϳјɉ",
    "J":"Ｊ𝐉𝐽𝑱𝒥𝓙𝔍𝕁𝕵𝖩𝗝𝘑𝙅𝙹ꞲͿЈᎫᒍꓙɈᒙ",
    "k":"𝐤𝑘𝒌𝓀𝓴𝕜𝗄𝗸𝘬𝙠𝚔ƙ",
    "K":"KＫ𝐊𝐾𝑲𝒦𝓚𝕂𝖪𝗞𝘒𝙆𝙺Κ𝚱𝛫𝜥𝝟𝞙ⲔКᏦᛕꓗⱩҚ₭ꝀҞƘ",
    "l":"∣IＩⅠℐℑ𝐈𝐼𝑰𝓘𝕀𝕴𝖨𝗜𝘐𝙄𝙸Ɩｌⅼℓ𝐥𝑙𝒍𝓁𝓵𝔩𝕝𝖑𝗅𝗹𝘭𝙡𝚕Ι𝚰𝛪𝜤𝝞𝞘ⲒІӀ",
    "L":"Ⅼℒ𝐋𝐿𝑳𝓛𝕃𝖫𝗟𝘓𝙇𝙻ⳐᏞᒪꓡ𐐛Ł",
    "m":"ⅿ𝐦𝑚𝒎𝓂𝓶𝔪𝕞𝖒𝗆𝗺𝘮𝙢𝚖",
    "M":"ＭⅯℳ𝐌𝑀𝑴𝓜𝔐𝕄𝕸𝖬𝗠𝘔𝙈𝙼Μ𝚳𝛭𝜧𝝡𝞛ϺⲘМᎷᗰᛖꓟ𐊰𐌑Ӎ",\
    "n":"𝐧𝑛𝒏𝓃𝓷𝔫𝕟𝖓𝗇𝗻𝘯𝙣𝚗ոռɳƞη𝛈𝜂𝜼𝝶𝞰ᵰ",
    "N":"Ｎℕ𝐍𝑁𝑵𝒩𝓝𝔑𝕹𝖭𝗡𝘕𝙉𝙽Ν𝚴𝛮𝜨𝝢𝞜ⲚꓠƝ",
    "o":"०੦૦௦౦೦൦๐໐၀۵ｏℴ𝐨𝑜𝒐𝓸𝔬𝕠𝖔𝗈𝗼𝘰𝙤𝚘ᴏᴑꬽο𝛐𝜊𝝄𝝾𝞸σ𝛔𝜎𝝈𝞂𝞼ⲟоჿօഠဝ𐓪𐐬øꬾɵꝋөѳꮎꮻꭴơ",
    "O":"0০୦〇Ｏ𝐎𝑂𝑶𝒪𝓞𝕆𝖮𝗢𝘖𝙊𝙾Ο𝚶𝛰𝜪𝝤𝞞ⲞОՕⵔዐଠ𐓂ꓳ𐊒𐊫𐐄",
    "p":"⍴ｐ𝐩𝑝𝒑𝓅𝓹𝔭𝕡𝖕𝗉𝗽𝘱𝙥𝚙ρϱ𝛒𝛠𝜌𝜚𝝆𝝔𝞀𝞎𝞺𝟈ⲣрƥᵽ",
    "P":"Ｐℙ𝐏𝑃𝑷𝒫𝓟𝔓𝕻𝖯𝗣𝘗𝙋𝙿Ρ𝚸𝛲𝜬𝝦𝞠ⲢРᏢᑭꓑ𐊕ᒆᑷ",
    "q":"𝐪𝑞𝒒𝓆𝓺𝔮𝕢𝖖𝗊𝗾𝘲𝙦𝚚ԛգզ",
    "Q":"ℚ𝐐𝑄𝑸𝒬𝓠𝖰𝗤𝘘𝙌𝚀ⵕ",
    "r":"𝐫𝑟𝒓𝓇𝓻𝔯𝕣𝖗𝗋𝗿𝘳𝙧𝚛ꭇꭈᴦⲅгꮁɽɼɍғᵲґ",
    "R":"ℛℜℝƦᎡᏒ𐒴ᖇꓣ",
    "s":"ｓ𝐬𝑠𝒔𝓈𝓼𝔰𝕤𝖘𝗌𝘀𝘴𝙨𝚜ꜱƽѕꮪ𐑈ʂᵴ🝜",
    "S":"Ｓ𝐒𝑆𝑺𝒮𝓢𝕊𝖲𝗦𝘚𝙎𝚂ЅՏᏕᏚꓢ𐊖𐐠",
    "t":"𝐭𝑡𝒕𝓉𝓽𝔱𝕥𝖙𝗍𝘁𝘵𝙩𝚝ƭ",
    "T":"⊤⟙🝨Ｔ𝐓𝑇𝑻𝒯𝓣𝕋𝖳𝗧𝘛𝙏𝚃Τ𝚻𝛵𝜯𝝩𝞣ⲦТᎢꓔ𐊗𐊱𐌕⍡ƮҬ₮Ŧ",
    "u":"𝐮𝑢𝒖𝓊𝓾𝔲𝕦𝖚𝗎𝘂𝘶𝙪𝚞ꞟᴜꭎꭒʋυ𝛖𝜐𝝊𝞄𝞾ս𐓶",
    "U":"∪⋃𝐔𝑈𝑼𝒰𝓤𝔘𝕌𝖀𝖴𝗨𝘜𝙐𝚄Սሀ𐓎ᑌꓴɄᏌᑘᑧ",
    "v":"∨⋁ｖⅴ𝐯𝑣𝒗𝓋𝓿𝕧𝖛𝗏𝘃𝘷𝙫𝚟ᴠν𝛎𝜈𝝂𝝼𝞶ѵꮩ",
    "V":"Ⅴ𝐕𝑉𝑽𝒱𝓥𝕍𝖵𝗩𝘝𝙑𝚅ѴⴸᏙᐯꓦᐻ🜈",
    "w":"ɯ𝐰𝑤𝒘𝓌𝔀𝔴𝕨𝖜𝗐𝘄𝘸𝙬𝚠ᴡѡԝաꮃ",
    "W":"ԜᎳᏔꓪ₩",
    "x":"᙮×⤫⤬⨯ｘⅹ𝐱𝑥𝒙𝓍𝔁𝔵𝕩𝖝𝗑𝘅𝘹𝙭𝚡хᕁᕽ⨰",
    "X":"᙭╳𐌢ＸⅩ𝐗𝑋𝑿𝒳𝓧𝕏𝖷𝗫𝘟𝙓𝚇ꞳΧ𝚾𝛸𝜲𝝬𝞦ⲬХⵝᚷꓫ𐊐𐊴𐌗Ҳ",
    "y":"ɣᶌｙ𝐲𝑦𝒚𝓎𝔂𝕪𝗒𝘆𝘺𝙮𝚢ʏỿꭚγℽ𝛄𝛾𝜸𝝲𝞬уүყƴɏұ",
    "Y":"Ｙ𝐘𝑌𝒀𝒴𝓨𝔜𝕐𝖄𝖸𝗬𝘠𝙔𝚈Υϒ𝚼𝛶𝜰𝝪𝞤ⲨУҮᎩᎽꓬ𐊲¥ɎҰ",
    "z":"𝐳𝑧𝒛𝓏𝔃𝕫𝗓𝘇𝘻𝙯𝚣ᴢꮓʐƶȥᵶ",
    "Z":"Ｚℤ𝐙𝑍𝒁𝒵𝓩𝖹𝗭𝘡𝙕𝚉Ζ𝚭𝛧𝜡𝝛𝞕ᏃꓜƵȤ",
    "0":"ØⵁǾ⊖⊝⍬ƟꝊθ𝛉𝜃",
    "1":"𝟏𝟙𝟣𝟭𝟷",
    "2":"𝟐𝟚𝟤𝟮𝟸ᒿƻ🄃",
    "3":"𝟑𝟛𝟥𝟯𝟹ꞫȜƷꝪⳌЗӠҘ🄄",
    "4":"𝟒𝟜𝟦𝟰𝟺Ꮞ",
    "5":"𝟓𝟝𝟧𝟱𝟻Ƽ",
    "6":"𝟔𝟞𝟨𝟲𝟼ⳒбᏮ",
    "7":"𝟕𝟟𝟩𝟳𝟽𐓒",
    "8":"৪੪𝟖𝟠𝟪𝟴𝟾ȣȢ𐌚🄉",
    "9":"੧୨৭൭𝟗𝟡𝟫𝟵𝟿ꝮⳊ"
}