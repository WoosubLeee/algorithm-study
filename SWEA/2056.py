t = int(input())

for i in range(t):
    full_date = input()
    year = full_date[0:4]
    month = full_date[4:6]
    day = full_date[6:8]

    if (not 1 <= int(month) <= 12) or (not 1 <= int(day) <= 31):
        result = -1
    elif (int(month) in [4, 6, 9, 11]) and (int(day) > 30):
        result = -1
    elif (int(month) == 2) and (int(day) > 28):
        result = -1
    else:
        result = f'{year}/{month}/{day}'
    print(f'#{i+1} {result}')