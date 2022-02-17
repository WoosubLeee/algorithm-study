def num_count(n, divide):
    count = 0
    while n:
        n //= divide
        count += n
    return count


n, m = map(int, input().split())
if m > n/2:
    m = n - m

two = num_count(n, 2) - num_count(m, 2) - num_count(n-m, 2)
five = num_count(n, 5) - num_count(m, 5) - num_count(n-m, 5)

print(min(two, five))