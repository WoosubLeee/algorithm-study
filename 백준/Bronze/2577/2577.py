a = int(input())
b = int(input())
c = int(input())

num = a*b*c

result = [0]*10
for i in str(num):
    result[int(i)] += 1

for i in result:
    print(i)