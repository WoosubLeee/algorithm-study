result = []
for i in range(10):
    n = int(input())
    x = n % 42
    if x not in result:
        result.append(x)
print(len(result))