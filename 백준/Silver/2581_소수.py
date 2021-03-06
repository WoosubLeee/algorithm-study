M, N = int(input()), int(input())

total = 0
min_num = 0
if M <= 2:
    total, min_num = 2, 2
    if M == 1:
        total = -1
for i in range(M, N+1):
    count = 0
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            break
    else:
        total += i
        if min_num <= 1:
            min_num = i
if total:
    print(f'{total}\n{min_num}')
else:
    print(-1)
