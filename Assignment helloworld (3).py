print("Hello, I will help you to find out if you are old enough to drive.")
print("")

age = int(input("Please enter your current age: "))
print("")

retire = 65 - age

if age >= 17:
    print("Congratulations, you are old enough to drive!")
    print("")
          
else:
    print("Sorry you have to be 17 to drive. You're not old enough.")
    print("")
