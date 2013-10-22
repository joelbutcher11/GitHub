#21-09-2013
#Joel Butcher
#Display the state water is at when at a certain temperature.

import time

print("Hello, I will tell what state water is in when you enter the temperature in degrees centegrade.")
print("")

time.sleep(5)

temperature = int(input("Please enter the current temperature of the water: "))
print("")

time.sleep(2)

if temperature < 1:
    print ("The water is currently frozen.")
elif temperature >100:
    print("The water is currently boiling.")
else:
    print("The water is neither frozen or boiling, it is in a liquid state.")
