# 표준 입력으로 양의 정수 두 개가 입력됩니다. 
# 다음 소스 코드를 완성하여 두 숫자의 공약수를 세트 형태로 구하도록 만드세요.
# 단, 최종 결과는 공약수의 합으로 판단합니다.

x, y = map(int, input().split())

a = {i for i in range(1, x + 1) if x % i == 0}
b = {i for i in range(1, y + 1) if y % i == 0}
divisor = a & b

result = 0
if type(divisor) == set:
    result = sum(divisor)
    
print(result)