for t in range(10):
    dump = int(input())
    box_list = list(map(int, input().split()))
    # 상자들을 높이를 기준으로 카운팅 정렬 시행
    count = [0] * 100
    for i in box_list:
        count[i-1] += 1
    new_list = []
    for i in range(len(count)):
        new_list += ([i] * count[i])

    # 덤프 반복 시행
    for _ in range(dump):
        # 최고 높이에서는 한 개 빼고, 최저 높이에는 한 개 더한다
        new_list[0] += 1
        new_list[-1] -= 1
        # 1 높아진 기존 최저값이 다시 정렬될 수 있도록 한다
        idx = 0
        while True:
            if new_list[idx] > new_list[idx+1]:
                new_list[idx], new_list[idx+1] = new_list[idx+1], new_list[idx]
                idx += 1
            else:
                break
        # 1 낮아진 기존 최고값이 다시 정렬될 수 있도록 한다
        idx = -1
        while True:
            if new_list[idx] < new_list[idx-1]:
                new_list[idx], new_list[idx-1] = new_list[idx-1], new_list[idx]
                idx -= 1
            else:
                break
    print(f'#{t+1} {new_list[-1] - new_list[0]}')