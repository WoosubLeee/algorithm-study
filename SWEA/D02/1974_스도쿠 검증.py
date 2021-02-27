def check():
    for line in sudoku:
        for i in range(1, 10):
            if line.count(i) != 1:
                return 0
    for i in range(9):
        line = []
        for j in range(9):
            line.append(sudoku[j][i])
        for j in range(1, 10):
            if line.count(j) != 1:
                return 0
    for i in range(3):
        for j in range(3):
            box = []
            for m in range(3):
                for n in range(3):
                    box.append(sudoku[3*i + m][3*j + n])
            for m in range(1, 10):
                if box.count(m) != 1:
                    return 0
    return 1


T = int(input())

for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{tc} {check()}')
