# UNIT 31 함수에서 재귀호출 사용하기
- 파이썬에서 최대 재귀 깊이는 1000임, 초과하면 RecursionError 발생

## 재귀호출로 팩토리얼 구하기
```python
def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n - 1)

print(factorial(5))
```
*결과:* `120`