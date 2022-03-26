def solution(name):
    length = len(name)

    answer = 0
    horizontal = length - 1
    for i in range(length):
        answer += calc_updown(name[i])

        next_not_a = i + 1
        while next_not_a < length and name[next_not_a] == 'A':
            next_not_a += 1

        forward = i*2 + length - next_not_a
        back = (length - next_not_a)*2 + i

        horizontal = min(horizontal, forward, back)

    return answer + horizontal


def calc_updown(target):
    gap = ord(target) - 65
    if gap > 13:
        gap = 26 - gap
    return gap


name = "AAAAA"
print(solution(name))