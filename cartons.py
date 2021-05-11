xl, l, m , s, j =  0,0,0,0,0

nb = int(input('N = '))
if not 0 < nb < 1000:
    print('INVALID INPUT')
    exit()
b = nb
while nb > 0:
    if nb >= 48:
        xl += 1
        nb -= 48
    elif nb >= 24:
        l += 1
        nb -= 24
    elif nb >= 12:
        m += 1
        nb -= 12
    else:
        if nb < 6:
            j += 1
            break 
        s += 1
        nb -= 6

if xl > 0:
    print(f'48 X {xl} = {48 * xl}')
if l > 0:
    print(f'24 X {l} = {24 * l}')
if m > 0:
    print(f'12 X {m} = {12 * m}')
if s > 0:
    print(f'6 X {s} = {6 * s}')
if j:
    print(f'Remaining boxes {nb} X 1 = {nb}')
else:
    print('Remaining boxes = 0')

print(f'Total number of boxes = {b}\nTotal number of cartons = {xl + l + m + s + j}')

