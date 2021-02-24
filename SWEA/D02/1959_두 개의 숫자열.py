T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if N > M:
        a, b, N, M = b, a, M, N
    max_sum = -100000
    for i in range(M-N+1):
        sum_val = 0
        for j in range(N):
            sum_val += (a[j]*b[i+j])
        if sum_val > max_sum:
            max_sum = sum_val

    print(f'#{tc} {max_sum}')