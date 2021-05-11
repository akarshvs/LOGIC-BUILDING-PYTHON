#eventual digit sum
def eventual_dsum(num):
    n = str(num)
    if len(n) < 2:
        return num
    sum = 0
    for digit in n:
        sum += int(digit)
    return eventual_dsum(sum)

#composite num t / f
def compnum(num):
    for i in range(2, num):
        if num % i == 0:
            return True
    return False

#input
m = int(input('M = '))
n = int(input('N = '))
if m > n:
    print('INVALID INPUT')
    exit()

mcn = []
for num in range(m,n+1):
    if eventual_dsum(num) == 1 and compnum(num):
       mcn.append(num)
print('THE COMPOSITE MAGIC INTEGERS ARE: ')
print(*mcn,sep=', ')
print(f'FREQUENCY OF COMPOSITE MAGIC INTEGERS IS: {len(mcn)}') 
 