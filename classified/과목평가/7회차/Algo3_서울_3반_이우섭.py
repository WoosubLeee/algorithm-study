def search():
    global queue, zones, move, result
    # 이미 지나간 곳은 다시 지나가지 않도록 하기 위해
    included = [[0]*N for _ in range(N)]
    # bfs 활용
    while queue:
        # 갈 수 있는 zone이 여러 개라면 값이 적은 곳으로 갈 수 있도록 하기 위해 최대 zone(blue)값인 5보다 큰 6으로 설정
        temp = 6
        move += 1
        # 이동 거리를 계산하기 위해 while문 안에 for문 한 번 더 활용
        for i in range(len(queue)):
            now = queue.pop(0)
            for d in drc:
                new_r, new_c = now[0] + d[0], now[1] + d[1]
                # 조회하려는 좌표가 index 내에 있는지 검사
                if 0 <= new_r < N and 0 <= new_c < N:
                    # 이전에 지나온 적이 없고, 이미 통과한 zone도 아니고, 벽이 아니라면
                    if not included[new_r][new_c] and not zones[new_r][new_c] and map_i[new_r][new_c] != 1:
                        # queue와 include에 추가
                        queue.append([new_r, new_c])
                        included[new_r][new_c] = 1
                        # 해당 좌표가 zone이라면 temp와 비교하여 더 작다면 교체
                        if 3 <= map_i[new_r][new_c] < temp:
                            next_start = [new_r, new_c]
                            temp = map_i[new_r][new_c]
                            zones[new_r][new_c] = 1
        # 만약 zone이 조회된게 있다면
        if temp < 6:
            # queue를 해당 zone부터 시작하는 것으로 초기화 하고
            queue = [next_start]
            included = [[0]*N for _ in range(N)]
            # 결과값에 move값 저장
            # 만약 마지막까지 더이상 조회할 zone이 없었다면(if temp < 6: 안으로 들어오지 못했다면)
            # 그때까지 기록된 move값은 버려지고 마지막에 저장된 result값만 출력됨
            result = move


for tc in range(1, int(input())+1):
    # input값을 저장한다
    N = int(input())
    map_i = [list(map(int, input().split())) for _ in range(N)]
    # 로봇의 위치를 찾는다
    for i in range(N):
        for j in range(N):
            if map_i[i][j] == 2:
                robot = [i, j]
    drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    # bfs를 활용하는데 시작 좌표로 로봇의 좌표 추가
    queue = [robot]
    # 이미 지나간 zone은 통과할 수 없으므로 지나간 zone 저장하기 위한 배열
    zones = [[0]*N for _ in range(N)]
    move, result = 0, 0
    search()
    print(f'#{tc} {result}')
