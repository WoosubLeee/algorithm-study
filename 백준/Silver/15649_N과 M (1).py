N, M = map(int, input().split())

# 1
# def do(n):
#     if n == M:
#         print(*nums)
#     else:
#         for i in range(1, N+1):
#             if not picked[i]:
#                 nums.append(i)
#                 picked[i] = 1
#                 do(n+1)
#                 nums.remove(i)
#                 picked[i] = 0
# nums = []
# picked = [0]*(N+1)
# do(0)

# 2
import itertools


for i in itertools.permutations(range(1, N+1), M):
    print(*i)