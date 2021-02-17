T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [[0 for i in range(N)] for j in range(N)]
    drc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    r, c = 0, 0
    delta = 0
    for i in range(1, (N ** 2) + 1):
        matrix[r][c] = i
        # 끝에 다다르거나(0 미만 혹은 5 이상), 이미 0이 아닌 값이 들어가 있을 경우 delta 증가시켜 방향 변화
        if not 0 <= r + drc[delta % 4][0] < N or not 0 <= c + drc[delta % 4][1] < N:
            delta += 1
        elif matrix[r + drc[delta % 4][0]][c + drc[delta % 4][1]]:
            delta += 1
        r += drc[delta % 4][0]
        c += drc[delta % 4][1]
    print(f'#{tc}')
    for i in matrix:
        for j in i:
            print(j, end=' ')
        if i != len(matrix) - 1:
            print()