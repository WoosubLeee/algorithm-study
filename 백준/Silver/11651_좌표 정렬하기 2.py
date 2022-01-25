import sys


def quick_sort(arr, start, end):
    if start < end:
        pivot = start
        l, r = start+1, end
        while l <= r:
            while l <= end and compare(arr, pivot, l):
                l += 1
            while r > start and compare(arr, r, pivot):
                r -= 1

            if l > r:
                arr[r], arr[pivot] = arr[pivot], arr[r]
            else:
                arr[l], arr[r] = arr[r], arr[l]

        quick_sort(arr, start, r-1)
        quick_sort(arr, r+1, end)


def compare(arr, is_bigger, is_smaller):
    big, small = arr[is_bigger], arr[is_smaller]
    return big[1] > small[1] or (big[1] == small[1] and big[0] > small[0])


N = int(sys.stdin.readline())
inputs = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(N)]
quick_sort(inputs, 0, N-1)

result = ''
for dot in inputs:
    result += f'{dot[0]} {dot[1]}' + '\n'
print(result.strip())