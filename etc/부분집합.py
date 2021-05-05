def backtrack(n):
    global total
    if n == len(nums):
        if total == target:
            print(*included)
    else:
        included.append(nums[n])
        total += nums[n]
        if total <= target:
            backtrack(n + 1)
        included.remove(nums[n])
        total -= nums[n]
        backtrack(n + 1)


nums = list(map(int, input().split()))
target = 10
included, total = [], 0
backtrack(0)
