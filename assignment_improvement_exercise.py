#john bain
#variable improvement exercise
#05-09-12

import math
import time

radius = float(input("Please enter the radius of the circle: "))

circumference = 2* math.pi * radius
circumference = round(circumference,2)

area = math.pi * radius**2
area = round(area,2)

time.sleep(1)

print()
print("The circumference of this circle is {0} cm.".format(circumference))

time.sleep(1)
print()
print("The area of this circle is {0}.".format(area))
