for tc in range(1, int(input())+1):
    N = int(input())
    points = list(map(int, input().split()))

    scores = {0}
    for point in points:
        temp = set()
        for score in scores:
            temp.add(score + point)
        scores = scores | temp
    print(f'#{tc} {len(scores)}')
