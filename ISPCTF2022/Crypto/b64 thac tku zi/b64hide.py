from base64 import b64encode, b64decode

charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
raw = open('text.inp', 'rb').readlines()
f = open('strawberriesncigarettes.enc', 'w')
# f = open('text.o2', 'w')
flag = 'ISPCTF{now_you_know_your_b64}'
flagbin = ''.join(format(ord(c), 'b').zfill(8) for c in flag)
while True:
    for line in raw:
        line = line.decode().replace("\n", "")
        b64 = b64encode(line.encode()).decode()
        bits = b64.count("=") * 2
        if bits > 0 and bits <= len(flagbin):
            # f.write(flagbin[:bits])
            shift = int(flagbin[:bits], 2)
            flagbin = flagbin[bits:]
            pos = b64.find('=') - 1
            b64 = list(b64)
            b64[pos] = charset[charset.find(b64[pos]) + shift]
            b64 = ''.join(b64)
        f.write(b64)
        f.write('\n')
        if (len(flagbin) == 0):
            break
    if len(flagbin) == 0:
        break
f.close()
