def dfs(r, c):
    global total, result
    if r == N - 1 and c == N -1:
        result = total
    else:
        for d in drc:
            new_r, new_c = r + d[0], c + d[1]
            if new_r < N and new_c < N:
                total += board[new_r][new_c]
                if total < result:
                    dfs(new_r, new_c)
                total -= board[new_r][new_c]


for tc in range(1, int(input())+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    drc = [[1, 0], [0, 1]]
    total, result = board[0][0], 1000000
    dfs(0, 0)
    print(f'#{tc} {result}')
