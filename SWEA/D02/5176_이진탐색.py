def fill(t):
    global num
    if t:
        fill(tree[t][0])
        nodes[t] = num
        num += 1
        fill(tree[t][1])


for tc in range(1, int(input())+1):
    N = int(input())
    tree = [[0]*2 for _ in range(N+1)]
    for n in range(2, N+1):
        tree[n // 2][n - 2*(n//2)] = n
    nodes = [0]*(N+1)
    num = 1
    fill(1)
    print(f'#{tc} {nodes[1]} {nodes[N // 2]}')
