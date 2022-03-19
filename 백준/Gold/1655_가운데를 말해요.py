import sys
import heapq


N = int(sys.stdin.readline())
max_heap = []
min_heap = []
middle = []

result = []
for _ in range(N):
    x = int(sys.stdin.readline())

    if not middle:
        if max_heap and x < -max_heap[0]:
            middle.append(-heapq.heappushpop(max_heap, -x))
        elif min_heap and x > min_heap[0]:
            middle.append(heapq.heappushpop(min_heap, x))
        else:
            middle.append(x)
        result.append(middle[0])
    else:
        middle.append(x)
        heapq.heappush(max_heap, -min(middle))
        heapq.heappush(min_heap, max(middle))
        result.append(-max_heap[0])
        middle = []

print(*result, sep='\n')