N, M = map(int, input().split(' '))


# # 1
# def make():
#     if len(nums) == M:
#         print(' '.join(nums))
#     else:
#         for i in range(1, N+1):
#             nums.append(str(i))
#             make()
#             nums.pop()
#
#
# nums = []
# make()


# 2
import itertools


nums = list(map(str, range(1, N+1)))
print('\n'.join(list(map(' '.join, itertools.product(nums, repeat=M)))))