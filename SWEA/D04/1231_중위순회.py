def inorder(t):
    if t:
        inorder(left[t])
        print(alphabet[t], end='')
        inorder(right[t])


for tc in range(1, 11):
    N = int(input())
    alphabet, left, right = ['']*(N+1), [0]*(N+1), [0]*(N+1)
    for i in range(1, N+1):
        inputs = list(map(str, input().split()))
        alphabet[i] = inputs[1]
        try:
            left[i] = int(inputs[2])
            right[i] = int(inputs[3])
        except:
            pass
    print(f'#{tc}', end=' ')
    inorder(1)
    print()
