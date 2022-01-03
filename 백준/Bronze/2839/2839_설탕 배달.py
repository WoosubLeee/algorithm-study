N = int(input())
five = N // 5
three = 0
while five >= 0:
    if (N - 5*five) % 3:
        five -= 1
    else:
        three = (N - 5*five) // 3
        print(five + three)
        break
else:
    print(-1)
