# 표준 입력으로 정수 두 개가 입력됩니다.
# (첫 번째 입력 값의 범위: 1~200, 두 번째 입력 값의 범위: 10~200이며 첫 번째 입력 값은 두 번째 입력 값보다 항상 작습니다.)
# 다음 소스 코드를 완성하여 첫 번째 정수와 두 번째 정수 사이의 숫자 중 3으로 끝나지 않는 숫자가 출력되게 만드세요.

start, stop = map(int, input().split())

i = start

while True:
    #TODO
    if i > stop:
        break
    
    if i % 10 == 3:
        i += 1
        continue
    
    print(i, end=' ')
    i += 1