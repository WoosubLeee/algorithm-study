def merge_sort(num_list):
    global count
    if len(num_list) == 1:
        return num_list

    left = merge_sort(num_list[:len(num_list) // 2])
    right = merge_sort(num_list[len(num_list) // 2:])

    l, r, merged = 0, 0, []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1

    (temp, idx) = (left, l) if r == len(right) else (right, r)
    merged.extend(temp[idx:])
    if left[-1] > right[-1]:
        count += 1
    return merged


for tc in range(1, int(input())+1):
    N = int(input())
    nums = list(map(int, input().split()))
    count = 0
    merged = merge_sort(nums)
    print(f'#{tc} {merged[len(nums) // 2]} {count}')
