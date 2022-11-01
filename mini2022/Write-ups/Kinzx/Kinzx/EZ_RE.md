# RE: EZ RE

### Challenge

#### Source Code 

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

### Solution

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
