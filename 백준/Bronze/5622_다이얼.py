time = 0
nums = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
for c in input():
    for i in range(8):
        if c in nums[i]:
            time += i+3
            break
print(time)