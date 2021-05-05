for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    freights, trucks = list(map(int, input().split())), list(map(int, input().split()))

    for i in range(N):
        max_idx, max_w = i, freights[i]
        for j in range(i+1, N):
            if freights[j] > max_w:
                max_idx, max_w = j, freights[j]
        freights[i], freights[max_idx] = freights[max_idx], freights[i]

    result = 0
    for freight in freights:
        if freight <= max(trucks):
            result += freight
            trucks[trucks.index(max(trucks))] = 0
    print(f'#{tc} {result}')
