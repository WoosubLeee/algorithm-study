def calc(n):
    global result, max_result, min_result
    if n == N:
        if result > max_result:
            max_result = result
        if result < min_result:
            min_result = result
    else:
        for i in range(4):
            if opers[i]:
                opers[i] -= 1
                temp = result
                if i == 0:
                    result += nums[n]
                elif i == 1:
                    result -= nums[n]
                elif i == 2:
                    result *= nums[n]
                else:
                    if result < 0:
                        result = -(-result // nums[n])
                    else:
                        result //= nums[n]
                calc(n + 1)
                opers[i] += 1
                result = temp


N = int(input())
nums = list(map(int, input().split()))
opers = list(map(int, input().split()))

result, max_result, min_result = nums[0], -1000000000, 1000000000
calc(1)
print(max_result)
print(min_result)
