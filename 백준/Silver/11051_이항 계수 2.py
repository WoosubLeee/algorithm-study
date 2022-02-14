N, K = map(int, input().split(' '))
result = 1
for i in range(K+1, N+1):
    result *= i
divide = 1
for i in range(1, N-K+1):
    divide *= i
print((result // divide) % 10007)