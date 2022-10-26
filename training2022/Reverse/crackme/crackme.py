import binascii

s = binascii.unhexlify("137d52502c68745a0c254c2e46481b05327d597c571d577670")
l = len(s)
for byte in range(256):
    flag = [c for c in s]
    key = byte
    prevbyte = 0
    for _ in range(2606):
        prev = [0] * l
        prev[l - 1] = key ^ prevbyte
        for i in range(l - 1)[::-1]:
            prev[i] = prev[i + 1] ^ flag[i + 1]
            key = prev[i]
        prevbyte = flag[0]
        flag = prev
    flag = "".join([chr(c) for c in flag])
    if "ISPCTF{" in flag:
        print(flag)
