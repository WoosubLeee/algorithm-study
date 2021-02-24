T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    max_count = 0
    for i in str1:
        count = 0
        for j in str2:
            if i == j:
                count += 1
        if count > max_count:
            max_count = count

    print(f'#{tc} {max_count}')
