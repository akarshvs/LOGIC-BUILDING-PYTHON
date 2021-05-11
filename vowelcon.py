#check given alph is vowel or cons
def vow(a):
    v = 'aeiou' 
    if a.lower() in v:
        return 'v'
    elif a in '? .':
        return 'b'
    else:
        return 'c'

sent = input('')
if sent[-1] not in '?.':
    print('Invalid Input')
    exit()

print(sent.title())
print('Word\t\tVowels\t\tConsonants')
for word in sent.split(' '):
    vc,cc = 0,0
    word = word.replace('.', '')
    word = word.replace('?', '')
    for letter in word:
        x = vow(letter)
        if x == 'v':
            vc+=1
        elif x == 'c':
            cc+=1
        else:
            pass
    print(f'{word.title(): <17}{vc: <17}{cc: <17}')

