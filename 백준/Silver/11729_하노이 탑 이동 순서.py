def move(n, now, goal, left, result):
    if n == 1:
        result[0] += 1
        result.append(f'{now} {goal}')
    else:
        move(n-1, now, left, goal, result)
        move(1, now, goal, left, result)
        move(n-1, left, goal, now, result)


result = [0]
move(int(input()), 1, 3, 2, result)
print('\n'.join(map(str, result)))