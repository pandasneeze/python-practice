# UNIT 16 for 반복문으로 Hello, world! 100번 출력하기
파이썬에서 for 사용법에 대해 공부합니다.

## for와 range 사용하기
- range() 안에 반복할 횟수를 입력
```
for 변수 in range(횟수):
    반복할 코드
```
- i에 range의 숫자가 하나하나씩 대입됨
```
for i in range(0, 5):
    print(i, end=' ')
```
* 실행 결과: `0 1 2 3 4`

```
for i in range(0, 10, 2):
    print(i, end=' ')
```
* 실행 결과: `0 2 4 6 8`

- ***reversed()*** 를 사용하여 내림차순으로 출력 가능
```
for i in reversed(range(0, 5)):
    print(i, end=' ')
```
* 실행 결과: `4 3 2 1 0`

## 시퀀스 객체로 반복하기
- range() 대신 시퀀스 객체를 넣어도 작동함
```
a = [0, 1, 2, 3, 4]
for i in a:
    print(i, end=' ')
```
* 실행 결과: `0 1 2 3 4`
- 튜플, 문자열도 가능
- ***reversed()*** 를 사용하여 역순으로 출력 가능
