# Forensics: Are you Wibu?  
#### Challenge

Tại sao lại có bức ảnh này ở đây thế nhỉ ? Có điều gì sai chăng

[Are_you_wibu.zip](https://github.com/Dongkong1908/MiniCTF-2022/blob/main/Are%20you%20Wibu/Are_u_wibu.zip?raw=true)

#### Solution

Tải file về không mở được, thử đổi đuôi tên thành .jpg , mở lên được file như thế này 

<img src= https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/Are%20you%20Wibu/wibu_1.png height=600>

Nhìn qua ảnh, biết được ảnh bị chồng/ dồn pixel theo chiều ngang, nên phải sửa độ phân giải của ảnh. Xem propertises/ detail của ảnh, biết được chiều rộng của ảnh hiện tại đang là 642px

<img src= https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/Are%20you%20Wibu/wibu_2.png height=500>


Đổi 642 sang Hex thấy được giá trị của nó là 02 82. Mở ảnh bằng Hxd hoặc Hexed.it để tìm vị trí byte chứa size ảnh 

<img src= https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/Are%20you%20Wibu/wibu_3.png>

Thử thay đổi liên tục thì biết được giá trị đúng của nó là 07 82 tương ứng 1922px, mở ảnh ta thấy flag

<img src= https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/Are%20you%20Wibu/wibu_4.png>

Flag: `ISPCTF{w1bu_n3v3r_d13_1337}`