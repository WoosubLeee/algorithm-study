def pick(n, start):
    global total, result
    for i in range(start, N):
        total += nums[i]
        if total <= M:
            if n == 3:
                if total > result:
                    result = total
            else:
                pick(n + 1, i + 1)
        total -= nums[i]


N, M = map(int, input().split())
nums = list(map(int, input().split()))

total = 0
result = 0
pick(1, 0)

print(result)
