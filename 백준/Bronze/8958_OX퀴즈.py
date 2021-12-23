import sys

T = int(sys.stdin.readline())
for _ in range(T):
    line = sys.stdin.readline()
    total, score = 0, 0
    for result in line:
        if result == 'O':
            score += 1
            total += score
        else:
            score = 0
    print(total)