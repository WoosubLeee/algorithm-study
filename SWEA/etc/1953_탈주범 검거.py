# 1
match = [[], [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]
drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
check = [1, 0, 3, 2]

# 2
# match = {
#     0: [],
#     1: ['U', 'D', 'L', 'R'],
#     2: ['U', 'D'],
#     3: ['L', 'R'],
#     4: ['U', 'R'],
#     5: ['D', 'R'],
#     6: ['D', 'L'],
#     7: ['U', 'L']
# }
# check = {
#     'U': 'D',
#     'D': 'U',
#     'L': 'R',
#     'R': 'L'
# }
# drc = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}

for tc in range(1, int(input())+1):
    N, M, R, C, L = map(int, input().split())
    under = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    visited[R][C] = 1
    queue = [(R, C)]
    possible = 0
    for _ in range(L):
        for _ in range(len(queue)):
            q = queue.pop(0)
            possible += 1
            for i in match[under[q[0]][q[1]]]:
                r, c = q[0] + drc[i][0], q[1] + drc[i][1]
                if 0 <= r < N and 0 <= c < M and check[i] in match[under[r][c]] and not visited[r][c]:
                    queue.append((r, c))
                    visited[r][c] = 1
    print(f'#{tc} {possible}')
