result = 0
for i in input():
    if ord(i) < 68:
        result += 3
    elif ord(i) < 71:
        result += 4
    elif ord(i) < 74:
        result += 5
    elif ord(i) < 77:
        result += 6
    elif ord(i) < 80:
        result += 7
    elif ord(i) < 84:
        result += 8
    elif ord(i) < 87:
        result += 9
    elif ord(i) < 91:
        result += 10
print(result)
