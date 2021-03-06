primes = [True]*10000
for i in range(2, 10000):
    if i ** 2 > 10000:
        break
    if primes[i]:
        j = 2
        while i * j < 10000:
            primes[i * j] = False
            j += 1

T = int(input())
for _ in range(T):
    n = int(input())
    for i in range(2, n//2 + 1):
        if primes[i] and primes[n-i]:
            result = i
    print(f'{result} {n - result}')
