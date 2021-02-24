T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # list comprehension으로 정원 영역 구성
    matrix = [list(map(int, input().split())) for _ in range(N)]

    cost = 0
    count = 0
    expen = 0
    expen_col = 0
    # 전체 열에 대해
    for i in range(M):
        # 만약 열이 홀수라면(1부터 시작 기준)
        if not i % 2:
            # 전체 행에 대해
            for j in range(N):
                # 총 비용에 해당 칸 나무 심는 비용 추가
                cost += matrix[j][i]
                # 심은 나무의 수 증가
                count += 1
                # 만약 해당 칸 나무 심는 비용이 이때까지 구한 가장 비싼 나무의 가격보다 비싸다면
                if matrix[j][i] >= expen:
                    # 가장 비싼 나무의 가격을 변수에 저장하고
                    expen = matrix[j][i]
                    # 해당 열을 저장
                    expen_col = i + 1

    print(f'#{tc} {cost} {count} {expen} {expen_col}')
