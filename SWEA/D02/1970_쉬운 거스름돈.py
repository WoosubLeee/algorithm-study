moneys = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for tc in range(1, int(input())+1):
    change = int(input())
    result = [0]*8
    for i in range(8):
        while change >= moneys[i]:
            change -= moneys[i]
            result[i] += 1
    print(f'#{tc}')
    print(*result)
