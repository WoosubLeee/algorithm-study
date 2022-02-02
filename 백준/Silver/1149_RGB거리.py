N = int(input())
houses = [list(map(int, input().split())) for _ in range(N)]
costs = [0, 0, 0]

for n in range(N):
    temp = [
        houses[n][0] + min(costs[1], costs[2]),
        houses[n][1] + min(costs[0], costs[2]),
        houses[n][2] + min(costs[0], costs[1])
    ]
    costs = temp

print(min(costs))