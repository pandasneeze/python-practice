# UNIT 30 함수에서 위치 인수와 키워드 인수 사용하기
위치 인수, 키워드 인수와 리스트, 딕셔너리 언패킹을 활용하는 방법을 공부합니다.

## 위치 인수
- 위치 인수(positional argument): 함수에 인수를 순서대로 넣는 방식(인수의 위치가 정해져 있음)
  * 예: 숫자를 넣은 순서대로 출력되는 함수
  ```python
  def print_numbers(a, b, c):
    print(a)
    print(b)
    print(c)
  ```

## 언패킹 
- 인수를 순서대로 넣을 때는 리스트나 튜플 사용 가능, 리스트 또는 튜플 앞에 *을 붙여 사용
```python
x = [10, 20, 30]
print_numbers(*x)
```
- 리스트(튜플) 앞에 *을 붙이면 언패킹 됨
- 리스트 바로 앞에 *을 붙여도 됨: `*[10, 20, 30]`
- 이 때 리스트의 요소 개수와 매개변수 개수는 같아야함

## 가변 인수 함수
- 가변 인수(variable argument): 인수의 개수가 정해지지 않음
- 가변 인수 함수는 매개변수 앞에 *을 붙여 만듦
```python
def 함수이름(*매개변수):
    코드
```
- 예: 숫자 여러 개를 받고 숫자를 각 줄에 출력하는 함수
```python
def print_numbers(*args):
    for i in args:
        print(i)
```
- *(참고)* 고정 인수와 가변 인수를 함께 사용하기
  * 고정 매개변수를 먼저 지정, 그 다음 매개변수에 *를 붙여줌(가변 인수는 반드시 마지막에 와야함)
  ```python
  def print_numbers(a, *args):
    print(a)
    print(args)
  ```

## 키워드 인수
- 키워드 인수(keyword argument): 인수에 이름을 붙이는 기능, `키워드=값` 형식으로 사용
- 인수의 용도가 명확하게 보임, 순서를 기억하지 않아도 됨
- print함수에서의 sep, end도 키워드 인수임
- 예: 개인 정보를 출력하는 함수
```python
def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')
```
*결과:*<br>
```
이름: 홍길동
나이: 30
주소: 서울시 용산구 이촌동
```

## 키워드 인수와 딕셔너리 언패킹
- 딕셔너리 언패킹은 딕셔너리 앞에 **를 붙여 사용
- 예: 개인 정보를 출력하는 함수에 딕셔너리 언패킹 사용
```python
def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info(**x) 
```
*결과:*<br>
```
이름: 홍길동
나이: 30
주소: 서울시 용산구 이촌동
```
- 딕셔너리 바로 앞에 **붙여도 됨 `**{딕셔너리}`

## *을 두 번 붙이는 이유
- 딕셔너리 앞에 *을 하나만 붙이면 x의 키만 사용됨
```
>>> x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
>>> personal_info(*x)
이름:  name
나이:  age
주소:  address
```
- 값을 사용하려면 딕셔너리를 두 번 언패킹 해야함

## 키워드 인수를 사용하는 가변 인수 함수 만들기
```python
def 함수이름(**매개변수):
    코드
```
- 예: 값 여러 개를 받아서 매개변수 이름과 값을 각 줄에 출력하는 함수
```python
def personal_info(**kwargs):
    for kw, arg in kwargs.items():
        print(kw, ': ', arg, sep='')
```
[items()](https://github.com/pandasneeze/python-practice/blob/main/UNIT_25%20%EB%94%95%EC%85%94%EB%84%88%EB%A6%AC%20%EC%9D%91%EC%9A%A9%ED%95%98%EA%B8%B0/UNIT_25_%EC%9A%94%EC%95%BD.md#items "UNIT 25 딕셔너리 응용하기")
- 값을 직접 넣어서 실행:
```
>>> personal_info(name='홍길동')
name: 홍길동
>>> personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동') 
name: 홍길동
age: 30
address: 서울시 용산구 이촌동
```
- 딕셔너리 언패킹 사용:
```
>>> x = {'name': '홍길동'}
>>> personal_info(**x)
name: 홍길동
>>> y = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
>>> personal_info(**y)
name: 홍길동
age: 30
address: 서울시 용산구 이촌동
```
- 보통 `**kwargs`를 사용한 가변 인수 함수는 함수 안에서 해당 키가 있는 지 확인한 뒤 해당 기능을 만듦
```python
def personal_info(**kwargs):
    if 'name' in kwargs: # in으로 딕셔너리 안에 특정 키가 있는 지 확인
        print('이름: ', kwargs['name'])
    if 'age' in kwargs:
        print('나이: ', kwargs['age'])
    if 'address' in kwargs:
        print('주소: ', kwargs['address'])
```
- 마찬가지로 고정 인수와 함께 사용할 때는 고정 인수를 먼저 지정하고 마지막에 가변 인수를 지정해야함<br>
### *(참고)* 위치 인수와 키워드 인수 함께 사용하기
- 위치 인수와 키워드 인수를 함께 사용하는 함수는 `print()`가 있음(출력 값은 위치 인수, sep, end 등은 키워드 인수)
- 예:
```python
def custom_print(*args, **kwargs):
    print(*args, **kwargs)

custom_print(1, 2, 3, sep=':', end='')
```
*결과:* `1:2:3`
- `*args`가 `**kwargs`보다 앞에 와야함
- 고정 매개변수와 함께 사용 시 `def custom_print(a, b, *args, **kwagrs):`처럼<br>
고정 매개변수 --> *args --> **kwargs 순으로 지정

## 매개변수에 초깃값 지정
```python
def personal_info(name, age, address='비공개'):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)
```
- address를 비워두고 호출 시 비공개가 대입됨
- 초깃값이 지정된 매개변수는 초깃값이 없는 매개변수보다 뒤에 와야함
