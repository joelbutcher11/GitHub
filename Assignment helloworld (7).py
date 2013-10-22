#21-09-2013
#Joel Butcher
#Number Limit

import time

number = int(input("Please enter a number between 1 and 20: "))
print("")

time.sleep(3)

if number > 20:
    print("Sorry, that number is too big")
    print("")
          
elif number < 1:
    print("Sorry, That number is too small.")
    print("")

else:
    print("{0} is within the range 1 - 20." .format(number)) 
