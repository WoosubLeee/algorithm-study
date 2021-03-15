from collections import deque


drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    map_a = [input() for _ in range(N)]

    visited = [[0]*M for _ in range(N)]
    queue = deque()
    for i in range(N):
        for j in range(M):
            if map_a[i][j] == 'W':
                queue.append((i, j))
                visited[i][j] = 1

    distance = 1
    total = 0
    while queue:
        for _ in range(len(queue)):
            q = queue.popleft()
            for d in drc:
                new_i, new_j = q[0] + d[0], q[1] + d[1]
                if 0 <= new_i < N and 0 <= new_j < M and not visited[new_i][new_j]:
                    total += distance
                    visited[new_i][new_j] = 1
                    queue.append((new_i, new_j))
        distance += 1
    print(f'#{tc} {total}')
