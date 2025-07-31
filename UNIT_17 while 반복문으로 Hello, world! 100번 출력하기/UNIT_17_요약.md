# UNIT 17 whlie 반복문으로 Hello, world! 100번 출력하기
while 반복문에 대해 공부합니다. 

## while 반복문 사용하기
```
python

초기식
while 조건식:
    반복할 코드
    변화식
```
- 조건식이 True인 경우 실행
- 주로 반복 횟수가 정해지지 않은 경우 사용 (for은 반복 횟수가 정해져 있을 때 사용)
- 변화식이 없는 경우 무한루프 발생

## 난수 생성
- random 모듈을 가져와야함
`import random`
- random.random(): 실행마다 실수 난수 생성
    * 범위 지정 가능
    `random.random(a, b)   # a에서 b까지의 난수 생성(a, b도 포함)`

    