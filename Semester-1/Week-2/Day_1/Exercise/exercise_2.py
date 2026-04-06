"""Task 1: Write a function 'celsius_to_fahrenheit'
# Formula: (celsius * 9/5) + 32
# celsius_to_fahrenheit(0)   → 32.0
# celsius_to_fahrenheit(100) → 212.0"""

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(celsius_to_fahrenheit(0))   # Output: 32.0
print(celsius_to_fahrenheit(100)) # Output: 212.0

''' Task 2: Write a function 'get_grade'
 Takes a score, returns the grade letter
 get_grade(95) → "A"
 get_grade(82) → "B"
 get_grade(55) → "F"
'''
def main():
    score = int(input("Enter a score: "))
    print(f"Grade for {score} is {get_grade(score)}")

def get_grade(score):
    if 90 <= score <= 100:
        return "A🏆"
    elif 80 <= score < 90:
        return "B✅"
    elif 70 <= score < 80:
        return "C📘"
    elif 60 <= score < 70:
        return "D⚠"
    else:
        return "F❌"

if __name__ == "__main__":
    main()
    
"""# Task 3: Write a function 'rectangle_info'
Takes length and width
Returns BOTH area AND perimeter
rectangle_info(5, 3) → area=15, perimeter=16"""
def rectangle_info(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

area, perimeter = rectangle_info(5, 3)

print(f"Area: {area}")          # Output: Area: 15
print(f"Perimeter: {perimeter}")# Output: Perimeter: 16