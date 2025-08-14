# UNIT 28 회문 판별과 N-gram 만들기
회문(palindrome): 순서를 거꾸로 읽어도 제대로 읽은 것과 같은 단어와 문장

## 회문 판별하기
### 반복문으로 문자 검사하기
```python
word = input('단어를 입력하세요: ')

is_palindrom = True
for i in range(len(word) // 2): # 0부터 문자열 길이의 절반만큼 반복
    if word[i] != word[-1 - i]: 
        is_palindrom = False
        break

print(is_palindrom)
```
- 문자열을 절반으로 나눠서 왼쪽 문자와 오른쪽 문자가 같은지 검사
- 파이썬에서 음수 인덱스를 지정하면 뒤에서부터 접근한다는 것을 이용
- 문자열 길이가 홀수인 경우 가운데 문자는 검사하지 않음

### 시퀀스 뒤집기로 문자 검사하기
```python
word = input('단어를 입력하세요: ')

print(word == word[::-1]) # 원래 문자열과 반대로 뒤집은 문자열을 비교
```
- `word[::-1]`는 인덱스를 1씩 감소시키면서 요소를 가져옴[슬라이스](https://github.com/pandasneeze/python-practice/blob/main/UNIT_11%20%EC%8B%9C%ED%80%80%EC%8A%A4%20%EC%9E%90%EB%A3%8C%ED%98%95%20%ED%99%9C%EC%9A%A9%ED%95%98%EA%B8%B0/UNIT_11_%EC%9A%94%EC%95%BD.md#%EC%8A%AC%EB%9D%BC%EC%9D%B4%EC%8A%A4 "슬라이스")

### 리스트와 reversed 사용하기
```
>>> word = 'level'
>>> list(word) == list(reversed(word))
True
```
- `list()`에 문자열을 넣으면 문자 하나하나가 리스트의 요소로 들어감

### 문자열의 join 메서드와 reversed 사용하기
```
>>> word = 'level'
>>> word == ''.join(reversed(word))
True
```
- [`join()`](https://github.com/pandasneeze/python-practice/blob/main/UNIT_24%20%EB%AC%B8%EC%9E%90%EC%97%B4%20%EC%9D%91%EC%9A%A9%ED%95%98%EA%B8%B0/UNIT_24_%EC%9A%94%EC%95%BD.md#join "join")은 구분자 문자열과 문자열 리스트의 요소를 연결함

## N-gram 만들기
- N-gram: 문자열에서 N개의 연속된 요소를 추출하는 방법
- 문자열의 처음부터 문자열의 끝까지 한 글자씩 이동하면서 N글자 추출
- 예: 'Hello'를 2-gram으로 추출
```
He
el
ll
lo
```

### 반복문으로 N-gram 출력하기
- **문자 단위 N-gram:**
```python
text = 'Hello'

for i in range(len(text) - 1):
    print(text[i], text[i + 1], sep='')
```
- 2-gram이므로 문자열의 끝에서 한 글자 앞까지만 반복
- **단어 단위 N-gram:**
```python
text = 'this is python script'
words = text.split()

for i in range(len(words) - 1):
    print(words[i], words[i + 1])
```
*결과:*
```
this is
is python
python script
```

### zip으로 2-gram 만들기
- **문자 단위:**
```python
text = 'hello'

two_gram = zip(text, text[1:])
for i in two_gram:
    print(i[0], i[1], sep='')
```
- `zip()` 함수는 반복 가능한 객체의 각 요소를 튜플로 묶어줌
- `text[1:]`은 인덱스 처음부터 마지막 문자까지 가져옴
- `list(zip(text, text[1:]))`는 `[('h', 'e'), ('e', 'l'), ('l', 'l'), ('l', 'o')]`과 같음
- **단어 단위:**
```
>>> text = 'this is python script'
>>> words = text.split()
>>> list(zip(words, words[1:]))
[('this', 'is'), ('is', 'python'), ('python', 'script')]
```
- 3-gram을 만들고 싶으면 `zip(words, words[1:], words[2:])`와 같이 하면됨

### zip과 리스트 표현식으로 N-gram 만들기
```
>>> text = 'hello'
>>> [text[i:] for i in range(3)]
['hello', 'ello', 'llo']
>>> list(zip(*['hello', 'ello', 'llo']))
[('h', 'e', 'l'), ('e', 'l', 'l'), ('l', 'l', 'o')]
```
- `zip()`은 반복 가능한 객체 여러 개를 콤마로 구분해서 넣어야함 --> 리스트 앞에 `*`를 붙이면 됨(리스트 언패킹)
- 리스트 표현식을 바로 zip에 넣어도 됨
```
>>> list(zip(*[text[i:] for i in range(3)]))
[('h', 'e', 'l'), ('e', 'l', 'l'), ('l', 'l', 'o')]
```
