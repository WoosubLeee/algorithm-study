import sys


N, M = map(int, sys.stdin.readline().split(' '))
A = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]
M, K = map(int, sys.stdin.readline().split(' '))
B = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(M)]

result = []
for n in range(N):
    line = []
    for k in range(K):
        multiply = 0
        for m in range(M):
            multiply += A[n][m]*B[m][k]
        line.append(str(multiply))
    result.append(' '.join(line))
print(*result, sep='\n')