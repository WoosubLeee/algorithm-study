N = int(input())
# isPrime = [1 for _ in range(N+1)]
num = 2
# while True:
#     if isPrime[num]:
#         n = 2
#         while n*num <= N:
#             isPrime[n*num] = 0
#             n += 1
#
#         while True:
#             if N % num:
#                 break
#             print(num)
#             N //= num
#
#         if N == 1:
#             break
#     num += 1


while N > 1:
    while N % num == 0:
        print(num)
        N //= num
    num += 1