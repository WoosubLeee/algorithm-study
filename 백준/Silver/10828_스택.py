import sys


result = ''
stack = []
for _ in range(int(sys.stdin.readline())):
    line = sys.stdin.readline().split(' ')
    output = ''
    keyword = line[0].strip()
    if keyword == 'push':
        stack.append(int(line[1]))
    elif keyword == 'pop':
        output = stack.pop() if stack else -1
    elif keyword == 'size':
        output = len(stack)
    elif keyword == 'empty':
        output = 0 if stack else 1
    else:
        output = stack[-1] if stack else -1
    if output != '':
        result += f'{output}\n'
print(result)