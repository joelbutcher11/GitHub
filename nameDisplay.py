# 04/11/2013
# Joel Butcher

def get_first_name ():
    first_name = input("Please enter your first name: ")
    return first_name

def get_last_name ():
    last_name = input("Please enter your last name: ")
    return last_name

def get_gender ():
    gender = input("Please enter your gender (m/f): ")
    return gender.upper()

def get_details ():
    valid = False
    while not valid:
        gender = get_gender()
        if len(gender) > 0:
            valid = True
    valid = False
    while not valid:
        first_name = get_first_name()
        if len(first_name) > 0:
            valid = True
    valid = False
    while not valid:
        last_name = get_last_name()
        if len(last_name) > 0:
            valid = True
    return first_name, last_name, gender

def format_name_male (gender, first_name, last_name):
    title_name =  ("Mr {0} {1}".format(first_name, last_name))
    return title_name

def format_name_female (gender, first_name, last_name):
    title_name = ("Ms {0} {1}".format(first_name, last_name))
    return title_name

def format_name(first_name, last_name, gender):
    if gender == "M":
        title_name = format_name_male(gender, first_name, last_name)
        return title_name
    elif gender == "F" or gender == "f":
        title_name = format_name_female(gender, first_name, last_name)
        return title_name
    else:
        ValueError

def output_name(title_name):
    print(title_name)

def name_display():
    first_name, last_name, gender = get_details()
    title_name = format_name(first_name, last_name, gender)
    output_name(title_name)

name_display()
