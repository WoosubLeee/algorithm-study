T = int(input())

for t in range(T):
    N = int(input())

    num_list = list(map(int, input().split()))
    max_num = 5
    min_num = 1000000
    for num in num_list:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    print(f'#{t+1} {max_num - min_num}')