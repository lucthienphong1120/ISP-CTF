# You are noob !!
---

Đề cho ta 1 đoạn text với dòng chữ:
`aHR0cHM6Ly93d3cuaW5zdGFncmFtLmNvbS80Y2MzZXNzX20zLw==`

Với kinh nghiệm của mình thì mã có dấu "=" ở cuối thì 90% là Base64 rồi!, mình decode và nhận được:

Sau khi quét thì nhận được 1 bức ảnh với 1 dòng chữ bên dưới trông có vẻ giống form Flag nhưng đã bị mã hóa

![1](https://raw.githubusercontent.com/LeeDiay/MiniCTF_2022/main/You%20are%20noob/S1.png)

Link dẫn tới trang cá nhân instagram của 1 hecke lỏ, hắn bảo rằng "Đố anh bắt được em"

![2](https://github.com/LeeDiay/MiniCTF_2022/raw/main/You%20are%20noob/S2.png)

Phần tiểu sử có chứa các đoạn mã, đoạn `173 83 80 67 84 70 123 99 52 84 95 77 51` mình đã đoán được đây là mã Decimal, decode thì ra được đoạn đầu của Flag:

![3](https://github.com/LeeDiay/MiniCTF_2022/raw/main/You%20are%20noob/S3.png)

Còn đoạn mã phía sau chắc chắn là Base64 rồi, decode thì ra được: 

![4](https://github.com/LeeDiay/MiniCTF_2022/raw/main/You%20are%20noob/S4.png)

Link dẫn tới 1 trang web lại có thêm thông tin:

![5](https://github.com/LeeDiay/MiniCTF_2022/raw/main/You%20are%20noob/S5.png)

Khúc này, cứ ngỡ như mình đã tìm thấy đoạn còn lại của Flag, nhưng không, sau khi thử hơn 50 lần thì nó vẫn báo WA...
Phía bên dưới còn 1 đoạn mã Base64 nữa nên mình sẽ tiếp tục nghiên cứu thêm nó, mã hóa thì ta đc 1 đường link dẫn tới 1 bức ảnh: 

![6](https://github.com/LeeDiay/MiniCTF_2022/raw/main/You%20are%20noob/S6.png)

Phần tiêu đề của link này là "9R34t_w4y" làm mình lại bị mắc cú lừa lần 2, thử hơn chục lần vẫn sai...
Nhìn thấy ảnh ông chú áo vàng đã bị quay sang trái với 1 tay là chữ "DEC" và 1 tay là chữ "RAIL". Ngẫm 1 lúc lâu thì mình cũng đã hiểu được ẩn ý của tác giả: đó là Flag được ghép từ 2 phần. Một phần là mã Decimal từ ban đầu, và phần còn lại là "_un1__4?fC}" chắc chắn bị mã hóa bằng code "Rail Fence". Tốn 100 xu mua hint thì mình đã có key để giải bằng 3. Lúc này mình chỉ việc decode và sub flag thôi :D

![7](https://github.com/LeeDiay/MiniCTF_2022/raw/main/You%20are%20noob/S7.png)

Flag `ISPCTF{c4T_M3_1f_u_C4n?}`
