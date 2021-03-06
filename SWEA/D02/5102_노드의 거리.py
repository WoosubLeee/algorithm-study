def find_distance(s, g):
    # 방문한 적 있는지 여부를 담은 리스트
    visited = [0]*(V+1)
    # 시작 지점부터의 거리를 담은 리스트
    distance = [0]*(V+1)
    queue = [s]
    while queue:
        node = queue.pop(0)
        for i in range(1, V+1):
            # node에서 i 지점이 연결되어 있고, i 지점을 조회한 적이 없다면
            if matrix[node][i] and not visited[i]:
                visited[i] = 1
                # 시작 지점부터 i 지점까지의 거리를 저장
                distance[i] = distance[node] + 1
                # 만약 i가 goal지점과 같다면 distance return
                if i == g:
                    return distance[i]
                queue.append(i)
    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    matrix = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        matrix[a][b], matrix[b][a] = 1, 1

    start, goal = map(int, input().split())
    print(f'#{tc} {find_distance(start, goal)}')
