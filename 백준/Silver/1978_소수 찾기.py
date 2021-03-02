N = int(input())
nums = list(map(int, input().split()))
count = 0
for num in nums:
    if num == 1 or (num != 2 and num % 2 == 0):
        continue
    for i in range(1, num // 4):
        if not num % (2*i + 1):
            break
    else:
        count += 1
print(count)
