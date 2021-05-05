def calc(t):
    try:
        return int(tree[t][1])
    except:
        operator, left, right = tree[t][1], int(tree[t][2]), int(tree[t][3])
        if operator == '+':
            return calc(left) + calc(right)
        elif operator == '-':
            return calc(left) - calc(right)
        elif operator == '*':
            return calc(left)*calc(right)
        elif operator == '/':
            return calc(left)/calc(right)


for tc in range(1, 11):
    N = int(input())
    tree = [[]]
    for i in range(1, N+1):
        tree.append(list(map(str, input().split())))
    print(f'#{tc} {int(calc(1))}')
