f = open("shiftNbases.txt", "r")
cipher = f.read().split()
f.close()

base = [8, 10, 16, 10]
text = ""
for i in range(0, len(cipher)):
    text += chr(int(cipher[i], base[i % 4]))

print(text)