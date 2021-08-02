import heapq


def calc_distance():
    distances = []
    for from_to in ['from', 'to']:
        distance = [float('inf')]*(N+1)
        distance[0], distance[X] = 0, 0
        visited = [False]*(N+1)

        queue = [(0, X)]
        while queue:
            min_dist, node = heapq.heappop(queue)
            if visited[node]:
                continue
            visited[node] = True
            for i in range(1, N+1):
                dist = adj[node][i] if from_to == 'from' else adj[i][node]
                if dist and not visited[i]:
                    new_dist = min_dist + dist
                    if new_dist < distance[i]:
                        distance[i] = new_dist
                        heapq.heappush(queue, (new_dist, i))
        distances.append(distance)
    return distances


for tc in range(1, int(input())+1):
    N, M, X = map(int, input().split())
    adj = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        adj[x][y] = c

    distances = calc_distance()
    result = [0]*(N+1)
    for i in range(1, N+1):
        result[i] = (distances[0][i] + distances[1][i])
    print(f'#{tc} {max(result)}')
