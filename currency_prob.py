# 16-09-2013
# Joel Butcher
# currency problem

total = int(input("Please enter the total amount of cash you have: "))
print()

no_20 = (total//20)

remainder = (total%20)

no_10 = (remainder//10)

remainder2 = (total%10)

no_5 = (remainder2//5)

remainder3 = (total%5)

no_2 = (remainder3//2)

sub_total = (total/


print("The minimum number of £20 notes you can have is {0}".format(no_20))
print()

print("The minimum number of £10 notes you can have is {0}".format(no_10))
print()


print("The minimum number of £5 notes you can have is {0}".format(no_5))
print()


print("The minimum number of £2 coins you can have is {0}".format(no_2))
print()


print("The minimum number of £1 coins you can have is {0}".format(no_1))
