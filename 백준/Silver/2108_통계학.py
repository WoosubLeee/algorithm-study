N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

total = 0
n_count = [0]*4000
p_count = [0]*4001
for i in nums:
    total += i
    if i < 0:
        n_count[i] += 1
    else:
        p_count[i] += 1
print(round(total / len(nums)))

count = 0
mode = []
mode_count = 0
for i in range(-4000, 0):
    temp_count = 0
    for j in range(n_count[i]):
        count += 1
        if count == N // 2 + 1:
            median = i
        temp_count += 1
    if temp_count > mode_count:
        mode, mode_count = [i], temp_count
    elif temp_count == mode_count:
        mode.append(i)
for i in range(4001):
    temp_count = 0
    for j in range(p_count[i]):
        count += 1
        if count == N // 2 + 1:
            median = i
        temp_count += 1
    if temp_count > mode_count:
        mode, mode_count = [i], temp_count
    elif temp_count == mode_count:
        mode.append(i)
print(median)

if len(mode) > 1:
    print(mode[1])
else:
    print(mode[0])

for i in range(-4000, 4001):
    if i < 0:
        if n_count[i]:
            min_num = i
            break
    else:
        if p_count[i]:
            min_num = i
            break
for i in range(4000, -4001, -1):
    if i >= 0:
        if p_count[i]:
            max_num = i
            break
    else:
        if n_count[i]:
            max_num = i
            break
print(max_num - min_num)
