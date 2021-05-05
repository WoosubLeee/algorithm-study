for tc in range(1, int(input())+1):
    inputs = list(map(int, input().split()))

    # 결과값
    count = 0
    # 출발지점
    now = 1
    while now + inputs[now] < inputs[0]:
        # 현재 출발 지점에서 갈 수 있는 후보군 중(ex - 2에서 출발, 배터리가 3이라면 (3, 4, 5)가 후보군)
        # 어느 지점을 교환 지점으로 해야 그 다음에 가장 멀리갈 수 있는지 구한다
        next_stop, next_reach = now, 0
        for i in range(now+1, now+1+inputs[now]):
            if i < len(inputs) and i + inputs[i] > next_reach:
                next_stop, next_reach = i, i + inputs[i]
        count += 1
        now = next_stop
    print(f'#{tc} {count}')
