import sys


for _ in range(int(sys.stdin.readline())):
    K = int(sys.stdin.readline())
    sizes = list(map(int, sys.stdin.readline().split(' ')))

    costs = [[0]*K for _ in range(K)]

    for j in range(1, K):
        for i in range(j-1, -1, -1):
            min_cost = sys.maxsize
            for k in range(1, j-i+1):
                min_cost = min(costs[i][i+k-1] + costs[i+k][j], min_cost)
            costs[i][j] = min_cost + sum(sizes[i:j+1])
    print(costs[0][K-1])