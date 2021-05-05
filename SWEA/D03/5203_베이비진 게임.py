def is_run(p_cards):
    for i in p_cards:
        for j in range(1, 3):
            if i+j not in p_cards:
                break
        else:
            return max(p_cards.index(i), p_cards.index(i+1), p_cards.index(i+2))
    return 6


def is_triplet(p_cards):
    for i in p_cards[:4]:
        if p_cards.count(i) >= 3:
            return [idx for idx, x in enumerate(p_cards) if x == i][2]
    return 6


for tc in range(1, int(input())+1):
    cards = list(map(int, input().split()))
    one, two = [], []
    for i in range(6):
        one.append(cards[2*i])
        two.append(cards[2*i+1])

    one_result = min(is_run(one), is_triplet(one))
    two_result = min(is_run(two), is_triplet(two))
    if one_result == 6 and two_result == 6:
        print(f'#{tc} 0')
    elif one_result <= two_result:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 2')
