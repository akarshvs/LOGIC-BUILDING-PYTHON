def odd_encrypt(a):
    key = 'abcdefghijklmnopqrstuvwxyzab'
    if a.lower() in key:
        indx = key.find(a.lower())
        return key[indx + 2].upper()
    else:
        return a

n = int(input('n = '))
if not 1 < n < 10:
    print('INVALID ENTRY')
    exit()
sarray = []
for i in range(n):
    sarray.append(input())

#encrypt
for k,sentence in enumerate(sarray,start = 1):
    sentence = sentence[:-1]
    op = ''
    if k%2 == 1:
        for word in sentence.split(' '):
            for alph in word:
                op = op + odd_encrypt(alph)
            op = op + ' '
    else:
         for word in reversed(sentence.split(' ')):
             op = op +' '+ word
    sarray[k-1] =  op.strip() + '.'


#output
print('OUTPUT: ')
for sentence in sarray:
    print(sentence)
