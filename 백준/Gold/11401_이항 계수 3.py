def dnq(n):
    if n in divs.keys():
        return divs[n]
    half = n // 2
    divs[n] = (dnq(half)*dnq(n - half)) % 1000000007
    return divs[n]


N, K = map(int, input().split(' '))

if K >= N // 2:
    K = N - K
result = 1
for n in range(K + 1, N + 1):
    result *= n
    result %= 1000000007

divide = 1
for k in range(2, N - K + 1):
    divide *= k
    divide %= 1000000007

divs = {1: divide}
divide = dnq(1000000007 - 2)
print((result*divide) % 1000000007)
