frequency = float(input("Please enter the frequency of electromagnetic radiation (in hertz): "))

categories = {
    "Radio Waves": (3, 3e9),       
    "Microwaves": (3e9, 3e12),      
    "Infrared": (3e12, 4.3e14),      
    "Visible Light": (4.3e14, 7.5e14),
    "Ultraviolet": (7.5e14, 3e17),   
    "X-Rays": (3e17, 3e19),          
    "Gamma Rays": (3e19, float('inf'))
}

category = None
for name, (lower, upper) in categories.items():
    if lower <= frequency <= upper:
        category = name
        break

if category:
    print("The electromagnetic radiation falls into the category: {category}")
else:
    print("Frequency is out of range for classification.")
