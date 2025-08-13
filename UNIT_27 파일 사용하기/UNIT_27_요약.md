# UNIT 27 파일 사용하기
파일에서 문자열을 읽고 쓰는 법과 파이썬 객체를 파일에 읽고 쓰는 법을 공부합니다.

## 파일에 문자열 쓰기, 읽기
### 쓰기
- `open()`으로 파일을 열어서 파일 객체를 얻은 뒤에 `write()` 메서드 사용
- `open()` 함수 안에 파일 모드는 'w'(write)로 지정
- 열기: `파일객체 = open(파일 이름, 파일 모드)`
- 쓰기: `파일객체.write('문자열')`
- 닫기: `파일객체.close()`
```python
file = open('hello.txt', 'w') # w: 쓰기 모드
file.write('hello, world')
file.close()
```
### 읽기
- `open()`으로 파일을 열어서 파일 객체를 얻은 뒤에 `read()` 메서드 사용
- `open()` 함수 안에 파일 모드는 'r'(read)로 지정
- 읽기: `변수 = 파일객체.read()`
```python
file = open('hello.txt', 'r') # r: 읽기 모드
s = file.read()
print(s)
file.close()
```

### 자동으로 파일 객체 닫기
- `with as`를 사용하면 파일을 사용한 뒤 자동으로 파일 객체를 닫을 수 있음
```python
with open(파일이름, 파일모드) as 파일객체:
    코드
```
```python
with open('hello.txt', 'r') as file:
    s = file.read()
    print(s)
```

## 문자열 여러 줄을 파일에 쓰기
### 반복문으로 쓰기
```python
with open('hello.txt', 'w') as file:
    for i in range(3):
        file.write('hello, world {0}\n'.format(i))
```
[format_메서드](https://github.com/pandasneeze/python-practice/blob/main/UNIT_24%20%EB%AC%B8%EC%9E%90%EC%97%B4%20%EC%9D%91%EC%9A%A9%ED%95%98%EA%B8%B0/UNIT_24_%EC%9A%94%EC%95%BD.md#format-%EB%A9%94%EC%84%9C%EB%93%9C "format 메서드")
* *결과:*
```hello.txt
hello, world 0
hello, world 1
hello, world 2
```

### 리스트 안의 문자열을 파일에 쓰기
- `파일객체.writelines(문자열리스트)`
```python
lines = ['안녕하세요. \n', '파이썬\n', '코딩 도장입니다.\n']

with open('hello.txt', 'w') as file:
    file.writelines(lines)
```
### 파일의 내용을 한 줄씩 리스트로 가져오기
- `readlines()` 메서드는 파일에서 문자열을 한 줄씩 읽어서 리스트 형태로 가져옴
```python
with open('hello.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
```
* *결과:* `['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']`

### 파일의 내용을 한 줄씩 읽기
- `변수 = 파일객체.readline()`
-  `readline()`은 더 이상 읽을 줄이 없을 때 빈 문자열 반환 -> while의 조건을 `line != ''`로 해야함
- line을 None으로 초기화하지 않고 사용하면 while에서 없는 변수와 빈 문자열 `''`을 비교하게 됨 --> 에러 발생
```python
with open('hello.txt', 'r') as file:
    line = None
    while line != '':
        line = file.readline()
        print(line.strip('\n')) # 파일에서 읽어온 문자열에 이미 \n가 포함되어 있으므로 제거하지 않으면 두 번 줄바꿈 됨
```

### for 반복문으로 파일을 줄 단위로 읽기
- for 반복문에 파일 객체를 지정하면 한 줄씩 읽어서 변수에 저장됨
```python
with open('hello.txt', 'r') as file:
    for line in file:
        print(line.strip('\n'))
```

### (참고) 파일 객체는 이터레이터
- 파일 객체는 이터레이터이므로 언패킹이 가능함
- 예: 'hello.txt'
```
hello 
world
```
```python
with open('hello.txt', 'r') as file:
    a, b = file
    print(a.strip('\n'), b)
```
* *결과:* `hello world`

## 파이썬 객체를 파일에 저장하기, 가져오기
- 피클링(pickling): 파이썬 객체를 파일에 저장하는 과정
- 언피클링(uppickling): 파일에서 객체를 읽어오는 과정

### 파이썬 객체를 파일에 저장하기
- `pickle` 모듈의 `dump` 메서드 사용
- 파일 모드는 'wb'(바이너리 쓰기 모드)로 지정
```python
import pickle

name = 'james'
age = 17
address = '서울시 서초구 반포동'
scores = {'korean': 90, 'english': 95, 'mathmatics': 85, 'science': 82}

with open('james.p', 'wb') as file:
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)
```

### 파일에서 파이썬 객체 읽기
- `pickle` 모듈의 `load` 메서드 사용
- 언피클링할 때는 파일 모드를 'rb'(바이너리 읽기 모드)로 지정
- 저장한 순서대로 가져오게 됨
```python
import pickle

with open('james.p', 'rb') as file:
    name = pickle.load(file)
    age = pickle.load(file)
    address = pickle.load(file)
    scores = pickle.load(file)
    print(name, age, address, scores, sep='\n')
```
