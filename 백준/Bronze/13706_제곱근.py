N = int(input())

if N == 0:
    result = 0
else:
    length = len(str(N))
    for i in range(length//2, length//2):
        if i ** 2 == N:
            result = i
            break
print(result)
