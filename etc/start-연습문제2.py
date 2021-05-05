def to_binary(n):
    output = ''
    for i in range(3, -1, -1):
        if n & (1 << i):
            output += '1'
        else:
            output += '0'
    return output


input_text = '0F97A3'

bin_num = ''
for i in input_text:
    try:
        x = int(i)
    except:
        x = ord(i) - 55
    bin_num += to_binary(x)

start = 0
while start < len(bin_num):
    number = 0
    if start < len(bin_num) - 7:
        for j in range(7):
            number += (2 ** (6 - j)) * int(bin_num[start + j])
    else:
        for j in range(len(bin_num)-start):
            number += (2 ** (len(bin_num) - start - j - 1)) * int(bin_num[start + j])
    start += 7
    print(number)
