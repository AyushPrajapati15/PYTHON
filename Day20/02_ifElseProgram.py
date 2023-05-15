month = int(input("Enter the month number (1-12): "))

if month == 2:
    year = int(input("Enter the year: "))

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        days = 29
    else:
        days = 28
elif month in [4, 6, 9, 11]:
    days = 30
else:
    days = 31

print(f"The number of days in month {month} is {days}.")
