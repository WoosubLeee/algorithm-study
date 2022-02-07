n = int(input())
nums = list(map(int, input().split(' ' )))

for i in range(1, n):
    if nums[i-1] > 0:
        nums[i] += nums[i-1]
print(max(nums))