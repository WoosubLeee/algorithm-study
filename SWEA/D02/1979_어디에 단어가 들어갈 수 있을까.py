T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for i in range(N)]
    count = 0
    drc = [[0, 1], [1, 0]]
    for i in range(N):
        for j in range(N):
            for d in drc:
                if matrix[i][j] and (i-d[0] == -1 or j-d[1] == -1 or not matrix[i-d[0]][j-d[1]]):
                    length = 1
                    r = i
                    c = j
                    while True:
                        r += d[0]
                        c += d[1]
                        if r == N or c == N:
                            break
                        if matrix[r][c]:
                            length += 1
                        else:
                            break
                    if length == K:
                        count += 1
    print(f'#{tc} {count}')