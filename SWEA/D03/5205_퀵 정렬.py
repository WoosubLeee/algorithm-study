def quick_sort(l, r):
    if r > l:
        pivot = nums[l]
        i, j = l + 1, r
        while i <= j:
            while i <= j and nums[i] <= pivot:
                i += 1
            while i <= j and nums[j] >= pivot:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        nums[l], nums[j] = nums[j], nums[l]
        quick_sort(l, j - 1)
        quick_sort(j + 1, r)


def lomuto_quick_sort(p, r):
    if r > p:
        pivot = nums[r]
        i = p - 1
        for j in range(p, r):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[r], nums[i + 1] = nums[i + 1], nums[r]
        lomuto_quick_sort(p, i)
        lomuto_quick_sort(i + 2, r)


for tc in range(1, int(input())+1):
    N = int(input())
    nums = list(map(int, input().split()))
    lomuto_quick_sort(0, N - 1)
    print(f'#{tc} {nums[len(nums) // 2]}')
