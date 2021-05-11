sent = input()
sent = sent[:-1]
count = 0
word_lis = sent.split(' ')
for word in word_lis:
    count +=1
print(f'LENGTH : {count}') 
print('REARRANGED SENTENCE')
print(*sorted(word_lis),sep=' ',end='.')
