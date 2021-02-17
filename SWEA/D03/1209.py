for _ in range(10):
    tc = int(input())
    max_num = 0
    arr = []
    for i in range(100):
        row = list(map(int, input().split()))
        total = 0
        for i in row:
            total += i
        if total > max_num:
            max_num = total
        arr.append(row)

    for i in range(100):
        total = 0
        for j in range(100):
            total += arr[j][i]
        if total > max_num:
            max_num = total

    for i in range(2):
        total = 0
        for j in range(100):
            if i:
                total += arr[j][j]
            else:
                total += arr[j][99-j]
        if total > max_num:
            max_num = total
    print(f'#{tc} {max_num}')