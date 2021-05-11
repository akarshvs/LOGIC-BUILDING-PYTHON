n = int(input('N = '))
m = [[0 for x in range(n)] for y in range(n)]
for i in range(n):
    for j in range(n):
        m[i][j] = input(f'({i},{j}): ')
print('--MATRIX--')
for r in m:
    print(*r, sep = ' ')
