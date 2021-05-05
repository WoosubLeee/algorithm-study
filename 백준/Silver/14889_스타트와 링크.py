def make_team(n):
    global result
    if len(start) == N // 2:
        gap = compare_stat()
        if gap < result:
            result = gap
    else:
        for i in range(n, N // 2 + len(start) + 1):
            start.append(i)
            link.remove(i)
            make_team(i+1)
            start.remove(i)
            link.append(i)


def compare_stat():
    start_stat, link_stat = 0, 0
    for i in start:
        for j in start:
            start_stat += stats[i][j]
    for i in link:
        for j in link:
            link_stat += stats[i][j]
    return abs(start_stat - link_stat)


N = int(input())
stats = [list(map(int, input().split())) for _ in range(N)]

start, link = [], list(range(N))
result = 10000
make_team(0)
print(result)
