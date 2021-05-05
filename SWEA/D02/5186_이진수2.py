for tc in range(1, int(input())+1):
    num = float(input())
    result = ''
    binary = -1
    while num:
        result += str(int(num // (2 ** binary)))
        num %= (2 ** binary)
        binary -= 1
        if binary < -13:
            print(f'#{tc} overflow')
            break
    else:
        print(f'#{tc} {result}')
