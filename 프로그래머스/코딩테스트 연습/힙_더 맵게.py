import heapq


def solution(scoville, K):
    heapq.heapify(scoville)

    count = 0
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + 2*second)
        count += 1

    return count


scoville = [1, 2, 3, 9, 10, 12]
K = 7

print(solution(scoville, K))