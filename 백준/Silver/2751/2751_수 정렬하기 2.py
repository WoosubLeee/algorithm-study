N = int(input())
p_nums = [0]*1000001
n_nums = [0]*1000000
for _ in range(N):
    num = int(input())
    if num >= 0:
        p_nums[num] += 1
    else:
        n_nums[num] += 1
for i in range(-1000000, 0):
    for j in range(n_nums[i]):
        print(i)
for i in range(1000001):
    for j in range(p_nums[i]):
        print(i)
