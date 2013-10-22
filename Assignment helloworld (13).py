#Joel Butcher
#30-09-2013
#A program that asks the user for the date in three seperate integers
#and displays the result as the day number with the correct suffix
#correct month name and year.
#if the numbers are too low or too high the program quits


import time

day = int(input("Please enter the day number (1-31): "))

while day not in range(1,32):

    day = int(input("That is not a valid day number please enter another (1-31):  "))  

print("")
month = int(input("Please enter the month number (1-12): "))

while month not in range(1,13):

    month = int(input("That is not a valid month please try again (1-12):"))

print("")

while month == 2 and day not in range(1,29):

    day = int(input("The max number of days in February is 28. Please re-enter the day number: "))

    month = int(input("Please re-enter the month number: "))

if month == 1:
    monthName = "January"
if month == 2:
    monthName = "February"
if month == 3:
    monthName == "March"
if month == 4:
    monthName == "April"
if month == 5:
    monthName == "May"
if month == 6:
    monthName == "June"
if month == 7:
    monthName == "July"
if month == 8:
    monthName == "August"
if month == 9:
    monthName == "September"
if month == 10:
    monthName == "October"
if month == 11:
    monthName == "November"
if month == 12:
    monthName == "December"
        
print("")
year = int(input("Please enter the year: "))

while year not in range(1931, 2021):

    year = int(input("That is not a valid year please enter the year:   "))

        
time.sleep(1)

if 4 <= day <=20 or 24 <= day <= 30:
    suffix = "th"
else:
    suffix = ["st", "nd", "rd"][day % 10 - 1]


print("")
print ("The date is {0}{1} {2} {3}. ".format(day,suffix,monthName,year))
