# Asks the user for a message and the number of times they want that message entered

message = input("Enter your message: ")
times = int(input("How many times do you want to see this message?: "))
for count in range(times):
    print(message)
