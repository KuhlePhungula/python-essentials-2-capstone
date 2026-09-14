# Environment report and data report

import platform
import os
import calendar
import datetime

students_file = "data/student.txt"

def enviro_report():
    print("--- Environment Report ---")
    print(f"Operatting System: {platform.system()}")
    print(f"Python version: {platform.python_version()}")
    print(f"Working Directory: {os.getcwd()}")

    if os.path.exists(students_file):
        size = os.path.getsize(students_file)
        print(f"data.students.txt: {size} bytes")
    else:
        print(f"data/students.txt: not found")

def data_report():
    today = datetime.date.today()
    now = datetime.datetime.now()

    print("--- Data Report ---")
    print("Today's date:", today.strftime("%A, %d %B %Y"))
    print("Current timestamp:", now)

    year = today.year
    month = today.month

    month_name = calendar.month_name[month]
    is_leap = calendar.isleap(year)
    days_in_month = calendar.monthrange(year, month[1])

    print("Current Month:", month_name)
    print(f"Is {year} a leap year?", is_leap)
    print(f"Days in {month_name} {year}:", days_in_month)

    future_date = datetime.date(2027, 11, 15)
    days_left = (future_date - today).days
    print(f"Days until the target date ({future_date}): {days_left}")