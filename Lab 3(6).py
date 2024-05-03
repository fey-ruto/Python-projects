year_name = int(input("Please enter a year: "))

if (year_name % 400 == 0) or (year_name % 4 == 0 and year_name % 100 != 0):
    print("This is a leap year.")
else:
    print("This is not a leap year.")
