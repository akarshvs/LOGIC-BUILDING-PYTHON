n = int(input('N = '))
if not(2 < n < 10):
    print('MATRIX SIZE OUT OF RANGE')
    exit()

slis = [int(x) for x in input('ENTER ELEMENTS OF SINGLE DIMENSIONAL ARRAY:').split(' ')]
s_slis = sorted(slis)
print('SORTED ARRAY:',end =' ')
print(*s_slis,sep=' ')
m = []
for r in range(n):
    m.append(s_slis[:n-r] + s_slis[:r])
print('FILLED MATRIX')
for r in range(n):
    for c in range(n):
        print(m[r][c],end=' ')
    print('')