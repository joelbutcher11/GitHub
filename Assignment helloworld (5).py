print("Hello, I will help you to find out if you are old enough to vote, and how many years until you can retire.")
print("")

age = int(input("Please enter your current age: "))
print("")

retire = 65 - age

if age >= 18:
    print("Congratulations, you are old enough to vote!")
    print("")
          
if age < 18:
    print("Sorry you have to be 18 to vote. You're not old enough.")
    print("")

print("I will now calculate the number of years before you can retire")
print("")

print("Ok, you will be able to retire in {0} years" .format(retire))
