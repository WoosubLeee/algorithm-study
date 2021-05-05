def backtrack(n, cost):
    global result
    if cost < result:
        if n == N:
            result = cost
        else:
            for i in range(N):
                if not included[i]:
                    included[i] = 1
                    backtrack(n+1, cost + costs[n][i])
                    included[i] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]
    result, included = 1500, [0]*N
    backtrack(0, 0)
    print(f'#{tc} {result}')
