def celsius_to_fahrenheit(celsius):
    """convert a temperature from celsius to fahrenheit 
    parameters: 
               celsius(float): a temperature in celsius.
    return: 
            float: a temperature in fahrenheit.
    """
    return (celsius * 9/5) + 32
# Access the docstring anytime
help(celsius_to_fahrenheit)
print(celsius_to_fahrenheit.__doc__)

#Function Best Practices:
# ✅ 1. ONE function = ONE job
def get_grade(score):
    if score >= 90:
        return "Grade A"
    if score >= 80:
        return "Grade B"
    if score >= 70:
        return "Grade C"
    if score >= 60:
        return "Grade D"
    return "Grade F"    
# ✅ 2. Use descriptive names
def calculate_average():             # ✅ clear and descriptive name
    pass

def ca():                            # ❌ meaningless
    pass

# ✅ 3. Return values, don't just print
def square(n):
    return n ** 2          # ✅ flexible — caller decides what to do

# ✅ 4. Default parameters for optional arguments
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# ✅ 5. Keep functions short & focused
# If your function is over 20 lines — split it up!

def get_score():
    """Ask user for a valid score"""
    while True:
        score = int(input("Enter a score (0-100): "))
        if 0 <= score <= 100:
            return score
        print("Invalid score. Please enter a score between 0 and 100.")

def get_grade(score):
    """Return the grade for a given score"""
    if 90 <= score <= 100:
        return "A🏆"
    if 80 <= score < 90:
        return "B✅"
    if 70 <= score < 80:
        return "C📘"
    if 60 <= score < 70:
        return "D⚠"
    return "F❌"

def print_result(name, score, grade):
    """Print the result in a nice format"""
    print(f"\n{'='*30}")
    print(f"Student: {name}")
    print(f"Score: {score}")
    print(f"Grade: {grade}")
    print(f"{'='*30}")
# Main program
name = input("Enter student name: ")
score = get_score()
grade = get_grade(score)
print_result(name, score, grade)