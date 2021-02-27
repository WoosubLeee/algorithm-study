def check(xc, yc):
    board[yc][xc] = bw
    for d in drc:
        try:
            count = 1
            while True:
                if yc + count*d[0] < 0 or xc + count*d[1] < 0:
                    raise Exception
                look = board[yc + count*d[0]][xc + count*d[1]]
                count += 1
                if look == 0:
                    raise Exception
                elif look == bw:
                    break
            for n in range(1, count):
                board[yc + n*d[0]][xc + n*d[1]] = bw
        except:
            pass


T = int(input())

drc = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0]*N for _ in range(N)]
    board[N//2-1][N//2-1], board[N//2-1][N//2], board[N//2][N//2-1], board[N//2][N//2] = 2, 1, 1, 2

    for m in range(M):
        x, y, bw = map(int, input().split())
        check(x-1, y-1)

    b_count = 0
    w_count = 0
    for i in board:
        b_count += i.count(1)
        w_count += i.count(2)
    print(f'#{tc} {b_count} {w_count}')
