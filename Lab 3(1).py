num1 = int(input("Please enter the first integer: "))
num2 = int(input("Please enter the second integer: "))
num3 = int(input("Please enter the third integer: "))

min_value = min(num1, num2, num3)
max_value = max(num1, num2, num3)

middle_value = num1 + num2 + num3 - min_value - max_value

print("Ascending Order:", min_value, middle_value, max_value)
