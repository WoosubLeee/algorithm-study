import sys


for _ in range(int(sys.stdin.readline())):
    stack = 0
    for b in sys.stdin.readline().strip():
        if b == '(':
            stack += 1
        else:
            if stack == 0:
                break
            stack -= 1
    else:
        if stack == 0:
            print('YES')
            continue
    print('NO')