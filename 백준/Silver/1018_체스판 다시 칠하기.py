N, M = map(int, input().split())
board = [input() for _ in range(N)]

min_count = 64
for n in range(N-7):
    for m in range(M-7):
        for start in ['B', 'W']:
            count = 0
            left = 'B' if start == 'W' else 'W'

            for i in range(8):
                for j in range(8):
                    should_be = left if (i+j) % 2 else start
                    if board[n+i][m+j] != should_be:
                        count += 1
                        if count >= min_count:
                            break

                if count >= min_count:
                    break

            if count < min_count:
                min_count = count

print(min_count)