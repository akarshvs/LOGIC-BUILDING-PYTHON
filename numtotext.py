convert={1:'ONE',2:'TWO',3:'THREE',4:'FOUR',5:'FIVE',6:'SIX',7:'SEVEN',8:'EIGHT',9:'NINE',
        10:'TEN', 11:'ELEVEN',12:'TWELVE',13:'THIRETEEN',14:'FOUTEEN',15:'FIFTEEN',16:'SIXTEEN',
        17:'SEVENTEEN',18:'EIGHTEEN',19:'NINETEEN',20:'TWENTY',30:'THIRTY',40:'FOURTY',
        50:'FIFTY',60:'SIXTY',70:'SEVENTY',80:'EIGHTY',90:'NINTY'}

n = input('INPUT: ')
if not 0 < int(n) < 1000:
    print('OUT OF RANGE')
    exit()

if len(n) == 3:
    try:
        if n[1] == '1':
            op = convert[int(n[0])] + ' HUNDRED AND ' + convert[int(n[1:])]
        else:
            op = convert[int(n[0])] + ' HUNDRED AND ' + convert[int(n[1]) * 10] +' '+ convert[int(n[2])]
    except KeyError:
        try:
            op = convert[int(n[0])] + ' HUNDRED AND ' + convert[int(n[1]) * 10]
        except KeyError:
            op = convert[int(n[0])] + ' HUNDRED'
elif len(n) == 2:
    try:
        if n[0] == '1':
            op = convert[int(n)]
        else:
            op = convert[int(n[0]) * 10] + ' ' + convert[int(n[1])]
    except KeyError:
        op = convert[int(n[0]) * 10]
else:
    op = convert[int(n)]

print('OUTPUT: ',op)