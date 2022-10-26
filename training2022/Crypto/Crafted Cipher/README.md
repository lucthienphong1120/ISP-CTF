- Đề bài cung cấp 1 file mã nguồn viết bằng C cùng với 1 kết nối netcat tới server.
- Khi kết nối tới server bằng netcat, chúng ta thấy một chương trình nhận vào input, 
và trả về kết quả mã hóa gồm 2 thông tin:
  + Kết quả mã hóa chuỗi input nhập vào (Cipher text)
  + Một mảng số nguyên (Index)
	----- Welcome to the Crafted Cipher -----
	  Plaintext:  abcdefgh
	> Ciphertext: _9f__c__
	> Index: -1 14 21 -1 -1 20 -1 -1

- Dựa vào mã nguồn được cung cấp, chúng ta xác định được 2 điều:
  + Chương trình sử dụng dạng mã hóa thay thế
	dòng 17: plaintext[i] = alphabet[(i+j)%32]
  + "Index" là vị trí của của ký tự thay thế vào vị trí thứ "i" của input
	dòng 18: index[i+1] = (i+j)%32
    do mảng index được tạo với len(input) + 1 và phần tử index[0] sẽ không được trả về
	dòng 31: for (int i = 1; i <= strlen(plaintext); ++i) {
                     printf("%d ", index[i]);
        	 }

- Trong dữ liệu trả về, chúng ta không cần để ý tới các vị trí được thay thế thành ký tự "_" và có "index = -1".
Vì theo như mã nguồn, kết quả như vậy là do trong FLAG (tương ứng trong mã nguồn là mảng alphabet) 
không có ký tự đó.

(1): chúng ta có thể nhập input chứa các ký tự a-z, A-Z, 0-9 và xác định xem FLAG chứa những ký tự nào
	----- Welcome to the Crafted Cipher -----
	  Plaintext:  abcdefghijklmnopqrstuvwxyz
	> Ciphertext: _9f__c____________________
	> Index: -1 14 21 -1 -1 20 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
    => FLAG chứa: "b", "c", "f"

	----- Welcome to the Crafted Cipher -----
	  Plaintext:  ABCDEFGHIJKLMNOPQRSTUVWXYZ
	> Ciphertext: __________________________
	> Index: -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
    => FLAG không chứa ký tự in hoa

	----- Welcome to the Crafted Cipher -----
	  Plaintext:  0123456789
	> Ciphertext: 06_9__36cf
	> Index: 8 17 -1 14 -1 -1 11 5 1 21
    => FLAG chứa: "0", "1", "3", "6", "7", "8", "9"
  => Không gian của FLAG gồm: "b", "c", "f", "0", "1", "3", "6", "7", "8", "9"

- Khi xác định được không gian của FLAG rồi, việc tiếp theo là xác định vị trí của các ký tự.
- Chúng ta sẽ xác định qua mảng "index".

(2): thử nhập vào 1 chuỗi toàn ký tự "b", chúng ta nhận được kết quả như sau:
	----- Welcome to the Crafted Cipher -----
	  Plaintext:  bbbbbbbbb
	> Ciphertext: b8cc6b_cc
	> Index: 13 25 28 0 17 29 -1 20 0
  - index[1] = index[i + 1] = 13 = (i + j) % 32
  <=> (0 + j) % 32 = 13
  <=> j % 32 = 13
  <=>  j thuộc [13, 26, 39,...], thỏa mãn j < 32 và j > i (theo điều kiện thứ 2 trong hàm if() tại dòng 16)
  => j = 13 => FLAG[13] = b

  - index[2] = index[i + 1] = 25 = (i + j) % 32
  <=> (1 + j) % 32 = 25
  <=> j % 32 = 24
  <=> j thuộc [24, 56,...], thỏa mãn j < 32 và j > i
  => j = 13 => FLAG[24] = b

  - index[3] = index[i + 1] = 28 = (i + j) % 32
  <=> (2 + j) % 32 = 28
  <=> j % 32 = 26
  <=> j thuộc [26, 90,...], thỏa mãn j < 32 và j > i
  => j = 26 => FLAG[26] = b

- Làm tương tự với input toàn ký tự "c", "f",... , "9" ta có thể xác định được toàn bộ FLAG.

Vậy FLAG là: cc2886d10c739b9f16fccfc9b8b8cb73