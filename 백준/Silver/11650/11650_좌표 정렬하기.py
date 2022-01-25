N = int(input())

n_loc = [[] for _ in range(100000)]
p_loc = [[] for _ in range(100001)]
for _ in range(N):
    loc = list(map(int, input().split()))
    if loc[0] < 0:
        n_loc[loc[0]].append(loc[1])
    else:
        p_loc[loc[0]].append(loc[1])
for i in range(-100000, 100001):
    if i < 0:
        for j in sorted(n_loc[i]):
            print(i, j)
    else:
        for j in sorted(p_loc[i]):
            print(i, j)
