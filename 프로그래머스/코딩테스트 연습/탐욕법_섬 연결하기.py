def solution(n, costs):
    costs.sort(key=lambda x: x[2])

    answer = 0
    included = [False]*n
    included[costs[0][0]] = True
    included_count = 1

    while included_count < n:
        for i in range(len(costs)):
            [origin, destination, cost] = costs[i]
            if included[origin] != included[destination]:
                answer += cost
                included[origin], included[destination] = True, True
                included_count += 1
                costs.pop(i)
                break

    return answer


print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))