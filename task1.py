monthlength = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

year1, month1, day1, hour1, min1, sec1 = map(int, input("Enter date 1: ").split())
year2, month2, day2, hour2, min2, sec2 = map(int, input("Enter date 2: ").split())

def finddays(month1, month2, day1, day2):
    founddays = 0
    yearflag = False
    if month2 > month1:
        founddays += sum(monthlength[month1:month2])
        founddays += day2 - day1
    elif month2 < month1:
        yearflag = True
        founddays += sum(monthlength[month2:])
        founddays += sum(monthlength[:month1])
        founddays += day1 - day2
    else:
        founddays = day2 - day1
    return founddays, yearflag

def findtime(n1, n2, pool):
    if n1 > n2:
        return pool - n1 + n2, 0
    elif n1 != n2:
        return n2 - n1, 1
    return n2 - n1, 2

years = year2 - year1

days, yearflag = finddays(month1-1, month2-1, day1, day2)
if yearflag == True:
    years -= 1
days += years * 365



hours, hourflag = findtime(hour1, hour2, 24)
minutes, minuteflag = findtime(min1, min2, 60)
seconds, secondflag = findtime(sec1, sec2, 60)

if hourflag == 0:
    days -= 1
elif hourflag == 2:
    if minuteflag == 0:
        days -= 1
    elif minuteflag == 2:
        if secondflag == 0:
            days -= 1

fullseconds = hours *  60 * 60 + minutes * 60 + seconds

print(years, days, hours, minutes, seconds)

print(days, fullseconds)
