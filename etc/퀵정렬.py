def quick_sort(num_list):
    if len(num_list) <= 1:
        return num_list

    pivot = num_list[0]
    i, j = 1, len(num_list) - 1
    while i <= j:
        while i <= j and num_list[i] <= pivot:
            i += 1
        while i <= j and num_list[j] >= pivot:
            j -= 1
        if i <= j:
            num_list[i], num_list[j] = num_list[j], num_list[i]
    num_list[0], num_list[j] = num_list[j], num_list[0]
    return quick_sort(num_list[:j]) + [num_list[j]] + quick_sort(num_list[j+1:])


for tc in range(1, 4):
    nums = list(map(int, input().split()))
    print(f'#{tc} {quick_sort(nums)}')
