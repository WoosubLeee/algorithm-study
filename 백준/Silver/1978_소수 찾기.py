input()

nums = list(map(int, input().split()))
max_num = max(nums)

isPrime = [1 for _ in range(max_num+1)]
isPrime[1] = 0
for n in range(2, max_num//2 + 1):
    if isPrime[n]:
        x = 2
        while x*n <= max_num:
            isPrime[x*n] = 0
            x += 1

result = 0
for num in nums:
    if isPrime[num]:
        result += 1
print(result)