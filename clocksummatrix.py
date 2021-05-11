
def rotatem(matrix,m):
    op = [[0 for x in range(m)] for y in range(m)]
    for i in range(m):
        for j in range(m):
            op[j][i] = matrix[i][j]
    for i in range(m):
        op[i] = op[i][::-1]
    return op 

def printm(matrix,msg):
    print(f'{msg}')
    for r in matrix:
        print(*r, sep = ' ')  

#input Matrix
m = int(input('M = '))
if not(2 < m < 10) or not(2 < m < 10):
    print('MATRIX SIZE OUT OF RANGE')
    exit()

matrix = [[0 for x in range(m)] for y in range(m)]
for i in range(m):
    for j in range(m):
        matrix[i][j] = int(input(f'({i},{j}): '))

#print matrix
printm(matrix,'ORGINAL MATRIX')
printm(rotatem(matrix,m), 'MATRIX AFTER ROTATION')


#print sum of corner
sum = 0
for r in range(m):
    for c in range(m):
        if r in [0, m-1] and c in [0, m-1]:
            sum += matrix[r][c]
print(f'Sum of the corner elements = {sum}')