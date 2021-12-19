import sys


max_num = 0
max_order = 0
for i in range(1, 10):
    num = int(sys.stdin.readline())
    if num > max_num:
        max_num, max_order = num, i
print(max_num, max_order,sep='\n')