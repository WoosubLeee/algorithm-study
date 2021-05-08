def binary_search(n, l, r, count):
    global result_num, result
    # 이때까지의 탐색 횟수가 현재까지의 결과값보다 크다면 중지(백트래킹)
    if count <= result and r >= l:
        # 중심 원소 설정
        m = (l + r) // 2
        if nums[m] == n:
            # 최소 탐색 횟수가 같은 경우 대비
            if count < result or (count == result and n < result_num):
                result_num, result = n, count
        elif nums[m] > n:
            binary_search(n, l, m-1, count+1)
        elif nums[m] < n:
            binary_search(n, m+1, r, count+1)


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    # M개의 탐색할 숫자
    targets = list(map(int, input().split()))
    # N개의 숫자 목록
    nums = list(map(int, input().split()))
    # 결과값들 초기값 설정
    result_num, result = 1024, 1024
    for target in targets:
        binary_search(target, 0, len(nums) - 1, 1)
    print(f'#{tc} {result_num} {result}')
