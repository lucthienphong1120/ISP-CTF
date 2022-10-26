import itertools

def multiply(m1,m2):
    ret = []
    for i in range(0,len(m1)):
        tmp=[]
        for j in range(0,len(m2[0])):
            s = 0
            for k in range(0,len(m1[0])):
                s += round(m1[i][k] * m2[k][j])
            tmp.append(s)
        ret.append(tmp)
    return ret

def transpose(m):
    rows = len(m)
    columns = len(m[0])
    m_T = []
    for j in range(columns):
        row = []
        for i in range(rows):
           row.append(m[i][j])
        m_T.append(row)
    return m_T

def eliminate(r1, r2, col, target=0):
    fac = (r2[col]-target) / r1[col]
    for i in range(len(r2)):
        r2[i] -= fac * r1[i]

def gauss(m):
    for i in range(len(m)):
        if m[i][i] == 0:
            for j in range(i+1, len(m)):
                if m[i][j] != 0:
                    m[i], m[j] = m[j], m[i]
                    break
            else: raise ValueError("Matrix is not invertible")
        for j in range(i+1, len(m)):
            eliminate(m[i], m[j], i)
    for i in range(len(m)-1, -1, -1):
        for j in range(i-1, -1, -1):
            eliminate(m[i], m[j], i)
    for i in range(len(m)):
        eliminate(m[i], m[i], i, target=1)
    return m

def inverse(m):
    tmp = [[] for _ in m]
    for i,row in enumerate(m):
        assert len(row) == len(m)
        tmp[i].extend(row + [0]*i + [1] + [0]*(len(m)-i-1))
    gauss(tmp)
    ret = []
    for i in range(len(tmp)):
        ret.append(tmp[i][len(tmp[i])//2:])
    return [[round(ret[i][j], 1) for j in range(len(ret[i]))] for i in range(len(ret))]

def roundm(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j] = round(m[i][j])


def a1z26_encode(plain:str) -> list:
    s = plain.replace('_', '`')
    return [ord(elem) - 96 for elem in s]

def a1z26_decode(encoded: list) -> str:
    return ("".join(chr(elem + 96) for elem in encoded)).replace('`', '_')

def printm(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print('{:4}'.format(m[i][j]), end = ' ')
        print()
    print()

if __name__ == '__main__':

    EncodeKey = [[1, 3,  2],
                 [2, 1, -1],
                 [5, 7,  1]]

    """ Encode """
    EncodeKey = transpose(EncodeKey)
    printm(EncodeKey)
    flag = 'matrix_multiplication'
    PlaintText = a1z26_encode(flag)
    PlaintText = [PlaintText[i:i+3] for i in range(0, len(flag), 3)]
    printm(PlaintText)
    CipherText = multiply(PlaintText, EncodeKey)
    printm(CipherText)

    print('Matrix:\n')
    print(EncodeKey)
    print('Ciphertext:\n')
    print(' '.join([str(elem) for elem in list(itertools.chain.from_iterable(CipherText))]))

    """ Decode """
    DecodeKey = transpose(inverse(EncodeKey))
    CipherText = transpose(CipherText)
    Message = transpose(multiply(DecodeKey, CipherText))
    Message = list(itertools.chain.from_iterable(Message))
    print(a1z26_decode(Message))