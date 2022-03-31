N, M = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))

total_cost = sum(costs)
dp = [0]

for i in range(N):
    prev_dp = dp
    dp = []

    for j in range(len(prev_dp) + costs[i]):
        if j < costs[i]:
            if j < len(prev_dp):
                dp.append(prev_dp[j])
            else:
                dp.append(dp[-1])
        else:
            if j < len(prev_dp):
                dp.append(max(prev_dp[j], prev_dp[j-costs[i]] + memories[i]))
            else:
                dp.append(prev_dp[j-costs[i]] + memories[i])
        if dp[j] >= M:
            break
print(len(dp) - 1)