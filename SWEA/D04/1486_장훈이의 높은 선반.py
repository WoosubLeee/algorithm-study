def backtrack(n):
    global total, result
    if total < result:
        result = total
    if n < N:
        backtrack(n+1)
        total -= heights[n]
        if total >= B:
            backtrack(n+1)
        total += heights[n]


for tc in range(1, int(input())+1):
    N, B = map(int,input().split())
    heights = list(map(int, input().split()))

    total = sum(heights)
    result = total
    backtrack(0)
    print(f'#{tc} {result-B}')
