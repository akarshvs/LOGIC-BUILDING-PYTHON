def digit_sum(num):
    sum = 0
    for dig in str(num):
        sum += int(dig)
    return sum

m = int(input('M = ')) 
n = int(input('N = '))

if (not 0 < n < 100) or (not 100 <= m <= 1000):
    print('INVALID INPUT')
    exit()

for num in range(m, 10001):
    if digit_sum(num) == n:
        print(f'The required number = {num}')
        print(f'Total number of digits = {len(str(num))}')
        break