numbers = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    for _ in range(N):
        temp = input()
        if '1' in temp:
            code_input = temp

    code = []
    odd = 0
    even = 0
    for i in range(M):
        if code_input[i] == '1':
            start = i - 55
    for i in range(7):
        num = numbers[code_input[(7*i+start):(7*(i+1)+start)]]
        code.append(num)
        if i % 2:
            even += num
        else:
            odd += num
    verify = numbers[code_input[start+49:start+56]]
    if (odd*3 + even + verify) % 10 == 0:
        print(f'#{tc} {sum(code)+verify}')
    else:
        print(f'#{tc} 0')
