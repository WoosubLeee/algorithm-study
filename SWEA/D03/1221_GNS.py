T = int(input())

for _ in range(T):
    tc, N = input().split()

    num_list = list(input().split())
    count_list = [0]*10
    num_str = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    for i in num_list:
        count_list[num_str.index(i)] += 1
    print(tc)
    for i in range(10):
        print(f'{num_str[i]} '*count_list[i], end='')
    print()