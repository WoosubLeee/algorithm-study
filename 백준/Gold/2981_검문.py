def calc_gcd(a, b):
    while True:
        a, b = b, a % b
        if b == 0:
            return a


N = int(input())
inputs = [int(input()) for _ in range(N)]

diffs = [abs(inputs[i]-inputs[i+1]) for i in range(N-1)]
gcd = diffs[0]
for i in range(1, N-1):
    gcd = calc_gcd(gcd, diffs[i])

result = set()
for i in range(2, int(gcd ** 0.5)+1):
    if gcd % i == 0:
        result.add(i)
        result.add(gcd // i)
result.add(gcd)

print(' '.join(map(str, sorted(list(result)))))