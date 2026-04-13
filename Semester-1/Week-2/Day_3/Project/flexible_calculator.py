# ============================================
#   FLEXIBLE CALCULATOR 🧮
#   Week 2, Day 3 Project
# ============================================

def add(*args):
    "Add any number of value"
    return sum(args)

def subtract(start, *args):
    "Subtract all subsequent values from start."""
    result = start
    for n in args:
        result -= n
    return result

def multiply(*args):
    "Multiply any number of values"
    result = 1
    for n in args:
        result *= n
    return result

def divide(dividend, divisor):
    """Divide dividend by divisor safely."""
    if divisor == 0:
        return "Cannot divide by zero."
    return dividend / divisor

def calculator(*args, operation = "add", **options):
    """
    Master calculator function.
    operation → add, subtract, multiply, divide
    options   → round_to (decimal places)
    """
    round_to = options.get("round_to", 2)
    if operation == "add":
        result = add(*args)
    elif operation == "subtract":
        result = subtract(*args)
    elif operation == "multiply":
        result = multiply(*args)
    elif operation == "divide":
        result = divide(*args)
    else:
        return "⚠ Invalid operation."
    return round(result, round_to)

def show_menu():
    """Display calculator menu."""
    print("\n" + "=" * 45)
    print("    FLEXIBLE CALCULATOR 🧮")
    print("=" * 45)
    print("1. Add   (any number of value)")
    print("2. Subtract   (any number of value)")
    print("3. Multiply   (any number of value)")
    print("4. Divide     (exactly two value)")
    print("5. Exit")
    print("=" * 45)
    
def get_numbers():
    """Get numbers from user."""
    raw = input("Enter numbers separated by spaces: ")
    return tuple(float(x) for x in raw.split())
def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == "5":
            print("👋 Goodbye!")
            break
        elif choice not in ("1", "2", "3", "4"):
            print("⚠ Invalid choice! ")
            continue
        numbers = get_numbers()
        ops = {"1": "add", "2": "subtract",
               "3": "multiply", "4": "divide"}
        operation = ops[choice]
        decimals = input("Round to how many decimal places? (default 2): ")
        round_to = int(decimals) if decimals else 2

        result = calculator(*numbers, operation = operation, round_to = round_to)
        print(f"\n  Result: {result}")

if __name__ == "__main__":
    main()

        
        