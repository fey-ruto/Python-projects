year = int(input("Kindly enter the year in this format (yyyy): "))
month = int(input("Kindly enter the month in this format (1-12): "))
day = int(input("Kindly enter the day between (1-31): "))

def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("true")
    else:
        print("false")

days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if leap_year(year):
    days_in_month[2] = 29

if month < 1 or month > 12 or day < 1 or day > days_in_month[month]:
    print("Invalid date input.")

elif day < days_in_month[month]:
        day += 1

elif  day == 1 :
      month < 12
      month += 1

else:
      month = 1
      year += 1

print("The day immediately after", {year}-{month}-{day},"is", {year}-{month}-{day}.)
