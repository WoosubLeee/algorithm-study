import sys


N = int(sys.stdin.readline())
counts = [0]*10001

for i in range(N):
    counts[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
    for _ in range(counts[i]):
        print(i)
