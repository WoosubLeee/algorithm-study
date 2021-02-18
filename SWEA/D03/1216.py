def is_palindrome(word):
    if len(word) == 0 or len(word) == 1:
        return True
    elif word[0] == word[-1]:
        return is_palindrome(word[1:-1])


for _ in range(10):
    tc = int(input())

    max_length = 0
    lines = []
    for _ in range(100):
        line = input()
        lines.append(line)

        try_length = max_length + 1
        while try_length < 101:
            for i in range(101 - try_length):
                if is_palindrome(line[i:i+try_length]):
                    max_length = try_length
                    break
            try_length += 1

    for i in range(100):
        line = ''.join([lines[j][i] for j in range(100)])
        try_length = max_length + 1
        while try_length < 101:
            for j in range(101 - try_length):
                if is_palindrome(line[j:j+try_length]):
                    max_length = try_length
                    break
            try_length += 1
    print(f'#{tc} {max_length}')
