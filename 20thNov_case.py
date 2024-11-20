"""
This program helps you keep track of deadlines by allowing you
to input a specific date and time. It calculates whether
the deadline has already passed, is happening today, or
how many days remain until the deadline.
"""
from datetime import datetime
def compare_dates(user_date):
    cur_time=datetime.now()
    try:
        diff_date=datetime.strptime(user_date,"%Y-%m-%d %H:%M") - cur_time
        number_days=diff_date.days
    except ValueError:
        print("invalid date time stamp ")
        exit()

    if number_days > 0:
        message=f"The Dealine is in {number_days} Days. Keep wokring !!"
    else:
        message="the Dealine has Passed "
    return message



user_date=input("Enter the deadline (e.g 2024-11-15 17:00")

print(compare_dates(user_date))




