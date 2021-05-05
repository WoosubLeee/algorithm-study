from copy import deepcopy


def get_virus_position():
    viruses = []
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 2:
                viruses.append([i, j])
    return viruses


def make_wall(n, start):
    if n == 0:
        calc_safe()
    else:
        for i in range(start, N):
            for j in range(M):
                if lab[i][j] == 0:
                    lab[i][j] = 1
                    make_wall(n-1, i)
                    lab[i][j] = 0


def calc_safe():
    global max_safe
    global lab
    temp_lab = deepcopy(lab)
    for virus in viruses:
        spread_virus(virus[0], virus[1])
    safe = 0
    for row in lab:
        for i in row:
            if i == 0:
                safe += 1
    if safe > max_safe:
        max_safe = safe
    lab = temp_lab


def spread_virus(r, c):
    for d in drc:
        new_r, new_c = r + d[0], c + d[1]
        if 0 <= new_r < N and 0 <= new_c < M and lab[new_r][new_c] == 0:
            lab[new_r][new_c] = 2
            spread_virus(new_r, new_c)


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

drc = [[0, -1], [0, 1], [-1, 0], [1, 0]]
viruses = get_virus_position()
max_safe = 0
make_wall(3, 0)
print(max_safe)
