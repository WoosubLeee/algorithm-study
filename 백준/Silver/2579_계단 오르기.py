N = int(input())
steps = [int(input()) for _ in range(N)]

if N >= 2:
    one_before = [steps[0]]
    score = [steps[1], steps[1]+steps[0]]
    for i in range(2, N):
        score, one_before = [steps[i]+max(one_before), steps[i]+score[0]], score
    print(max(score))
else:
    print(steps[0])