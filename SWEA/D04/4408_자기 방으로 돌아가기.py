T = int(input())

for tc in range(1, T+1):
    N = int(input())
    way = [0]*200
    for n in range(N):
        start, dest = map(int, input().split())
        if start > dest:
            start, dest = dest, start
        for i in range((start-1) // 2, (dest+1) // 2):
            way[i] += 1
    max_way = 0
    for i in way:
        if i > max_way:
            max_way = i
    print(f'#{tc} {max_way}')
