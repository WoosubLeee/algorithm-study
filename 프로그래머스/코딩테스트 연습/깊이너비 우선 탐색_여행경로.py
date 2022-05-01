from collections import defaultdict


def solution(tickets):
    paths = defaultdict(list)
    for ticket in tickets:
        paths[ticket[0]].append(ticket[1])
    for destinations in paths.values():
        destinations.sort()

    return dfs(paths, 'ICN', tickets, ['ICN'])


def dfs(paths, origin, tickets, answer):
    if len(answer) - 1 == len(tickets):
        return answer

    for i in range(len(paths[origin])):
        destination = paths[origin].pop(i)
        answer.append(destination)

        result = dfs(paths, destination, tickets, answer)
        if result:
            return result

        paths[origin].insert(i, answer.pop())


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
print(solution([["ICN", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "D"], ["D", "A"]]))