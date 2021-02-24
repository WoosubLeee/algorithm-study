t = int(input())

for i in range(t):
    num_list = list(map(int, input().split()))
    max_num = num_list[0]
    for num in num_list:
        if num > max_num:
            max_num = num
    print(f'#{i + 1} {max_num}')