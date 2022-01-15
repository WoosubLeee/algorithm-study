N = int(input())
people = []
for _ in range(N):
    people.append(list(map(int, input().split())))
for i in people:
    rank = 1
    for j in people:
        if j[0] > i[0] and j[1] > i[1]:
            rank += 1
    print(rank, end=' ')
