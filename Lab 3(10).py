wavelength = float(input("Kindly enter the wavelength (in nanometers): "))

min_wavelength = 380
max_wavelength = 750

color_ranges = {
    "Violet": (380, 450),
    "Blue": (450, 495),
    "Green": (495, 570),
    "Yellow": (570, 590),
    "Orange": (590, 620),
    "Red": (620, 750)
}

if min_wavelength <= wavelength <= max_wavelength:
    color = None
    for color_name, (min_range, max_range) in color_ranges.items():
        if min_range <= wavelength <= max_range:
            color = color_name
            break

    if color:
        print("The color of the wavelength {wavelength} nm is {color}.")
    else:
        print("Unable to determine the color for this wavelength.")
else:
    print("Error: Wavelength is outside the visible spectrum.")
