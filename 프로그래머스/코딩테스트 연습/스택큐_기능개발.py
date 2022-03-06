progresses = [93, 30, 55]
speeds = [1, 30, 5]


def solution(progresses, speeds):
    # 1
    result = []

    for p, s in zip(progresses, speeds):
        need = -((p - 100) // s)
        if len(result) == 0 or result[-1]['need'] < need:
            result.append({
                'need': need,
                'count': 1
            })
        else:
            result[-1]['count'] += 1
    return [r['count'] for r in result]

    # # 2
    # answer = []
    # completed = 0
    #
    # while completed < len(progresses):
    #     for i in range(completed, len(progresses)):
    #         progresses[i] += speeds[i]
    #     count = 0
    #     while completed != len(progresses) and progresses[completed] >= 100:
    #         count += 1
    #         completed += 1
    #     if count:
    #         answer.append(count)
    # return answer


print(solution(progresses, speeds))