for _ in range(int(input())):
    K = int(input())
    N = int(input())

    floor = list(range(N+1))

    # 1
    # for k in range(1, K):
    #     floor.append([])
    #     for n in range(N):
    #         floor[k].append(sum(floor[k-1][:n+1]))
    # print(sum(floor[K-1]))

    # 2
    for k in range(K):
        for n in range(1, N+1):
            floor[n] += floor[n-1]
    print(floor[N])