import sys

n = int(sys.stdin.readline())

count = 0
num = n
while True:
    count += 1
    a = num // 10
    b = num % 10

    num = b*10 + ((a+b) % 10)
    if num == n:
        break

print(count)
