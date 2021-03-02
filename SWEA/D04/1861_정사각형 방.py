def search(r, c):
    for i in drc:
        if 0 <= r+i[0] < N and 0 <= c+i[1] < N:
            if matrix[r+i[0]][c+i[1]] == matrix[r][c]+1:
                nums[matrix[r][c]] = 1


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]
    drc = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    nums = [0]*(N**2)
    for i in range(N):
        for j in range(N):
            search(i, j)

    temp_num, max_num = 0, 0
    temp_count, max_count = 1, 1
    for i in range(len(nums)):
        if nums[i]:
            temp_count += 1
        else:
            if temp_count > max_count:
                max_num = temp_num
                max_count = temp_count
            temp_num = i + 1
            temp_count = 1
    print(f'#{tc} {max_num} {max_count}')
