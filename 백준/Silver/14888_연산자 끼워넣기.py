def put(num, idx):
    global max_result, min_result
    if idx == N:
        if num > max_result:
            max_result = num
        if num < min_result:
            min_result = num
    else:
        for i in range(4):
            if operators[i] > 0:
                operators[i] -= 1
                if i == 0:
                    put(num+nums[idx], idx+1)
                elif i == 1:
                    put(num-nums[idx], idx+1)
                elif i == 2:
                    put(num*nums[idx], idx+1)
                else:
                    if num >= 0:
                        put(num//nums[idx], idx+1)
                    else:
                        put(-(-num//nums[idx]), idx+1)
                operators[i] += 1


N = int(input())
nums = list(map(int, input().split(' ')))
operators = list(map(int, input().split(' ')))

max_result, min_result = -1000000000, 1000000000
put(nums[0], 1)
print(f'{max_result}\n{min_result}')