from sys import stdout


nums = [0]*10001
for _ in range(int(input())):
    nums[int(input())] += 1
for i in range(10001):
    for j in range(nums[i]):
        stdout.write(f'{i}\n')
