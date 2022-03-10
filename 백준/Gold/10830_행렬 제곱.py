import sys


def dnq(n):
    if n not in memo:
        half = n // 2
        mat_a, mat_b = dnq(half), dnq(n - half)

        new_matrix = []
        for i in range(N):
            row = []
            for j in range(N):
                num = 0
                for k in range(N):
                    num += mat_a[i][k]*mat_b[k][j]
                row.append(num % 1000)
            new_matrix.append(row)
        memo[n] = new_matrix

    return memo[n]


N, B = map(int, sys.stdin.readline().split(' '))
matrix = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]

for i in range(N):
    for j in range(N):
        matrix[i][j] = matrix[i][j] % 1000

memo = {
    1: matrix
}

result = []
for row in dnq(B):
    result.append(' '.join(map(str, row)))
print('\n'.join(result))