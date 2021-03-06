T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = []
    sub_matrix = []
    for i in range(N):
        for j in range(N):
            # 부분 행렬의 왼쪽 위 좌표값을 찾는 조건문
            if (i == 0 or matrix[i-1][j] == 0) and (j == 0 or matrix[i][j-1] == 0) and matrix[i][j]:
                sub_matrix.append([[i, j]])
            # 부분 행렬의 오른쪽 끝 x좌표를 찾는 조건문
            if sub_matrix and (j == N-1 or matrix[i][j+1] == 0) and matrix[i][j] and len(sub_matrix[0]) == 1:
                # 찾았다면 아래로 내려가며 아래 끝 y좌표를 찾는다
                sub_matrix[0].append([0, j])
                for m in range(i, N):
                    if matrix[m+1][j] == 0:
                        sub_matrix[0][1][0] = m
                        result.append(sub_matrix.pop(0))
                        break
    # 현재 result에는 부분 행렬들의 [왼쪽 위 좌표값, 오른쪽 아래 좌표값]이 들어가 있는데 이를 [높이, 너비, 넓이]로 변환하여 저장
    for i in range(len(result)):
        temp = result.pop(0)
        height = temp[1][0] - temp[0][0] + 1
        width = temp[1][1] - temp[0][1] + 1
        result.append([height, width, height*width])

    for i in range(len(result)):  # 선택 정렬
        min_square = result[i][2]
        min_idx = i
        for j in range(i+1, len(result)):
            if result[j][2] < min_square:
                min_square = result[j][2]
                min_idx = j
        result[i], result[min_idx] = result[min_idx], result[i]

    print(f'#{tc} {len(result)}', end='')  # 결과 출력
    for i in result:
        print(f' {i[0]} {i[1]}', end='')
    print()
