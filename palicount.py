
sent = input('')
if sent[-1] not in '?.!,':
    print('Invalid Input')
    exit()

pali_lis = []
for word in sent.split():
    word = word.replace('.', '')
    word = word.replace('?', '')
    word = word.replace('!', '')
    word = word.replace('?', '')
    word = word.replace(',', '')
    if word[::-1] == word:
        pali_lis.append(word)

if len(pali_lis):
    print(*pali_lis, sep= ' ')
    print(f'NUMBER OF PALINDROMIC WORDS: {len(pali_lis)}')
else: 
    print('NO PALINDROMIC WORDS')