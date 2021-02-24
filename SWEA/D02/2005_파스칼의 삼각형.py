def pascal(n, x):
    if not 1 < x < n:
        return 1
    return pascal(n-1, x-1) + pascal(n-1, x)


T = int(input())

for tc in range(1, T+1):
    print(f'#{tc}')
    N = int(input())
    for n in range(1, N+1):
        for m in range(1, n+1):
            print(pascal(n, m), end=' ')
        print()
