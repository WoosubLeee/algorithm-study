a, b = map(int, input().split(' '))

gcd = 1

isPrime = [True]*10001
prime = 1
while prime <= min(a, b):
    prime += 1
    if isPrime[prime]:
        while a % prime == 0 and b % prime == 0:
            gcd *= prime
            a //= prime
            b //= prime

        multi = 2
        while prime*multi <= 10000:
            isPrime[prime*multi] = False
            multi += 1

print(gcd, gcd*a*b, sep='\n')