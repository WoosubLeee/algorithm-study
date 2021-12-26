def isHansu(num):
    num_str = str(num)
    for i in range(1, len(num_str)-1):
        if int(num_str[i]) - int(num_str[i-1]) != int(num_str[i+1]) - int(num_str[i]):
            return False
    return True


N = int(input())

result = 0
for i in range(1, N+1):
    if isHansu(i):
        result += 1
print(result)