N = int(input())
nums = []
for i in list(str(N)):
    nums.append(i)
for i in range(len(nums)):
    max_idx = i
    max_num = nums[i]
    for j in range(i+1, len(nums)):
        if nums[j] > max_num:
            max_idx = j
            max_num = nums[j]
    nums[i], nums[max_idx] = nums[max_idx], nums[i]
for i in nums:
    print(i, end='')
