N = int(input())
counts = [1]*10
for _ in range(1, N):
    new_counts = []

    new_counts.append(counts[1])
    for i in range(1, 9):
        new_counts.append(counts[i-1] + counts[i+1])
    new_counts.append(counts[8])

    counts = new_counts
print(sum(counts[1:]) % 1000000000)