def dfs(start):
    visited[start] = 1
    print(start, end=' ')
    for i in range(N+1):
        if matrix[start][i] and visited[i] == 0:
            dfs(i)


N, M, V = map(int, input().split())
matrix = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    matrix[a][b], matrix[b][a] = 1, 1
visited = [0]*(N+1)
dfs(V)
print()

# bfs
queue = [V]
visited = [0]*(N+1)
while queue:
    start = queue.pop(0)
    if visited[start]:
        continue
    print(start, end=' ')
    visited[start] = 1
    for i in range(N+1):
        if matrix[start][i]:
            queue.append(i)
print()
