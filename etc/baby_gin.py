num =456789
c = [0] * 12

for i in str(num):
    c[int(i)] += 1

result = 0
while True:
    for i in range(len(c)-2):
        if c[i] and c[i+1] and c[i+2]:
            result += 1
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            break
    else:
        break

for i in c:
    if i >= 3:
        result += 1

if result == 2:
    print('Baby-Gin')