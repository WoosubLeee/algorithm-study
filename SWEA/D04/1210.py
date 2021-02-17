for _ in range(10):
    tc = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if matrix[99][i] == 2:
            idx = i
            break
    r = 99
    c = idx

    drc = [[-1, 0], [0, 1], [0, -1]]
    delta = 0
    while r:
        r += drc[delta][0]
        c += drc[delta][1]
        if delta:
            if matrix[r-1][c]:
                delta = 0
        else:
            for i in range(1, 3):
                if 0 <= c+drc[i][1] < 100:
                    if matrix[r][c+drc[i][1]] == 1:
                        delta = i
    print(f'#{tc} {c}')