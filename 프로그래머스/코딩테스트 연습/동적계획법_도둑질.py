def solution(money):
    dp_zero = [money[0], money[1]]
    dp_first = [0, money[1]]

    for i in range(2, len(money)-1):
        for dp in [dp_zero, dp_first]:
            max_sum = dp[i-2] + money[i]
            if i >= 3:
                max_sum = max(max_sum, dp[i-3] + money[i])
            dp.append(max_sum)
    else:
        dp_first.append(money[i+1] + max(dp_first[i-2:i]))

    return max(max(dp_zero[-2:]), max(dp_first[-2:]))


print(solution([1, 2, 3, 1]))