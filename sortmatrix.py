def input_matrix(t,r,c):
    m = [[0 for x in range(c)] for y in range(r)]
    print(f'--MATRIX {t}--')
    for i in range(r):
        for j in range(c):
            m[i][j] = int(input(f'({i+1},{j+1}): '))
    return m

def printm(m):
    print(f'--ORGINAL MARIX--')
    for r in m:
        print(*r, sep = ' ')  

m = int(input('M = '))
n = int(input('N = '))
if not(2 < m < 10) or not(2 < n < 10):
    print('MATRIX SIZE OUT OF RANGE')
    exit()


matrix = input_matrix(1, m, n)
printm(matrix)

print(f'--SORTED MARIX--')

for r in matrix:
    for c in sorted(r):
        print(c, end=' ')
    print('')  