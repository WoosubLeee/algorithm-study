T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    # # 1
    # matrix = [list(map(int, input().split())) for _ in range(N)]
    #
    # max_num = 0
    # for i in range(N - M + 1):
    #     for j in range(N - M + 1):
    #         sum_m = 0
    #         for m in range(M):
    #             for n in range(M):
    #                 sum_m += matrix[i+m][j+n]
    #         if sum_m > max_num:
    #             max_num = sum_m

    # # 2
    # matrix = []
    # for _ in range(N):
    #     nums = list(map(int, input().split()))
    #     line = []
    #     for i in range(N - M + 1):
    #         sum_m = 0
    #         for j in range(M):
    #             sum_m += nums[i+j]
    #         line.append(sum_m)
    #     matrix.append(line)
    #
    # max_num = 0
    # for i in range(N - M + 1):
    #     for j in range(N - M + 1):
    #         sum_m = 0
    #         for k in range(M):
    #             sum_m += matrix[j+k][i]
    #         if sum_m > max_num:
    #             max_num = sum_m
    print(f'#{tc} {max_num}')