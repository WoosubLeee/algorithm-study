T = int(input())

for tc in range(1, T+1):
    line = input()

    total = 0
    stick_count = 0
    for i in range(len(line)):
        if line[i] == '(':
            stick_count += 1
            total += 1
        elif line[i-1] == '(':
            stick_count -= 1
            total -= 1
            total += stick_count
        else:
            stick_count -= 1

    print(f'#{tc} {total}')
