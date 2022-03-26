import sys
import heapq


M, N = map(int, sys.stdin.readline().split(' '))
heights = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(M)]
counts = [[0]*N for _ in range(M)]
counts[0][0] = 1

drc = [[-1, 0], [0, 1], [1, 0], [0, -1]]
heap = [(-heights[0][0], 0, 0)]
while heap:
    now = heapq.heappop(heap)
    now_h = -now[0]
    for d in drc:
        near_r, near_c = now[1]+d[0], now[2]+d[1]
        if 0 <= near_r < M and 0 <= near_c < N:
            near_h = heights[near_r][near_c]
            if near_h < now_h:
                if (-near_h, near_r, near_c) not in heap:
                    heapq.heappush(heap, (-near_h, near_r, near_c))
            elif near_h > now_h:
                counts[now[1]][now[2]] += counts[near_r][near_c]

    if now[1] == M-1 and now[2] == N-1:
        print(counts[M-1][N-1])
        break
else:
    print(counts[M - 1][N - 1])