# RE: XOR

### Challegen

#### Source Code

```c++
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

### Solution

- Sau khi đọc đề ta thấy để ra được flag thì sau khi encrypt `input` đc `your_cipher` phải bằng với `cipher` .

```c++

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
    ```c++
    char ISPCLUB(char a, char b) {
    return END(OO(a, LOST(b)), OO(LOST(a), b));
    ```
    +  Kết quả của hàm này sẽ return Bit_1 `XOR` Bit_2
    ```c++
    for (char k = 7; k >= 0; k--) {
            result = (result << 1) + tmp[k];
        }
    ```
    + Đến với hàm này có tác dụng ghép 8 bit lại sau khi tách ra để encrypt.

```c++
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
