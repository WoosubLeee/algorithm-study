N = int(input())
field = []
max_height = 0
for i in range(N):
    field.append(list(map(int, input().split())))
    for j in field[-1]:
        if j > max_height:
            max_height = j
max_count = 0
drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for height in range(max_height):
    included = [[0]*N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if field[i][j] > height and not included[i][j]:
                count += 1

                queue = [[i, j]]
                while queue:
                    popped = queue.pop(0)
                    for d in drc:
                        new_r = popped[0]+d[0]
                        new_c = popped[1]+d[1]
                        if 0 <= new_r < N and 0 <= new_c < N and not included[new_r][new_c]:
                            if field[new_r][new_c] > height:
                                queue.append([new_r, new_c])
                                included[new_r][new_c] = 1
    if count > max_count:
        max_count = count
print(max_count)
