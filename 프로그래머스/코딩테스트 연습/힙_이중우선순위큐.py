import heapq


def solution(operations):
    min_heap = []
    max_heap = []
    for op in operations:
        if op[0] == 'I':
            num = int(op[2:])
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        else:
            if not min_heap:
                continue

            if op[2] == '-':
                popped = heapq.heappop(min_heap)
                max_heap.remove(-popped)
            else:
                popped = -heapq.heappop(max_heap)
                min_heap.remove(popped)

    if min_heap:
        return [-max_heap[0], min_heap[0]]
    else:
        return [0, 0]


print(solution(["I 16","D 1"]))
print(solution(["I 7","I 5","I -5","D -1"]))
print(solution(["I 2","I 4","D -1", "I 1", "D 1"]))