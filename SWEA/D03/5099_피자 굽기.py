T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))

    # 오븐 속 N개의 피자의 치즈의 양을 담을 queue
    queue = []
    # queue 내 피자의 index
    indexes = []
    idx = 0
    # 처음 N개의 피자 queue에 추가
    for i in range(N):
        queue.append(Ci.pop(0))
        idx += 1
        indexes.append(idx)
    # queue(오븐 속에) 1개의 피자만 남을 때까지
    while len(queue) > 1:
        pizza = queue.pop(0)
        p_idx = indexes.pop(0)
        # 이전에 남은 치즈가 1이었다면 이번에 빼야함
        if pizza == 1:
            # Ci에 남은 피자가 없을 수도 있으므로 try 활용
            try:
                queue.append(Ci.pop(0))
                idx += 1
                indexes.append(idx)
            except:
                pass
        # 피자를 빼야하지 않는다면 치즈양을 반으로 줄이고 queue 뒤로 append
        else:
            queue.append(pizza // 2)
            indexes.append(p_idx)
    print(f'#{tc} {indexes[0]}')
