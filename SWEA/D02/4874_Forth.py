T = int(input())

for tc in range(1, T+1):
    line = list(input().split())

    stack = []
    try:
        for i in line[:-1]:
            if i not in ['+', '-', '*', '/']:
                stack.append(int(i))
            else:
                top = stack.pop()
                if i == '+':
                    stack.append(stack.pop() + top)
                elif i == '-':
                    stack.append(stack.pop() - top)
                elif i == '*':
                    stack.append(stack.pop()*top)
                else:
                    stack.append(stack.pop() // top)
        if len(stack) > 1:
            raise Exception
    except:
        print(f'#{tc} error')
        continue
    print(f'#{tc} {stack[0]}')
