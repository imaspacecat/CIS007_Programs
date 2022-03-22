month = eval(input("Enter the month as a number: "))
year = eval(input("Enter the year as a number: "))

monthName = "invalid month name"
days = "invalid number of days"

if month == 1:
    days = 31
    monthName = "January"
elif month == 2:
    monthName = "February"
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        days = 29
    else:
        days = 28
elif month == 3:
    monthName = "March"
    days = 31
elif month == 4:
    monthName = "April"
    days = 30
elif month == 5:
    monthName = "May"
    days = 31
elif month == 6:
    monthName = "June"
    days = 30
elif month == 7:
    monthName = "July"
    days = 31
elif month == 8:
    monthName = "August"
    days = 31
elif month == 9:
    monthName = "September"
    days = 30
elif month == 10:
    monthName = "October"
    days = 31
elif month == 11:
    monthName = "November"
    days = 30
elif month == 12:
    monthName = "December"
    days = 31

print(monthName, year, "has", days, "days.")