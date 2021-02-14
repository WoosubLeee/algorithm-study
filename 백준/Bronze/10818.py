N = int(input())
min_val = 1000000
max_val = -1000000

n_list = list(map(int, input().split()))
for n in n_list:
    if n < min_val:
        min_val = n
    if n > max_val:
        max_val = n
print(min_val, max_val)