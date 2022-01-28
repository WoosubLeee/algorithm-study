def do(n, start):
    if n == M:
        print(*nums)
    else:
        for i in range(start, N+1):
            nums.append(i)
            do(n+1, i)
            nums.remove(i)


N, M = map(int, input().split())
nums = []
do(0, 1)
