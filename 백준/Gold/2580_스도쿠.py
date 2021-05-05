import sys


def get_filled(r, c):
    filled = [0]*10
    for i in range(9):
        filled[sudoku[r][i]] = 1
    for i in range(9):
        filled[sudoku[i][c]] = 1
    new_r = 0 if r < 3 else 3 if r < 6 else 6
    new_c = 0 if c < 3 else 3 if c < 6 else 6
    for i in range(3):
        for j in range(3):
            filled[sudoku[new_r+i][new_c+j]] = 1
    return filled


def fill(r, c):
    filled = get_filled(r, c)
    if filled.count(0) == 1:
        sudoku[r][c] = filled.index(0)
        return True
    return False


def backtrack(n):
    if n == len(blank):
        return True
    filled = get_filled(blank[n][0], blank[n][1])
    for i in range(1, 10):
        if filled[i]:
            continue
        sudoku[blank[n][0]][blank[n][1]] = i
        if backtrack(n+1):
            return True
        sudoku[blank[n][0]][blank[n][1]] = 0


sudoku = []
for _ in range(9):
    sudoku.append(list(map(int, sys.stdin.readline().split())))
blank = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append((i, j))
while blank:
    length = len(blank)
    for _ in range(length):
        now = blank.pop(0)
        if not fill(now[0], now[1]):
            blank.append(now)
    else:
        if len(blank) == length:
            break
backtrack(0)

for i in sudoku:
    print(*i)
