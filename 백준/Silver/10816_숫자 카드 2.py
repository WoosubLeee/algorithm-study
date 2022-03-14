N = int(input())
cards = list(map(int, input().split(' ')))

card_dict = {}
for card in cards:
    if card in card_dict:
        card_dict[card] += 1
    else:
        card_dict[card] = 1

M = int(input())
targets = list(map(int, input().split(' ')))

result = []
for target in targets:
    result.append(card_dict[target] if target in card_dict else 0)

print(*result)