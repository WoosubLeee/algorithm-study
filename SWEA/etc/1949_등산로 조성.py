def find(y, x, height):
    global length, longest, used
    visited[y][x] = 1
    length += 1
    if length > longest:
        longest = length
    for d in drc:
        if 0 <= y + d[0] < N and 0 <= x + d[1] < N and not visited[y+d[0]][x+d[1]]:
            d_height = map_x[y+d[0]][x+d[1]]
            if d_height < height:
                find(y+d[0], x+d[1], d_height)
            elif not used and d_height - K < height:
                used = True
                find(y+d[0], x+d[1], height - 1)
                used = False
    visited[y][x] = 0
    length -= 1


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    map_x = [list(map(int, input().split())) for _ in range(N)]
    high = 0
    high_yx = []
    for i in range(N):
        for j in range(N):
            if map_x[i][j] > high:
                high = map_x[i][j]
                high_yx = [[i, j]]
            elif map_x[i][j] == high:
                high_yx.append([i, j])
    drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    length = 0
    longest = 0
    visited = [[0]*N for _ in range(N)]
    used = False
    for i in high_yx:
        find(i[0], i[1], high)
    print(f'#{tc} {longest}')