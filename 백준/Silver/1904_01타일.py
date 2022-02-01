N = int(input())

prev = 1
result = 1
for _ in range(2, N+1):
    result, prev = (result+prev) % 15746, result
print(result)