def prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

m = int(input('M = '))
n = int(input('N = '))

if not 0  < m < 3000 or not 0 < n < 3000 or m > n:
    print('INVALID/OUT OF RANGE')
    exit() 


pnum_lis = []
for num in range(m, n +1):
    if str(num)[::-1] == str(num) and prime(num):
        pnum_lis.append(num)
print('THE PRIME PALINDROME INTEGERS ARE: ')
print(*pnum_lis,sep=', ')
print(f' FREQUENCY OF PRIME PALINDROME INTEGERS : {len(pnum_lis)}')