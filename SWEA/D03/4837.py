T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    count = 0
    for i in range(1<<12):
        n_count = 0
        total = 0
        for j in range(12):
            if i & (1<<j):
                n_count += 1
                total += j+1
        if n_count == N and total == K:
            count += 1
    print(f'#{tc} {count}')
