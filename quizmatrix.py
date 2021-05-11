#valid input
n = int(input('N = '))
if not 3 < n < 11:
    print('INPUT SIZE OUT OF RANGE')
    exit()

#input answer matrix
quiz = [[] for y in range(n)]
for i in range(n):
    print(f'Particpiant {i+1} ', end='')
    quiz[i].extend(input().split(' '))

#get key
key = input('Key: ').upper().split(' ')

#calculate and print socres
hs = 0
score = [0 for x in range(n)]
print('Scores:')
for i in range(n):
    temp = 0
    for j in range(5):
        if quiz[i][j] == key[j]:
            temp+=1
    score[i] = temp
    print(f'Particpiant {i + 1} = {score[i]}')
    if score[i] >= hs:
        hs = score[i]

#high scorer
print(f'Highest score: ')
for i in range(n):
    if score[i] == hs:
        print(f'Particpant {i+1}')