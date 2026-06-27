day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    leap = True
else:
    leap = False

# days in month
if month == 2:
    if leap:
        max_days = 29
    else:
        max_days = 28
elif month in (4, 6, 9, 11):
    max_days = 30
else:
    max_days = 31

# find next date
if day < max_days:
    day += 1
else:
    day = 1
    if month < 12:
        month += 1
    else:
        month = 1
        year += 1

print("Next Date:")
print("day =", day, "month =", month, "year =", year)