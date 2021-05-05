def calc(n):
    global count
    if n == N:
        count += 1
    else:
        for i in range(N):
            for pick in picked:
                if i == pick[1] or abs((n-pick[0]) / (i-pick[1])) == 1:
                    break
            else:
                picked.append([n, i])
                calc(n+1)
                picked.pop()


N = int(input())

picked = []
count = 0
calc(0)
print(count)
