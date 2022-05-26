import sys
from collections import deque


M, N = map(int, sys.stdin.readline().split())

box = []
queue = deque()
count = 0
for i in range(N):
    box.append(list(map(int, sys.stdin.readline().split())))
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i, j, 0))
        elif box[i][j] == 0:
            count += 1

drc = [[0, 1], [0, -1], [1, 0], [-1, 0]]
while queue:
    ripen = queue.popleft()

    for d in drc:
        new_r, new_c = ripen[0] + d[0], ripen[1] + d[1]

        if 0 <= new_r < N and 0 <= new_c < M and box[new_r][new_c] == 0:
            queue.append((new_r, new_c, ripen[2] + 1))
            box[new_r][new_c] = 1
            count -= 1

print(ripen[2] if count == 0 else -1)
