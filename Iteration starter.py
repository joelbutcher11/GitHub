# Program to total up 4 number by the user

total = 0
i = 0
while i < 5:
    print("Please enter number {0} in the series: ".format(i))
    number = int(input())
    total = total + number
    i = i + 1
print("The total of the numbers you entered is {0}
      ".format(total))
