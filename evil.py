def bin(n):
    #generate binary
    res = ''
    n = int(n)
    while n:
        r = n%2
        res = res + str(r)
        n = n//2
    return res[::-1]

n = input('INPUT: ')

if int(n) > 100:
    print('OUT OF RANGE')
    exit()

binary = bin(n)

print(f'BINARY EQUIVALENT: {binary}',f"NUMBER OF 1's: {binary.count('1')}", sep='\n')

print({True:"EVIL", False:"Not Evil"}[binary.count('1')%2 == 0])