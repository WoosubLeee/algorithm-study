for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    # - 절대 겹칠 수 없는 조건 소거 -
    if (x1 > p2) or (p1 < x2) or (y1 > q2) or (q1 < y2):
        print('d')
    # - 한 점이 겹칠 조건 소거 -
    elif (x1 == p2) or (p1 == x2):
        if (y1 == q2) or (q1 == y2):
            print('c')
    # - 선분으로 겹칠 조건 소거 -
        else:
            print('b')
    elif (y1 == q2) or (q1 == y2):
        print('b')
    # - 위에 해당 되지 않으면 겹치는 부분이 직사각형 -
    else:
        print('a')