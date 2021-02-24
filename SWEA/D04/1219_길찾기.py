def find_route(s, g):
    visited[s] = 1
    for i in range(100):
        if adj[s][i] == 1:
            if i == g:
                return 1
            elif visited[i] == 0:
                if find_route(i, g):
                    return 1
    else:
        return 0

try:
    while True:
        tc, N = map(int, input().split())
        adj = [[0]*100 for _ in range(100)]
        visited = [0]*100
        way_list = list(map(int, input().split()))
        for i in range(N):
            adj[way_list[2*i]][way_list[2*i + 1]] = 1
        print(f'#{tc} {find_route(0, 99)}')
except:
    pass
