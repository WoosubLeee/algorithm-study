T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())

    if N % H:
        floor = N % H
        width = (N // H) + 1
    else:
        floor = H
        width = N // H
    print(f'{floor}{width:02}')
