T = int(input())

for tc in range(T):
    results = input()
    score = 0
    total = 0
    for result in results:
        if result == 'O':
            score += 1
            total += score
        else:
            score = 0
    print(total)