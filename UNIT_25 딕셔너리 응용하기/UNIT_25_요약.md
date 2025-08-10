# UNIT 25 딕셔너리 응용하기
딕셔너리 메서드와 for 반복문을 사용하여 키와 값에 접근하는 법, 딕셔너리 표현식, 중첩 딕셔너리에 대해 공부합니다.
## 키워드
- [setdefault](#setdefault)
- [pop](#pop)
- [del](#del)
- [popitem](#popitem)
- [clear](#clear)
- [get](#get)
- [items](#items)
- [keys](#keys)
- [values](#values)
- [fromkeys](#fromkeys)
- [defaultdict](#참고-defaultdict-사용하기)
- [반복문](#반복문으로-딕셔너리의-키-값-출력하기)
- [표현식](#딕셔너리-표현식-사용하기)
- [중첩_딕셔너리](#중첩-딕셔너리)
- [깊은_복사](#딕셔너리의-할당과-복사)

## 딕셔너리에 키-값 쌍 추가하기
### setdefault
- `setdefault(키, 기본값)`에 키만 지정하면 값은 None이 됨
- 키와 기본값을 같이 지정하면 키-값을 저장하고 값을 반환함
- 이미 있는 키를 수정하려 해도 값은 바뀌지 않음
```
>>> x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
>>> x.setdefault('e')
>>> x
{'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': None}
>>> x.setdefault('f', 100)
100
>>> x
{'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': None, 'f': 100}
```

## 딕셔너리에서 키의 값 수정하기
### update
- `update(키=값)`은 키의 값을 수정함 **(키가 문자열일 경우에만 가능)**
- 따옴표는 빼야함
- 딕셔너리에 키가 없으면 키-값 쌍을 추가함
- 키-값 쌍 여러 개를 콤마로 구분하면 값을 한 번에 수정할 수 있음
```
>>> x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}  
>>> x.update(a=900, e=50)
>>> x
{'a': 900, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
```
- 키가 숫자일 경우에는 딕셔너리를 통째로 넣어서 수정
```
>>> y = {1: 'one', 2: 'two'}
>>> y.update({1: 'ONE', 2: 'TWO'})  
>>> y
{1: 'ONE', 2: 'TWO'}
```
- 리스트를 이용하는 방법도 가능
- `[[키1, 값1], [키2, 값2]]`형식(튜플도 같음)
```
>>> y = {1: 'one', 2: 'two'}     
>>> y.update([[1, 'ONE'], [2, 'TWO'], [3, 'THREE']]) 
>>> y
{1: 'ONE', 2: 'TWO', 3: 'THREE'}
```
- `update(반복가능한객체)`형식도 가능
- `zip([키1, 키2], [값1, 값2])`
```
>>> y
{1: 'ONE', 2: 'TWO', 3: 'THREE'}
>>> y.update(zip([1, 2], ['one', 'two']))
>>> y
{1: 'one', 2: 'two', 3: 'THREE'}
```

## 딕셔너리에서 키-값 쌍 삭제하기
### pop
- `pop(키)`는 키-값 쌍을 삭제한 뒤 값을 반환
- `pop(키, 기본값)`은 키가 있을 땐 키-값 쌍을 삭제한 뒤 원래 값 반환, 키가 없는 경우 기본값만 반환
```
>>> y
{1: 'one', 2: 'two', 3: 'THREE'}
>>> y.pop(1, 'two')
'one'
>>> y
{2: 'two', 3: 'THREE'}
>>> y.pop(4, 'four')
'four'
>>> y
```

### del
- `del 딕셔너리[키]`로 키-값 쌍 삭제 가능
```
>>> y
{2: 'two', 3: 'THREE'}
>>> del y[2]
>>> y
{3: 'THREE'}
```

### popitem
- `popitem()`은 임의의 키-값 쌍을 삭제한 뒤 삭제한 키-값 쌍을 튜플로 반환
- 파이썬 3.6 이상에서는 마지막 키-값 쌍을 삭제
```
>>> x = {'a': 90, 'b': 20, 'c': 30, 'd': 40}
>>> x.popitem()
('d', 40)
>>> x
{'a': 90, 'b': 20, 'c': 30}
```

### clear
- `clear()`는 모든 키-값 쌍 삭제
```
>>> x
{'a': 90, 'b': 20, 'c': 30}
>>> x.clear()
>>> x
{}
```

## 딕셔너리에서 키의 값을 가져오기
### get
- `get(키)`는 딕셔너리에서 키의 값을 가져옴
- `get(키, 기본값)`처럼 기본값을 지정해주면 딕셔너리에 키가 없을 때 기본값을 반환함
```
>>> x
{'a': 10, 'b': 20, 'c': 30, 'd': 40}
>>> x.get('a')
10
```

## 딕셔너리에서 키-값 쌍을 모두 가져오기
- items: 키-값 쌍을 모두 가져옴
- keys: 키를 모두 가져옴
- values: 값을 모두 가져옴

### items
- 키-값 쌍을 모두 가져옴
```
>>> x
{'a': 10, 'b': 20, 'c': 30, 'd': 40}
>>> x.items()
dict_items([('a', 10), ('b', 20), ('c', 30), ('d', 40)])
```

### keys
- 키를 모두 가져옴
```
>>> x
{'a': 10, 'b': 20, 'c': 30, 'd': 40}
>>> x.keys()
dict_keys(['a', 'b', 'c', 'd'])
```

### values
- 값을 모두 가져옴
```
>>> x
{'a': 10, 'b': 20, 'c': 30, 'd': 40}
>>> x.values()
dict_values([10, 20, 30, 40])
```

## 리스트와 튜플로 딕셔너리 만들기
### fromkeys
- 먼저 `keys = ['a', 'b', 'c', 'd']`처럼 키가 들어있는 리스트를 준비함(튜플도 가능)
- `dict.fromkeys(keys)`로 딕셔너리 생성
- 값은 모두 `None`으로 저장
- `dict.fromkeys(키 리스트, 값)`처럼 값을 지정해주면 해당 값으로 초기화 됨
```
>>> keys = ['a', 'b', 'c', 'd'] 
>>> x = dict.fromkeys(keys)
>>> x
{'a': None, 'b': None, 'c': None, 'd': None}
```
```
>>> keys = ['a', 'b', 'c', 'd']
>>> x = dict.fromkeys(keys, 100)
>>> x
{'a': 100, 'b': 100, 'c': 100, 'd': 100}
```

### (참고) defaultdict 사용하기
- 딕셔너리는 없는 키에 접근할 경우 에러 발생
- `defaultdict(기본값생성함수)`로 기본값을 정해주면 에러가 발생되지 않음
- `collections` 모듈에 들어있음
```
>>> from collections import defaultdict
>>> y = defaultdict(int)
>>> y
defaultdict(<class 'int'>, {})
>>> y['z']
0
```
- int를 넣었는데 기본값이 0인 이유: int에 아무것도 넣지 않고 호출하면 0을 반환함
```
>>> int()
0
```
- 0이 아닌 다른 값을 넣고 싶은 경우 기본값 생성함수를 만들어서 넣으면 됨
```
>>> z = defaultdict(lambda: 'python') 
>>> z['a']
'python'
```

## 반복문으로 딕셔너리의 키-값 출력하기
### 키-값 모두 출력
- 키-값 쌍을 모두 출력하려면 [items()](#items)를 사용해야함(`items()`: 키-값 쌍을 모두 가져옴)
```python
x = {'a': 10, 'b': 20, 'c': 30, 'd':40}
for key, value in x.items():
    print(key, value)
```
*결과:*
```
a 10
b 20
c 30
d 40
```
### 키만 출력
- [keys()](#keys)를 사용(`keys()`: 키를 모두 가져옴)
```python
x = {'a': 10, 'b': 20, 'c': 30, 'd':40}
for key in x.keys():
    print(key, end=' ')
```
*결과:* `a b c d`
- in 뒤에 x만 넣어도 키만 출력됨

### 값만 출력
- [values()](#values)를 사용(`values()`: 값을 모두 가져옴)
```python
x = {'a': 10, 'b': 20, 'c': 30, 'd':40}
for value in x.values():
    print(value, end=' ')
```
*결과:* `10 20 30 40`

## 딕셔너리 표현식 사용하기
- `{키: 값 for 키, 값 in 딕셔너리}`
- `dict({키: 값 for 키, 값 in 딕셔너리})`
1. 키가 들어있는 리스트 준비
2. [`dict.fromkeys()`](#fromkeys)와 `items()`로 키-값 쌍 생성(값을 지정하지 않으면 None이 됨)
3. `key: value` 다음 for 구문 작성
```
>>> keys = ['a', 'b', 'c', 'd']
>>> x = {key: value for key, value in dict.fromkeys(keys).items()}
>>> x
{'a': None, 'b': None, 'c': None, 'd': None}
```
- `keys()`로 키만 가져온 뒤 `key: value`에 특정 값을 넣거나, `values()`로 값만 가져온 뒤 값을 키로 사용할 수도 있음
```
>>> keys = ['a', 'b', 'c', 'd']
>>> {key: 0 for key in dict.fromkeys(keys).keys()}
{'a': 0, 'b': 0, 'c': 0, 'd': 0}
>>> {value: 0 for value in {'a': 10, 'b': 20, 'c': 30, 'd':40}.values()}
{10: 0, 20: 0, 30: 0, 40: 0}
```
- 키와 값의 자리를 바꿀 수 있음
```
>>> x
{'a': None, 'b': None, 'c': None, 'd': None}
>>> {value: key for key, value in x.items()}
{10: 'a', 20: 'b', 30: 'c', 40: 'd'}
```

### 표현식에서 if 사용하기
- 특정 값을 삭제할 때 유용함
- `pop()`은 특정 키를 삭제하기만 할 뿐 특정 값을 찾아 삭제할 수는 없음
- 반복문 안에 if를 넣어 삭제하면 루프 도중 딕셔너리 크기가 바뀌어 오류 발생
```python
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x = {key: value for key, value in x.items() if value != 20}
print(x)
```
*결과:* `{'a': 10, 'c': 30, 'd': 40}`

## 중첩 딕셔너리
- 딕셔너리 안에 딕셔너리가 계속 들어갈 수 있음
- `딕셔너리 = {키1: {키A: 값A}, 키2: {키B: 값B}}`
- 예: 지구형 행성의 반지름, 질량, 공전주기를 딕셔너리로 표현
```python
terrestrial_planet = {
    'Mercury': {
        'mean_radius': 2439.7,
        'mass': 3.3322E+23,
        'orbital_period': 87.969,
    },
    'Venus': {
        'mean_radius': 6051.8,
        'mass': 4.8676E+24,
        'orbital_period': 224.70069,
    },
    'Earth': {
        'mean_radius': 6371.0,
        'mass': 5.97219E+24,
        'orbital_period': 365.25641,
    },
    'Mars': {
        'mean_radius': 3389.5,
        'mass': 6.4185E+23,
        'orbital_period': 686.9600,
    }
}

print(terrestrial_planet['Venus']['mean_radius']) #6051.8
```

## 딕셔너리의 할당과 복사
- `y = x`와 같이 할당하면 얕은 복사가 일어남
- `copy()` 메서드로 깊은 복사를 해야함
```
>>> x
{'a': 0, 'b': 0, 'c': 0, 'd': 0}
>>> y = x.copy()
```

### 중첩 딕셔너리의 할당과 복사
- 중첩 딕셔너리를 깊은 복사하려면 `deepcopy()` 함수를 사용해야함
```
>>> x = {'a': {'python': 2.7}, 'b': {'python': 3.6}}
>>> import copy
>>> y = copy.deepcopy(x)
>>> y['a']['python'] = 2.8   
>>> x
{'a': {'python': 2.7}, 'b': {'python': 3.6}}
>>> y
{'a': {'python': 2.8}, 'b': {'python': 3.6}}
```