days = int(input("Kindly enter the number of days "))
hours = int(input("Kindly enter the number of hours"))
minutes = int(input("Kindly enter the number of minutes"))
seconds = int(input("Kindly enter the number of seconds"))

days_seconds = days * 86400
hours_seconds = hours * 3600
minutes_seconds = minutes * 60

total_seconds = days_seconds + hours_seconds + minutes_seconds

print("The total seconds is:" + str(total_seconds))
              
           