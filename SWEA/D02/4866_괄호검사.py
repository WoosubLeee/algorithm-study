T = int(input())

for tc in range(1, T+1):

    stack = []
    result = True
    for i in input():
        if i in ['{', '(']:
            stack.append(i)
        elif i in ['}', ')']:
            try:
                last = stack.pop()
            except:
                result = False
                break

            if (i == '}' and last != '{') or (i == ')' and last != '('):
                result = False
                break

    if stack or not result:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')