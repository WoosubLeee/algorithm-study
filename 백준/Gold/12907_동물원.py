N = int(input())
ranks = list(map(int, input().split()))
counts = [0]*41
for rank in ranks:
    counts[rank] += 1

if 0 < counts[0] <= 2:
    cases = 2
    for i in range(1, 42):
        if counts[i] > counts[i-1]:
            cases = 0
            break
        elif counts[i] == 2 or (counts[i] == 1 and counts[i-1] == 2):
            cases *= 2
else:
    cases = 0
print(cases)
