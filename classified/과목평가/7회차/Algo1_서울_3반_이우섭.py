def calc(bomb):
    global result
    # 폭탄이 떨어진 자리의 적군 피해 추가
    result += field[bomb[0]][bomb[1]]
    included[bomb[0]][bomb[1]] = 1
    # 각 대각선 방향에 대해
    for d in drc:
        # 폭탄의 피해 거리를 1씩 증가시켜 나가며
        for i in range(1, bomb[2]+1):
            # 폭탄의 피해가 닿은 좌표를 설정하고
            new_r, new_c = bomb[0] + i*d[0], bomb[1] + i*d[1]
            # 해당 좌표가 index를 벗어나지 않는지, 이전에 다른 폭탄에 피해를 입은 적이 없는지 확인하여
            if 0 <= new_r < N and 0 <= new_c < N and not included[new_r][new_c]:
                # 해당 사항 없다면 결과값에 피해량 추가, included에 좌표 추가
                result += field[new_r][new_c]
                included[new_r][new_c] = 1


for tc in range(1, int(input())+1):
    # input 값들을 받아온다
    N, M = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(N)]
    bombs = [list(map(int, input().split())) for _ in range(M)]

    # delta를 활용하는데 4 대각선 방향을 향하도록 한다
    drc = [[-1, -1], [-1, 1], [1, 1], [1, -1]]
    # 폭탄 간의 적군 피해가 중복 계산되지 않도록 해당 좌표의 적군이 피해를 입은 적이 있는지 기록하는 리스트 생성
    included = [[0]*N for _ in range(N)]
    result = 0
    # 각 폭탄에 대해 적군 피해량을 계산한다
    for bomb in bombs:
        calc(bomb)
    print(f'#{tc} {result}')
