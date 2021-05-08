def is_run(n):
    if nums[n] and nums[n + 1] and nums[n + 2]:
        return True


for tc in range(1, int(input())+1):
    nums = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    # input으로 받은 숫자들을 count한다
    for num in input():
        nums[int(num)] += 1
    result = 0
    # 숫자 0~9에 대해
    for i in range(10):
        # triplet이면
        if nums[i] >= 3:
            # 해당 숫자의 count를 3 줄이고
            nums[i] -= 3
        # run이면
        elif is_run(i):
            # 3 연속 숫자의 count를 1씩 줄이고
            nums[i] -= 1
            nums[i + 1] -= 1
            nums[i + 2] -= 1
        else:
            continue
        # 다시 run과 triplet을 탐색한다
        for j in range(i, 10):
            if nums[j] >= 3 or is_run(j):
                result = 1
                break
        else:
            continue
        break
    print(f'#{tc} {result}')
