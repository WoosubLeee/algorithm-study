def one_to_ten(n):
    if n == 1:
        return 1
    return n + one_to_ten(n-1)


print(one_to_ten(10))
