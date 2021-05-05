import heapq


drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for tc in range(1, int(input())+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    distance, visited = [[2000]*N for _ in range(N)], [[False]*N for _ in range(N)]
    distance[0][0] = 0
    heap = [[0, 0, 0]]
    while heap:
        candi = heapq.heappop(heap)
        if visited[candi[1]][candi[2]]:
            continue
        if candi[1:3] == [N-1, N-1]:
            break
        visited[candi[1]][candi[2]] = True
        for d in drc:
            new_r, new_c = candi[1] + d[0], candi[2] + d[1]
            if 0 <= new_r < N and 0 <= new_c < N and not visited[new_r][new_c]:
                new_dist = candi[0] + 1 + max(grid[new_r][new_c] - grid[candi[1]][candi[2]], 0)
                if new_dist < distance[new_r][new_c]:
                    heapq.heappush(heap, [new_dist, new_r, new_c])
                    distance[new_r][new_c] = new_dist
    print(f'#{tc} {candi[0]}')
