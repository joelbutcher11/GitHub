# asks the user how many number they wnat to be averaged
# enter integers that many times
# calculates the average

total = 0
integer = 1
times = int(input("Please enter the number of numbers you want to be averaged: "))

for count in range(times):
    number = int(input("Please enter number {0} in series: ".format(integer)))
    total = total + number
    integer = integer + 1

average = total / times
    
print("The total of you numbers is {0}".format(average))
