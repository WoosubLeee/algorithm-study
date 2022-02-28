participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]


def solution(participant, completion):
    participants, completions = {}, {}
    hash()
    for p in participant:
        if p in participants:
            participants[p] += 1
        else:
            participants[p] = 1
    for p in completion:
        if p in completions:
            completions[p] += 1
        else:
            completions[p] = 1

    for p, count in participants.items():
        if p not in completions or count != completions[p]:
            return p

print(solution(participant, completion))