T = int(input())

for tc in range(1, T+1):
    N, L = map(int, input().split())
    ing = [list(map(int, input().split())) for i in range(N)]
    max_score = 0
    for i in range(1<<N):
        score = 0
        cal = 0
        for j in range(N+1):
            if i & (1<<j):
                score += ing[j][0]
                cal += ing[j][1]
        if cal <= L and score > max_score:
            max_score = score
    print(f'#{tc} {max_score}')
