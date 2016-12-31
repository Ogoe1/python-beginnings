
import time
import webbrowser

def nextDay(year, month, day):
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def LeapYear(year):
	if year % 400 == 0:
		return True
	if year % 100 == 0:
		return False
	if year % 4 == 0:
		return True
	return False

def daysInMonth(year, month):
	daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	if month == 2:
		if LeapYear(year):
			return 29
		else:
			return 28
	return daysOfMonths[month - 1]


def countDays(year1, month1, day1, year2, month2, day2):
	days = 0
	while (year1, month1, day1) != (year2, month2, day2):
		(year1, month1, day1) = nextDay(year1, month1, day1)
		days += 1
	return days

def ifDateIsBefore(year1, month1, day1, year2, month2, day2):
	if year1 < year2:
		return True
	if year1 == year2:
		if month1 < month2:
			return True
		if month1 == month2:
			return day1 < day2
	return False
	
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
	numberOfDays = countDays(year1, month1, day1, year2, month2, day2)
	return numberOfDays



name = raw_input('WHAT IS YOUR NAME?  ')    
birthYear = int(raw_input(name + ', ENTER YOUR YEAR OF BIRTH  '))
curr_Year = int(raw_input('ENTER THE CURRENT YEAR  '))
birthMonth = int(raw_input('ENTER YOUR MONTH OF BIRTH IN NUMBERS '))
assert birthMonth <= 12
curr_Month = int(raw_input('ENTER THE CURRENT MONTH  '))
assert curr_Month <= 12
birthDay = int(raw_input('ENTER THE DAY OF THE MONTH (IN NUMBERS)  '))
assert birthDay <= 31
curr_Day = int(raw_input('ENTER THE CURRENT DAY OF THE MONTH  '))
str_dBD = str(daysBetweenDates(birthYear, birthMonth, birthDay, curr_Year, curr_Month, curr_Day))
dBD = int(str_dBD)
ageInYears = dBD / 365

def isYear(ageInYears):
    if ageInYears < 1:
        return False
    return True

def monthsOld(ageInYears):
    if isYear(ageInYears) == False:
        ageInMonths = str((float(dBD)/365) * 12)
        ageInMonths2 = ageInMonths[:ageInMonths.find('.')]
        return 'You thought you could trick me. You are not even 1 year old yet. You are a little ' + ageInMonths2 + ' month old baby! How cute!!'
            
def yearsOld(dBD):    
    if isYear(ageInYears):
        return 'You are ' + str(ageInYears) + ' years old!'
    else:
        return monthsOld(ageInYears)
    
ageYears = str(yearsOld(dBD))    

print 'Calculating your age in days...'
time.sleep(2)
print 'Complex calculations like these take a lot of time...Please bear with me. I am working as fast as I can'

time. sleep(2)
movie = raw_input('Meanwhile, would you like to watch a movie (YES/NO)  ').lower()
if movie.find('y' and 'e') == True:
    print 'Coming right up...'
    webbrowser.open_new('http://putlocker.is/a-z/')
    time.sleep(30)
    print 'Dearest ' + name + ', you are currently ' + str_dBD + ' days old!'
else:
    print 'suit yourself'
    time.sleep(2)
    print 'Dearest ' + name + ', you are currently ' + str_dBD + ' days old!'
    

question = raw_input("Would you like to know your age in years? YES/NO ").lower()

if question.find('y' and 'e') == True:
    if not monthsOld(ageInYears):
        print yearsOld(dBD)
    else:
        print monthsOld(ageInYears)
else:
    print 'Fine!!! Have it your way!'
    time.sleep(3)
    print 'In fact i will tell you anyway..........'
    time.sleep(2)
    print yearsOld(dBD)

    

 
                               

def test():
	assert daysBetweenDates(2013, 1, 1, 2013, 1, 1) == 0
	assert daysBetweenDates(2013, 1, 1, 2013, 1 ,2) == 1
	assert nextDay(2013, 1, 1) == (2013, 1, 2)
	assert nextDay(2013, 4, 30) == (2013, 5, 1)
	assert nextDay(2012, 12, 31) == (2013, 1, 1)
	assert nextDay(2013, 2, 28) == (2013, 3, 1)
	assert nextDay(2013, 9, 30) == (2013, 10, 1)
	assert daysBetweenDates(2013, 1, 1, 2014, 1, 1,) == 365
	print "Tests finished."
