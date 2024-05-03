n = int(input("Kindly enter the amount of money you want to deposit"))

first_i = 0.04 * n

total_first_savings = n + first_i

second_i = 0.04 * (n + first_i)

total_second_savings = total_first_savings + second_i

third_i = 0.04 * (n + first _i) + second_i

total_third_savings = total_second_savings + third_i

print("The total savings after 1 year is:" + str(total_first_savings))
print("The total savings after 2 years is:" + str(total_second_savings))
print("The total savings after 3 years is:" + str(total_third_savings))