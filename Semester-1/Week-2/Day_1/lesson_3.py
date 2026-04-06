# print → shows something on screen
#          but gives NOTHING back to the program

def add_print(a, b):
    print(a + b) 

result = add_print(5, 10)
print(result) # Output: None (because add_print doesn't return anything)

# return → sends a value back to whoever called the function
def add_return(a, b):
    return a + b

result = add_return(5, 10)
print(result) # Output: 15 (because add_return returns the sum of a and b)

# With return you can USE the result in further calculations

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

temp_c = 100
temp_f = celsius_to_fahrenheit(temp_c)
double = temp_f * 2 # Using the returned value from celsius_to_fahrenheit to calculate double the Fahrenheit temperature
print(f"{temp_c}°C is equal to {temp_f}°F")  # Output: 100°C is equal to 212.0°F
print(f"Double: {double}°F")  # Output: Double: 424.0°F

#check score function with return
def check_score(score):
    if score < 0:
        return "Invalid score"
    if score >= 90:
        return "Grade A"
    if score >= 80:
        return "Grade B"
    return "Below Grade B"

print(check_score(-5))  # Output: Invalid score
print(check_score(95))  # Output: Grade A
print(check_score(85))  # Output: Grade B
print(check_score(75))  # Output: Below Grade B

# Return multiple values

def rectangle_info(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

area, perimeter = rectangle_info(5, 3)
print(f"Area: {area}")          # Area: 15
print(f"Perimeter: {perimeter}")# Perimeter: 16
    