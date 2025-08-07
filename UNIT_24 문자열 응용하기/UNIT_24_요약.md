# UNIT 24 문자열 응용하기

## 키워드
- [replace](#replace)
- [translate](#translate)
- [split](#split)
- [join](#join)
- [upper](#upper)
- [lower](#lower)
- [lstrip](#lstrip)
- [rstrip](#rstrip)
- [strip](#strip)
- [punctuation](#참고-구두점을-간단하게-삭제하기)
- [ljust](#ljust)
- [rjust](#rjust)
- [center](#center)
- [zfill](#zfill)
- [find](#find)
- [rfind](#rfind)
- [index](#index)
- [rindex](#rindex)
- [count](#count)
- [서식지정자](#서식-지정자)
- [문자열_포매팅](#format-메서드)
## 문자열 메서드

### 문자열 바꾸기
#### replace
- **문자열**을 다른 문자열로 바꿈
- 문자열 자체는 변경하지 않고 결과만 반환
- `raplace('바꿀문자열', '새문자열')`
```
>>> '안녕 세상'.replace('세상', '파이썬')
'안녕 파이썬'
```

#### translate
- **문자**를 다른 문자로 바꿈
    1. `str.maketrans('바꿀문자', '새문자')`로 변환 테이블 생성
    2. `translate(테이블)` 사용 --> 결과 반환
- 예시: a -> 1, e -> 2, i -> 3, o -> 4, u -> 5로 변경
```
>>> table = str.maketrans('aeiou', '12345')
>>> 'apple'.translate(table)
'1ppl2'
```

### 문자열 분리하기
#### split
- `split()`은 공백을 기준으로 문자열 분리, 리스트로 만듦
```
>>> 'apple pear grape'.split()
['apple', 'pear', 'grape']
```
- `split()` 안에 값을 대입하면 기준 문자열을 지정할 수 있음
```
>>> 'apple, pear, grape'.split(', ')
['apple', 'pear', 'grape']
```

### 문자열 연결하기
#### join
- `join(리스트)`은 문자열을 연결
- 구분자를 지정하여 문자열 사이에 구분자로 연결할 수 있게 함
```
>>> ' '.join(['apple', 'pear', 'grape'])
apple pear grape
```

### 소문자 -> 대문자, 대문자 -> 소문자
#### upper
- `upper()`은 문자열을 모두 대문자로 만듦
```
>>> 'python'.upper()
'PYTHON'
```

#### lower
- `lower()`은 문자열을 모두 소문자로 만듦
```
>>> 'PYTHON'.lower()
'python'
```

### 문자 삭제하기
#### lstrip
- 왼쪽에 있는 문자를 삭제함
- 인수를 넣지 않으면 공백을 삭제함
```
>>> '    python    '.lstrip()
'python    '
```
```
>>> ', python.'.lstrip(',.')
' python.'
```

#### rstrip
- 오른쪽에 있는 문자를 삭제함
- `lstrip()`과 마찬가지로 인수를 넣지 않으면 공백을 삭제함
```
>>> '    python    '.lstrip()
'    python'
```
```
>>> ', python.'.lstrip(',.')
', python'
```

#### strip
- 양쪽의 특정 문자를 삭제함
- 인수를 넣지 않으면 공백을 삭제함
```
>>> '    python    '.lstrip()
'python'
```
```
>>> ', python.'.lstrip(',.')
' python'
```

#### (참고) 구두점을 간단하게 삭제하기
- string 모듈의 `punctuation`에는 모든 구두점이 들어있음
- `strip()` 메서드에 `string.punctuaation`을 넣으면 문자열 양쪽의 구두점을 간단하게 삭제할 수 있음
```
>>> import string
>>> ', python.'.strip(string.punctuation)
' python'
>>> string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
```
- 공백까지 삭제: `string.punctuation + ' '` 대입
- 메서드 체이닝도 가능: `.strip(string.punctuation).strip()`

### 문자열 정렬
#### ljust
- `ljust(길이)`는 문자열의 길이를 지정하고 왼쪽으로 정렬, 남은 공간을 공백으로 채움
```
>>> 'python'.ljust(10)
'python    '
```

#### rjust
- `rjust(길이)`는 문자열의 길이를 지정하고 오른쪽으로 정렬, 남은 공간을 공백으로 채움
```
>>> 'python'.ljust(10)
'    python'
```

#### center
- `center(길이)`는 문자열의 길이를 지정하고 가운데로 정렬, 남은 공간을 공백으로 채움
```
>>> 'python'.ljust(10)
'  python  '
```

### 메서드 체이닝
- 메서드를 계속 연결하여 호출할 수 있음
- 예: 문자열을 오른쪽으로 정렬 후 대문자로 바꾸기
```
>>> 'python'.rjust(10).upper()
'    PYTHON'
```

### 문자열 왼쪽에 0 채우기
#### zfill
- `zfill(길이)`는 지정된 길이에 맞춰 문자열의 왼쪽에 0을 채움
```
>>> '35'.zfill(4)
'0035'
>>> '3.5'.zfill(6)
'0003.5'
>>> 'hello'.zfill(10) 
'00000hello'
```

### 문자열 위치 찾기
#### find
- `find('찾을문자열')`은 특정 문자열을 찾아서 인덱스 반환, 없으면 -1 반환
- 왼쪽에서부터 문자열을 찾음
```
>>> 'apple pineapple'.find('pl')
2
```

#### rfind
- `find('찾을문자열')`과 달리 오른쪽에서부터 문자열을 찾음
```
>>> 'apple pineapple'.rfind('pl') 
12
```

#### index
- 왼쪽에서부터 탐색
- 문자열이 없으면 에러 발생
```
>>> 'apple pineapple'.index('pl')
2
```

#### rindex
- 오른쪽에서부터 탐색
- 문자열이 없으면 에러 발생
```
>>> 'apple pineapple'.rindex('pl')
12
```

### 문자열 개수 세기
#### count
- `count('문자열')`은 특정 문자열이 몇 번 나오는 지 알아냄
```
>>> 'apple pineapple'.count('pl')
2
```

## 서식 지정자
- %s: 문자열
- %d: 정수
- %f: 실수
```
>>> 'I am %s.' % 'james'
'I am james.'
```
- `%0길이d`: 정수를 길이에 맞춰서 출력, 나머지는 0으로 채움(예: `'%03d' % 1` --> '001')
- `%길이s`로 문자열을 오른쪽으로 정렬할 수 있음(왼쪽 정렬은 `%-길이s`)
```
>>> '%10s' % 'python'
'    python'
```
- `%.자릿수f`로 소수점 이하 자릿수를 지정할 수 있음
- 값 여러개를 넣을 땐 괄호로 묶어줌
```
>>> 'Today is %d %s.' % (3, 'April')
'Today is 3 April.'
```

## format 메서드
- `{인덱스:<채우기><정렬><길이><.자릿수><자료형>}`

### 인덱스
- format 안에 값의 순서대로 인덱스 부여됨
```
>>> 'Hello, {0} {2} {1}'.format('Python', 'Script', 3.6)
'Hello, Python 3.6 Script'
```
- 인덱스 생략 시 format에 지정된 순서대로 출력
- 인덱스 대신 이름 지정 가능
```
>>> 'Hello, {language} {version}'.format(language='Python', version=3.6)
'Hello, Python 3.6'
```
- 앞에 f를 붙여서 문자열 포매팅도 가능
```
>>> language = 'python'
>>> version = 3.6
>>> f'Hello, {language} {version}' 
'Hello, python 3.6'
```

### 정렬
- `<`: 왼쪽 정렬, `>`: 오른쪽으로 정렬

### 숫자 길이 맞추기
- `'{인덱스:0길이d}'.format(숫자)`: 숫자를 길이만큼 출력, 나머지는 0으로 채움
```
>>> '{0:03d}'.format(35)
'035'
```

### 예시
```
>>> '{0:0<10}'.format(15)
'1500000000'
>>> '{0:0>10.2f}'.format(15)
'0000015.00'
>>> '{0:>10}'.format(15)
'        15'
>>> '{0:x>10}'.format(15)
'xxxxxxxx15'
```

### (참고) 금액에서 천단위로 콤마 넣기
- `format(숫자, ',')`
```
>>> format(1493500, ',') 
'1,493,500'
```