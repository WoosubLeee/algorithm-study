string = input()
count = 0
for i in range(len(string)):
    if string[i] != ' ' and (i == 0 or string[i-1] == ' '):
        count += 1
print(count)
