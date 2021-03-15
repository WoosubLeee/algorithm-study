def move(n, start, end, left):
    if n == 1:
        print(start, end)
    else:
        move(n-1, start, left, end)
        print(start, end)
        move(n-1, left, end, start)


def count(n):
    if n == 1:
        return 1
    else:
        return 2 ** (n-1) + count(n-1)


N = int(input())
print(count(N))
move(N, 1, 3, 2)
