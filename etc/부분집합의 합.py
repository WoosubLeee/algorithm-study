data = [-7, -3, -2, 5, 8]

n = len(data)

count = 0
for i in range(1 << n):
    part = []
    for j in range(n+1):
        if i & (1<<j):
            part.append(data[j])
    total = 0
    for j in part:
        total += j
    if total == 0:
        count += 1
print(count)
