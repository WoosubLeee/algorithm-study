N = int(input())
nums = list(map(int, input().split(' ')))


# 1 O(n log n)
counts = [0]
for i in range(1, N):
    if nums[i] > nums[counts[-1]]:
        counts.append(i)
    else:
        l = 0
        r = len(counts) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[counts[m]] == nums[i]:
                break
            elif nums[counts[m]] > nums[i]:
                r = m - 1
            else:
                l = m + 1
        else:
            counts[l] = i
            # 이 부분에서
            # if nums[i] < nums[counts[l]]:
            #     counts[l] = i
            # 처럼 대소를 비교해야한다고 생각했으나
            # 이진 탐색 시 탐색이 멈추는 자리(l == r인 자리)는
            # nums[counts[l-1]]이 nums[i]보다 작고,
            # nums[counts[l]]이 nums[i]보다 큰 자리이기 때문에
            # 대소를 비교할 필요가 없다
print(len(counts))


# # 2 O(n^2)
# counts = [1]
# for i in range(1, N):
#     max_count = 0
#     for j in range(i):
#         if nums[j] < nums[i] and counts[j] > max_count:
#             max_count = counts[j]
#     counts.append(max_count + 1)
# print(max(counts))