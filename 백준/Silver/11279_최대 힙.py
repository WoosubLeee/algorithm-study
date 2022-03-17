import sys


def push(heap, end, num):
    end += 1
    heap[end] = num

    position = end
    while position > 1 and heap[position // 2] < heap[position]:
        heap[position // 2], heap[position] = heap[position], heap[position // 2]
        position //= 2

    return end


def pop(heap, end):
    print(heap[1])

    heap[1], heap[end] = heap[end], 0
    end -= 1

    position = 1
    while position <= end // 2:
        big = position
        if heap[big] < heap[2*position]:
            big = 2*position
        if heap[big] < heap[2*position + 1]:
            big = 2*position + 1

        if big != position:
            heap[position], heap[big] = heap[big], heap[position]
            position = big
        else:
            break

    return end


N = int(sys.stdin.readline())
heap = [0]*(N+1)
end = 0
for _ in range(N):
    x = int(sys.stdin.readline())

    if x:
        end = push(heap, end, x)
    else:
        if end:
            end = pop(heap, end)
        else:
            print(0)