N = int(input())
count = 0
for _ in range(N):
    word = input()
    chr_list = [word[0]]
    for i in range(1, len(word)):
        if word[i] == word[i-1]:
            continue
        elif word[i] in chr_list:
            break
        else:
            chr_list.append(word[i])
    else:
        count += 1
print(count)
