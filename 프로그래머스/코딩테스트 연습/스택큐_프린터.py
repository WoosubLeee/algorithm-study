from collections import deque


def solution(priorities, location):
    priorities_dict = {}
    for i, priority in enumerate(priorities):
        if priority not in priorities_dict:
            priorities_dict[priority] = []
        priorities_dict[priority].append(i)

    priority_values = sorted(priorities_dict.keys(), reverse=True)
    queue = deque(range(len(priorities)))
    count = 0
    while True:
        left = queue.popleft()
        if left in priorities_dict[priority_values[0]]:
            count += 1
            if left == location:
                return count

            priorities_dict[priority_values[0]].remove(left)
            if not priorities_dict[priority_values[0]]:
                priority_values.pop(0)
        else:
            queue.append(left)


priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))