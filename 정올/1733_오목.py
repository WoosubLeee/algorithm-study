def is_win(dol_list, row, col, bw):
    drc = [[0, 1], [1, 0], [1, 1], [-1, 1]]
    for i in drc:
        if [row-i[0], col-i[1], bw] not in dol_list:
            count = 1
            while count < 5:
                if [row+i[0]*count, col+i[1]*count, bw] in dol_list:
                    count += 1
                else:
                    break
            else:
                if [row+i[0]*count, col+i[1]*count, bw] not in dol_list:
                    return True


matrix = [list(map(int, input().split())) for _ in range(19)]
try_list = [[i, j, matrix[i][j]] for i in range(19) for j in range(19) if matrix[i][j]]

for i in try_list:
    if is_win(try_list, i[0], i[1], matrix[i[0]][i[1]]):
        print(matrix[i[0]][i[1]])
        print(i[0]+1, i[1]+1)
        break
else:
    print(0)
