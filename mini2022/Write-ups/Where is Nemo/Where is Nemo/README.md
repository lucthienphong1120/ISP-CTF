# Forensics: Where is Nemo?
#### Challegen
Nemuuu là chú pet robot được Bốp rất yêu quý. Không may chú đã bị dính code bẩn và chạy lung tung không nhớ được về. Hãy giúp Bốp mang Nemu về nhé, đừng bỏ cuộc!!! Rescue Nemooo :<

[Where_is_Nemo.jpg](https://github.com/Dongkong1908/MiniCTF-2022/blob/main/Where%20is%20Nemo/Where_is_Nemo.zip?raw=true)

#### Solution

Tải ảnh về, mở lên không có gì ẩn trong ảnh cả, có thể file ẩn bên trong là dạng file khác, thử đổi tên ảnh từ đuôi .jpg thành đuôi .zip

<img src=https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/Where%20is%20Nemo/img/where_nemo_1.png>

Giải nén file trên lại được 1 cái ảnh khác 

<img src=https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/Where%20is%20Nemo/img/where_nemo_2.png>

Cứ đổi tên rồi lại giải nén cho đến khi gặp được file nemo.txt

<img src=https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/Where%20is%20Nemo/img/where_nemo_3.png>

Mở thử lên, ở đoạn đầu thấy được dạng đúng của file là dạng jfif tương ứng với đuôi file là .jpg hoặc .jpeg. 

<img src= https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/Where%20is%20Nemo/img/where_nemo_4.png>

Mở lên và lấy được flag 

<img src= https://raw.githubusercontent.com/Dongkong1908/MiniCTF-2022/main/Where%20is%20Nemo/img/nemo.jpg height=600px >

Flag: `ISPCTF{y0u_5ave_Nem0_f15h}`