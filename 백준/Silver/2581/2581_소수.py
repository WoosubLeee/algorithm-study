M, N = int(input()), int(input())

total = 0
min_num = 0
excluded = [False]*(N+1)
for i in range(2, N + 1):
    if not excluded[i]:
        if i >= M:
            total += i
            if not min_num:
                min_num = i
        mul = 2*i
        while mul <= N:
            excluded[mul] = True
            mul += i
if total:
    print(f'{total}\n{min_num}')
else:
    print(-1)
