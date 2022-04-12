# 1 정석 - 플로이드 와샬
def solution(n, results):
    versus = [[0]*(n+1) for _ in range(n+1)]
    for [a, b] in results:
        versus[a][b] = 1
        versus[b][a] = -1

    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                continue

            for k in range(1, n+1):
                if j == k or versus[j][k]:
                    continue

                if versus[j][i] == versus[i][k] == 1:
                    versus[j][k] = 1
                    versus[k][j] = -1

    answer = 0
    for v in versus:
        if v.count(0) == 2:
            answer += 1
    return answer


# # 2
# from collections import defaultdict
#
#
# def solution(n, results):
#     win, lose = defaultdict(set), defaultdict(set)
#
#     for result in results:
#         lose[result[1]].add(result[0])
#         win[result[0]].add(result[1])
#
#     for i in range(1, n + 1):
#         for winner in lose[i]:
#             win[winner].update(win[i])
#         for loser in win[i]:
#             lose[loser].update(lose[i])
#
#     answer = 0
#     for i in range(1, n+1):
#         if len(win[i]) + len(lose[i]) == n - 1:
#             answer += 1
#
#     return answer


# # 3 내 원래 풀이
# from copy import deepcopy
#
#
# def solution(n, results):
#     versus = [[0]*(n+1) for _ in range(n+1)]
#     for [a, b] in results:
#         versus[a][b] = 1
#         versus[b][a] = -1
#
#     while True:
#         previous = deepcopy(versus)
#         for i in range(1, n+1):
#             result = versus[i]
#             for j in range(1, n+1):
#                 if result[j]:
#                     for k in range(1, n+1):
#                         if versus[j][k] and k != i and not result[k]:
#                             result[k] = max(result[j]*versus[j][k], 0)*result[j]
#         if versus == previous:
#             break
#
#     result = 0
#     for v in versus:
#         if v.count(0) == 2:
#             result += 1
#     return result


n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
from pprint import pprint
pprint(solution(n, results))