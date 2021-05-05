def backtrack(n):
    global count
    if n == N:
        count += 1
    else:
        for j in range(N):
            if check(n, j):
                on_board.append([n, j])
                backtrack(n+1)
                on_board.remove([n, j])


def check(r, c):
    for queen in on_board:
        if queen[1] == c or abs((queen[0]-r) / (queen[1]-c)) == 1:
            return False
    return True


for tc in range(1, int(input())+1):
    N = int(input())
    on_board = []
    count = 0
    backtrack(0)
    print(f'#{tc} {count}')
