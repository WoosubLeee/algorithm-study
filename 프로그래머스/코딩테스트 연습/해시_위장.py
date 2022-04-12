# 1
from collections import Counter


def solution(clothes):
    count = Counter([type for name, type in clothes])

    answer = 1
    for type, count in count.items():
        answer *= count+1
    answer -= 1
    return answer


# # 2 원래 풀이
# from collections import defaultdict
#
#
# def solution(clothes):
#     types = defaultdict(int)
#     for cloth in clothes:
#         types[cloth[1]] += 1
#
#     answer = 1
#     for type, count in types.items():
#         answer *= count+1
#     answer -= 1
#     return answer


clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))