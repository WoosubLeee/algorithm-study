import sys


# # 분할정복
# def calc_mid_area(left, mid, right):
#     height = line[mid]
#     result = height
#     l, r = mid, mid
#     while l >= left and r <= right:
#         l_height = line[l-1] if l > left else 0
#         r_height = line[r+1] if r < right else 0
#
#         if l_height >= r_height:
#             l -= 1
#             height = min(height, l_height)
#         else:
#             r += 1
#             height = min(height, r_height)
#
#         result = max(result, height * (r-l+1))
#
#     return result
#
#
# def dnq(left, right):
#     if left == right:
#         return line[left]
#
#     mid = (right+left) // 2
#     return max(dnq(left, mid), calc_mid_area(left, mid, right), dnq(mid+1, right))
#
#
# while True:
#     line = list(map(int, sys.stdin.readline().split(' ')))
#     if len(line) == 1:
#         break
#
#     print(dnq(1, line[0]))


# 스택
import sys


while True:
    line = list(map(int, sys.stdin.readline().split(' ')))
    if len(line) == 1:
        break

    histogram = line[1:]

    result = 0
    histogram.insert(0, -1)
    histogram.append(0)
    stack = [0]
    for i in range(1, len(histogram)):
        height = histogram[i]

        while histogram[stack[-1]] >= height:
            top = stack.pop()
            width = i - stack[-1] - 1

            result = max(result, histogram[top]*width)

        stack.append(i)

    print(result)