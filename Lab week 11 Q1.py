def count_letters(input_string):
    letter_count = {}

    input_string = input_string.lower()
    
# add the character in the letter_count dictionary
    for char in input_string:
        if char.isalpha():
            
            letter_count[char] = letter_count.get(char, 0) + 1

    return letter_count

user_input = input("Please enter a sentence: ")

letter_counts = count_letters(user_input)

sorted_letter_counts = sorted(letter_counts.items())

for letter, count in sorted_letter_counts:
    print(letter, count)
