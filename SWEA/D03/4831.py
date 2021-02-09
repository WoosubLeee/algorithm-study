T = int(input())

for t in range(T):
    K, N, M = map(int, input().split())

    # 출발 지점(0)과 도착 지점(N)까지 포함하여 충전소 리스트 선언
    charger_list = [0] + list(map(int, input().split())) + [N]

    charge_count = 0
    driven = 0
    for m in range(0, M):
        # 만약 현재 충전소에서 다음 충전소까지의 거리가 K보다 크다면 갈 수 없으므로 charge_count(출력값)에 0을 넣고 break
        if charger_list[m+1] - charger_list[m] > K:
            charge_count = 0
            break
        # 이전 충전소에서 현재 충전소까지의 거리를 driven에 추가
        driven += (charger_list[m+1]-charger_list[m])

        # 만약 직전 충전 후 운전한 거리 + 다음 충전소까지의 거리가 K보다 크다면 이번 충전소에서 충전해야 하므로
        # charge_count에 1을 추가하고, driven을 초기화
        if driven + (charger_list[m+2] - charger_list[m+1]) > K:
            charge_count += 1
            driven = 0
    print(f'#{t+1} {charge_count}')