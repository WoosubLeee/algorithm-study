def solution(N, number):
    dictionary = {
        1: [N]
    }

    if number == N:
        return 1

    for i in range(2, 9):
        possibles = []

        for j in range(1, i//2 + 1):
            for num_a in dictionary[j]:
                for num_b in dictionary[i-j]:
                    arr = [
                        num_a + num_b,
                        num_a - num_b,
                        num_b - num_a,
                        num_a * num_b,
                    ]
                    if num_b != 0:
                        arr.append(num_a // num_b)
                    if num_a != 0:
                        arr.append(num_b // num_a)

                    possibles.extend(arr)

        possibles.append(int(str(N) * i))

        if number in possibles:
            return i

        possibles = list(set(possibles))
        dictionary[i] = possibles
    return -1


N = 5
number = 12
print(solution(N, number))