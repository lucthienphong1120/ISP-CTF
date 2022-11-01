# RE: Baby Kinzx

### Challegen

#### Source Code

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

### Solution

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
