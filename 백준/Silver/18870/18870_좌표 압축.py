def binary_search(n):
    s, e = 0, len(new_nums)-1
    while s <= e:
        m = (s + e) // 2
        if new_nums[m] == n:
            return m
        elif new_nums[m] > n:
            e = m - 1
        elif new_nums[m] < n:
            s = m + 1


N = int(input())
nums = list(map(int, input().split()))

new_nums = sorted(list(set(nums)))
for num in nums:
    print(binary_search(num), end=' ')
