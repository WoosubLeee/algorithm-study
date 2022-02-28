import sys


for _ in range(int(sys.stdin.readline())):
    N, M = map(int, sys.stdin.readline().split(' '))
    importances = list(map(int, sys.stdin.readline().split(' ')))

    front, rear = -1, N-1
    print_count = 0
    while True:
        front += 1
        if importances[front] != max(importances[front:]):
            importances.append(importances[front])
            rear += 1
            if front == M:
                M = rear
        else:
            print_count += 1
            if front == M:
                break
    print(print_count)