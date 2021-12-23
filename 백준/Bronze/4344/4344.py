T = int(input())

for tc in range(T):
    scores = list(map(int, input().split()))
    num = 0
    avg = sum(scores[1:])/scores[0]
    for i in scores[1:]:
        if i > avg:
            num += 1
    print(f'{(num/scores[0])*100:.3f}%')