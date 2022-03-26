def solution(triangle):
    totals = []
    for i in range(len(triangle)):
        level = []
        for j in range(i+1):
            num = triangle[i][j]
            if i:
                left_parent = totals[i-1][j-1] if j > 0 else 0
                right_parent = totals[i-1][j] if j < i else 0

                num += max(left_parent, right_parent)
            level.append(num)
        totals.append(level)

    return max(totals[-1])


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))