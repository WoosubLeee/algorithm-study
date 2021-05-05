def dfs(from_z):
    global total, result, count
    if count < N:
        for i in range(2, N+1):
            if left[i] == 0:
                left[i] = 1
                total += arr[from_z-1][i-1]
                count += 1
                if total < result:
                    dfs(i)
                left[i] = 0
                total -= arr[from_z-1][i-1]
                count -= 1
    else:
        total += arr[from_z-1][0]
        if total < result:
            result = total
        total -= arr[from_z-1][0]


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total, result = 0, 1000000
    left, count = [0]*(N+1), 1
    dfs(1)
    print(f'#{tc} {result}')
