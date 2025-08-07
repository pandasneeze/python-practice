# 표준 입력으로 문자열이 입력됩니다.
# 입력된 문자열에서 'the'의 개수를 출력하는 프로그램을 만드세요.
# 단, 모든 문자가 소문자인 'the'만 찾으면 되며 'them', 'there', 'their'등은 포함하지 않아야 합니다.

import string

s = input().split()
for i in range(len(s)):
    s[i] = s[i].strip(string.punctuation)

count = 0
for i in s:
    if i == 'the':
        count += 1

print(count)