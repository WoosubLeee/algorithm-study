def solution(distance, rocks, n):
    rocks.sort()
    left, right = 1, distance // (len(rocks) - n)

    rocks.append(distance)
    while left <= right:
        mid = (left + right) // 2

        prev = 0
        count = 0
        for rock in rocks:
            if rock - prev < mid:
                count += 1
                if count > n:
                    right = mid - 1
                    break
            else:
                prev = rock
        else:
            left = mid + 1

    return right


distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2
print(solution(distance, rocks, n))