N = int(input())
time = list(map(int, input().split()))
time.sort()
total = 0
for i in range(N):
    total += time[i]*(N-i)
print(total)
