import sys


def dnq(r_start, c_start, n):
    isSame = True
    for i in range(n):
        for j in range(n):
            if nums[r_start + i][c_start + j] != nums[r_start][c_start]:
                isSame = False
                break
        if not isSame:
            break
    else:
        return nums[r_start][c_start]

    half = n // 2
    result = '('
    for i in range(2):
        for j in range(2):
            result += dnq(r_start + i*half, c_start + j*half, half)
    result += ')'
    return result


N = int(sys.stdin.readline())
nums = [sys.stdin.readline() for _ in range(N)]

print(dnq(0, 0, N))