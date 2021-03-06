# 에라토스테네스의 체
import sys


M, N = map(int, sys.stdin.readline().split())
primes = [True]*(N+1)
for i in range(2, N+1):
    if i ** 2 > N:
        break
    if primes[i]:
        j = 2
        while i*j <= N:
            primes[i*j] = False
            j += 1

for i in range(2, N+1):
    if primes[i] and i >= M:
        print(i)
