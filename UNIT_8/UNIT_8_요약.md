# UNIT 8 불과 비교, 논리 연산자 알아보기
참(True), 거짓(False)을 나타내는 불(boolean)을 공부합니다.

## 비교 연산자
- >, <, >=, <=
- ==(equal), !=(not equal)
- is, is not: 객체 비교 연산자

    1 == 1.0  --> True
    1 is 1.0  --> False (둘은 다른 객체이므로)
    1 is not 1.0  --> True
    * id(): 객체의 메모리 주소를 알려줌

## 논리 연산자
- and
- or
- not

## 우선 순위
비교 연산자(부등호, is, is not) --> 논리 연산자(not, and, or)

### (참고) 단락 평가
단락 평가는 첫 번째 값만으로 결과가 확실할 때 두 번째 값은 확인하지 않는 방법이다. 파이썬에서는 단락 평가에 따라 반환 값이 달라진다. **논리 연산자는 무조건 불을 반환하지 않음**

- True and 'Python'
    'Python'
    --> 마지막으로 단락 평가를 실시한 값이 출력됨

- False and 'Python'
    False
    --> and 연산자는 하나만 거짓이어도 거짓이므로 뒤의 값인 'Python'은 확인하지 않음

- True or 'Python'
    True
    --> or 연산자는 하나만 참이어도 참이므로 뒤의 값인 'Python'은 확인하지 않음

- False or 'Python'
    Python
    --> 마지막으로 단락 평가를 실시한 값이 출력됨