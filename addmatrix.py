n = int(input('SIZE: '))

def input_matrix(c):
    m = [[0 for x in range(n)] for y in range(n)]
    print(f'--MATRIX {c}--')
    for i in range(n):
        for j in range(n):
            m[i][j] = int(input(f'({i+1},{j+1}): '))
    return m

def add_matrix(m1,m2):
    res = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            res[i][j] = m1[i][j] + m2[i][j]
    return res 

def printm(m,t):
    print(f'--{t} MARIX--')
    for r in m:
        print(*r, sep = ' ')  

m1 = input_matrix(1)
m2 = input_matrix(2)
res = add_matrix(m1, m2)

printm(m1, 1)
printm(m2, 2)
printm(res, 'OUTPUT')