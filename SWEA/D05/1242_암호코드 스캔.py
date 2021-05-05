def to_binary(line):
    output = ''
    for i in line:
        output += hex_bin[i]
    return output


def shorten(binary):
    output = ''
    for i in range(len(binary) // multiple):
        output += binary[multiple * i]
    return output


hex_bin = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}
numbers = {
    '0001101': 0,
    '0010011': 2,
    '0011001': 1,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}
num_gaps = [
    [2, 1, 1],
    [2, 2, 1],
    [1, 2, 2],
    [4, 1, 1],
    [1, 3, 2],
    [2, 3, 1],
    [1, 1, 4],
    [3, 1, 2],
    [2, 1, 3],
    [1, 1, 2]
]

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    # code를 담고 있는 line들을 선별하기
    lines = []
    for _ in range(N):
        lines.append(to_binary(input()))

    total = 0
    for r in range(N):
        # print(f'#{tc} {r}')
        binary = lines[r]

        if '1' not in binary:
            continue
        start = binary.index('1')
        while start < 4*M:
            # 암호가 몇 배수의 길이를 갖는지 계산
            for i in range(start, 4*M):
                if binary[i] == '1':
                    # 코드 블록의 첫줄인지 확인
                    if r and lines[r-1][i] == '1':
                        start += 2
                        continue
                    plus, gaps = 1, []
                    for num in ['0', '1', '0']:
                        while binary[i+plus] != num:
                            plus += 1
                        if gaps:
                            gaps.append(plus-sum(gaps))
                        else:
                            gaps.append(plus)
                    for j in range(1, 6):
                        if [gaps[0]/j, gaps[1]/j, gaps[2]/j] in num_gaps:
                            multiple = j
                            break
                    # 다음에 조회를 시작할 부분(지금 암호의 끝 부분) 설정
                    start = i + plus + 49*multiple

                    # 2진수 중 암호코드 부분만 추출
                    binary_code = binary[(i+plus) - 7*multiple:(i+plus) + 49*multiple]
                    if multiple > 1:
                        binary_code = shorten(binary_code)

                    odd, even = 0, 0
                    for i in range(7):
                        num = numbers[binary_code[7*i:7*(i+1)]]
                        if i % 2:
                            even += num
                        else:
                            odd += num
                    verify = numbers[binary_code[49:56]]
                    if (odd * 3 + even + verify) % 10 == 0:
                        total += (odd + even + verify)
                    break
            else:
                break
    print(f'#{tc} {total}')
