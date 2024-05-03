def count_unique_characters(input_string):
    input_string = input_string.replace(" ", "").lower()
    unique_characters = {}
    
    for char in input_string:
        if char.isdigit():
            digit = int(char)
            if digit in unique_characters:
                unique_characters[digit]=digit + 1
            else:
                unique_characters[digit] =1 
    
    return unique_characters              
            
user_string = input("Enter a string: ")
print(count_unique_characters(user_string))

                                                                        