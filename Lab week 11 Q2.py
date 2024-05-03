def lower_upper_count(input_string):
    lower_count = 0
    upper_count = 0

    for char in input_string:
        if char.islower():
            lower_count +=1
        elif char.isupper():
            upper_count += 1


    count_dict = {'lower': lower_count, 'upper': upper_count}

    return count_dict

input_string = input("Enter a word")
print(lower_upper_count(input_string))

