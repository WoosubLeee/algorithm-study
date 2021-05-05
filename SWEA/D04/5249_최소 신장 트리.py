for tc in range(1, int(input())+1):
    V, E = map(int, input().split())

    # # Prim's algorithm

    # def find_min():
    #     min_v, min_w = queue[0], 10
    #     for q in queue:
    #         if weights[q] < min_w:
    #             min_v, min_w = q, weights[q]
    #     return min_v
    #
    # adj = [[10]*(V+1) for _ in range(V+1)]
    # for _ in range(E):
    #     n1, n2, w = map(int, input().split())
    #     adj[n1][n2], adj[n2][n1] = w, w
    #
    # weights = [10]*(V+1)
    # weights[0] = 0
    #
    # queue = list(range(V+1))
    # result = 0
    # while queue:
    #     v = queue.pop(queue.index(find_min()))
    #     result += weights[v]
    #     for i in range(V+1):
    #         if i in queue and adj[v][i] < weights[i]:
    #             weights[i] = adj[v][i]

    # KRUSKAL algorithm
    def find_set(n):
        if n == parents[n]:
            return n
        return find_set(parents[n])


    def union(parent, child):
        parents[find_set(child)] = find_set(parent)


    edges = [list(map(int, input().split())) for _ in range(E)]
    edges.sort(key=lambda x: x[2])

    parents = list(range(V+1))
    result = 0
    for edge in edges:
        if find_set(edge[0]) != find_set(edge[1]):
            result += edge[2]
            union(edge[0], edge[1])

    print(f'#{tc} {result}')
