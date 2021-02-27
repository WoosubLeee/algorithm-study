N = int(input())

count = -6
if N == 1:
    print(1)
else:
    count = 1
    for i in range(N):
        count += i*6
        if N <= count:
            print(i+1)
            break
