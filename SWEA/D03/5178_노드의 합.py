def calc(l):
    if l <= N:
        if l in nodes:
            return nodes[l]
        return calc(2*l) + calc(2*l + 1)
    return 0


for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    nodes = {}
    for i in range(M):
        node, value = map(int, input().split())
        nodes[node] = value
    print(f'#{tc} {calc(L)}')
