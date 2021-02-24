T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    N, M = len(str1), len(str2)

    i = 0
    j = 0
    while j < N and i < M:
        if str2[i] != str1[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == N:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
