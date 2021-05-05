def cnt(t):
    global result
    if t:
        try:
            result += 1
            cnt(tree[t][0])
            cnt(tree[t][1])
        except:
            pass


for tc in range(1, int(input())+1):
    e, n = map(int, input().split())
    nodes = list(map(int, input().split()))
    tree = [[] for _ in range(e+2)]
    for i in range(e):
        tree[nodes[2*i]].append(nodes[2*i + 1])
    result = 0
    cnt(n)
    print(f'#{tc} {result}')
