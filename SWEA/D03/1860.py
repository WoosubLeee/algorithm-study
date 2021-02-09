T = int(input())

for t in range(T):
    N, M, K = map(int, input().split())
    seconds = list(map(int, input().split()))
    # sorting seconds list
    for i in range(len(seconds)-1, 0, -1):
        for j in range(i):
            if seconds[j] > seconds[j+1]:
                seconds[j], seconds[j+1] = seconds[j+1], seconds[j]

    sold = 0
    result = 'Possible'
    '''
    각 손님이 올 때까지의 시간인 i를
    M으로 나누면 붕어빵을 몇 번 찍어냈는지 알 수 있다.
    거기에 K를 곱하면 i까지 몇 개를 찍어냈는지 알아낼 수 있다.
    
    각 i마다(손님이 올 때마다) sold를 1씩 증가시켜 이때까지 몇 개가 팔렸는지 저장하고
    만약 sold가 made보다 많다면 Impossible을 출력한다.
    '''
    for i in seconds:
        made = (i // M) * K
        sold += 1
        if sold > made:
            result = 'Impossible'
            break

    print(f'#{t+1} {result}')