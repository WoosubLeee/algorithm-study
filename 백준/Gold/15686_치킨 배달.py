def calc_distance(home, shop):
    return abs(home[0] - shop[0]) + abs(home[1] - shop[1])


def close_shops(n, start):
    if n == 0:
        calc_min()
    else:
        for i in range(start, len(shops)):
            closed.append(i)
            close_shops(n-1, i+1)
            closed.remove(i)


def calc_min():
    global min_distance
    distance = 0
    for home in homes:
        for shop in home[1]:
            if shop[0] not in closed:
                distance += shop[1]
                break
    if distance < min_distance:
        min_distance = distance


N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
homes = []
shops = []
for i in range(N):
    for j in range(len(city[0])):
        if city[i][j] == 1:
            homes.append([[i, j]])
        elif city[i][j] == 2:
            shops.append([i, j])
for home in homes:
    distances = []
    for i in range(len(shops)):
        distances.append([i, calc_distance(home[0], shops[i])])
    distances.sort(key=lambda x: x[1])
    home.append(distances)

closed = []
min_distance = 1300
close_shops(len(shops) - M, 0)
print(min_distance)
