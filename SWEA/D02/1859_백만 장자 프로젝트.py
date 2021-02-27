T = int(input())

for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))
    total = 0
    costly = 0
    for i in range(N-1, -1, -1):
        if prices[i] > costly:
            costly = prices[i]
        else:
            total += (costly - prices[i])
    print(f'#{tc} {total}')
