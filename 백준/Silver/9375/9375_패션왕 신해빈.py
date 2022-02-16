import sys


sys.stdin = open('input.txt', 'r')
for _ in range(int(input())):
    n = int(input())

    types = {}
    for _ in range(n):
        name, cloth_type = input().split(' ')
        if cloth_type not in types:
            types[cloth_type] = 0
        types[cloth_type] += 1

    result = 1
    for i in types.values():
        result *= (i + 1)
    print(result - 1)