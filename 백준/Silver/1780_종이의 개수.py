import sys


def dnq(r_start, c_start, n):
    for i in range(n):
        for j in range(n):
            if nums[r_start+i][c_start+j] != nums[r_start][c_start]:
                break
        else:
            continue
        break
    else:
        result[nums[r_start][c_start]] += 1
        return

    divide = n // 3
    for i in range(3):
        for j in range(3):
            dnq(r_start + i*divide, c_start + j*divide, divide)


N = int(sys.stdin.readline())
nums = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]
result = {
    -1: 0,
    0: 0,
    1: 0
}
dnq(0, 0, N)
print(*result.values(), sep='\n')