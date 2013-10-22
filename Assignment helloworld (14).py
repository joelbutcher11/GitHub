# program to prompt for 8 numbers and report the total to the user

total = 0
number = 1
for number in range(1,9):
    num1 = int(input("Please enter number {0}: ".format(number)))
    total = total + number
    number = number + 1
print("The total is {0}.".format(total))
