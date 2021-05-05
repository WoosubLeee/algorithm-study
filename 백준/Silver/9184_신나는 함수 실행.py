def func(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return func(20, 20, 20)
    elif (a, b, c) in memo:
        return memo[(a, b, c)]
    else:
        if a > 20 or b > 20 or c > 20:
            memo[(a, b, c)] = func(a, b, c-1) + func(a, b-1, c-1) - func(a, b-1, c)
        else:
            memo[(a, b, c)] = func(a-1, b, c) + func(a-1, b-1, c) + func(a-1, b, c-1) - func(a-1, b-1, c-1)
        return memo[(a, b, c)]


memo = {}
a, b, c = map(int, input().split())
while (a, b, c) != (-1, -1, -1):
    print(f'w({a}, {b}, {c}) = {func(a, b, c)}')
    a, b, c = map(int, input().split())
