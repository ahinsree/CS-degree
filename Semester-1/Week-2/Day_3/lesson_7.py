# Lambda with Built-in Functions

"""Lambdas are most powerful when combined with sorted(), map(), filter():"""

# sorted() with lambda:

students = [
    {"name": "Charlie", "grade": 85},
    {"name": "Alice",   "grade": 92},
    {"name": "Bob",     "grade": 78},
]
# sorrted by Grade
by_grade = sorted(students, key=lambda student: student["grade"])
for s in by_grade:
    print(f"{s['name']} : {s['grade']}")
print("=" * 20)
    
# Sort by name
by_name = sorted(students, key=lambda s: s["name"])
for s in by_name:
    print(f"{s['name']} : {s['grade']}")
print("=" * 20)
    
# Sort by grade DESCENDING
by_grade = sorted(students, key=lambda student: student["grade"], reverse=True)
for s in by_grade:
    print(f"{s['name']} : {s['grade']}")
print("=" * 20)

# map() with lambda:

# map() applies a function to every item in a list
numbers = [1, 2, 3, 4, 5]

# Without lambda — verbose
def square(n):
    return n ** 2
squared = list(map(square, numbers))
print(squared)

# With lambda
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

# Convert Celsius to Fahrenheit for a list
temps_c = [0, 20, 37, 100]
temps_f = list(map(lambda c: (c * 9/5) + 32, temps_c))
print(temps_f) 

# filter() with lambda:

# filter() keeps only items where function returns True
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Keep only even numbers
evens = list(filter(lambda n: n % 2 == 0, numbers))
print(evens)      

# Keep only positive numbers
mixed = [-5, -3, 0, 2, 4, 7, -1, 9]
positives = list(filter(lambda n: n > 0, mixed))
print(positives)   

# Filter students with grade above 80
students = [
    {"name": "Alice", "grade": 92},
    {"name": "Bob",   "grade": 65},
    {"name": "Charlie", "grade": 85},
    {"name": "David", "grade": 71},
]
top_students = list(filter(lambda s: s["grade"] >= 80, students))
for s in top_students:
    print(f"{s['name']}: {s['grade']}")
