N, K = map(int, input().split(' '))
coins = [int(input()) for _ in range(N)]

count = 0
idx = -1
while K:
    count += K // coins[idx]
    K %= coins[idx]
    idx -= 1
print(count)