import sys


N = int(sys.stdin.readline())
matrix = [sys.stdin.readline() for _ in range(N)]
visited = [[False]*N for _ in range(N)]
drc = [[1, 0], [-1, 0], [0, 1], [0, -1]]

result = []

for i in range(N):
    for j in range(N):
        if matrix[i][j] == '1' and not visited[i][j]:
            stack = [[i, j]]
            visited[i][j] = True
            count = 1

            while stack:
                house = stack.pop()
                for d in drc:
                    r, c = house[0] + d[0], house[1] + d[1]
                    if 0 <= r < N and 0 <= c < N and matrix[r][c] == '1' and not visited[r][c]:
                        stack.append([r, c])
                        visited[r][c] = True
                        count += 1

            result.append(count)

print(len(result))
print(*sorted(result), sep='\n')