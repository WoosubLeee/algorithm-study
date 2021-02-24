T = int(input())

for tc in range(1, T+1):
    matrix = [input() for _ in range(5)]

    print(f'#{tc}', end=' ')
    for i in range(15):
        for j in range(5):
            try:
                print(matrix[j][i], end='')
            except:
                pass
    print()