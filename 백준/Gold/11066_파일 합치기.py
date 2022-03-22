import sys


for _ in range(int(sys.stdin.readline())):
    K = int(sys.stdin.readline())
    sizes = list(map(int, sys.stdin.readline().split(' ')))

    memos = [[0]*K for _ in range(K)]
    for i in range(1, K):
        for j in range(i-1, -1, -1):
            memos[j][i] = min(memos[j][j+k] + memos[j+k+1][i] for k in range(i-j)) + sum(sizes[j:i+1])
    print(memos[0][K-1])