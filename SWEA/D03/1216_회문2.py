def is_palindrome(word):
    if len(word) == 0 or len(word) == 1:
        return True
    elif word[0] == word[-1]:
        return is_palindrome(word[1:-1])

# # 1
# def find_palindrome(line, length):
#     for i in range(100):
#         for j in range(101-length):
#             if is_palindrome(line[i][j:j+length]):
#                 return True
#             else:
#                 line_i = ''
#                 for k in range(100):
#                     line_i += lines[k][i]
#                 for k in range(101-length):
#                     if is_palindrome(line_i[k:k+length]):
#                         return True
#
#
# for _ in range(10):
#     tc = int(input())
#
#     lines = [input() for _ in range(100)]
#     for i in range(100, 0, -1):
#         if find_palindrome(lines, i):
#             max_length = i
#             break

    # 2
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
