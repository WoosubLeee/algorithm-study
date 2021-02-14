width, height = map(int, input().split())
N = int(input())
positions = []
for i in range(N+1):
    a, b = list(map(int, input().split()))
    if a == 1:
        positions.append([b, 0])
    elif a == 2:
        positions.append([b, height])
    elif a == 3:
        positions.append([0, b])
    else:
        positions.append([width, b])

total = 0
for i in positions[:-1]:
    x = i[0] - positions[-1][0]
    y = i[1] - positions[-1][1]
    if (x ** 2) ** 0.5 == width:
        y = i[1] + positions[-1][1]
        if y > height:
            y = height*2 - y
    elif (y ** 2) ** 0.5 == height:
        x = i[0] + positions[-1][0]
        if x > width:
            x = width*2 - x
    total += (y ** 2) ** 0.5 + (x ** 2) ** 0.5
print(int(total))