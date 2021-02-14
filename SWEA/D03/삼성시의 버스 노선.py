T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 1
    stop_list = [0] * 5001
    for i in range(N):
        a, b = map(int, input().split())
        for j in range(a, b+1):
            stop_list[j] += 1
    P = int(input())
    print(f'#{tc}', end='')
    for i in range(P):
        print(f' {stop_list[int(input())]}', end='')
    print()

    # 2
    # bus_list = [[0, 0]] * N
    # for i in range(N):
    #     bus_list[i] = list(map(int, input().split()))
    #
    # P = int(input())
    # print(f'#{tc}', end=' ')
    # for i in range(P):
    #     c = int(input())
    #     count = 0
    #     for bus_stop in bus_list:
    #         if bus_stop[0] <= c <= bus_stop[1]:
    #             count += 1
    #     print(count, end=' ')
    # print('')