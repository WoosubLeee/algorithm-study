N, M = map(int, input().split(' '))


# 1
def combine(combined, N, M):
    if len(combined) == M:
        print(' '.join(map(str, combined)))
    for i in range(1, N+1):
        if i not in combined:
            combined.append(i)
            combine(combined, N, M)
            combined.pop(-1)


combine([], N, M)


# # 2
# from itertools import permutations
#
#
# nums = map(str, range(1, N+1))
# print('\n'.join(list(map(' '.join, permutations(nums, M)))))