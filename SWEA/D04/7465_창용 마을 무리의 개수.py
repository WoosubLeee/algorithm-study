def find_set(n):
    if n == nodes[n]:
        return n
    return find_set(nodes[n])


def union(parent, child):
    nodes[find_set(child)] = find_set(parent)


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    nodes = list(range(N + 1))

    for _ in range(M):
        x, y = map(int, input().split())
        union(x, y)

    count = 0
    for i in range(1, N+1):
        if nodes[i] == i:
            count += 1
    print(f'#{tc} {count}')
