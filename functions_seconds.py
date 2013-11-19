# 18/11/2013
# Joel Butcher
# number of seconds in hours, minutes and  seconds

import datetime

def get_hours():
    hours = int(input("Please enter a number of hours: "))
    hour_seconds = (hours * 60) * 60
    return hour_seconds

def get_minutes():
    minutes = int(input("Please enter a number of minutes: "))
    minute_seconds = minutes * 60
    return minute_seconds

def get_seconds():
    seconds = int(input("Please enter a number of seconds: "))
    return seconds

def calculate_total_seconds():
    h_seconds = get_hours()
    m_seconds = get_minutes()
    s_seconds = get_seconds()
    total_seconds = (h_seconds + m_seconds + s_seconds)
    output_seconds = print("The total number of secinds in this time period is {0}.".format(total_seconds))
    return output_seconds

convert_time = calculate_total_seconds()
print(convert_time)

