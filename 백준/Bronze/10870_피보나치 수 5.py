def fibo(num):
    if num <= 1:
        return num
    else:
        return fibo(num-1) + fibo(num-2)


n = int(input())
print(fibo(n))
