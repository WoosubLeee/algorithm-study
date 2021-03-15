def is_end(num):
    count = 0
    while num:
        if num % 10 == 6:
            count += 1
            if count == 3:
                return True
        else:
            count = 0
        num //= 10


N = int(input())
num = 665
while True:
    num += 1
    if is_end(num):
        N -= 1
        if N == 0:
            break
print(num)
