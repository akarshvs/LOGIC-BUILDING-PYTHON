def printm(matrix,msg):
    print(f'{msg}')
    for r in matrix:
        for c in r:
            print(f'{c: ^3}', end=' ')
        print('')  

def mirror(matrix):
    for k,r in enumerate(matrix):
        matrix[k] = matrix[k][::-1]
    return matrix

#input Matrix
m = int(input('M = '))
if not(2 < m < 20):
    print('MATRIX SIZE OUT OF RANGE')
    exit()

matrix = [[] for y in range(m)]
for i in range(m):
    matrix[i].extend(input().split(' '))

printm(matrix, 'ORGINAL MATRIX')

mir_matrix = mirror(matrix)
printm(matrix, 'MIRROR IMAGE MATRIX')
    