#Joel Butcher
#27-09-2013
#Date recognistion and year


def IsLeapYear(year):
    if ((year % 4) ==0):
        if((year % 100) == 0):
            if((year % 400) == 0):
                return 1
            else:
                return 0
        else:
            return 1
        return 0

month = int(input("Please enter a month as a number between 1-12: "))
if month == 1:
    print("The month you entered is January")
elif month == 2:
    print("The month you entered is February")
elif month == 3:
    print("The month you entered is March")
elif month == 4:
    print("The month you entered is April")
elif month == 5:
    print("The month you entered is May")
elif month == 6:
    print("The month you entered is June")
elif month == 7:
    print("The month you entered is July")
elif month == 8:
    print("The month you entered is August")
elif month == 9:
    print("The month you entered is September")
elif month == 10:
    print("The month you entered is October")
elif month == 11:
    print("The month you entered is November")
else:
    print("The month you entered is December")

year = int(input("Please enter the year: "))
if ( IsLeapYear(year) == 1):
     print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))
