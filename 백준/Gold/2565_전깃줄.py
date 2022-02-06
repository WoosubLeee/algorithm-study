N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]

lines.sort()

counts = [0]
for i in range(1, N):
    if lines[i][1] > lines[counts[-1]][1]:
        counts.append(i)
    else:
        l, r = 0, len(counts) - 1
        while l <= r:
            m = (l + r) // 2
            if lines[counts[m]][1] > lines[i][1]:
                r = m - 1
            else:
                l = m + 1
        counts[l] = i
print(N - len(counts))