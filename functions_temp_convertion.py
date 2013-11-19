def temperature_convertion():
    fahrenheit = int(input("Please enter the current temperature in fahrenheit: "))
    celsius = int((fahrenheit - 32) * (5/9))
    output = ("The temperature is {0:.0f} degrees celsius.".format(celsius))
    return output

convertion = temperature_convertion()
print(convertion)
