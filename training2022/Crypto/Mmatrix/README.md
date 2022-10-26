# Mmatrix

Đề bài có file [encode.py](./encode.py) và một output thu được khi chạy file `encode.py`

```txt
Matrix:

1  2 5
3  1 7
2 -1 1

Ciphertext:

56 7 92 93 21 177 81 -8 112 90 35 209 70 35 173 46 -13 42 82 19 164
```

Trong file `encode.py` ta thấy được rằng:
- Hàm `b7708e77a` dùng để encode từ string thường ra `a1z26`
- Hàm `b67227539` dùng để chuyển vị ma trận
- Ma trận `k` ban đầu sẽ được chuyển vị và lưu vào `l`
- String `flag` thì được encode thành `a1z26` rồi chuyển thành một ma trận,
sau đó ma trận này được nhân với ma trận `l`, ma trận thu được sẽ được viết ra thành một dãy số

Từ đó để tìm ngược lại được flag ta cần thực hiện lần lượt các bước:
- Tính toán ma trận nghịch của ma trận `l` và thực hiện chuyển vị ma trận đó (ma trận thu được lưu vào `d`)
- Đưa dãy số `Ciphertext` về ma trận và thực hiện chuyển vị ma trận đó (ma trận thu được lưu vào `c`)
- Thực hiện nhân ma trận `d` và `c` sau đó chuyển ma trận về thành dãy số và thực hiện decode `a1z26` ta sẽ thu được flag

Chi tiết các bước có thể tham khảo [source code](./source.py) mà mình viết cho bài này

Flag: `ISPCTF{matrix_multiplication}`
