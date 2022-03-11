import sys


def binary_search(left, right, target):
    if left > right:
        return 0

    mid = (right + left) // 2
    if target == arr[mid]:
        return 1
    elif target < arr[mid]:
        return binary_search(left, mid-1, target)
    else:
        return binary_search(mid+1, right, target)


N = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split(' '))))
M = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split(' ')))

result = []
for num in nums:
    result.append(str(binary_search(0, N-1, num)))
print('\n'.join(result))