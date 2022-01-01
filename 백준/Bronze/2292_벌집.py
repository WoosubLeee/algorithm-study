N = int(input())
x = 1
while N > 1:
    x += 1
    N -= 6*(x-1)
print(x)