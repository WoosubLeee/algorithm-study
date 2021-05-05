def switch(node):
    if node[1] and node[0] < tree[node[1]][0]:
        node[0], tree[node[1]][0] = tree[node[1]][0], node[0]
        switch(tree[node[1]])


for tc in range(1, int(input())+1):
    N = int(input())
    nums = list(map(int, input().split()))
    tree = [[]]
    for n in range(1, N+1):
        tree.append([nums[n-1], n // 2])
        switch(tree[-1])
    result = 0
    parent = tree[N][1]
    while parent:
        result += tree[parent][0]
        parent = tree[parent][1]
    print(f'#{tc} {result}')
