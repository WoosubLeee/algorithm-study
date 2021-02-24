word = input()
start = 0
result = 0
while start < len(word):
    result += 1
    if word[start:start+3] == 'dz=':
        start += 3
    elif word[start:start+2] in ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']:
        start += 2
    else:
        start += 1
print(result)
