for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    number = ''
    while M:
        number = str(M % 2) + number
        M //= 2
    try:
        for i in range(N):
            if number[-i-1] == '0':
                raise Exception
        else:
            print(f'#{tc} ON')
    except:
        print(f'#{tc} OFF')
