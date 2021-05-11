

def input_matrix(t,r,c):
    m = [[0 for x in range(c)] for y in range(r)]
    print(f'--MATRIX {t}--')
    for i in range(r):
        for j in range(c):
            m[i][j] = int(input(f'({i+1},{j+1}): '))
    return m


def printm(m,t):
    print(f'--{t} MARIX--')
    for r in m:
        print(*r, sep = ' ')  

r1 = int(input('ROW SIZE 1st MATRIX: '))
c1 = int(input('COL SIZE 1st MATRIX: '))
m1 = input_matrix(1, r1, c1)
r2 = int(input('ROW SIZE 2nd MATRIX: '))
c2 = int(input('COL SIZE 2nd MATRIX: '))
m2 = input_matrix(2, r2, c2)

def mul_matrix(m1, m2):
    try:
        res = [[0 for x in range(c2)] for y in range(r1)]
        for i in range(r1):
            for j in range(c2):
                for k in range(r2):
                    res[i][j] += m1[i][k] * m2[k][j]
        return res
    except:
        print("NO ANSWER")
        exit()

printm(m1, 1)
printm(m2, 2)
res = mul_matrix(m1, m2)
printm(res, 'OUTPUT')