def get_num(floor, room):
    if memo[floor][room-1]:
        return memo[floor][room-1]
    else:
        if floor == 0 or room == 1:
            memo[floor][room-1] = room
            return room
        else:
            memo[floor][room-1] = get_num(floor, room-1) + get_num(floor-1, room)
            return memo[floor][room-1]


memo = [[0]*14 for _ in range(15)]
T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    print(get_num(k, n))
