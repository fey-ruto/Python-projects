def calculate_income_tax(gross_salary):
    # Tax rate table as per the Ghana Revenue Authority
    tax_blocks = [402, 110, 130,3000,16395,29963,50000, float('inf')]
    tax_rates = [0, 0.05, 0.1, 0.175,0.25,0.3,0.35]

    # Initialize variables
    remaining_salary = gross_salary
    total_tax = 0

    # Calculate tax for each block
    for block, rate in zip(tax_blocks, tax_rates):
        if remaining_salary <= 0:
            break

        taxable_income = min(remaining_salary, block)
        tax_amount = taxable_income * rate
        total_tax += tax_amount

        remaining_salary -= block

    # Calculate net salary
    net_salary = gross_salary - total_tax

    return total_tax, net_salary


def main():
    # Prompt the user for his /her gross salary
    gross_salary = float(input("Kindly enter your gross monthly salary (GH¢): "))
    
    # Calculate income tax and net salary
    income_tax, net_salary = calculate_income_tax(gross_salary)

    # Display results
    print(f"Your Income Tax is: GH¢{income_tax:.2f}")
    print(f"Your Net Monthly Salary is: GH¢{net_salary:.2f}")
    
main()

