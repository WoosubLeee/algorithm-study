def calc_need(s_r, s_c):
    white, black = 0, 0
    for i in range(s_r, s_r+8):
        for j in range(s_c, s_c+8):
            if i % 2 == 0:
                if j % 2 == 0:
                    if board[i][j] == 'B':
                        white += 1
                    else:
                        black += 1
                else:
                    if board[i][j] == 'W':
                        white += 1
                    else:
                        black += 1
            else:
                if j % 2 == 0:
                    if board[i][j] == 'W':
                        white += 1
                    else:
                        black += 1
                else:
                    if board[i][j] == 'B':
                        white += 1
                    else:
                        black += 1
    return min(white, black)

N, M = map(int, input().split())
board = [input() for _ in range(N)]

result = N*M
for i in range(N-7):
    for j in range(M-7):
        temp = calc_need(i, j)
        if temp < result:
            result = temp
print(result)
