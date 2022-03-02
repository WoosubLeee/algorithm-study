import sys


def dnq(r_start, c_start, n):
    isSame = True
    for i in range(n):
        for j in range(n):
            if paper[r_start + i][c_start + j] != paper[r_start][c_start]:
                isSame = False
                break
        if not isSame:
            break
    else:
        if paper[r_start][c_start]:
            global black
            black += 1
        else:
            global white
            white += 1
        return

    half = n // 2
    for i in range(2):
        for j in range(2):
            dnq(r_start + i*half, c_start + j*half, half)


N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]
white, black = 0, 0

dnq(0, 0, N)
print(white)
print(black)