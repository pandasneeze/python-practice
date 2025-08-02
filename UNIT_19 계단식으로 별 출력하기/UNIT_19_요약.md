# UNIT 19 계단식으로 별 출력하기
중첩 루프는 n차원 데이터를 다룰 수 있고 이미지처리, 영상 처리, 좌표계 처리 등에 주로 쓰입니다.

## 중첩 루프
```
for i in range(횟수):
    for j in range(횟수):
        가로 처리 코드
    세로 처리 코드
```
- j는 가로 방향, i는 세로 방향 

## 계단식으로 별 출력하기
```
for i in range(5):
    for j in range(5):
        if j <= i:
            print('*', end='')
    print()
```
***실행 결과***
```
*
**
***
****
*****
```
* 책에는 저렇게 나와있지만, 나는 if문을 사용하지 않고 짰다.
```
for i in range(1, 6):
    for j in range(i):
        print('*', end='')
    print()
```
책의 방법이 읽기에는 더 쉬운 것 같다.

## 대각선으로 별 출력하기
```
for i in range(5):
    for j in range(5):
        if j == i:
            print('*', end='')
        else:
            print(' ', end='')
    print()
```
***실행 결과***
```
*
 *
  *
   *
    *
```
