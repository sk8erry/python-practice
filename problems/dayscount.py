#This program is used to count how many days you have lived!
import datetime

#My birthday
birthYear = int(input('Please enter birth year: '))
birthMonth = int(input('Please enter birth month: '))
birthDay = int(input('Please enter birth day: '))

#Get current date
now = datetime.datetime.now()
currentYear = now.year
currentMonth = now.month
currentDay = now.day

daysInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]

def isLeapYear(year):
    if year % 4 == 0:
        return 1
    else:
        return 0

def daysInBirthYear(birthYear,birthMonth,birthDay):
    daysIBY = 0 #daysIBY = days in birth year before birth!
    for i in range (0, birthMonth-1):
        daysIBY = daysInMonth[i] + daysIBY
    daysIBY = daysIBY + birthDay
    if (birthMonth > 2) & (isLeapYear(birthYear) == 1):
        daysIBY += 1
        print ('wow leap year')
    else: pass
    return (365 - daysIBY + isLeapYear(birthYear))

def daysInCurrentYear(currentYear,currentMonth,currentDay):
    daysICY = 0
    for i in range (0,currentMonth-1):
        daysICY = daysInMonth[i] + daysICY
    daysICY = daysICY + currentDay
    if (currentMonth > 2) & (isLeapYear(currentYear) == 1):
        daysICY += 1
        print ('wow this year is leap year')
    else: pass
    return daysICY

def daysInBetween(currentYear,birthYear):
    daysIBtw = (currentYear - birthYear - 1) * 365
    for i in range (birthYear + 1, currentYear):
        daysIBtw = daysIBtw + isLeapYear(i)
        #print (i)
        #if isLeapYear(i) == 1:
            #print (i, 'is leap year')
    if currentYear - birthYear > 2:
        return daysIBtw
    else:
        return 0
print ('You have lived for', daysInBirthYear(birthYear,birthMonth,birthDay) +
        daysInCurrentYear(currentYear,currentMonth,currentDay) +
          daysInBetween(currentYear,birthYear), 'days, congrats and keep on living!')

input("Press Enter to exit")

#Lines below are for testing only
#print ('daysInBetween = ', daysInBetween(currentYear, birthYear))
#print ('daysInBirthYear = ', daysInBirthYear(birthYear,birthMonth,birthDay))
#print ('daysInCurrentYear = ', daysInCurrentYear(currentYear,currentMonth,currentDay))
