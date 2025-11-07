#unit converter using python
def unit_converter():
    print("Welcome to the Unit Converter!")
    print("Choose the conversion type:")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        km = float(input("Enter distance in kilometers: "))
        miles = km * 0.621371
        print(f"{km} kilometers is equal to {miles} miles.")
    elif choice == '2':
        miles = float(input("Enter distance in miles: "))
        km = miles / 0.621371
        print(f"{miles} miles is equal to {km} kilometers.")
    elif choice == '3':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit}°F.")
    elif choice == '4':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius}°C.")
    else:
        print("Invalid choice. Please try again.")
unit_converter()