import copy


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    # 1
    print(f'#{tc} {nums[M % N]}')

    # 2 Queue 활용
    queue = copy.deepcopy(nums)
    for i in range(M):
        queue.append(queue.pop(0))
    print(f'#{tc} {queue[0]}')
