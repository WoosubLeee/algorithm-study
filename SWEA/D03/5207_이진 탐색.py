def binary_search(num_list, target):
    low, high = 0, len(num_list) - 1
    prior = 'first'
    while low <= high:
        mid = (low + high) // 2
        if num_list[mid] == target:
            return True
        elif num_list[mid] > target and prior in ('first', 'right'):
            prior = 'left'
            high = mid - 1
        elif num_list[mid] < target and prior in ('first', 'left'):
            prior = 'right'
            low = mid + 1
        else:
            return False


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    nums_a = list(map(int, input().split()))
    nums_a.sort()
    count = 0
    for num in list(map(int, input().split())):
        if binary_search(nums_a, num):
            count += 1
    print(f'#{tc} {count}')
