# Joel Butcher
# 09/09/2013
# DIV and MOD division and remainder


import time

print("Hello, I will help you to divide a number by another number and find the remainder.")
print()

time.sleep(4)

number1 = int(input("Please enter your original number: "))
print()

time.sleep(1)

number2 = int(input("Please enter the dividing number: "))
print()

divResult = (number1 // number2)

modResult = (number1 % number2)

time.sleep(2)

print("The number of times {0} goes into {1} is {2}".format(number2, number1, divResult))
print()

time.sleep(3)

print ("When you divide {0} by {1}, the remainder is {2}".format(number1, number2, modResult))
