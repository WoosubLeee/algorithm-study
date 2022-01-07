from math import sqrt


n = int(input())
ns = []
while n:
    ns.append(n)
    n = int(input())

max_n = max(ns)
isPrime = [1 for _ in range(2*max_n+1)]
isPrime[1] = 0

x = 2
while x <= sqrt(2*max_n):
    if isPrime[x]:
        y = 2
        while x*y <= 2*max_n:
            isPrime[x*y] = 0
            y += 1
    x += 1

for num in ns:
    print(isPrime[num+1:2*num+1].count(1))