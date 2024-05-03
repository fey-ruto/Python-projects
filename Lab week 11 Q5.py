def count_digit_occurrences_in_float(number):
    num_str = str(number)
    
    digit_counts = {}
    
    for char in num_str:
        digit = int(char)
        if char.isdigit():    
            if digit in digit_counts:
                digit_counts[digit] = digit + 1
            else:
                digit_counts[digit] = 1
    
    return digit_counts


float_number = input("Kindly enter a float number")
print(count_digit_occurrences_in_float(float_number))


