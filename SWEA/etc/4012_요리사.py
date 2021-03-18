def search(start):
    global picked, min_gap
    for i in range(start, N - (N//2-1-picked)):
        picked_a.append(i)
        picked_b.remove(i)
        picked += 1
        if len(picked_a) == N // 2:
            synergy_a = calc_synergy(picked_a)
            synergy_b = calc_synergy(picked_b)
            gap = abs(synergy_a - synergy_b)
            if gap < min_gap:
                min_gap = gap
        else:
            search(i + 1)
        picked_a.remove(i)
        picked_b.append(i)
        picked -= 1


def calc_synergy(foods):
    synergy = 0
    for i in foods:
        for j in foods:
            synergy += syn[i][j]
    return synergy


for tc in range(1, int(input())+1):
    N = int(input())
    syn = [list(map(int, input().split())) for _ in range(N)]
    picked_a, picked_b = [], list(range(N))
    picked = 0
    min_gap = 1000000
    search(0)
    print(f'#{tc} {min_gap}')
