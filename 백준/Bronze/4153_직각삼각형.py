while True:
    a, b, c = map(int, input().split())
    if not a:
        break

    if max(a, b, c)**2 == (a**2 + b**2 + c**2 - max(a, b, c)**2):
        print('right')
    else:
        print('wrong')