# Task 1: Write 'student_report(name, *subjects, grade_scale=100, **extra)'
# name          → student name (required)
# *subjects     → any number of subject scores
# grade_scale   → max score (default 100)
# **extra       → any extra info (e.g. teacher="Mr. Smith")
#
# Calculate average, assign grade, print full report

def student_report(name, *subjects, grade_scale = 100, **extra):
    average = sum(subjects) / len(subjects)
    if average >= grade_scale * 0.9:
        grade = "A"
    elif average >= grade_scale * 0.8:
        grade = "B"
    elif average >= grade_scale * 0.7:
        grade = "C"
    elif average >= grade_scale * 0.6:
        grade = "D"
    else:
        grade = "F"
    print("Student Report:")
    print(f"=" * 30)
    print(f"Student: {name}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")
    for key, value in extra.items():
        print(f"{key}: {value}")
student_report("Alice", 85, 92, 78, grade_scale = 100, teacher = "Mr. Smith")


# Task 2: Write a function that accepts a list OR
# individual numbers — works BOTH ways:
# total([1, 2, 3, 4, 5])   → 15
# total(1, 2, 3, 4, 5)     → 15
def total(*args):
     # If only one argument AND it's a list, unpack it
    if len(args) == 1 and isinstance(args[0], list):
        return sum(args[0])
    # Otherwise, treat as multiple individual numbers
    return sum(args)
print(total([1, 2, 3, 4, 5]))
print(total(1, 2, 3, 4, 5))
        
    

