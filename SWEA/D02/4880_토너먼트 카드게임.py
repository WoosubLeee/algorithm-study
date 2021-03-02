def match(ij, idx):
    if len(ij) == 1:
        return idx
    else:
        i = match(cards[idx:(2*idx+len(ij)-1)//2 + 1], idx)
        j = match(cards[(2*idx+len(ij)-1)//2 + 1:idx+len(ij)], (2*idx+len(ij)-1)//2 + 1)
        # 번호가 큰 카드가 이길 경우(해당되지 않으면 번호가 작은 카드가 올라감)
        if [cards[j], cards[i]] in win:
            return j
        else:
            return i


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))

    win = [[1, 3], [2, 1], [3, 2]]
    print(f'#{tc} {match(cards, 0) + 1}')
