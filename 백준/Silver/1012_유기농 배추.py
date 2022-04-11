from sys import stdin


for _ in range(int(stdin.readline())):
    M, N, K = map(int, stdin.readline().split())

    matrix = [[0]*M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, stdin.readline().split())
        matrix[Y][X] = 1

    drc = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    count = 0

    for i in range(N):
        for j in range(M):
            if matrix[i][j]:
                stack = [(i, j)]
                matrix[i][j] = 0

                while stack:
                    popped = stack.pop()
                    for d in drc:
                        new_r, new_c = popped[0] + d[0], popped[1] + d[1]
                        if 0 <= new_r < N and 0 <= new_c < M and matrix[new_r][new_c]:
                            stack.append((new_r, new_c))
                            matrix[new_r][new_c] = 0
                count += 1

    print(count)