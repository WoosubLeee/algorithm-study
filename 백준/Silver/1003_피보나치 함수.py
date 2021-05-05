for _ in range(int(input())):
    # memoization 사용
    memo = [[1, 0], [0, 1]]
    N = int(input())
    for i in range(2, N+1):
        memo.append([memo[i-1][0] + memo[i-2][0], memo[i-1][1] + memo[i-2][1]])
    print(*memo[N])
