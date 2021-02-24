def del_overlap(word):
    fir = word[0]
    for i in range(1, len(word)):
        sec = word[i]
        if fir == sec:
            return del_overlap(word[:i-1]+word[i+1:])
        fir = sec
    return len(word)


T = int(input())

for tc in range(1, T+1):
    print(f'#{tc} {del_overlap(input())}')
