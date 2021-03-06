def get_distance():
    queue = [start]
    distance = [-1]
    visited = [[0]*N for _ in range(N)]
    drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    while queue:
        position = queue.pop(0)
        dist_p = distance.pop(0)
        for i in drc:
            new_r = position[0] + i[0]
            new_c = position[1] + i[1]
            if 0 <= new_r < N and 0 <= new_c < N:
                if maze[new_r][new_c] == 0 and not visited[new_r][new_c]:
                    visited[new_r][new_c] = 1
                    queue.append([new_r, new_c])
                    distance.append(dist_p + 1)
                elif maze[new_r][new_c] == 3:
                    return dist_p + 1
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    start = [-1, -1]
    for i in range(N):  # 시작점(2)를 찾아 start에 저장
        for j in range(N):
            if maze[i][j] == 2:
                start = [i, j]
    print(f'#{tc} {get_distance()}')
