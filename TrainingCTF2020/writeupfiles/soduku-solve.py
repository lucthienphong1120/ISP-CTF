# sudoku solve tool modded to solve sudoku challenge 
def test_cell(s, row, col):
    used = [0]*10
    used[0] = 1
    block_row = row // 3
    block_col = col // 3
    for m in range(9):
        used[s[m][col]] = 1;
        used[s[row][m]] = 1;
    for m in range(3):
        for n in range(3):
            used[s[m + block_row*3][n + block_col*3]] = 1
    return used
def initial_try(s):
    stuck = False
    while not stuck:
        stuck = True
        for row in range(9):
            for col in range(9):
                used = test_cell(s, row, col)
                if used.count(0) != 1:
                    continue
                for m in range(1, 10):
                    if s[row][col] == 0 and used[m] == 0:
                        s[row][col] = m
                        stuck = False
                        break
def DFS_solve(s, row, col):
    if row == 8 and col == 8:
        used = test_cell(s, row, col)
        if 0 in used:
            s[row][col] = used.index(0)
        return True
    if col == 9:
        row = row+1
        col = 0
    if s[row][col] == 0:
        used = test_cell(s, row, col)
        for i in range(1, 10):
            if used[i] == 0:
                s[row][col] = i
                if DFS_solve(s, row, col+1):
                    return True
        s[row][col] = 0
        return False
    return DFS_solve(s, row, col+1)
def main():
    s = []
    text =""
    # chuoi string input vao
    sudoku="haagaacadacaibaafaaafajcaaacaaahafaidahaajacaajaaeaaahbaiadhaacaaabaaiaagacaaajda"
    # chuyen tu chuoi ky tu thanh chuoi so
    for i in sudoku:
        text += str(ord(i)-97)
    # chuyen chuoi so thanh dang ma tran 9*9 va giai sudoku
    while len(text) > 0:
        l = []
        while len(l) < 9:
            if text[0].isdigit():
                l.append(int(text[0]))
            text = text[1:]
        s.append(l)
        if len(s) == 9:
            initial_try(s)
            for line in s:
                if 0 in line:
                    DFS_solve(s, 0, 0)
                    break
    # in ra string solved theo format cua challenge
    for row in range(9):
        for col in range(9):
            print(chr(int(s[row][col])+97), end='')
if __name__ == "__main__":
    main()
 