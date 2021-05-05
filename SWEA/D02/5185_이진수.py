def to_binary(n):
    output = ''
    for i in range(3, -1, -1):
        if n & (1 << i):
            output += '1'
        else:
            output += '0'
    return output


for tc in range(1, int(input())+1):
    N, hexa = map(str, input().split())

    result = ''
    for i in hexa:
        try:
            x = int(i)
        except:
            x = ord(i) - 55
        result += to_binary(x)
    print(f'#{tc} {result}')
