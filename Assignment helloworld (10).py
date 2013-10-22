#21-09-2013
#Joel Butcher
#Ask for hours worked and rate of pay to display gross pay

import time
import sys

print("Hello, I will help you to work out your gross weekly pay. ")
print("")

time.sleep(3)

hoursWorked = float(input("Please enter the number of hours you have worked this week: "))
print("")

time.sleep(2)

if hoursWorked > 48:
    print("Error, the legal maximum number of working hours is 48 hours")
from sys.exit

rateOfPay = float(input("Please enter the amount you are paid per hour: £"))
print("")

time.sleep(2)
if hoursWorked > 40:
    grossPay = 2 * (hoursWorked * rateOfPay)    
else:
    grossPay = hoursWorked * rateOfPay

print("Ok, your gross pay for this week is £{0:.2f}" .format(grossPay,))
