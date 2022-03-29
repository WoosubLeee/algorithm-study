import sys


N = int(sys.stdin.readline())
weights = list(map(int, sys.stdin.readline().split()))
K = int(sys.stdin.readline())
balls = list(map(int, sys.stdin.readline().split()))

possibles = {0}
for weight in weights:
    new_possibles = set()
    for possible in possibles:
        new_possibles.add(possible + weight)
        new_possibles.add(abs(possible - weight))
    possibles.update(new_possibles)

result = ['Y' if ball in possibles else 'N' for ball in balls]
print(*result)