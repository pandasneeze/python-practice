# 다음 소스 코드를 완성하여 리스트 a에 들어있는 문자열 중에서 길이가 5인 것들만 리스트 형태로 출력되게 만드세요
# (리스트 표현식 사용)

a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']

#TODO
b = [i for i in a if len(i) == 5]

print(b)