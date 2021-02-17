str_list = list(input())
for i in range(len(str_list) // 2):
    str_list[i], str_list[-i-1] = str_list[-i-1], str_list[i]
print(''.join(str_list))
