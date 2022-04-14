def solution(numbers, target):
    records = [[0]]
    for num in numbers:
        possibles = []
        for record in records[-1]:
            possibles.append(record + num)
            possibles.append(record - num)
        records.append(possibles)
    return records[-1].count(target)


numbers = [4, 1, 2, 1]
target = 4
print(solution(numbers, target))