import math
from itertools import permutations


def solution(numbers):
    nums = set()
    for n in range(1, len(numbers)+1):
        nums |= set(map(int, map(''.join, permutations(numbers, n))))

    max_num = max(nums)
    max_check = math.ceil(max_num ** 0.5)
    primes = [True]*(max_num+1)
    primes[0], primes[1] = False, False

    for i in range(2, max_check+1):
        if primes[i]:
            multiply = 2
            while multiply*i <= max_num:
                primes[multiply*i] = False
                multiply += 1

    answer = 0
    for num in nums:
        if primes[num]:
            answer += 1

    return answer


numbers = "1124"
print(solution(numbers))