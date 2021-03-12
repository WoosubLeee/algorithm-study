xs = []
ys = []
for i in range(3):
    a, b = map(int, input().split())
    if a in xs:
        xs.remove(a)
    else:
        xs.append(a)
    if b in ys:
        ys.remove(b)
    else:
        ys.append(b)
print(*xs, *ys)
