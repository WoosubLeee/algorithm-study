def way(s, e):
    visited.append(s)
    for i in drc:
        new_r, new_c = s[0]+i[0], s[1]+i[1]
        if 0 <= new_r < N and 0 <= new_c < N:
            if miro[new_r][new_c] == '3':
                return 1
            elif miro[new_r][new_c] == '0' and [new_r, new_c] not in visited:
                if way([new_r, new_c], e):
                    return 1
    else:
        return 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    miro = [input() for _ in range(N)]
    for i in miro:
        for j in i:
            if j == '2':
                loc = [miro.index(i), i.index(j)]
            elif j == '3':
                end = [miro.index(i), i.index(j)]

    drc = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    visited = []
    print(f'#{tc} {way(loc, end)}')
