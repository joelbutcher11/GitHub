#Joel Butcher
#23.09.2013
#Determine Grade

score = int(input("Please enter the socre you achieved in the test: "))
print()

if score > 100:
    print("That is not a possible mark for this test")

if score >= 81 and score <= 100:
    print("Grade:  A")

elif score >= 71 and score <= 80:
    print("Grade:  B")

elif score >= 61 and score <= 70:
    print("Grade:  C")

elif score >= 51 and score <= 60:
    print("Grade:  D")

elif score >= 41 and score <= 50:
    print("Grade:  E")

else:
    print("Grade:  U")
