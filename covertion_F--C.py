#Joel Butcher
#12/09/2013
#Conversion of Fahrenheit to Centegrade

import time

print("Hello, will I help you to convert the out side temperature from Fahrenheit to Centegrade")
print()

time.sleep(3)

fahrenheit = int(input("Please input the outside temperature (F): "))
print()

convertion = (fahrenheit*5/7)

time.sleep(3)

print("O.K, the temperature is {0} degrees Centegrade").format(convertion)
