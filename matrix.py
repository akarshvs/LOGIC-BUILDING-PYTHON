n = int(input('N = '))
if n > 10 or n < 3:
    print('SIZE OUT OF RANGE')   
    exit()

f = input('FIRST CHARACTER: ')
s = input('SECOND CHARACTER: ')
t = input('THIRD CHARACTER: ')

m = [[t for x in range(n)] for y in range(n)]

for r in range(n):
    for c in range(n):
        if r in [0, n-1] and c in [0, n-1]:
            m[r][c] = f
        elif r in [0, n-1] or c in [0, n-1]:
             m[r][c] = s

for r in m:
    print(*r, sep = ' ')


#for x in range(x,n):
    