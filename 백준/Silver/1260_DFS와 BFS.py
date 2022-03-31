import sys
from collections import deque


N, M, V = map(int, sys.stdin.readline().split())
connected = [[] for _ in range(N+1)]
visited = [False]*(N+1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    connected[a].append(b)
    connected[b].append(a)

connected = list(map(lambda x: sorted(x, reverse=True), connected))

stack = [V]
result = []
while stack:
    node = stack.pop()

    if visited[node]:
        continue
    visited[node] = True

    result.append(node)
    for con in connected[node]:
        stack.append(con)

print(*result)

visited = [False]*(N+1)
visited[V] = True

queue = deque([V])
result = []
while queue:
    node = queue.popleft()
    result.append(node)

    for con in reversed(connected[node]):
        if not visited[con]:
            queue.append(con)
            visited[con] = True

print(*result)