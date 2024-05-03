string = input("Please enter a string of characters: ")

def is_valid(string):
    if len(string) == 6:
        letters = string[:3]
        numbers = string[3:]
        if letters.isalpha() and letters.isupper() and numbers.isdigit():
            print("True")
        else:
            print("False")
    
def is_valid(string):
    if len(string) == 7:
        letters = string[4:]
        numbers = string[:4]
        if letters.isalpha() and letters.isupper() and numbers.isdigit():
            print("True")
        else:
            print("False")

if is_valid(string):
    print("Valid for an older style license plate.")
elif is_valid(string):
    print("Valid for a newer style license plate.")
else:
    print("Not valid for either style of license plate.")
