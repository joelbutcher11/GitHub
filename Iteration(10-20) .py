number = int(input("Please enter an number (10-20): "))
while number not in range(10,21):
    number = int(input("Number not in range - Please try again: "))
print("Number accepted")
