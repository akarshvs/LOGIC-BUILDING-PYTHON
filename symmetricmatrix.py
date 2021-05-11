
def transm(matrix,m):
    op = [[0 for x in range(m)] for y in range(m)]
    for i in range(m):
        for j in range(m):
            op[j][i] = matrix[i][j]
    return op 

def equalm(m1, m2, m):
    for i in range(m):
        for j in range(m):
           if m1[i][j] != m2[i][j]:
               return False
    return True

def printm(matrix,msg):
    print(f'{msg}')
    for r in matrix:
        print(*r, sep = ' ')  

#input Matrix
m = int(input('M = '))
if not(2 < m < 10):
    print('MATRIX SIZE OUT OF RANGE')
    exit()

m1 = [[0 for x in range(m)] for y in range(m)]
for i in range(m):
    for j in range(m):
        m1[i][j] = int(input(f'({i},{j}): '))


printm(m1,'ORGINAL MATRIX')

m2 = transm(m1, m)

if equalm(m1, m2, m):
    print('THE GIVEN MATRIX IS SYMMETRIC')
else:
    print('THE GIVEN MATRIX IS NOT SYMMETRIC')


ld,rd = 0,0

for r in range(m):
    ld += m1[r][r]
    rd += m1[r][-(r + 1)]
        

print(f'The sum of the left diagonal = {ld}')
print(f'The sum of the right diagonal = {rd}') 
