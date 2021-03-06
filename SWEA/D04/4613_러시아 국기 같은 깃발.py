def get_num(row, color):
    count = 0
    for i in flag[row]:
        if i != color:
            count += 1
    return count


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]

    result = N*M
    # 1
    w_cnt = [0]*N
    b_cnt = [0]*N
    r_cnt = [0]*N
    for i in range(N-2):
        w_cnt[i] = get_num(i, 'W')
    for i in range(1, N-1):
        b_cnt[i] = get_num(i, 'B')
    for i in range(2, N):
        r_cnt[i] = get_num(i, 'R')

    for i in range(1, N-1):
        for j in range(i, N-1):
            temp = 0
            for m in range(i):
                temp += w_cnt[m]
            for m in range(i, j+1):
                temp += b_cnt[m]
            for m in range(j+1, N):
                temp += r_cnt[m]
            if temp < result:
                result = temp
    print(f'#{tc} {result}')
