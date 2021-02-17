def itoa(int_input):
    result = ''
    while int_input:
        result = chr((int_input % 10) + ord('0')) + result
        int_input //= 10
    return result


print(itoa(345), type(itoa(345)))
