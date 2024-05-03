base_charge = 15.00
additional_minute = 0.25
additional_text = 0.15
fee = 0.44
tax_rate= 0.05

minutes_used = int(input("Kindly enter the number of minutes used: "))
text_messages_used = int(input("Kindly enter the number of text messages used: "))

additional_minute_charge = max(0, minutes_used - 50) * additional_minute
additional_text_charge = max(0, text_messages_used - 50) * additional_text

base_charge += additional_minute_charge + additional_text_charge

tax = base_charge * tax_rate
total_bill = base_charge + fee + tax

print("The base charge is ", {base_charge},"dollars")
if additional_minute_charge > 0:
    print("The additional minute charge is ", {additional_minute_charge} ,"dollars")
if additional_text_charge > 0:
    print("The additional text message charge",{additional_text_charge},"dollars")

print("The fee is",{fee},"dollars")
print("The total bill amount is",{total_bill}, "dollars")
print("The tax is", {tax} , "dollars")
