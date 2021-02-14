N = int(input())
cycle = 0

new = N
while True:
    sum_new = new // 10 + new % 10
    new = (new % 10) * 10 + sum_new % 10
    cycle += 1

    if N == new:
        break

print(cycle)