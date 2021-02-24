# Programming - Intermediate
# 파이썬 SW문제해결 기본 - LIST1
# 구간합

T = int(input())

for t in range(T):
    n, m = map(int, input().split())
    num_list = list(map(int, input().split()))

    # 1
    tmp = 0
    for i in range(m):
        tmp += num_list[i]

    max_num = tmp
    min_num = tmp

    for i in range(m, n):
        tmp = tmp + num_list[i] - num_list[i - m]
        if tmp > max_num:
            max_num = tmp
        if tmp < min_num:
            min_num = tmp

    # 2
    # max_num = m
    # min_num = 10000*m
    # for i in range(n-m+1):
    #     sum_m = sum(num_list[i:i+m])
    #     if sum_m > max_num:
    #         max_num = sum_m
    #     if sum_m < min_num:
    #         min_num = sum_m
    # print(f'#{t+1} {max_num - min_num}')