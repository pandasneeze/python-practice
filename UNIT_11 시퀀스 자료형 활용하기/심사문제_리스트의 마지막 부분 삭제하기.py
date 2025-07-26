x = input().split()

# 리스트 x의 마지막 요소 5개를 삭제한 뒤 튜플로 출력
del x[-5:]
print(tuple(x))