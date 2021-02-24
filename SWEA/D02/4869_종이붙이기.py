def paste(n):
    if n >= 20:
        return paste(n - 10) + 2*paste(n - 20)
    else:
        return 1


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc} {paste(N)}')
