def solution(n, computers):
    answer = 0

    visited = [False]*n

    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True

        stack = [i]
        while stack:
            com_idx = stack.pop()
            for j, connected in enumerate(computers[com_idx]):
                if not visited[j] and connected:
                    stack.append(j)
                    visited[j] = True
        answer += 1

    return answer


n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))