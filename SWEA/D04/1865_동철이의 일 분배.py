def backtrack(n, percent):
    global result
    if percent > result:
        if n == N:
            result = percent
        else:
            for i in range(N):
                if not included[i]:
                    included[i] = 1
                    backtrack(n+1, percent*(pros[n][i]/100))
                    included[i] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    pros = [list(map(int, input().split())) for _ in range(N)]
    result, included = 0, [0]*N
    backtrack(0, 100)
    print(f'#{tc} {result:.6f}')
