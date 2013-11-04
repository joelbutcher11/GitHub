def get_first_name ():
    first_name = input("Please enter your first name: ")
    return first_name

def get_last_name ():
    last_name = input("Please enter your last name: ")
    return last_name

def get_gender ():
    gender = input("Please enter your gender (M/F): ")
    return gender.upper()

def get_details ():
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
    valid = False
    while not valid:
        gender = get_gender()
        if len(gender) > 0:
            valid = True
    return first_name, last_name, gender

def format_name_male (gender, first_name, last_name):
    return "Mr {0} {1}".format(frist_name, last_name)

def format_name_female (gender, first_name, last_name):
    return "Ms {0} {1}".format(frist_name, last_name)

def format_name(first_name, last_name, gender):
    if gender == "M":
        title_name = format_name_male(first_name, last_name)
    else:
        title_name = format_name_female(fist_name, last_name)

def output_name(title_name):
    print(title_name)
