# 단어가 줄 단위로 저장된 words.txt 파일이 주어집니다.
# 다음 소스 코드를 완성하여 10자 이하인 단의의 개수가 출력되게 만드세요.

with open('words.txt', 'r') as file:
    count = 0
    lines = file.readlines()
    for i in lines:
        if len(i.strip('\n')) <= 10:
            count += 1

print(count)

# words.txt
"""
anonymously
compatibility
dashboard
experience
photography
spotlight
warehouse
"""