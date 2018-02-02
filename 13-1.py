# Given your birthday and the current date, calculate your age
# in days. Compensate for leap days. Assume that the birthday
# and current date are correct dates (and no time travel).
# Simply put, if you were born 1 Jan 2012 and todays date is
# 2 Jan 2012 you are 1 day old.

# IMPORTANT: You don't need to solve the problem yet!
# Just brainstorm ways you might approach it!

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
daysOfMonthsLeap = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def isLeapYear(year):
    
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def dateisbefore(y1, m1, d1, y2, m2, d2):
    if y1 < y2:
        return True
    if y1 == y2:
        if m1 < m2:
            return True
        elif m1 == m2:
            return d1 < d2
    return False
def checkValidDate(y,m,d):
    if y > 1582 and 0 < m <= 12:
         if isLeapYear(y) and d <= daysOfMonthsLeap[m-1] :
            return True
         elif d <= daysOfMonths[m-1]:
             return True
         else:
             return False
    else:
        return False
def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    days = 0
    ##
    # Your code here.
    if checkValidDate(y1, m1, d1) and checkValidDate(y2, m2, d2) and dateisbefore(y1, m1, d1, y2, m2, d2):
        if y2 == y1:
            if m1 == m2:
                days = d2 - d1
            else:
                if isLeapYear(y1):
                    firstMonthdays = daysOfMonthsLeap[m1 - 1]
                    days += firstMonthdays - d1
                    index = m1
                    while index < m2:
                        days += daysOfMonthsLeap[index]
                        index += 1
                    days -= daysOfMonthsLeap[m2-1] - d2
                else:
                    firstMonthdays = daysOfMonths[m1 - 1]
                    days += firstMonthdays - d1
                    index = m1
                    while index < m2:
                        days += daysOfMonths[index]
                        index += 1
                    days -= daysOfMonths[m2-1] - d2
        else:
            for year in range(y1, y2 + 1):
                if isLeapYear(year):
                    if year == y1:
                        firstMonthdays = daysOfMonthsLeap[m1 - 1]
                        days += firstMonthdays - d1
                        index = m1
                        while index < len(daysOfMonthsLeap):
                            days += daysOfMonthsLeap[index]
                            index += 1
                    elif year == y2:
                        index = 0
                        while index < m2 - 1:
                            days += daysOfMonthsLeap[index]
                            index += 1
                        days += d2
                    else:
                        for eachdays in daysOfMonthsLeap:
                            days += eachdays
                else:
                    if year == y1:
                        firstMonthdays = daysOfMonths[m1 - 1]
                        index = m1
                        while index < len(daysOfMonths):
                            days += daysOfMonths[index]
                            index += 1
                        days += firstMonthdays - d1
                    elif year == y2:
                        index = 0
                        while index < m2 - 1:
                            days += daysOfMonths[index]
                            index += 1
                        days += d2
                    else:
                        for eachdays in daysOfMonths:
                            days += eachdays
        return days
    else:
        return "Please input a Valid Date"
def daysBetweenDates2(y1, m1, d1, y2, m2, d2):
    if checkValidDate(y1, m1, d1) and checkValidDate(y2, m2, d2):
        from datetime import date
        age = date(y2, m2, d2) - date(y1, m1, d1)
        return (age.days)
    else:
        return "Please input a Valid Date"

print (daysBetweenDates(2012,1,1,2012,2,28))
print (daysBetweenDates(1978,9,8,1978,9,9))
print (daysBetweenDates(1900, 1, 1, 1999, 12, 31))
print (checkValidDate(2013, 6, 31))
print (daysBetweenDates2(1900, 1, 1, 1999, 12, 31))

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"
test()

'''
---
from datetime import date    
age = date.today()-date(1990,7,25)
print(age.days)
'''
