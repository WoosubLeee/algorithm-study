N = int(input())
dists = list(map(int, input().split(' ')))
prices = list(map(int, input().split(' ')))

result = 0
price = prices[0]
for i in range(N-1):
    result += dists[i]*price
    if prices[i+1] < price:
        price = prices[i+1]
print(result)