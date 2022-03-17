import sys


# 1
def push(heap, end, num):
    end += 1
    heap[end] = num

    position = end
    while position > 1 and heap[position] < heap[position // 2]:
        heap[position], heap[position // 2] = heap[position // 2], heap[position]
        position //= 2


def pop(heap, end):
    top = heap[1]
    heap[1], heap[end] = heap[end], 0
    end -= 1

    position = 1
    while True:
        smaller = position
        if 2*position <= end and heap[smaller] > heap[2*position]:
            smaller = 2*position
        if 2*position + 1 <= end and heap[smaller] > heap[2*position + 1]:
            smaller = 2*position + 1

        if position != smaller:
            heap[position], heap[smaller] = heap[smaller], heap[position]
            position = smaller
        else:
            break

    return top


N = int(sys.stdin.readline())
heap = [0]*(N+1)
end = 0
result = []
for _ in range(N):
    x = int(sys.stdin.readline())

    if x:
        push(heap, end, x)
        end += 1
    else:
        if end:
            result.append(str(pop(heap, end)))
            end -= 1
        else:
            result.append(str(0))

print('\n'.join(result))


# # 2
# import heapq
#
#
# N = int(sys.stdin.readline())
# heap = []
# result = []
# for _ in range(N):
#     x = int(sys.stdin.readline())
#
#     if x:
#         heapq.heappush(heap, x)
#     else:
#         try:
#             result.append(str(heapq.heappop(heap)))
#         except:
#             result.append(str(0))
#
# print('\n'.join(result))
