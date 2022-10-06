import numpy
import re
import pandas

def b7708e77a(b0ecf0b1):
    b0ecf0b1 = re.sub('[^a-z]', '`', b0ecf0b1)
    c09ff9d6 = [ord(elem) - 96 for elem in b0ecf0b1]
    if len(c09ff9d6) % 3 != 0: c09ff9d6 += [0] * ((len(c09ff9d6)//3 + 1)*3 - len(c09ff9d6))
    return [c09ff9d6[i:i+3] for i in range(0, len(c09ff9d6), 3)]

def b67227539(e8b7be43):
    ef2c6069 = [i[:min(len(e8b7be43), len(list(zip(*e8b7be43))))] for i in [e8b7be43[j] for j in range(min(len(e8b7be43), len(list(zip(*e8b7be43)))))]]
    for i in range(len(ef2c6069)):
        for j in range(i+1):
            if j ^ i != 0: 
                ef2c6069[i][j] = ef2c6069[i][j]^(ef2c6069[i][j]^e8b7be43[j][i])
                ef2c6069[j][i] = ef2c6069[j][i]^(e8b7be43[i][j]^ef2c6069[j][i])
    if len(ef2c6069) ^ len(e8b7be43) != 0:
        for i in range(len(ef2c6069), len(e8b7be43)):
            for j in range(len(list(zip(*e8b7be43)))):
                ef2c6069[j].append(e8b7be43[i][j])
    if len(list(zip(*e8b7be43))) ^ len(list(zip(*ef2c6069))) != 0:
        for i in range(len(list(zip(*ef2c6069))), len(list(zip(*e8b7be43)))):
            ef2c6069.append([e8b7be43[j][i] for j in range(len(e8b7be43))])
    return ef2c6069

k = [[1, 2, 3],
     [0, 1, 4],
     [5, 6, 0]]
flag = 'this_is_flag'

l = numpy.matrix(b67227539(k))
print('Matrix:\n', pandas.DataFrame(l).to_string(header=False, index=False), '', sep='\n')
c = (numpy.matrix(b7708e77a(flag)) * l).flatten()
print('Ciphertext:\n', pandas.DataFrame(c).to_string(header=False, index=False), '', sep='\n')
