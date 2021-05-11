def leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False

def day_count(d,m,y):
    months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    days = 0
    for i in range(m):
        if i == 0:
            pass
        else:
            days = days + months[i]
    if leap(y):
        days +=1
    return days + d

def valid(d,m,y):
    if 0 < d < 32 and 0 < m < 13:
        if m == 2:
            if (leap(y) and d <= 29) or (not leap(y) and d <=28):
                return True
            else: 
                return False
        else:
            return True
    else:
        return False 


print('Enter your date of birth in dd mm yyyy format')
d = int(input())
m = int(input())
y = int(input())

v = valid(d, m, y)
print({True:'VALID DATE', False: 'INVALID DATE'}[v])
if v:
    print(day_count(d, m, y))



