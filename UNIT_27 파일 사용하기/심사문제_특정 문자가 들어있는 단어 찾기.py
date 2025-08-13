# 문자열이 저장된 words.txt 파일이 주어집니다(문자열은 한 줄로 저장되어 있습니다). 
# words.txt 파일에서 문자 c가 포함된 단어를 각 줄에 출력하는 프로그램을 만드세요.
# 단어를 출력할 때는 등장한 순서대로 출력해야하며 ,와 .은 출력하지 않아야 합니다.

with open('words.txt', 'r') as file:
    line = file.readline()
    words = line.split()
    
for i in words:
    word = i.strip(',.')
    if word.count('c'):
        print(word)