import heapq


for tc in range(1, int(input())+1):
    N, E = map(int, input().split())
    adj = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w

    distance = [float('inf')]*(N+1)
    distance[0] = 0

    visited = [False]*(N+1)

    queue = [(0, 0)]
    while queue:
        min_dist, node = heapq.heappop(queue)
        if visited[node]:
            continue
        if node == N:
            break
        visited[node] = True
        for i in range(N+1):
            if adj[node][i] and not visited[i]:
                new_dist = min_dist + adj[node][i]
                if new_dist < distance[i]:
                    distance[i] = new_dist
                    heapq.heappush(queue, (new_dist, i))
    print(f'#{tc} {distance[N]}')
