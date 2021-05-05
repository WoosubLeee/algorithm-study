def bfs(n):
    made, count = [False]*1000001, 0
    queue, front, rear = [0]*1000001, -1, 1
    queue[0], made[n] = n, True
    while front != rear:
        count += 1
        for _ in range(rear - front - 1):
            front += 1
            q = queue[front]
            for new_q in [q + 1, q - 1, q * 2, q - 10]:
                if new_q == M:
                    return count
                if 1 <= new_q <= 1000000 and not made[new_q]:
                    made[new_q] = True
                    queue[rear] = new_q
                    rear += 1


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    print(f'#{tc} {bfs(N)}')
