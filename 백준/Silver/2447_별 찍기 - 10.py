def star(n):
    if n == 1:
        return ['*']
    else:
        star_n = []
        star_n3 = star(n // 3)
        for i in range(n):
            star_n.append(star_n3[i % (n//3)] * 3)
        for i in range(n // 3):
            star_n[n//3 + i] = star_n[i][:n//3] + (' ' * (n//3)) + star_n[i][2*(n//3):]
        return star_n


N = int(input())
for i in star(N):
    print(''.join(i))
