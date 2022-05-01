from collections import deque


def solution(n, vertex):
    cons = [[] for _ in range(n+1)]
    for edge in vertex:
        cons[edge[0]].append(edge[1])
        cons[edge[1]].append(edge[0])

    visited = [False]*(n+1)
    visited[0], visited[1] = True, True

    queue = deque([[1]])
    while queue:
        nodes = queue.popleft()
        size = len(nodes)

        next_nodes = []
        for node in nodes:
            for next_node in cons[node]:
                if not visited[next_node]:
                    next_nodes.append(next_node)
                    visited[next_node] = True

        if next_nodes:
            queue.append(next_nodes)

    return size


n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, vertex))