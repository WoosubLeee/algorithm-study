'''
2 7 4 3 6
8 5 8 3 2
2 2 3 6 9
5 9 2 5 7
3 6 2 9 4
'''
arr = []
for i in range(5):
    arr.append(list(map(int, input().split())))
drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]

total_total = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        total = 0
        for delta in drc:
            if 0 <= i+delta[0] < len(arr) and 0 <= j+delta[1] < len(arr[i]):
                new_d = arr[i + delta[0]][j + delta[1]]
                total += int(((new_d - arr[i][j]) ** 2) ** 0.5)
        print(total, end=' ')
    print()
