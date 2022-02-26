import sys


N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split(' ')))

stack = []
result = [-1]*N
for i in range(N):
    while stack and nums[i] > stack[-1]['num']:
        top = stack.pop()
        result[top['idx']] = nums[i]
    stack.append({
        'num': nums[i],
        'idx': i
    })
print(*result)