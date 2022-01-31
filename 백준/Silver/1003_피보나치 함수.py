def memoize(i):
    if memo[i-1] == [0, 0]:
        memoize(i-1)
    if memo[i-2] == [0, 0]:
        memoize(i-2)


T = int(input())
memo = [[1, 0], [0, 1]]
for _ in range(T):
    N = int(input())
    while len(memo) < N+1:
        memo.append([memo[-1][0]+memo[-2][0], memo[-1][1]+memo[-2][1]])
    print(' '.join(map(str, memo[N])))