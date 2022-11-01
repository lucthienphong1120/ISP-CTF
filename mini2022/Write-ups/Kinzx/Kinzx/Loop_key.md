
# RE: Loop Key 

### Challegen

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

### Solution

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
