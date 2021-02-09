t = int(input())

for i in range(t):
    p, k = map(int, input().split())
    print(f'#{i + 1} {p // k} {p % k}')