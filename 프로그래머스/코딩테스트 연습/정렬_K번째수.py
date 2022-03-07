def solution(array, commands):
    answer = []
    for cmd in commands:
        target_arr = array[cmd[0]-1:cmd[1]]
        target_arr.sort()
        answer.append(target_arr[cmd[2]-1])
    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))