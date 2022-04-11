import sys


def dfs(node):
    global result

    for con in cons[node]:
        if not visited[con]:
            visited[con] = 1
            result += 1
            dfs(con)


N = int(sys.stdin.readline())
cons = [[] for _ in range(N+1)]
for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    cons[a].append(b)
    cons[b].append(a)

visited = [0]*(N+1)
visited[1] = 1
result = 0
dfs(1)
print(result)