def calc(n):
    global result
    # input으로 제공된 V-1개의 노드를 조회하기 위해
    for i in range(V-1):
        # 만약 부모 노드 번호가 n과 같다면
        if nodes[2*i] == n:
            # 결과값에 1을 더하고
            result += 1
            # 자손 노드에 대해 다시 자손 노드가 있는지 조회한다
            calc(nodes[2*i+1])


for tc in range(1, int(input())+1):
    # input 값들을 받아온다
    V, N = map(int, input().split())
    nodes = list(map(int, input().split()))
    # 결과값을 초기화하고, 만든 함수를 실행한다
    result = 0
    calc(N)
    print(f'#{tc} {result}')
