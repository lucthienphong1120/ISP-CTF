# miniCTF 2020

Để chào mừng các tân sinh viên và những người có đam mê và muốn tìm hiểu về Cyber Security, ISP Club chúng mình đã tổ chức cuộc thi thường niên miniCTF và đây là writeup cho miniCTF năm 2020.
    
### Firstlooking

![miniCTF firstlook](/miniCTF2020/logo.png)

### Overview

 | Title | Category | Points | Flag
 | ------ | ------ | ------ | ------ |
 | [World these days](#OSINT-50:-World-these-days) | OSINT | 50 | `ispclub{ISP_ru1n_th3_w0rLd}` |
 | [ISP rules the world](#OSINT-250:-ISP-rules-the-world) | OSINT | 250 | `ispclub{b4k4_Ki3nM1ddL3}` |
 | [Teacher Ki3nM1ddL3](#Crypto-100:-Teacher-Ki3nM1ddL3) |	Crypto	| 100 | `ispclub{sUch_4_L0n9_w4y}` |
 | [Dancer Chick Chick](#Crypto-100:-Dancer-Chick-Chick) | Crypto | 100 | `ispclub{dancewithme}` |
 | [ReMo](#Crypto-100:-ReMo) | Crypto | 100| `ispclub{r3_m0}` |
 | [Chick Chick wants breakfast!](#Crypto-150:-Chick-Chick-wants-breakfast!) | Crypto | 150 | `ISPCLUB{YUMMYYUMMY}` |
 | [Forbidden Magic](#Crypto-222:-Forbidden-Magic)| Crypto | 222 | `ISPCLUB{THEBESTWIZARD}` |
 | [No magic here](#FOR-100:-No-magic-here) | FOR | 100 | `ispclub{w4Y5_T0_3xpL01t_pN9_f1L35}` | 
 | [QR's Chick Chick](#FOR-50:-QR's-Chick-Chick) | FOR | 50 | `ispclub{pl4y1n9_w1th_QR_c0d3_15_v3ry_1nt3r35t1n9}` | 
 | [Wanna play Hide and Seek?](#FOR-150:-Wanna-play-Hide-and-Seek?) | FOR | 150 | `ispclub{n4hhh_1_g0t_c4tch3D}` | 
 | [winRAR winNER](#Misc-150:-winRAR-winNER) | Misc | 150 | `ispclub{welcome_and_have_fun}` | 
 | [Secret Book](#Misc-500:-Secret-Book) | Misc | 500 | `ispclub{d0K_s@cK_d3_9141_tR1}` | 
 | [Call me daddy](#RE-50:-Call-me-daddy) | RE | 30 | `ispclub{programmingBasic}` | 
 | [Pascal n Python](#Programming-150:-Pascal-n-Python) | Programming | 150 | `ispclub{3asy_r1ght?}` | 
 | [Become Powerful](#Web-100:-Become-Powerful) | Web | 100 | `ispclub{j01n_t0_run_th1s_w0rLd}` | 
 | [Menhera](#Web-100:-Menhera) | Web | 150 | `ispclub{v3__v0i__d0i__cua__anh__d1_3m__e111__<333}` | 
 | [2048](#Web-100:-2048) | Web | 200 | `ispclub{4lw4y5_ch3ck_l0c4l_st0r4g3}` | 
 | [Scroll](#Web-100:-Scroll) | Web | 300 | `ispclub{sh0u1dnt_l34rn_j4v4scr1pt}` | 
 | [md5-1](#Web-100:-md5-1) | Web | 500 | `	ispclub{G00d_J0b_h4y_l4m_t41_n4ng_tr3!!!!!!!!!__<3}` |

# OSINT 50: World these days

#### Challenge 

First you have to know about the world these days. Read [this book](/miniCTF2020/writeupfiles/history.txt):

#### Solution

Đề bài yêu cầu chúng ta đọc file history, vậy hãy thử tải về xem chúng ta có gì nào.

Đây là phần cốt truyện cho minictf và đọc đến cuối ta thấy được flag.

Flag: `ispclub{ISP_ru1n_th3_w0rLd}`

# OSINT 250: ISP rules the world

#### Challenge

Ta là Lươn. Ta không đánh giá cao ngươi, tuy vậy ta vẫn sẽ cho ngươi một cơ hội để có được kho báu. Gần đây Ki3nM1ddL3 mới được trải nghiệm cỗ máy thời gian, và hắn rất thích thú với mạng xã hội thời xưa là Facebook, vì vậy hắn đã lập một page cho tổ chức ISP trên đó. Hắn còn đăng bài khiêu khích thế giới rằng hắn nhiều của cải tới mức phát tán lung tung và để luôn 1 flag ở đó. Quay về quá khứ và đào mảnh flag đó lên!

#### Solution

Khi đọc thì ta có thể thấy là đề bài có các từ khóa ***Facebook***, ***page ISP***, nội dung minigame. Flag có thể sẽ liên quan đến một bài đăng nào đó về minigame trên [fanpage của ISP](https://www.facebook.com/ATTT.PTIT). Sau khi tìm kiếm thì mình phát hiện ra bài [Open miniCTF](https://www.facebook.com/ATTT.PTIT/posts/3425688750875051) là có liên quan nhất đến các dữ kiện mà ta đã tìm được, hãy cùng xem xét nó 1 chút.

![FBpost](/miniCTF2020/writeupfiles/opengamepost.png)

Có vẻ là chúng ta không thấy điều gì có vẻ khả nghi ở đây cả. Đọc thật kỹ đề bài, ta sẽ thấy đề bài liên tục nhắc đến ***thời gian***, ***flag***. Facebook có 1 tính năng cho phép ta có thể xem được lịch sử đã chỉnh sửa của 1 bài viết, có vẻ flag sẽ được giấu ở đó. Hãy cùng kiểm tra edit history của post này!

![edit_history](/miniCTF2020/writeupfiles/edithistory.png)

Quả nhiên flag được cài vào đây

Flag: `ispclub{b4k4_Ki3nM1ddL3}`

# Crypto 100: Teacher Ki3nM1ddL3

#### Challenge

Ki3nM1ddL3 ta thật ra rất thích ra câu đố rồi nhìn bọn điêu dân đăm chiêu mà không thể giải được. Mi đã tìm ra được một vài flag, vì vậy ta thấy ngươi rất thú vị! Hãy thử xem lần này ngươi còn có thể tìm ra được nữa không!

Nếu ngươi được thừa hưởng một tí tẹo trí tuệ của ta ngươi sẽ biết máy tính hiểu được ngôn ngữ nào. Ta là một hắc cờ vì vậy ta sẽ luôn bắt đầu bằng nó!

[file](/miniCTF2020/writeupfiles/bin.txt)

#### Solution

Khi vừa mở tệp bin.txt thì có thể thấy được 1 loạt các ký tự 0 và 1. Đề bài cũng gợi ý đó là **ngôn ngữ máy tính hiểu**. Vậy đây chính là mã binary. Khi thực hiện decode từ bin trở thành ascii thì ta thu được dòng chữ:

```sh
After binary surely have hex 41 66 74 65 72 20 74 68 61 74 20 77 65 20 68 61 76 65 20 62 61 73 65 36 34 20 56 47 68 6c 62 69 42 6f 5a 58 4a 6c 49 48 64 6c 49 47 64 76 49 48 64 70 64 47 67 67 59 6d 46 7a 5a 54 4d 79 49 45 70 61 55 31 68 52 4e 55 4a 42 54 6b 5a 61 55 30 45 79 54 45 39 50 55 56 46 45 51 30 35 61 55 6b 64 52 57 56 52 44 54 6b 4a 58 53 45 55 79 52 45 4e 4f 55 6c 6c 48 56 54 4e 55 52 30 31 4b 57 55 64 46 57 6c 52 50 54 30 4a 5a 52 30 6b 7a 52 46 4e 50 53 6c 5a 49 52 54 52 45 54 30 31 61 57 6b 64 52 4d 30 52 44 54 55 70 57 52 31 55 30 56 45 31 4e 53 6c 68 48 52 54 4e 55 53 55 35 43 56 6b 68 46 4e 46 52 4a 54 6c 4a 52 52 30 30 7a 56 45 31 4f 53 6c 64 48 56 54 52 45 55 30 39 43 56 30 63 30 4e 45 52 54 54 6b 4a 58 52 30 46 61 52 45 6c 50 53 6c 4e 49 51 54 4e 55 51 55 31 43 57 45 64 4a 57 56 52 4e 54 30 70 57 53 45 46 61 56 45 46 4e 51 6c 4a 48 52 56 70 45 55 30 35 53 56 6b 64 4a 57 6b 52 50 54 6b 70 53 52 31 46 61 56 46 46 50 51 6c 5a 48 53 54 4e 55 52 30 39 4b 57 6b 64 52 57 6c 52 44 54 55 4a 52 52 31 6c 5a 52 45 6c 50 53 6c 52 48 51 56 70 45 55 30 31 43 57 67 3d 3d
```

Vậy là sẽ có nhiều mã được sử dụng. Đối với bài này thì một trang [website như thế này](https://kt.gy) rất tiện lợi.  

Đề bài đã gợi ý đây là đoạn mã hex. Tiếp tục decode từ hex sang ascii:

```sh
After that we have base64 VGhlbiBoZXJlIHdlIGdvIHdpdGggYmFzZTMyIEpaU1hRNUJBTkZaU0EyTE9PUVFEQ05aUkdRWVRDTkJXSEUyRENOUllHVTNUR01KWUdFWlRPT0JZR0kzRFNPSlZIRTRET01aWkdRM0RDTUpWR1U0VE1NSlhHRTNUSU5CVkhFNFRJTlJRR00zVE1OSldHVTREU09CV0c0NERTTkJXR0FaRElPSlNIQTNUQU1CWEdJWVRNT0pWSEFaVEFNQlJHRVpEU05SVkdJWkRPTkpSR1FaVFFPQlZHSTNUR09KWkdRWlRDTUJRR1lZRElPSlRHQVpEU01CWg==
```

Tiếp tới là base64:

```sh
Then here we go with base32 JZSXQ5BANFZSA2LOOQQDCNZRGQYTCNBWHE2DCNRYGU3TGMJYGEZTOOBYGI3DSOJVHE4DOMZZGQ3DCMJVGU4TMMJXGE3TINBVHE4TINRQGM3TMNJWGU4DSOBWG44DSNBWGAZDIOJSHA3TAMBXGIYTMOJVHAZTAMBRGEZDSNRVGIZDONJRGQZTQOBVGI3TGOJZGQZTCMBQGYYDIOJTGAZDSMBZ
```

Base32:

```sh
Next is int 171411469416857318137882699598739461155961717445994603765658986789460249287007216958300112965227514388527399431006049302909
```

Tiếp tới là mã int:

```sh
Bases are fun. Your prize: ispclub{sUch_4_L0n9_w4y}
```

Phew. Flag: `ispclub{sUch_4_L0n9_w4y}`

# Crypto 100: Dancer Chick Chick

#### Challenge

Hắc cờ Chick Chick đã bị bắt!!!! Nhưng nó đang nhảy múa??? Phải chăng đó là một loại mật mã???!

[Dancing man](/miniCTF2020/writeupfiles/Dancing_man_cipher.png)

#### Solution

Sau khi tải được tấm hình về ta có thể nhận định luôn đây là flag đã được mã hóa.

Nếu như tinh ý thì bạn có thể nhận ra ngay lập tức đây là loại mã Dancing man được dùng trong bộ chuyện Sherlock Home nổi tiếng và có thể dễ dàng giải được câu đố này. Mình đã sử dụng [webside](https://www.dcode.fr/dancing-men-cipher) để decode.

Flag: `ispclub{dancewithme}`

# Crypto 100: ReMo

#### Challenge

Đừng tưởng xâm nhập máy tính của Chick Chick là dễ :)

```
} −−−−− −− ••−−•− •••−− •−• { −••• ••− •−•• −•−• •−−• ••• ••
```

#### Solution

Đây là một đoạn mã morse. Ta có thể decode nó bằng các [website decode online](https://kt.gy)

Dịch đoạn mã morse này ra ta được : `}0M_3R{BULCPS`. Chuỗi này đang bị ngược so với form flag chuẩn. Thực hiện đảo ngược lại là ta sẽ có được flag.

Flag: `ISPCLUB{R3_M0}`

# Crypto 150: Chick Chick wants breakfast!

#### Challenge

Sáng nay Chick Chick bị thủ lĩnh Ki3nM1ddL3 phạt vì lỡ để hắc cờ xâm nhập máy tính. Nó quyết định sẽ nói bí mật của thủ lĩnh cho người nào mang cho nó đồ ăn sáng. Nhớ nhé, nó chỉ ăn thịt xông khói thôi!!!.

Mau giúp Chick Chick đi!!!!! (｡•́︿•̀｡)

```
abaaa baaab abbba aaaba ababa baabb aaaab babba baabb ababb ababb babba babba baabb ababb ababb babba
```

#### Solution

Đề bài cho một đoạn mã gì đó ta không hiểu và liên tục nhắc đi nhắc lại từ khóa **thịt xông khói**. Search google thì đúng là có tồn tại loại cipher tên là **Bacon cipher**. [Decode](https://www.dcode.fr/bacon-cipher) đoạn mã trên theo Bacon cipher sẽ ra được flag.

Flag: `ISPCLUB{YUMMYYUMMY}`

# Crypto 222: Forbidden Magic

#### Challenge

H3nlor đang thực hiện ma pháp tối thượng nhằm tước đoạt trí thông minh của các flag hunter. Nhưng vì đây là 1 cấm thuật cổ xưa nên hắn cần 6 ngày để có thể thực hiện được, trong thời gian đó hãy giải mã bí ẩn của phép thuật này và ngăn chặn H3nlor trước khi quá muộn!

File: [magic_circle](/miniCTF2020/writeupfiles/Magic_circle.png) [spell](/miniCTF2020/writeupfiles/SPELL.png)

#### Solution

Nếu như nhận thấy được rằng hình vẽ này được vẽ 1 cách có quy luật thì bài này không phải là 1 bài khó 1 chút nào cả.
Trong mỗi các ô tròn nhỏ đều chứa 3 ký tự và riêng ô cuối cùng chứa 2 ký tự (do trong bảng chữ cái tiếng anh chỉ có 26 ký tự) và trên SPELL.png cũng có rất nhiều các gạch ngang, dọc và chéo. Điểm chung của chúng là đều có 3 gạch và chỉ duy nhất có 1 ký tự là có 2 gạch, đối chiếu lên hình tròn lớn, dễ thấy sự liên hệ của 2 hình này với nhau, gạch dài hơn sẽ biểu diễn cho cả vị trí của ô và ký tự mà hình đó đang biểu diễn, từ đó suy ra được toàn bộ bảng chữ cái và dễ dàng decode, có được flag.
Bảng chữ cái:

![CharacterSystem](/miniCTF2020/writeupfiles/SOLVE-EZ.png)

Flag: `ISPCLUB{THEBESTWIZARD}`

# FOR 100: No magic here

#### Challenge

Gần đây H3nl0r bắt đầu thích thú nghiên cứu đống ma thuật vô dụng và bắt đầu làm mất flag của ta. Thật tức giận. Nhưng không sao, ta đã có biện pháp bảo vệ chúng.
[file](/miniCTF2020/writeupfiles/sthcrypty.png)

#### Solution

Sau khi tải file sthcrypty.png và mở lên ta thấy ngay nó được mã hóa tương tự như bài [Forbidden Magic](#Crypto-222:-Forbidden-Magic). Thử decode xem có ra flag được không và dịch ra ta có dòng chữ `WRONGDIRECTION`

Submit thử với form ISPCLUB{ANSWER} thì cho ra kết quả là *incorrect*. Chú ý đến categoty của bài, [Forbidden Magic](#Crypto-222:-Forbidden-Magic) là **Crypto** và [No magic here](#FOR-100:-No-magic-here) là **Forensic**. Hãy dùng cách làm của Forensic để xử lý bài này.

Việc đầu tiên khi có một file .png hẳn là xem hex xem file này liệu có ẩn giấu gì không. Sử dụng tool **HxD** để xem và ở ngay cuối file ta thấy flag.
![hex](/miniCTF2020/writeupfiles/hexpng.png)

Flag: `ispclub{w4Y5_T0_3xpL01t_pN9_f1L35}`

# FOR 50: QR's Chick Chick

#### Challenge

Hắc cờ Chick Chick khiêu khích các người bằng một mã QR. Tưởng quét một phát là ra à? Mơ đi nhé !!!

[QR](https://mega.nz/file/QkZSRJrB#tfTZdOaqB4WcxpfVHFXzCiGTv2ASihOhzTzRAncJl2w)

#### Solution

Khi bấm vào ta sẽ được forward tới trang download mega chứa 1 ảnh QR .png

![QR1](/miniCTF2020/writeupfiles/qrchickchick1.png)

Để quét QR, chúng ta có thể dùng smartphone, hoặc dùng các trang web online. Mình đã decode QR này với website [zxing](https://zxing.org/w/decode.jspx).

Giải mã QR này ra một link mega nữa.

Lặp lại như thế vài lần (5 lần) thì đã nhận được flag:

![QRflag](/miniCTF2020/writeupfiles/qrflag.png)

Flag: `ispclub{pl4y1n9_w1th_QR_c0d3_15_v3ry_1nt3r35t1n9}`

# FOR 150: Wanna play Hide and Seek?

#### Challenge

Hôm nay tên ChickChick lại quỵt tiền ăn xiên bẩn của ta. Khi ta đến đòi nợ, hắn vội vã trốn đi và để rơi một mảnh flag. Nó ở đâu đó trong này, hãy nhân cơ hội này chiếm lấy nó, ta muốn thấy ChickChick bị phạt lắm rồi!

[file .rar](/miniCTF2020/writeupfiles/map.rar)

#### Solution

Bài này khi giải nén tệp map.rar ta được một list các folder và file nhỏ. Flag là một chuỗi ký tự vậy nên ta có thể thử dùng chức năng Search ở File Explorer để tìm toàn bộ file .txt `*.txt` cũng sẽ ra một vài file .txt và mở lần lượt sẽ thấy được flag.

Đối với bài này thì phương pháp làm tay là 1 phương pháp không hiệu quả nếu phải tìm với số lượng lớn. Chúng ta sẽ dùng **CLI** (Command Line Interface) với các câu lệnh `findstr` hoặc `grep`. Về cơ bản thì mục đích sử dụng của 2 câu lệnh này là như nhau, dùng để tìm kiếm thông tin bên trong 1 file.

Đầu tiên ta sẽ mở CLI tại thư mục cần tìm kiếm (cmd đối với windows và Terminal đối với Linux) sau đó dùng 1 trong 2 câu lệnh để tìm kiếm.

- `findstr` đối với Windows: 

![cmdmap](/miniCTF2020/writeupfiles/cmdmap.png)

- `grep` đối với Linux:

![termap](/miniCTF2020/writeupfiles/terminalmap.png)

Flag: ispclub{n4hhh_1_g0t_c4tch3D}

# Misc 150: winRAR winNER

#### Challenge

Hừ. Flag của ta đang mất dần và người yêu ta đang không vui lắm. Lần này ta đã giấu khá kỹ, ngươi sẽ không tìm được đâu.

[Challenge](/miniCTF2020/writeupfiles/chall.txt)

#### Solution
Chúng ta có thể thấy đề bài đã cho chúng ta 1 file chall.txt và ở trong có 1 đường link drive. Khi truy cập vào ta được dẫn đến 1 thư mục chứa 1 tệp tên là **chall.zip** và 1 tệp **pass.txt**. Sau khi mình tải cả 2 file về và giải nén **chall.zip** thì thấy file yêu cầu có mật khẩu để giải nén và nó nằm trong file **pass.txt**. Sau khi nhập pass mình đã giải nén được thành công, bên trong tệp zip lại có thêm 2 file nữa:

![liar](/miniCTF2020/writeupfiles/fakeflag.png)

Mình đã ngay lập tức mở file flag-in-here và đây là những gì mình nhận được:

```sh
https://drive.google.com/drive/folders/1I2HcFsJzj9BUG0tp8NkRR6JMFpq-NGGZ?usp=sharing
```

[Alalalala.zip](/miniCTF2020\writeupfiles\Alalalala.zip)

Và đời không như là mơ :v

Tiếp tục truy cập thì chúng ta nhận được thêm **hint.txt** và 1 tệp **chall.zip** nữa. Sau khi tải về và mở file **hint.txt** thì đây là những gì mình nhận được:

```sh
Try to extract that or just open it, you'll see something strange, gud luk
It doesn't look like what u see.
can u change that to zip file?
I think u should search gg for "filename extension" 
```

Mình đã thử làm theo hint đầu tiên và giải nén file nhưng **chall2** lại yêu cầu pass để có thể mở khóa, mình đã thử lại pass đầu tiên nhưng có vẻ là không được. Thử đến ý tiếp theo của hint nào. Không cho giải nén thì ta cứ mở:

![chall2](/miniCTF2020/writeupfiles/chall2.png)

Cái ảnh kia mình đã thử mở và không được, nên mình đã thử mở file zip và thật bất ngờ khi nó không cần pass để mở.

Đây là những gì mình nhận được khi mở file NOT-important.txt:

```sh
change this from hex to ascii to get extract password(use your brain not your hand :> ): 0x73 0x68 0x69 0x6e 0x72 0x61 0x5f 0x74 0x65 0x6e 0x73 0x65 0x69
NOT password(don't notice the picture):
•−−−− ••−−•− •••• •−−−− −•• •••−− −•• ••−−•− ••• −−−−− −− •••−− − •••• •−−−− −• −−−−•
Don't do that, I swear to you that's NOT the password :<
and I do NOT know about something like M0rse. Truth me :<
I don't hide anything...
```

Okay, ngay dòng đầu tiên ta đã có được password giải nén nhưng mà yêu cầu phải đổi nó từ cơ số 16 về ascii để có pass. Sau khi [decode](https://kt.gy) ta có được pass giải nén: `shinra_tensei`

Đã giải nén thành công và nhận được bức ảnh:

![I_DO_NOT_HIDE_ANYTHING](/miniCTF2020/writeupfiles/I_DO_NOT_HIDE_ANYTHING.jpeg)

Okay got stuck again. Quay lại nghiền ngẫm file **hint.txt** tiếp và nhận ra có điều gì đó về *file extension*.

Quăng vào xem hex và ta nhận ra nó là một file .zip. Đổi định dạng của nó thành I_DO_NOT_HIDE_ANYTHING.zip và giải nén bằng mật khẩu là phần mã Morse trong **NOT-important.txt**.

Sau khi decode ta có pass: `1_H1D3D_S0M3TH1N9`.

[File extract](/miniCTF2020/writeupfiles/file-ext.png)

Và sau khi giải nén thành công ta có được thư mục **secrets** gồm rất nhiều ảnh gái xinh :3

[secrets](/miniCTF2020/writeupfiles/secrets.png)

"tận hưởng" toàn bộ ablum này xong :)) thì ở thư mục cuối ta có được flag:

![challflag](/miniCTF2020/writeupfiles/ISPCLUB.png)

Flag: `ispclub{welcome_and_have_fun}`

# Misc 500: Secret Book

#### Challenge

Là một thủ lĩnh của tổ chức toàn cầu như ta, tất nhiên ta có thói quen đọc sách để bồi dưỡng tri thức. Ngươi nên học tập ta đi.

[BOOK](/miniCTF2020/book.png)

#### Solution

Đề bài đã cho ta 1 bức ảnh khi mở nó ra ta có được một thứ có vẻ là 1 đường link đã được rút gọn, truy cập vào thì đó là một website có-vẻ-không-có-gì-nhiều :v

OKAY :| bị lừa rồi. Có vẻ như đây là 1 đường link nhưng mà đã bị thay đổi gì đó và thứ đáng nghi nhất là phần WH, chỉ có thể là Width và Height của 1 bức ảnh, sau đó mình đã kiểm tra thông số của bức ảnh (chuột phải -> Properties -> Detail), nhìn thấy *Dimensions* của ảnh là `728x90`.

Thay 728 vào W, 90 vào H ta nhận được [đường link mới](bit.ly/book_72890) và nhận được một quyển sách .pdf.

Sau khi lật được vài trang thì có vẻ đây là một quyển sách bình thường trừ số trang không theo quy luật.

Liệt kê chuỗi số trang ra thì ta có một chuỗi trông có vẻ là có những ký tự chữ cái trong cả hệ decimal, octal theo thứ tự so le:

```sh
105 163 112 143 108 165 98 173 100 60 75 137 115 100 99 113 95 144 51 137 57 61 52 61 95 164 82 61 125
```

Chuyển về ascii và ta sẽ có được flag.

Flag: `ispclub{d0K_s@cK_d3_9141_tR1}`

# RE 50: Call me daddy

#### Challenge

Trong quá trình hiện thực hoá giấc mơ trở thành hacker thành đạt kiêm bố đường, H3nl0r gặp vấn đề với việc tốt nghiệp cấp 3 khi gặp phải kẻ thù không đội trời chung là môn tin học 11. Hãy tìm hiểu xem H3nl0r có đạt được mơ ước của mình không, hay mãi vẫn không được lên lớp và phải ở nhà ăn bám!

[file](/miniCTF2020/writeupfiles/boduong.pas)

#### Solution

Đề bài cho ta 1 file .pas, vậy đây là file code của pascal. Hãy xem qua thử nào ta có thể thấy file code được chia thành các phần:

Phần khai báo biến:

![var](/miniCTF2020/writeupfiles/var.png)

Phần hàm con:

![func](/miniCTF2020/writeupfiles/func.png)

Và phần hàm main:

![main](/miniCTF2020/writeupfiles/main.png)

Ở phần khai báo biến ta thấy có 1 biến “name” kiểu string, 1 biến “daddy” kiểu string có giá trị là ‘ISP’ và 1 biến “flag” kiểu string có giá trị là `'hrqbmtczqsnfs`llhofC`rhb|'`. 
Ở phần chương trình con ta có thể thấy đó là hàm này dùng để xử lý flag đã được khai báo ở trên kia thành flag mà chúng ta có thể submit được.  
Đọc trong main thì ta thấy có câu lệnh so sánh, nếu như input của người dùng nhập vào bằng với giá trị của biến daddy thì sẽ gọi hàm con printFlag.  
Vậy thì dễ rồi, chỉ cần chạy rồi nhập input = ‘ISP’ là có thể ra được flag.

![pasrun](/miniCTF2020/writeupfiles/pasrun.png)

Flag: `ispclub{programmingBasic}`

# Programming 150: Pascal n Python

#### Challenge

Programming

Ki3nM1ddL3 mới tập lập trình Python và hắn nhận ra Python cũng có vài điểm chung với Pascal. Xem xem ai học Python nhanh hơn nhé.<br>
[c0d3.py](/miniCTF2020/writeupfiles/c0d3.py)

#### Solution

Bài này chỉ đơn giản là các ký tự trong flag đã được cộng thêm 160 và mình đã có chuỗi sau khi các ký tự được cộng với 160. Chỉ cần thực hiện lấy giá trị mỗi ký tự trừ đi 160 rồi in ra là ta sẽ có được flag rồi.
Flag: `ispclub{3asy_r1ght?}`

# Web 100: Become Powerful

#### Challenge

Gần đây tên đầu sỏ lại âm mưu truyền bá giáo phái của hắn lớn mạnh hơn nữa, vì thế Ki3nM1ddL3 đã bắt Lươn phải làm ra cái web này. Nhưng hắn đã tin lầm người. Lươn đã biến chỗ này thành động flag-hunter. Hắn còn tiện thể nhét luôn flag vào. Hãy tìm nó!

#### Solution

Bài này không có file đính kèm và dữ kiện duy nhất của ta là phần cốt truyện kia. Có thể thấy là cốt truyện đã đề cập đến việc Lươn đã nhét flag vào trang web này. Thử f12 xem source code xem sao!
Sau 1 hồi mình đã tìm thấy nó ngay trong trang About Us:

![about](/miniCTF2020/writeupfiles/aboutus.png)

Flag: `ispclub{j01n_t0_run_th1s_w0rLd}`

# Web 100: Menhera

#### Challenge

Chick Chick rất thích xem Menhera, trong một lần đang xem Mehera thì bỗng nhiên bị mất mạng. [Web](https://minictf-web02.herokuapp.com/)
[Source](/miniCTF2020/writeupfiles/) & [deploy](/miniCTF2020/writeupfiles/).


#### Solution

Click vào đường link sẽ dẫn ta đến 1 web chal, web này yêu cầu chúng ta tắt bật mạng 10 lần để ra flag. Thật may người ra đề là 1 người biết nghĩ cho thí sinh khi chỉ cần bật tắt 10 lần. Nhưng không, đó là 1 cách làm thật sự rất thiếu tinh tế, vậy nên mình đã quyết định check source code của trang web này và phát hiện ra 1 file *script.js* có đoạn code rất khả nghi:

```js
wordRunner(speech);
    let title = document.querySelector('.title span').innerHTML;
    let $$ = 10
    let $$$ = ['==QfzMzM881XxETMl9', '1XtNzXxQ2Xfhmbh91XhV3Yf9VawQ', '2XflGM291XzY3eiVHbjB3cpBiO5B', '6wuBSZn5WZsxWYoNGIhd6uhPGI', 'nFGbmByZu95uhDrxoRHIudqu', 'hjGcgA6wsBSeiOMkEDiLsOsc0', 'BibqOcarBSadub4wa8ZuBCoDzGI01quhjGdg4Wo6GuQ']
    let $$$$ = true
    const onlineEvent = () => {
        if (!$$$$) --$$
        document.querySelector('.title span').innerHTML = `Đếm nè: ${$$}`
        if ($$ === 0) {
            function $$$$$() {
                let flag = _.__($$$.join('').split('').reverse().join(''))
                wordRunner(flag)
            }
            return $$$$$();
        }
    }
```

Đọc hiểu thì đúng là sau khi chúng ta tắt bật mạng 10 lần `(if ($$ === 10))` thì web sẽ in ra flag cho chúng ta, nhưng để ý phần khai báo `let $$$` có thể nhận định được đây là 1 đoạn base64 đã bị đảo sau đó cắt ra, do ở dưới chúng ta có câu lệnh khai báo flag
`let flag = _.__($$$.join('').split('').reverse().join(''))`

Vậy là chỉ cần ghép những cụm từ trong `$$$` sau đó đảo lại và decode từ base64 về ascii là được, mình đã viết 1 script nhỏ bằng python3 để solve đoạn này:

```js
import base64
a = ['==QfzMzM881XxETMl9', '1XtNzXxQ2Xfhmbh91XhV3Yf9VawQ', '2XflGM291XzY3eiVHbjB3cpBiO5B', '6wuBSZn5WZsxWYoNGIhd6uhPGI', 'nFGbmByZu95uhDrxoRHIudqu', 'hjGcgA6wsBSeiOMkEDiLsOsc0', 'BibqOcarBSadub4wa8ZuBCoDzGI01quhjGdg4Wo6GuQ']
b = ""
for i in a:
    b += i
b = base64.b64decode(b[::-1]).decode('utf-8')
print (b)
```

Flag: `ispclub{v3__v0i__d0i__cua__anh__d1_3m__e111__<333}`

# Web 100: 2048

#### Challenge

2048 là một trò chơi mà H3nl0r rất yêu thích, bạn hãy phá kỉ lục của H3nl0r nhé <3 

[Web](http://minictf.hypnguyen.us/2048.html)
[deploy](/miniCTF2020/writeupfiles/2048deploy.rar) & [source](/miniCTF2020/writeupfiles/2048source.rar)

#### Solution

Đúng như cái tên sau khi bấm vào link, ta được dẫn đến 1 trang 2048 và với yêu cầu phải đạt 30102020 điểm thì trang web mới xuất hiện flag.

Game chơi thì rất vui nhưng để đạt đến con số kia thì không thể trong vòng ít nhất là vài ngày được. Vậy nên mình đã đi check thử xem có gì hay ho hay không và mình đã tìm ra, web này lưu Score trong mục local storage và có thể được chỉnh sửa:

![LocalStorage](/miniCTF2020/writeupfiles/localstorage.png)

Sau khi sửa bestScore thành 30102020 thì trên web đã xuất hiện flag:

![2048flag](/miniCTF2020/writeupfiles/2048flag.png)

Flag: `ispclub{4lw4y5_ch3ck_l0c4l_st0r4g3}`

# Web 100: Scroll

#### Challenge

Nếu biết về ma pháp JS thì ta đã không phải cuộn sushi rồi 

[Scroll] (/miniCTF2020/writeupfiles/Scroll.zip)

#### Solution

Khi bấm vào link nó dẫn ta tới 1 trang web được nhúng 1 vid youtube, sau 1 hồi SCROLL thì mình đã phát hiện ra đó là ở cuối trang có dòng chữ:

```
Hint: cuộn xuống tiếp đi 
```

Nhưng hint đó không có tác dụng gì cả. Vậy nên mình đã F12 để check source code của trang và phát hiện ra 1 hint khác:

![Scrollhint](/miniCTF2020/writeupfiles/Scrollhint.png)

Đường link background của trang web có gì đó khả nghi? 

```css
body {
    background-image: url(image.php?w=1&h=1);
    height: 10000px;
}
```

Thử [mở riêng](http://minictf.hypnguyen.us/image.php?w=1&h=1) nó ra và thử thay đổi giá trị w và h trở thành [thế này](http://minictf.hypnguyen.us/image.php?w=1000&h=500) và ta có được flag.

Flag: `ispclub{sh0u1dnt_l34rn_j4v4scr1pt}`

# Web 100: md5-1

#### Challenge

H3nl0r cho rằng mình rất giỏi về các loại mã hóa, hmm điều đó có đúng không nhỉ

https://minictf-web05.herokuapp.com/

#### Solution

Đối với chall này tụi mình xin phép trích `Wu của bạn Vũ Hoàng Anh` - người được giải Tiềm năng mùa miniCTF 2020 :3

