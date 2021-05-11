n = int(input('INPUT: '))
d = len(str(n))
sq = int(n) ** 2
sq = str(sq)
rh = int(sq[-d:])
lh = int(sq[:-d])
s = rh + lh 
print(f'{n}^2 = {sq} right-hand piece of {sq} = {rh} and left hand piece of {sq} = {lh}\nSum = {rh} + {lh} = {s}, i.e. ',end ='')
print({True:'equal to the number',False: 'not equal to the number'}[s==n])
