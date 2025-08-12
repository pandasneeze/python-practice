# 다음 소스 코드를 완성하여 1부터 100까지 숫자 중 3과 5의 공배수를 세트 형태로 출력되게 만드세요.
a = {i for i in range(3, 101, 3)}
b = {i for i in range(5, 101, 5)}

print(a & b)