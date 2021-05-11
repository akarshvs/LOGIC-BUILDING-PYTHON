#rot13
flis = 'abcdefghijklm'
slis = 'nopqrstuvwxyz'

#encrypt alph 'a'
def encrypt(a):
    org = a
    a = a.lower()
    if a in flis:
        indx = flis.find(a)
        e = slis[indx]
    elif a in slis:
        indx = slis.find(a)
        e = flis[indx]
    else:
         return org
    if org.isupper():
        return e.upper()
    else:
        return e

#input & display
sent = input()
if not 3 < len(sent) < 100:
    print('INVALID LENGTH')
    exit()
    
print('The cipher text is:')
for word in sent:
    for a in word:
        print(encrypt(a), end='')

