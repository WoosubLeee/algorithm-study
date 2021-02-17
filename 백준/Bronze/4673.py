# 1
whole = [0]*10050
for i in range(1, 10001):
    whole[i + sum(map(int, str(i)))] = 1
for i in range(1, 10001):
    if not whole[i]:
        print(i)

# 2
# num_list = [0]*10001
# for i in range(1, 10001):
#     dn = i
#     while i:
#         dn += i % 10
#         i //= 10
#     if dn <= 10000:
#         num_list[dn] = 1
# for i in range(1, 10001):
#     if not num_list[i]:
#         print(i)
