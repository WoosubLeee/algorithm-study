T = int(input())

for test in range(T):
    # 맵 2차원 리스트로 구성하고
    # tank 위치와 방향 구하기
    height, width = map(int, input().split())
    field = []
    t_idx = [0, 0]
    for i in range(height):
        line = list(input())
        field.append(line)
        tank = [j for j in ['^', 'v', '<', '>'] if j in line]
        if tank:
            t_idx = [i, line.index(tank[0])]
    
    move_num = int(input())
    move_list = list(input())
    for i in move_list:

        if i == 'U':
            field[t_idx[0]][t_idx[1]] = '^'
            if t_idx[0] == 0:
                continue
            elif field[t_idx[0]-1][t_idx[1]] == '.':
                # 자리를 맞바꾼다
                field[t_idx[0]-1][t_idx[1]], field[t_idx[0]][t_idx[1]] = field[t_idx[0]][t_idx[1]], field[t_idx[0]-1][t_idx[1]]
                t_idx = [t_idx[0]-1, t_idx[1]]
        elif i == 'D':
            field[t_idx[0]][t_idx[1]] = 'v'
            if t_idx[0] == height - 1:
                continue
            elif field[t_idx[0]+1][t_idx[1]] == '.':
                field[t_idx[0]+1][t_idx[1]], field[t_idx[0]][t_idx[1]] = field[t_idx[0]][t_idx[1]], field[t_idx[0]+1][t_idx[1]]
                t_idx = [t_idx[0] + 1, t_idx[1]]
        elif i == 'L':
            field[t_idx[0]][t_idx[1]] = '<'
            if t_idx[1] == 0:
                continue
            elif field[t_idx[0]][t_idx[1]-1] == '.':
                field[t_idx[0]][t_idx[1]-1], field[t_idx[0]][t_idx[1]] = field[t_idx[0]][t_idx[1]], field[t_idx[0]][t_idx[1]-1]
                t_idx = [t_idx[0], t_idx[1] - 1]
        elif i == 'R':
            field[t_idx[0]][t_idx[1]] = '>'
            if t_idx[1] == width - 1:
                continue
            elif field[t_idx[0]][t_idx[1]+1] == '.':
                field[t_idx[0]][t_idx[1]+1], field[t_idx[0]][t_idx[1]] = field[t_idx[0]][t_idx[1]], field[t_idx[0]][t_idx[1]+1]
                t_idx = [t_idx[0], t_idx[1] + 1]

        elif i == 'S':
            if field[t_idx[0]][t_idx[1]] == '^':
                for j in range(t_idx[0]-1, -1, -1):
                    if field[j][t_idx[1]] == '*':
                        field[j][t_idx[1]] = '.'
                        break
                    elif field[j][t_idx[1]] == '#':
                        break
            elif field[t_idx[0]][t_idx[1]] == 'v':
                for j in range(t_idx[0], height):
                    if field[j][t_idx[1]] == '*':
                        field[j][t_idx[1]] = '.'
                        break
                    elif field[j][t_idx[1]] == '#':
                        break
            elif field[t_idx[0]][t_idx[1]] == '<':
                for j in range(t_idx[1]-1, -1, -1):
                    if field[t_idx[0]][j] == '*':
                        field[t_idx[0]][j] = '.'
                        break
                    elif field[t_idx[0]][j] == '#':
                        break
            elif field[t_idx[0]][t_idx[1]] == '>':
                for j in range(t_idx[1], width):
                    if field[t_idx[0]][j] == '*':
                        field[t_idx[0]][j] = '.'
                        break
                    elif field[t_idx[0]][j] == '#':
                        break
    print(f'#{test+1}', end=' ')
    for i in field:
        print(''.join(i))
