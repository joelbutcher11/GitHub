# 15/11/2013
# Joel Butcher
# Times table tester

import random

def get_input_number():
    input_number = int(input("What times table do you want to be tested on? "))
    return input_number

def get_times_number():
    times_number = random.randrange(2,13)
    return times_number

def calculation(input_number, times_number):
    for times in range(1,13):
        userAnswer = int(input("{0} X {1} = ? : ".format(input_number, times_number)))
        answer = input_number * times_number
        if userAnswer == answer:
            print("Well done, that is correct.")
            print()
        else:
            print("Sorry, that is incorrect.")
            print()
            userAnswer = int(input("{0} X {1} = ? ".format(input_number, times_number)))
    return userAnswer


def main_program():
    user_number = get_input_number()
    multiplier = get_times_number()
    question = calculation(input_number, times_number)
    output = userAnswer
    
program = main_program()
print(program)
