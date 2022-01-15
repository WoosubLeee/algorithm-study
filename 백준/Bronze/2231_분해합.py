def get_sum(n):
    result = n
    while n:
        result += n % 10
        n //= 10
    return result


N = int(input())
n = N
min_num = N
while n >= 10:
    min_num -= 9
    n //= 10
else:
    min_num -= n

for i in range(min_num, N):
    if get_sum(i) == N:
        print(i)
        break
else:
    print(0)