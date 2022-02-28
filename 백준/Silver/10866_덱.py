import sys
from collections import deque


d = deque()
result = []
for _ in range(int(sys.stdin.readline())):
    line = sys.stdin.readline().strip()

    if line == 'pop_front':
        if len(d):
            result.append(d.popleft())
        else:
            result.append(-1)
    elif line == 'pop_back':
        if len(d):
            result.append(d.pop())
        else:
            result.append(-1)
    elif line == 'size':
        result.append(len(d))
    elif line == 'empty':
        result.append(0 if len(d) else 1)
    elif line == 'front':
        if len(d):
            result.append(d[0])
        else:
            result.append(-1)
    elif line == 'back':
        if len(d):
            result.append(d[-1])
        else:
            result.append(-1)
    else:
        order, num = line.split(' ')
        if order == 'push_back':
            d.append(int(num))
        else:
            d.appendleft(int(num))

print('\n'.join(map(str, result)))