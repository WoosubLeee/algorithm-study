def compare(bin_i, ter_i):
    bin_dec, ter_dec = 0, 0
    bin_len, ter_len = 1, 1
    while bin_i:
        bin_dec += (bin_i % 10) * bin_len
        bin_i //= 10
        bin_len *= 2
    while ter_i:
        ter_dec += (ter_i % 10) * ter_len
        ter_i //= 10
        ter_len *= 3
    if bin_dec == ter_dec:
        return bin_dec


ter_nums = ['0', '1', '2']
for tc in range(1, int(input())+1):
    binary = input()
    ternary = input()

    for i in range(len(binary)):
        if binary[i] == '0':
            new_binary = binary[:i] + '1' + binary[i+1:]
        else:
            new_binary = binary[:i] + '0' + binary[i+1:]
        for j in range(len(ternary)):
            for num in ter_nums:
                if num != ternary[j]:
                    new_ternary = ternary[:j] + num + ternary[j+1:]
                    result = compare(int(new_binary), int(new_ternary))
                    if result:
                        print(f'#{tc} {result}')
                        break
            if result:
                break
        if result:
            break
