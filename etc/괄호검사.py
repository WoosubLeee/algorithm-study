stack = []

try:
    for i in input():
        if i == '(':
            stack.append(i)
        else:
            stack.pop()
    if stack:
        raise Exception
    print('에러 미발생')
except:
    print('에러 발생')
