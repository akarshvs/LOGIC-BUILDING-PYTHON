alphs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!."
alph_dict = {}
for k, alph in enumerate(alphs, start=65):
    alph_dict[alph] = k

def potential(word):
    res = 0
    for letter in word.upper():
        res += alph_dict[letter]
    return res

def invalid(sent):
    for word in sent:
        for letter in word:
            if letter not in alphs:
                print("INVALID ENTRY!")
                return True
    return False

sent = input("INPUT: ").split()

if invalid(sent):
    exit()

word_dict = {}
plist = []

for word in sent:
    word = word.replace('.', '')
    word = word.replace('!', '')
    p = potential(word)
    print(f'{word} = {p}')
    word_dict[p] = word
    plist.append(p)

for p in sorted(plist):
    print(word_dict[p], end =' ')