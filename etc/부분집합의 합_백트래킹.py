def backtrack(a, k, input, target, total, left):
    if k < input:
        k += 1
        left -= arr[k]
        a[k] = True
        temp = total + arr[k]
        if temp == target:
            for j in range(1, k + 1):
                if a[j]:
                    print(arr[j], end=' ')
            print()
        elif temp < target:
            backtrack(a, k, input, target, temp, left)
        a[k] = False
        if total + left >= target:
            backtrack(a, k, input, target, total, left)


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
NMAX = len(arr) - 1
a = [0] * (NMAX+1)

backtrack(a, 0, NMAX, 10, 0, sum(arr))
