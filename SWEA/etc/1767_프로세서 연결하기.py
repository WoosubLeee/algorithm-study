def restore(r, c, d, original, length):
    while [r, c] != original:
        pro[r][c] = 0
        length -= 1
        r -= d[0]
        c -= d[1]
    return length


def look(core):
    global length, min_len, count, max_count
    if count + (len(cores)-core) >= max_count:
        if core == len(cores):
            if count > max_count or (count == max_count and length < min_len):
                max_count = count
                min_len = length
        else:
            for d in drc:
                r, c = cores[core]
                while 0 < r < N-1 and 0 < c < N-1:
                    if pro[r+d[0]][c+d[1]]:
                        break
                    else:
                        r += d[0]
                        c += d[1]
                        pro[r][c] = 2
                        length += 1
                        if count + (len(cores)-core) == max_count and length > min_len:
                            break
                else:
                    count += 1
                    look(core + 1)
                    count -= 1
                length = restore(r, c, d, cores[core], length)
            look(core + 1)


drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for tc in range(1, int(input())+1):
    N = int(input())
    pro = [list(map(int, input().split())) for _ in range(N)]
    cores = []
    for i in range(N):
        for j in range(N):
            if pro[i][j]:
                cores.append([i, j])
    length, min_len, count, max_count = 0, N*N, 0, 0
    look(0)
    print(f'#{tc} {min_len}')
