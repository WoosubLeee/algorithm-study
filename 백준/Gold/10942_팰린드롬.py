import sys


def is_palindrome(start, end):
    starts = ((start + end) // 2, (start + end + 1) // 2)
    length = memos[starts] if starts in memos else 0
    while starts[0]-length >= start:
        if nums[starts[0]-length-1] == nums[starts[1]+length-1]:
            length += 1
        else:
            return_val = 0
            break
    else:
        return_val = 1
    memos[starts] = length
    return return_val


N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split(' ')))
questions = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(int(sys.stdin.readline()))]

memos = {}

result = []
for q in questions:
    result.append(is_palindrome(q[0], q[1]))
print(*result, sep='\n')