for tc in range(1, int(input())+1):
    N = int(input())
    works = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        count = 0
        for j in range(N):
            if i != j:
                if works[i][0] < works[j][1] and works[i][1] > works[j][0]:
                    count += 1
        works[i].append(count)
    works.sort(key=lambda x: x[2])

    planned = []
    for work in works:
        for plan in planned:
            if work[0] < plan[1] and work[1] > plan[0]:
                break
        else:
            planned.append(work)
    print(f'#{tc} {len(planned)}')
