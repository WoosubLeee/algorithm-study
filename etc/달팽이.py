arr = [[9, 20, 2, 18, 11],
       [19, 1, 25, 3, 21],
       [8, 24, 10, 17, 7],
       [15, 4, 16, 5, 6],
       [12, 13, 22, 23, 14]]

# 1차원 리스트로 변경
num_list = []
for i in range(len(arr)):
    for j in range(len(arr[i])):
        num_list.append(arr[i][j])
        arr[i][j] = 0

# 선택 정렬
for i in range(len(num_list) - 1):
    min_idx = i
    for j in (range(i+1, len(num_list))):
        if num_list[min_idx] > num_list[j]:
            min_idx = j
    num_list[i], num_list[min_idx] = num_list[min_idx], num_list[i]

# 델타 활용
# 오른쪽 방향부터 시작하므로 [오른쪽, 아래, 왼쪽, 위] 순서
drc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
r, c = 0, 0
delta = 0
for i in num_list:
    arr[r][c] = i
    # 끝에 다다르거나(0 미만 혹은 5 이상), 이미 0이 아닌 값이 들어가 있을 경우 delta 증가시켜 방향 변화
    if not 0 <= r + drc[delta % 4][0] < 5 or not 0 <= c + drc[delta % 4][1] < 5:
        delta += 1
    elif arr[r + drc[delta % 4][0]][c + drc[delta % 4][1]]:
        delta += 1
    r += drc[delta % 4][0]
    c += drc[delta % 4][1]
for i in arr:
    for j in i:
        print(j, end=' ')
    print()