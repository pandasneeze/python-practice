# 다음 소스 코드를 완성하여 x를 y로 나누었을 때의 몫과 나머지가 출력되게 만드세요.
x = 10
y = 3

def get_quotient_remainder(x, y):
    return x // y, x % y

quotient, remainder = get_quotient_remainder(x, y)
print('몫: {0}, 나머지: {1}'.format(quotient, remainder))