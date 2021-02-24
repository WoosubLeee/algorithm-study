T = int(input())

for tc in range(1, T+1):
    N = int(input())

    nums = list(map(int, input().split()))
    for i in range(N):
        min_idx = i
        for j in range(i+1, N):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    print(f'#{tc}', end='')
    count = 0
    while count < 5:
        print(f' {nums[-count-1]} {nums[count]}', end='')
        count += 1
    else:
        print()