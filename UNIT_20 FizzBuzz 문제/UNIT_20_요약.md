# FizzBuzz 문제
FizzBuzz 문제의 규칙은 다음과 같습니다.
1. 1에서 100까지 출력
2. 3의 배수는 Fizz 출력
3. 5의 배수는 Buzz 출력
4. 3과 5의 공배수는 FizzBuzz 출력

## 정답
```python
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
```
- 공배수를 먼저 판단해야함

## 논리 연산자를 사용하지 않고 공배수 처리하기
```python
for i in range(1, 101):
    if i % 15 == 0:       # 3과 5의 최소공배수 = 15
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
```
- 실무에서는 `i % 3 == 0 and i % 5 == 0` 처럼 의미를 명확하게 드러내는 것이 좋음

## 코드 단축하기
```python
for i in range(1, 101):
    print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)
```
- 이렇게 작성하면 다른 사람이 읽기 곤란하므로 지양해야함
- `'Fizz' * (i % 3 == 0)`: i가 3의 배수이면 `(i % 3 == 0)`이 True가 되므로 해당 식은 `'Fizz'`가 된다.
- `'Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0)`: 3의 배수이면서 5의 배수인 경우, 식은 `'Fizz' + 'Buzz'`가 됨<br>
  문자열의 덧셈은 둘을 이어붙이는 것이므로 `'Fizz' + 'Buzz'` --> `'FizzBuzz'`가 됨
- `'Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i` : 파이썬의 단락 평가를 이용함. [UNIT_8_요약](https://github.com/pandasneeze/python-practice/blob/main/UNIT_08%20%EB%B6%88%EA%B3%BC%20%EB%B9%84%EA%B5%90%2C%20%EB%85%BC%EB%A6%AC%20%EC%97%B0%EC%82%B0%EC%9E%90%20%EC%95%8C%EC%95%84%EB%B3%B4%EA%B8%B0/UNIT_8_%EC%9A%94%EC%95%BD.md)<br>
3 또는 5의 배수가 아닐 경우 해당 식이 `'' or i`가 되어서 i만 출력됨
