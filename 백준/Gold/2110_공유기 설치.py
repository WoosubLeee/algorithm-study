import sys


def get_closest_distance(distance, houses, routers):
    closest = houses[-1]

    prev_router = houses[0]
    routers -= 1
    for house in houses[1:]:
        between = house - prev_router
        if between >= distance:
            prev_router = house
            routers -= 1
            closest = min(closest, between)

            if routers == 0:
                return closest
    return 0


N, C = map(int, sys.stdin.readline().split(' '))
houses = [int(sys.stdin.readline()) for _ in range(N)]
houses.sort()

short = 1
long = (houses[-1] - houses[0]) // (C-1) + 1

result = 0

while short <= long:
    mid = (short + long) // 2

    closest = get_closest_distance(mid, houses, C)
    if closest:
        result = closest
        short = mid + 1
    else:
        long = mid - 1

print(result)