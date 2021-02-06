str = input()

for i in str:
    num = ord(i)
    if 97 <= num <= 122:
        print(chr(num - 32), end='')
    else:
        print(i, end='')