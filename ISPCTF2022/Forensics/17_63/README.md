Đề bài gồm 2 file, 1 file không định dạng và 1 file được nén zip có mật khẩu.

Suy đoán: file không định dạng chứa mật khẩu của file được nén.

Để ý 1 chút ở file không định dạng và đề bài thì có kí tự | ở giữa, có thể liên quan đến loại dịch chuyển kí tự. Áp dụng dịch chuyển theo 17 ở bên phải và 63 ở bên trái ta thu được như sau:
`4dd2lunnbeRz|pcap`
-> có thể đoán đây là file pcap, như vậy kí tự | sẽ là '.'.
add 2 numbers ở đây chính là 2 số ở đề bài, ta cộng vào thì ra 80.

Tên file nén là protocol + 80 -> tìm những thứ có liên quan đến pass ở protocol = 80 (http) với wireshark -> `wjBun3veRdiE` (pass giải nén)

File flag với những dãy nhị phân ở đầu và đằng sau là 1 chữ cái -> chuyển thành desc thu được dãy số 80 và những số khác. Để í lại tên file zip.
cat flag.txt | grep '1010000' ->  
1010000 Big 
1010000 I 
1010000 Now 
1010000 Go 
1010000 Ohshit...

flag: `ISPCTF{BINGO}`

