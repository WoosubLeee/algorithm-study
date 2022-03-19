

# # 1
# import sys
#
#
# def is_a_smaller_than_b(a, b):
#     return abs(a) < abs(b) or (abs(a) == abs(b) and a < b)
#
#
# def heap_push(num, heap, end):
#     end += 1
#     heap[end] = num
#
#     position = end
#     while position > 1 and is_a_smaller_than_b(heap[position], heap[position // 2]):
#         heap[position], heap[position // 2] = heap[position // 2], heap[position]
#         position //= 2
#
#
# def heap_pop(heap, end):
#     top = heap[1]
#     heap[1], heap[end] = heap[end], 0
#     end -= 1
#
#     position = 1
#     while True:
#         smaller = position
#         if 2*position <= end and is_a_smaller_than_b(heap[2*position], heap[smaller]):
#             smaller = 2*position
#         if 2*position + 1 <= end and is_a_smaller_than_b(heap[2*position + 1], heap[smaller]):
#             smaller = 2*position + 1
#
#         if smaller == position:
#             return top
#         heap[position], heap[smaller] = heap[smaller], heap[position]
#         position = smaller
#
#
# N = int(sys.stdin.readline())
# heap = [0]*(N+1)
# end = 0
# result = []
# for _ in range(N):
#     x = int(sys.stdin.readline())
#
#     if x:
#         heap_push(x, heap, end)
#         end += 1
#     else:
#         if end:
#             result.append(heap_pop(heap, end))
#             end -= 1
#         else:
#             result.append(0)
#
# print(*result, sep='\n')


# 2
import sys
import heapq


N = int(sys.stdin.readline())
positive_heap = []
negative_heap = []
result = []
for _ in range(N):
    x = int(sys.stdin.readline())

    if x:
        if x > 0:
            heapq.heappush(positive_heap, x)
        else:
            heapq.heappush(negative_heap, -x)
    else:
        if not positive_heap and not negative_heap:
            result.append(0)
        elif not positive_heap:
            result.append(-heapq.heappop(negative_heap))
        elif not negative_heap:
            result.append(heapq.heappop(positive_heap))
        elif positive_heap[0] < negative_heap[0]:
            result.append(heapq.heappop(positive_heap))
        else:
            result.append(-heapq.heappop(negative_heap))

print(*result, sep='\n')