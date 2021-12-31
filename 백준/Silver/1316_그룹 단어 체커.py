# N = int(input())
# result = 0
# for _ in range(N):
#     chars = []
#     prev = ''
#     for c in input():
#         if c != prev:
#             if c not in chars:
#                 chars.append(c)
#                 prev = c
#             else:
#                 break
#     else:
#         result += 1
# print(result)

result = 0
for _ in range(int(input())):
    word = input()
    if list(word) == sorted(word, key=word.find):
        result += 1
print(result)