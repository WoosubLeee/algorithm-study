drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for tc in range(1, int(input())+1):
    grid = [list(map(str, input().split())) for _ in range(4)]
    result = grid
    for _ in range(6):
        temp = [[set() for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                for d in drc:
                    new_r, new_c = i+d[0], j+d[1]
                    if 0 <= new_r < 4 and 0 <= new_c < 4:
                        for num in result[i][j]:
                            temp[new_r][new_c].add(num + grid[new_r][new_c])
        result = temp
    for i in range(4):
        result[i] = set.union(*result[i])
    result = set.union(*result)
    print(f'#{tc} {len(result)}')
