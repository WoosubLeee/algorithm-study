T = int(input())

for tc in range(T):
    arr = [[0 for i in range(10)] for j in range(10)]
    N = int(input())
    for n in range(N):
        box = list(map(int, input().split()))
        for i in range(box[0], box[2]+1):
            for j in range(box[1], box[3]+1):
                if arr[i][j] != box[4]:
                    arr[i][j] += box[4]
    result = 0
    for i in arr:
        for j in i:
            if j == 3:
                result += 1
    print(f'#{tc+1} {result}')