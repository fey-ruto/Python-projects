pi = "3.1415926535897932384626433832795028841971693993751"

pi =pi.replace(".","")

digit_counts = {}

for char in pi:
    if char.isdigit():
        digit = int(char)  
        if digit in digit_counts:
            digit_counts[digit] = digit + 1
        else:
            digit_counts[digit] = 1

for digit, count in digit_counts.items():
    print(f"The digit {digit} has count {count}")
