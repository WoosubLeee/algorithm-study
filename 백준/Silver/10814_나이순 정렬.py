import sys


N = int(sys.stdin.readline())
ages = [[] for _ in range(201)]
for _ in range(N):
    member = sys.stdin.readline().strip().split(' ')
    ages[int(member[0])].append(member[1])

result = ''
for i, age in enumerate(ages):
    for member in age:
        result += f'{i} {member}\n'

print(result.strip())


# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     mid = len(arr) // 2
#     low_arr = merge_sort(arr[:mid])
#     high_arr = merge_sort(arr[mid:])
#
#     merged = []
#     l = h = 0
#     while l < len(low_arr) and h < len(high_arr):
#         if int(low_arr[l][0]) <= int(high_arr[h][0]):
#             merged.append(low_arr[l])
#             l += 1
#         else:
#             merged.append(high_arr[h])
#             h += 1
#     merged += low_arr[l:]
#     merged += high_arr[h:]
#
#     return merged
#
#
# N = int(sys.stdin.readline())
# members = [sys.stdin.readline().strip().split(' ') for _ in range(N)]
# sorted_members = merge_sort(members)
#
# result = []
# for member in sorted_members:
#     result.append(' '.join(member))
# print('\n'.join(result))