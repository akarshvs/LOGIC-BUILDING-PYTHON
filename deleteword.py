sent = input('')
if sent[-1] not in '?.!':
    print('Invalid Input')
    exit()

op =''

input('WORD TO BE DELETED: ')
dpos =  int(input('WORD POSITION IN THE SENTENCE: '))

for k, word in enumerate(sent.split(), start=1):
    word.strip()
    if k == dpos:
        pass
    else:
        op = op + word + ' ' 
print(op)



