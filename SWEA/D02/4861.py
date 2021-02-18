def is_palindrome(word):
    if len(word) == 0 or len(word) == 1:
        return True
    elif word[0] == word[-1]:
        return is_palindrome(word[1:-1])


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    lines = [input() for _ in range(N)]
    done = False
    for line in lines:
        for i in range(N - M + 1):
            if is_palindrome(line[i:i+M]):
                print(f'#{tc} {line[i:i+M]}')
                done = True
                break
        if done:
            break

    if not done:
        for i in range(N):
            line = ''.join([lines[j][i] for j in range(N)])
            for i in range(N - M + 1):
                if is_palindrome(line[i:i + M]):
                    print(f'#{tc} {line[i:i + M]}')
                    break
            if done:
                break
