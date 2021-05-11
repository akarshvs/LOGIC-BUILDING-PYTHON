def leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False

def datefinder(days,year):
    months = {'JANUARY':31, 'FEBRUARY':28, 'MARCH':31, 'APRIL':30, 'MAY':31, 'JUNE':30, 'JULY':31, 'AUGUST':31, 'SEPTEMBER':30, 'OCTOBER':31, 'NOVEMBER':30,
                'DECEMBER':31}
    copy_days = days
    m = 0
    day = 0
    if leap(year):
        months['FEBRUARY'] = 29

    for month in months.keys():
        m = month
        if copy_days < months[month]:
            break
        copy_days -= months[month]
    return str(copy_days) +' TH ' + m +','+str(year)

n = int(input('DAY NUMBER: '))
y = int(input('YEAR: '))
nd = int(input('DATE AFTER (N DAYS):'))
if not 0 < n < 366:
    print('DAY NUMBER OUT OF RANGE')
    exit()
if not 0 < nd < 101:
    print('DATE AFTER (N DAYS) OUT OF RANGE')
    exit()

print(datefinder(n,y))
if n + nd > 365:
    print(datefinder((n + nd) - 365, y+1))
elif n + nd > 364:
    print(datefinder((n + nd) - 364, y+1))
else:
    print(datefinder(n + nd, y))
