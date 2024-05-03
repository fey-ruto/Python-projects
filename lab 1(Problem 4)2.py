import math

radius = float(input("Kindly enter the radius of the cylinder: "))
height = float(input("Kindly enter the height of the cylinder: "))

area = math.pi * (radius ** 2)
volume = float(area * height)

print("The volume of the cylinder is: " + str(volume) + " cubic " )



