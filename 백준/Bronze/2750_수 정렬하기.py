N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))
for i in range(N):
    min_idx = i
    min_num = nums[i]
    for j in range(i+1, N):
        if nums[j] < min_num:
            min_idx = j
            min_num = nums[j]
    nums[i], nums[min_idx] = nums[min_idx], nums[i]
for i in nums:
    print(i)