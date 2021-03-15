N = int(input())

for i in range(1, N):
    num = i
    total = i
    while num:
        total += num % 10
        num //= 10
    if total == N:
        print(i)
        break
else:
    print(0)
