T = int(input())

for tc in range(1, T+1):
    first = input()
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # A, B 말의 현재 위치 지정
    a_gone = 1
    b_gone = 1
    # 10번 반복
    for i in range(10):
        # A부터 시작하면
        if first == 'A':
            # A를 순서에 맞게 이동시키고
            a_gone += A[i]
            # 만약 위치가 20번째 칸 이상이라면 결과를 출력하고 게임 종료
            if a_gone >= 20:
                print(f'#{tc} A')
                break
            # A가 움직임으로써 B와 위치가 같아졌다면 B를 다시 처음 위치로 보냄
            if b_gone == a_gone:
                b_gone = 1
            # A 다음으로 B에게도 똑같이 수행
            b_gone += B[i]
            if b_gone >= 20:
                print(f'#{tc} B')
                break
            if a_gone == b_gone:
                a_gone = 1
        # B부터 시작하면 위의 코드를 A와 B만 바꿔서 수행
        else:
            b_gone += B[i]
            if b_gone >= 20:
                print(f'#{tc} B')
                break
            if a_gone == b_gone:
                a_gone = 1
            a_gone += A[i]
            if a_gone >= 20:
                print(f'#{tc} A')
                break
            if b_gone == a_gone:
                b_gone = 1
    else:
        print(f'#{tc} AB')