def check(height, trees, target):
    total = 0
    for tree in trees:
        gap = tree - height
        if gap > 0:
            total += gap

    return total >= target


N, M = map(int, input().split(' '))
trees = list(map(int, input().split(' ')))

left = 0
right = max(trees)

while left <= right:
    mid = (left + right) // 2

    if check(mid, trees, M):
        left = mid + 1
    else:
        right = mid - 1

print(left - 1)