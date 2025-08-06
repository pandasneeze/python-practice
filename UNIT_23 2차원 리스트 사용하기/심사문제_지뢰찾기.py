# 표준 입력으로 2차원 리스트의 가로(col)와 세로(row)가 입력되고 그다음 줄부터 리스트의 요소로 들어갈 문자가 입력됩니다.
# 이때 2차원 리스트 안에서 *는 지뢰이고 .은 지뢰가 아닙니다. 
# 지뢰가 아닌 요소에는 인접한 지뢰의 개수를 출력하는 프로그램을 만드세요.
col, row = map(int, input().split())

matrix = []
for i in range(row):
    matrix.append(list(input()))
    
for r in range(row):
    while(1):
        count = 0
        p = matrix[r].index('.') if '.' in matrix[r] else -1 # p는 .의 열 변호
        if p == -1:
            break
        
        for i in range(r-1, r+2):
            for j in range(p-1, p+2):
                if (0 <= i < row) and (0 <= j < col): # 리스트 범위 외 참조를 방지
                    if matrix[i][j] == '*':
                        count += 1
        matrix[r][p] = count
    
for i in matrix:
    for j in i:
        print(j, end='')
    print()