for _ in range(10):
    tc = int(input())
    nums = list(map(int, input().split()))
    minus = 0
    while True:
        first = nums.pop(0)
        if minus < 5:
            minus += 1
        else:
            minus = 1
        first -= minus
        nums.append(first)
        if first <= 0:
            nums[-1] = 0
            break
    print(f'#{tc} {" ".join(map(str, nums))}')
