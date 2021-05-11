def filt(para):
    op = para
    for ch in [',','!']:
        op = op.replace(ch, ' ')
    op = op.replace('?', '#')
    op = op.replace('.', '#')
    new = ''
    for word in op.split('#'):
        word = word.strip()
        new = new + word + ' '
    return new.strip()



n = int(input('Enter number of sentences: '))
if not 0 < n < 5:
    print('Invalid entry')
    exit()
para = input('ENTER SENTENCES: \n')
print(filt(para))

res = {}
wc = 0
para = filt(para)
for word in para.split(' '):
    res[word] = 0
for word in para.split(' '):
    res[word] +=1
    wc += 1

print(f'Total number of words: {wc}')       
print('WORD\tFREQUENCY')

sort_res = dict(sorted(res.items(), key=lambda item: item[1]))

for j in sort_res:
    print(f'{j}\t{sort_res[j]}')
