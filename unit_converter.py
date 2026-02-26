#length converter kelometer to meeter and meters to feet
def length_converter():
    print("\n Length Converter")
    print("1. Kelometers to Miles")
    print("2. Meters to feet")
    choice = int(input("Choose option: "))
    value = float(input("Enter value: "))

    if choice == 1:
        print(f"{value} km = {value * 0.621371} miles")
    elif choice == 2:
        print(f"{value} meter = {value * 3.28084} feet")
    else:
        print("Invalid choice")

def weight_converter():
    print("\n Weight Converter")
    print("1. Kelometers to pounds")
    print("2. Grames to Onuces")
    choice = int(input("Choose option: "))
    value = float(input("Enter value: "))

    if choice == 1:
        print(f"{value} km = {value * 2.20462} lbs")
    elif choice == 2:
        print(f"{value} g = {value * 0.35274} ounces")
    else:
        print("Invalid choice")

def temperature_converter():
    print("\n Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to kelvin")
    choice = int(input("Choose option: "))
    value = float(input("Enter value: "))

    if choice == 1:
        print(f"{value} C = {(value * 9/5) + 32} F")
    elif choice == 2:
        print(f"{value} F = {((value -32) *5/9) + 273.15} K")
    else:
        print("Invalid choice")

# Main menu
while True:
    print("\n ---------Unit Convertor----------")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Exit")

    main_coice = int(input("Choose category"))

    if main_coice == 1:
        length_converter()
    elif main_coice == 2:
        weight_converter()
    elif main_coice == 3:
        temperature_converter()
    elif main_coice == 4:
        print("Thanks for choosing converter, Goodbye")
        break
    else:
        print("Invalid selection, try again")