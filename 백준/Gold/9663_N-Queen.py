def calc(i):
    if i == N:
        global result
        result += 1
    else:
        for j in range(N):
            if not ys[j]:
                for queen in stack:
                    if abs((i - queen[0]) / (j - queen[1])) == 1:
                        break
                else:
                    ys[j] = 1
                    stack.append([i, j])
                    calc(i+1)
                    stack.pop()
                    ys[j] = 0


N = int(input())
ys = [0]*N
stack = []
result = 0
calc(0)
print(result)