'''
7
2 3
1 4 5
1 7
2 6
2 6
4 5 7
3 6
'''

N = int(input())
matrix = [[0]*(N+1) for _ in range(N+1)]
for i in range(N):
    for j in list(map(int, input().split())):
        matrix[i+1][j] = 1

start = 1
visited = [0]*(N+1)
queue = [start]
while queue:
    now = queue.pop(0)
    if visited[now]:
        continue
    print(now, end=' ')
    visited[now] = 1
    for i in range(1, len(matrix[now])):
        if matrix[now][i]:
            queue.append(i)
