def solution(n, lost, reserve):
    lost_s = sorted(list(set(lost) - set(reserve)))
    reserve_s = sorted(list(set(reserve) - set(lost)))

    answer = n - len(lost_s)
    for l in lost_s:
        while reserve_s and reserve_s[0] <= l+1:
            if abs(reserve_s.pop(0) - l) <= 1:
                answer += 1
                break

    return answer


n = 5
lost = [2]
reserve = [1, 3]
print(solution(n, lost, reserve))