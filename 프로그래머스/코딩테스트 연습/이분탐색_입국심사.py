def solution(n, times):
    short = (n // len(times)) * min(times)
    long = (n // len(times)) * max(times)

    while short <= long:
        mid = (short + long) // 2

        if check(mid, times, n):
            long = mid - 1
        else:
            short = mid + 1

    return long + 1


def check(limit, times, target):
    total = sum(limit // time for time in times)
    return total >= target


n = 6
times = [7, 10]
print(solution(n, times))