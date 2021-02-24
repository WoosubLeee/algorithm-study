# Programming - Intermediate
# 파이썬 SW문제해결 기본 - LIST1
# 숫자카드

T = int(input())

for t in range(T):
    N = int(input())
    num_list = [0] * 10
    # input을 분해하여 0~9까지 각각의 숫자의 개수를 셈
    for i in input():
        num_list[int(i)] += 1
    max_num = 0
    max_count = 0
    # 가장 많은 카드를 찾아내 max_num에 해당 숫자를, max_count에 해당 숫자 카드의 수를 저장
    for i in range(len(num_list)):
        if num_list[i] >= max_count:
            max_num = i
            max_count = num_list[i]
    print(f'#{t+1} {max_num} {max_count}')