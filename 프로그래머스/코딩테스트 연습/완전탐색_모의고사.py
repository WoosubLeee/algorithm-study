def solution(answers):
    count = [0, 0, 0]
    one_answer = [1, 2, 3, 4, 5]
    two_answer = [2, 1, 2, 3, 2, 4, 2, 5]
    three_answer = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i, v in enumerate(answers):
        if one_answer[i % 5] == v:
            count[0] += 1

        if two_answer[i % 8] == v:
            count[1] += 1

        if three_answer[i % 10] == v:
            count[2] += 1

    answer = []
    max_count = max(count)
    for i, v in enumerate(count):
        if v == max_count:
            answer.append(i+1)
    return answer


answers = [1, 3, 2, 4, 2]
print(solution(answers))