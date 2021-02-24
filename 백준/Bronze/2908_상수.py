a, b = list(map(int, input().split()))
new_a = 0
while a:
    new_a = new_a*10 + a % 10
    a //= 10
new_b = 0
while b:
    new_b = new_b*10 + b % 10
    b //= 10

if new_a > new_b:
    print(new_a)
else:
    print(new_b)
