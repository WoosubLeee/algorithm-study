T = int(input())

for t in range(T):
    n, m = map(int, input().split())
    num_list = list(map(int, input().split()))

    sum_list = []
    for i in range(n-m+1):
        sum_list += [sum(num_list[i:i+m])]
    max_num = m
    min_num = 10000*m
    for i in sum_list:
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i
    print(f'#{t+1} {max_num - min_num}')