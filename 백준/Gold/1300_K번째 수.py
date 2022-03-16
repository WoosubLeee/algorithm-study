def is_in_matrix(num, size):
    for i in range(1, size+1):
        if num % i == 0 and num // i <= size:
            return True
    return False


def get_index(num, size):
    return sum(min(-(-num // i) - 1, size) for i in range(1, size + 1)) + 1


N = int(input())
K = int(input())

small = 1
big = K

while small <= big:
    mid = (small + big) // 2

    count = sum(min(mid // i, N) for i in range(1, N+1))

    if count >= K:
        answer = mid
        big = mid - 1
    else:
        small = mid + 1

print(answer)