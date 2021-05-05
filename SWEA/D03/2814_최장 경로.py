def dfs(n, count):
    global result
    if count > result:
        result = count

    visited[n] = True
    for i in range(1, N+1):
        if adj[n][i] and not visited[i]:
            dfs(i, count+1)
    visited[n] = False


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    adj = [[False]*(N+1) for _ in range(N+1)]
    visited = [False]*(N+1)
    for _ in range(M):
        x, y = map(int, input().split())
        adj[x][y], adj[y][x] = True, True
    result = 0
    for n in range(1, N+1):
        dfs(n, 1)
    print(f'#{tc} {result}')
