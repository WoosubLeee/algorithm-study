def my_sort(num_list):
    for i in range(len(num_list) - 1):
        min_idx, min_num = i, num_list[i]
        for j in range(i + 1, len(num_list)):
            if num_list[j] < min_num:
                min_idx, min_num = j, num_list[j]
        num_list[i], num_list[min_idx] = num_list[min_idx], num_list[i]


for tc in range(1, int(input())+1):
    nums_temp, switch = input().split()
    nums = []
    for num in nums_temp:
        nums.append(int(num))
    switch = int(switch)
    candidates = []
    for num in nums:
        if num < max(nums):
            candidates.append(num)
            if len(candidates) == switch:
                break
    for _ in range(switch - len(candidates)):
        candidates.append(max(nums))
    if switch <= nums.count(max(nums)):
        my_sort(candidates)

    for can in candidates:
        can_idx = nums.index(can)
        max_idx, max_num = can_idx, can
        for j in range(max_idx+1, len(nums)):
            if nums[j] >= max_num:
                max_idx, max_num = j, nums[j]
        if max_idx == can_idx:
            if nums.count(max(nums)) < 2:
                nums[len(nums)-2], nums[len(nums)-1] = nums[len(nums)-1], nums[len(nums)-2]
        else:
            nums[can_idx], nums[max_idx] = nums[max_idx], nums[can_idx]
    result = ''.join(map(str, nums))
    print(f'#{tc} {result}')
