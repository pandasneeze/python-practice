# UNIT 18 break, continue로 반복문 제어하기
- break: 제어 흐름 중단
- continue: 제어 흐름 유지, 코드 실행만 건너뜀
* 사용법은 C/C++과 같음

## 입력한 숫자까지 홀수 출력하기
```
count = int(input())

for i in range(count + 1):
    if i % 2 == 0:
        continue
    print(i, end = ' ')
```
***실행 결과(입력 5일 때): 1 3 5***

