def look(core):
    global length, min_len
    if core == len(cores):
        if length < min_len:
            min_len = length
    else:
        if cores[core][0] in [0, N] or cores[core][1] in [0, N]:
            look(core + 1)
        else:
            for d in drc:
                r, c = cores[core]
                while 0 < r < N-1 and 0 < c < N-1:
                    r += d[0]
                    c += d[1]
                    if pro[r][c]:
                        r -= d[0]
                        c -= d[1]
                        break
                    pro[r][c] = 2
                    length += 1
                else:
                    look(core + 1)
                while [r, c] != cores[core]:
                    pro[r][c] = 0
                    length -= 1
                    r -= d[0]
                    c -= d[1]


drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for tc in range(1, int(input())+1):
    N = int(input())
    pro = [list(map(int, input().split())) for _ in range(N)]
    cores = []
    for i in range(N):
        for j in range(N):
            if pro[i][j]:
                cores.append([i, j])
    length, min_len = 0, 1000000
    look(0)
    print(f'#{tc} {min_len}')
