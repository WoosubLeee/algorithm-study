def find_set(n):
    if n == nodes[n]:
        return n
    return find_set(nodes[n])


def union(parent, child):
    nodes[find_set(child)] = find_set(parent)


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    nodes = list(range(N+1))
    group = list(map(int, input().split()))

    for m in range(M):
        union(group[2*m], group[2*m+1])
    count = 0
    for n in range(1, N+1):
        if nodes[n] == n:
            count += 1
    print(f'#{tc} {count}')
