isbn = input('INPUT CODE: ')
if len(isbn) != 10:
    print('INVALID INPUT')
    exit()

sum = 0
for k,dig in enumerate(reversed(isbn), start = 1):
    sum += k * int(dig)

print(f'SUM = {sum}')
if sum % 11 == 0:
    print('LEAVES NO REMAINDER – VALID ISBN CODE ')
else:
    print('LEAVES REMAINDER – INVALID ISBN CODE ')

