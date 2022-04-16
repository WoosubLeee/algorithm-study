def solution(m, n, puddles):
    dp = [[0]*(m+1) for _ in range(n+1)]

    dp[0][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if [j, i] not in puddles:
                dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 1000000007
    return dp[n][m]


print(solution(4, 3, [[2, 2]]))
print(solution(7, 5, [[2, 3], [3, 6], [4, 3], [5, 4]]))