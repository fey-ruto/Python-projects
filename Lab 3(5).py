animals = [
    "Dragon", "Snake", "Horse", "Sheep",
    "Monkey", "Rooster", "Dog", "Pig",
    "Rat", "Ox", "Tiger", "Hare"
]

year = int(input("Kindly enter a year (>= 0): "))

zodiac_index = (year - 2000) % 12

if year >= 2000:
    animal = animals[zodiac_index]
    print("The animal for the year", {year},"is",{animal})
else:
    print("Please enter a valid year (>= 2000).")
