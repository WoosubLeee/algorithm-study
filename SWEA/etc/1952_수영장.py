# def look(start):
#     global paid, min_paid
#     if paid > min_paid:
#         return
#     for i in range(start, 12):
#         if plan[i]:
#             paid += min(plan[i]*d1, m1)
#             look(i+1)
#             paid -= min(plan[i]*d1, m1)
#             paid += m3
#             look(i+3)
#             paid -= m3
#             return
#     else:
#         if paid < min_paid:
#             min_paid = paid


T = int(input())
for tc in range(1, T+1):
    d1, m1, m3, y1 = map(int, input().split())
    plan = list(map(int, input().split()))

    # 1
    # paid, min_paid = 0, y1
    # look(0)
    # print(f'#{tc} {min_paid}')

    # 2
    min_list = [0]*15
    for i in range(12):
        if plan[i]:
            min_list[i+3] = min(min_list[i+2]+min(d1*plan[i], m1), min_list[i]+m3)
        else:
            min_list[i+3] = min_list[i+2]
    print(f'#{tc} {min(y1, min_list[-1])}')
