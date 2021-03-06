def find_way(s):
    for i in drc:
        new_r = s[0] + i[0]
        new_c = s[1] + i[1]
        if maze[new_r][new_c] == 0 and not visited[new_r][new_c]:
            visited[new_r][new_c] = 1
            if find_way([new_r, new_c]):
                return 1
        elif maze[new_r][new_c] == 3:
            return 1
    return 0


for _ in range(10):
    tc = input()
    maze = [list(map(int, input())) for _ in range(16)]
    i = -1
    done = False
    while not done:
        i += 1
        for j in range(16):
            if maze[i][j] == 2:
                start = [i, j]
                done = True
                break
    drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    visited = [[0]*16 for _ in range(16)]
    visited[start[0]][start[1]] = 1
    print(f'#{tc} {find_way(start)}')
