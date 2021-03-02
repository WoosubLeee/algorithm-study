T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    count = 0
    per_year = 0
    left = y - x
    while True:
        if left > 2 * (per_year+1):
            per_year += 1
            count += 2
            left -= 2*per_year
        elif left > per_year+1:
            count += 2
            break
        else:
            count += 1
            break
    print(count)
