# 1
from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    queue = deque([0]*bridge_length)

    time = 0
    total_weight = 0
    while queue:
        time += 1
        total_weight -= queue.popleft()

        if truck_weights:
            if total_weight + truck_weights[0] <= weight:
                queue.append(truck_weights.popleft())
            else:
                queue.append(0)

    return time


# # 2 원래 풀이
# from collections import deque
#
#
# def solution(bridge_length, weight, truck_weights):
#     queue = deque([0]*bridge_length)
#     next_truck = 0
#     time = 0
#     total_weight = 0
#     total_arrived = 0
#     while next_truck < len(truck_weights) or total_arrived < len(truck_weights):
#         time += 1
#         arrived = queue.popleft()
#         if arrived:
#             total_weight -= arrived
#             total_arrived += 1
#
#         if next_truck < len(truck_weights) and total_weight + truck_weights[next_truck] <= weight:
#             queue.append(truck_weights[next_truck])
#             total_weight += truck_weights[next_truck]
#             next_truck += 1
#         else:
#             queue.append(0)
#
#     return time


bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]
print(solution(bridge_length, weight, truck_weights))