word = input()

char_dict = {}
for i in word:
    order = ord(i)
    if order >= 97:
        order -= 32
    if order in char_dict:
        char_dict[order] += 1
    else:
        char_dict[order] = 1

max_count = 0
max_char = ''
same = False

for i in char_dict.keys():
    if char_dict[i] > max_count:
        max_count = char_dict[i]
        max_char = chr(i)
        same = False
    elif char_dict[i] == max_count:
        same = True
if same:
    print('?')
else:
    print(max_char)
