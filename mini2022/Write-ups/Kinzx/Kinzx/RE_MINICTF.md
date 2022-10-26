

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
#### Challegen
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

# RE: Baby Kinzx

#### Challegen

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

# RE: XOR
#### Challegen

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