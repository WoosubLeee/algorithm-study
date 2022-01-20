N = int(input())
nums = [int(input()) for _ in range(N)]

# Bubble sort

# for i in range(N):
#     for j in range(i+1, N):
#         if nums[i] > nums[j]:
#             nums[i], nums[j] = nums[j], nums[i]

# Selection sort

for i in range(N):
    min_idx = i
    for j in range(i+1, N):
        if nums[j] < nums[min_idx]:
            min_idx = j
    nums[i], nums[min_idx] = nums[min_idx], nums[i]

for i in range(N):
    print(nums[i])
