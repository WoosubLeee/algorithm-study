from sys import stdin
from collections import deque


def bfs(queue):
    drc = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    while True:
        [position, moved] = queue.popleft()
        for d in drc:
            new_r, new_c = position[0] + d[0], position[1] + d[1]
            if 0 <= new_r < N and 0 <= new_c < M and matrix[new_r][new_c]:
                if new_r == N-1 and new_c == M-1:
                    return moved + 1

                queue.append([(new_r, new_c), moved + 1])
                matrix[new_r][new_c] = 0


N, M = map(int, stdin.readline().split())
matrix = [list(map(int, stdin.readline().strip())) for _ in range(N)]
matrix[0][0] = 0

queue = deque([[(0, 0), 1]])

print(bfs(queue))