N = int(input())
num = int(input())

result = 0
while num:
    result += num % 10
    num //= 10
print(result)
