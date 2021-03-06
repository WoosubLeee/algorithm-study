num = int(input())
while num:
    primes = [True]*(2*num+1)
    for i in range(2, 2*num+1):
        if i ** 2 > 2*num:
            break
        if primes[i]:
            j = 2
            while j*i <= 2*num:
                primes[i*j] = False
                j += 1
    total = 0
    for i in range(num+1, 2*num+1):
        if primes[i] and i > num:
            total += 1
    print(total)
    num = int(input())
