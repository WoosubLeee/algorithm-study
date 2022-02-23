import sys


stack = []
stack_result = []
order = 1
for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    for i in range(order, num+1):
        stack.append(i)
        stack_result.append('+')
        order += 1

    top = stack.pop()
    if top != num:
        print('NO')
        break
    stack_result.append('-')
else:
    print('\n'.join(stack_result))