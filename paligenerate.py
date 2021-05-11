def pali(word):
    if len(word) <=1:
        return word 
    word_c = word
    word_c = word[:-1]
    rev = word_c[::-1]
    while rev[0] == word[-1]:
        rev = rev[1:]
    return word + rev

sent = input('INPUT: ')
if sent[-1] not in ['.', '?','!']:
    print('INVALID INPUT')
    exit()
sent_c = sent[:-1]

op=''
for word  in sent_c.split(' '):
    op = op + pali(word) + ' '
print(f"OUTPUT: {sent}\n{op.strip()}")



