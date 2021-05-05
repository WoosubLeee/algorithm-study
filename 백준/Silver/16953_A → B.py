A, B = map(int, input().split())
count = 1
while A < B:
    if B % 2 == 0:
        B //= 2
    else:
        if B % 10 == 1:
            B //= 10
        else:
            count = -1
            break
    count += 1
else:
    if A != B:
        count = -1
print(count)
