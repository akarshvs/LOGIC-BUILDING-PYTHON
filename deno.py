def text(n):
    op = ''
    convert={1:'ONE',2:'TWO',3:'THREE',4:'FOUR',5:'FIVE',6:'SIX',7:'SEVEN',8:'EIGHT',9:'NINE',0:'ZERO'}
    for dig in str(n):
        op = op + convert[int(dig)] + ' '
    return op.strip()


n = int(input('INPUT: '))
if not 0 < n < 100000:
    print('INVALID INPUT')
    exit()

note_count = 0
n_copy = n
print(f'OUTPUT: {text(n_copy)}')


print('DENOMINATION: ')
if n >= 1000:
    temp = n // 1000
    note_count += temp
    print(f'1000 X {temp} = {1000 * temp}')
    n = n % 1000
if n >= 500:
    temp = n // 500
    note_count += temp
    print(f'500 X {temp} = {500 * temp}')
    n = n % 500
if n >= 100:
    temp = n // 100
    note_count += temp
    print(f'100 X {temp} = {100 * temp}')
    n = n % 100
if n >= 50:
    temp = n // 50
    note_count += temp
    print(f'50 X {temp} = {50 * temp}')
    n = n % 50
if n >= 20:
    temp = n // 20
    note_count += temp
    print(f'20 X {temp} = {20 * temp}')
    n = n % 20
if n >= 10:
    temp = n // 10
    note_count += temp
    print(f'10 X {temp} = {10 * temp}')
    n = n % 10
if n >= 5:
    temp = n // 5
    note_count += temp
    print(f'5 X {temp} = {5 * temp}')
    n = n % 5
if n >= 2:
    temp = n // 2
    note_count += temp
    print(f'2 X {temp} = {2 * temp}')
    n = n % 2
if n == 1:
    note_count += 1
    print(f'1 X 1 = 1')

print(f'TOTAL = {n_copy}')
print(f'TOTAL NUMBER OF NOTES = {note_count}')
