import sys
from collections import deque


N, M = map(int, sys.stdin.readline().split(' '))
idxs = list(map(int, sys.stdin.readline().split(' ')))

d = list(range(1, N+1))
result = 0

# 1
for i in range(M):
    idx = d.index(idxs[i])
    result += min(len(d[:idx]), len(d[idx:]))
    d = d[idx+1:] + d[:idx]

# # 2
# for i in range(M):
#     count = 0
#     while True:
#         left = d.popleft()
#         if left != idxs[i]:
#             d.append(left)
#             count += 1
#         else:
#             if count > len(d) // 2:
#                 count = len(d)+1 - count
#             result += count
#             break

print(result)