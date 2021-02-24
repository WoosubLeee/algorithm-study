def find_route(s, g):
    visited[s] = 1
    for i in range(1, V+1):
        if adj[s][i] == 1:
            if i == g:
                return 1
            elif visited[i] == 0:
                if find_route(i, g):
                    return 1
    else:
        return 0


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]
    for e in range(E):
        S, G = map(int, input().split())
        adj[S][G] = 1

    S, G = map(int, input().split())
    visited = [0]*(V+1)
    result = find_route(S, G)
    print(f'#{tc} {result}')
