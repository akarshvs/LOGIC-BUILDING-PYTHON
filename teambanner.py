n = int(input('N = '))
if not(2 < n < 9):
    print('INVALID INPUT')
    exit()

tlis = []
maxl = 0
for i in range(n):
    x = input(f'Team {i+1}: ')
    tlis.append(x)
    if len(x) > maxl:
        maxl = len(x)

res  = [[' ' for x in range(n)] for y in range(maxl)]

for i, word in enumerate(tlis):
    for j, alph in enumerate(word):
        res[j][i] = tlis[i][j]

for r in res:
    print(*r, sep = '\t')   
