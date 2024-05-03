feet = int(input("Kindly enter the number of height in ft"))
inches = float(input("Kindly enter the number of height in inches"))

feet_inches = 12  * feet

total_feet = feet_inches + inches

total_feet_cm = 2.54 * total_feet

print("The total height in centimeters is:" + str(total_feet_cm))
              