n = int(input('N = '))

if n > 50 or n < 9:
    print("INVALID INPUT. NUMBER OUT OF RANGE")
    exit()
if n%2 == 1:
    print("INVALID INPUT. NUMBER IS ODD")
    exit()

def prime(n):
    for i in range(2, n):
        if n%i == 0: 
            return False
    return True

lis = []

for i in range(3, n):
    if i%2 == 1 and prime(i):
        lis.append(i)

check = []
print('PRIME PAIRS ARE:', end=' ')
for i in lis:
    for j in lis:
        if i + j == n and (j,i) not in check:
            print(f'({i},{j})')
            check.append((i,j))