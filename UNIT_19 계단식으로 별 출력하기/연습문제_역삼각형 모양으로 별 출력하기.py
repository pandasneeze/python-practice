# 다음 소스 코드를 완성하여 역삼각형 모양으로 별이 출력되게 만드세요.
for i in range(5):
    for j in range(5):
        # TODO
        if j < i:
            print(' ', end='')
        else:
            print('*', end='')
    print()