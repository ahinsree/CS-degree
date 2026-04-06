# ── Main Program ─────────────────────────────
def main():
    while True:
        show_menu()
        choice = input("Select on option (1-5): ")
        if choice == '1':
            km = float(input("Enter kilometers: "))
            miles = km_to_miles(km)
            print(f"{km} km is {miles:.2f} miles.")
        elif choice == '2':
            miles = float(input("Enter miles: "))
            km = miles_to_km(miles)
            print(f"{miles} miles is {km:.2f} km.")
        elif choice == '3':
            celsius = float(input("Enter Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is {fahrenheit:.2f}°F.")
        elif choice == '4':
            fahrenheit = float(input("Enter Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is {celsius:.2f}°C.")
        elif choice == '5':
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please enter 1-5.")

def km_to_miles(km):
    """Convert kilometers to miles."""
    return km * 0.621371

def miles_to_km(miles):
    """Convert miles to kilometers."""
    return miles / 0.621371

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def show_menu():
    """Display the conversion menu."""
    print("\n" + "=" * 40)
    print("     UNIT CONVERTER 🔄")
    print("1. Kilometers → Miles")
    print("2. Miles → Kilometers")
    print("3. Celsius → Fahrenheit")
    print("4. Fahrenheit → Celsius")
    print("5. Exit")
    print("=" * 40)
if __name__ == "__main__":
    main()