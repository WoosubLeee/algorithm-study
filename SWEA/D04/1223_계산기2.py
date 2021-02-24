def is_number(x):
    operator = ['+', '-', '*', '/']
    bracket = ['(', ')']
    if x not in operator and x not in bracket:
        return True
    else:
        return False


def icp(x):
    if x == '*' or x == '/':
        return 2
    elif x == '+' or x == '-':
        return 1
    elif x == '(':
        return 3


def isp(x):
    if x == '*' or x == '/':
        return 2
    elif x == '+' or x == '-':
        return 1
    elif x == '(':
        return 0


def calc(operator, y, x):
    if operator == '+':
        return int(x) + int(y)
    elif operator == '-':
        return int(x) - int(y)
    elif operator == '*':
        return int(x)*int(y)
    elif operator == '/':
        return int(x)/int(y)


for tc in range(1, 11):
    input()
    stack = []
    result = ''
    for i in input():
        if is_number(i):
            result += i
        elif i == ')':
            top = stack.pop()
            if top == '(':
                break
            result += top
        else:
            while stack:
                if icp(i) > isp(stack[-1]):
                    stack.append(i)
                    break
                else:
                    result += stack.pop()
            else:
                stack.append(i)
    while stack:
        result += stack.pop()

    for i in result:
        if is_number(i):
            stack.append(i)
        else:
            stack.append(calc(i, stack.pop(), stack.pop()))
    print(f'#{tc} {stack.pop()}')