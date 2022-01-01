X = int(input())
count = 0
for i in range(1, X+1):
    count += i
    if X <= count:
        if i % 2:
            print(f'{count-X+1}/{i-count+X}')
        else:
            print(f'{i-count+X}/{count-X+1}')
        break
