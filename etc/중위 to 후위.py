operator = ['+', '-', '*', '/']
bracket = ['(', ')']

top = -1
stack = []
priority = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
read = input()
for i in read:
    if i not in operator and i not in bracket:
        print(i, end='')
    elif i == '(':
        stack.append(i)
        top += 1
    elif i in operator:
        while priority[stack[top]] >= priority[i]:
            print(stack.pop(), end='')
            top -= 1
        stack.append(i)
        top += 1
    elif i == ')':
        while stack[top] != '(':
            print(stack.pop(), end='')
            top -= 1
        stack.pop()
        top -= 1
while stack:
    print(stack.pop(), end='')
