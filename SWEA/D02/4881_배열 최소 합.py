def search(row, total):
    global min_sum
    for i in range(N):
        if columns[i] == 0:
            columns[i] = 1
            total += matrix[row][i]

            if row == N-1:
                if total < min_sum:
                    min_sum = total
            elif total < min_sum:
                search(row+1, total)

            total -= matrix[row][i]
            columns[i] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    columns = [0]*N
    min_sum = 90
    search(0, 0)
    print(f'#{tc} {min_sum}')
