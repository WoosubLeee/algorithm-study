def binary_search(target, l, r):
    c = int((l+r)/2)
    if c == target:
        return 1
    elif c > target:
        return binary_search(target, l, c) + 1
    else:
        return binary_search(target, c, r) + 1


T = int(input())

for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    a = binary_search(A, 1, P)
    b = binary_search(B, 1, P)
    if a < b:
        print(f'#{tc} A')
    elif b < a:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')
