side_a = float(input("Kindly enter the length of the first side: "))
side_b = float(input("Kindly enter the length of the second side: "))
side_c = float(input("Kindly enter the length of the third side: "))

if side_a == side_b == side_c:
    type_triangle = "equilateral"
elif side_a== side_b or side_a == side_c or side_b == side_c:
    type_triangle = "isosceles"
else:
    type_triangle = "scalene"

print("The triangle is a",{type_triangle},"triangle.")
