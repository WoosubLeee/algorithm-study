# 1
# N = int(input())
# people = [[] for _ in range(201)]
# for _ in range(N):
#     person = list(sys.stdin.readline().split())
#     people[int(person[0])].append(person[1])
# for i in range(201):
#     for j in people[i]:
#         print(i, j)

# 2
people = (input() for _ in range(int(input())))
print(*sorted(people, key=lambda person: int(person.split()[0])), sep='\n')
