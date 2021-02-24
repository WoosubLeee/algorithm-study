'''
3
9
7 4 2 0 0 6 0 7 0
9
7 4 2 0 0 6 7 7 0
20
52 56 38 77 43 31 11 87 68 64 88 76 56 59 46 57 75 85 65 53
'''

T = int(input())

# 1
for t in range(1, T+1):
    N = int(input())
    boxTop = list(map(int, input().split()))
    room = [[0 for _ in range(100)] for _ in range(N)]
    for i in range(N):
        for j in range(boxTop[i]):
            room[i][j] = 1
    max_fall = 0
    for i in range(N):
        if boxTop[i] > 0:
            dist = 0
            for j in range(i+1, N):
                if room[j][boxTop[i]-1] == 0:
                    dist += 1
            if dist > max_fall:
                max_fall = dist
    print(f'#{t+1} {max_fall}')

# 2
for t in range(T):
    width = int(input())
    num_list = list(map(int, input().split()))

    max_fall = 0
    for i in range(width):
        below = 0
        for j in range(i+1, width):
            if num_list[j] >= num_list[i]:
                below += 1

        i_fall = (width-i) - below - 1
        if i_fall > max_fall:
            max_fall = i_fall
    print(f'#{t+1} {max_fall}')