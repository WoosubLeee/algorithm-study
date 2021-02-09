for i in range(10):
    T = int(input())
    test_list = list(map(int, input().split()))

    result = 0
    for t in range(2, T-2):
        # 1
        # view = test_list[t] - max(test_list[t-2], test_list[t-1], test_list[t+1], test_list[t+2])

        # 2
        if test_list[t-2] > test_list[t-1]:
            max_near = test_list[t-2]
        else:
            max_near = test_list[t-1]
        if test_list[t+1] > max_near:
            max_near = test_list[t+1]
        if test_list[t+2] > max_near:
            max_near = test_list[t+2]
        view = test_list[t] - max_near

        if view > 0:
            result += view

    print(f'#{i+1} {result}')