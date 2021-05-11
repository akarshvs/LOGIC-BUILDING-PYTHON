def input_matrix(r,c):
    m = [[0 for x in range(c)] for y in range(r)]
    for i in range(r):
        for j in range(c):
            m[i][j] = int(input(f'({i},{j}): '))
    return m

def printm(matrix,msg):
    print(f'{msg}')
    for r in matrix:
        print(*r, sep = ' ')  

def sortm(matrix):
    lis = []
    for i,r in enumerate(matrix):
        for j,c in enumerate(r):
            lis.append(matrix[i][j])
    lis = sorted(lis)
    count = 0
    for i,r in enumerate(matrix):
        for j,c in enumerate(r):
            matrix[i][j] = lis[count]
            count += 1
    return matrix  

m = int(input('M = '))
n = int(input('N = '))
if not(2 < m < 20) or not(2 < n < 20):
    print('MATRIX SIZE OUT OF RANGE')
    exit()

matrix = input_matrix(m, n)
printm(matrix,'ORGINAL MATRIX')

mine = matrix[0][0]
maxe = matrix[0][0]
minr,minc,maxr,maxc = 0,0,0,0
for i,r in enumerate(matrix):
    for j,c in enumerate(r):
        if matrix[i][j] > maxe:
            maxe = matrix[i][j]
            maxr = i
            maxc = j
        if matrix[i][j] < mine:
            mine = matrix[i][j]
            minr = i
            minc = j

print(f'LARGEST NUMBER :{maxe}\nROW = {maxr}\nCOLUMN = {maxc}\nSMALLEST NUMBER : {mine}\nROW = {minr}\nCOLUMN = {minc}\n ')
printm(sortm(matrix),'ORGINAL MATRIX')
