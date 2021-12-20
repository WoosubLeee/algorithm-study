import sys


# nums = set()
# for _ in range(10):
#     nums.add(int(sys.stdin.readline()) % 42)
# print(len(nums))

#

print(len(set([int(sys.stdin.readline()) % 42 for _ in range(10)])))