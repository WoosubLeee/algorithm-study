def plan_a():
    global result
    while False in visited:
        for i in range(E):
            if not included[i] and ((visited[edges[i][0]] and not visited[edges[i][1]]) or (not visited[edges[i][0]] and visited[edges[i][1]])):
                result += edges[i][2]
                if result > M:
                    mins = [1000000]*(V+1)
                    mins[1] = 0
                    plan_b(1)
                visited[edges[i][0]], visited[edges[i][1]] = True, True
                included[i] = True
                break
    else:
        result = M - result


def plan_b(n):
    for edge in edges:
        if edge[0] == n:
            s, e = n, edge[1]
        elif edge[1] == n:
            s, e = n, edge[0]
        else:
            continue



for tc in range(1, int(input())+1):
    V, E, M = map(int, input().split())
    edges = []
    for _ in range(E):
        edges.append(list(map(int, input().split())))
    edges.sort(key=lambda x: x[2])

    result = edges[0][2]
    visited, included = [False]*(V+1), [False]*E
    visited[0], visited[edges[0][0]], visited[edges[0][1]], included[0] = True, True, True, True
    plan_a()
    print(f'#{tc} {result}')
