'''### 📋 Project Specification:

Build a program that:

1. **Asks** how many students to enter (1–10)
2. **Collects** each student's name and scores for 3 subjects (Math, Science, English)
3. **Calculates** the average score for each student
4. **Assigns** a grade (A/B/C/D/F) based on average
5. **Prints** a formatted report card for each student
6. **At the end** prints a class summary showing:
   - Highest average in the class
   - Lowest average in the class
   - Class average overall'''
   
'''### 🧑‍💻 Code Implementation Plan:'''
'''STEP 1 → Get number of students (validate: must be 1-10)
STEP 2 → Loop for each student:
           → Get name
           → Get 3 subject scores (validate: must be 0-100)
           → Calculate average
           → Assign grade
           → Print report card
STEP 3 → Print class summary'''

print("=" * 50)
print("        STUDENT REPORT CARD GENERATOR 📊")
print("=" * 50)
# Step 1: Get number of students
while True:
    num_students = int(input("Enter number of students (1 - 10): "))
    if 1 <= num_students <= 10:
        break
    print("⚠ Please enter a valid number of students (1-10): ")
    
# Step 2: Collect data for each student
highest_avg = 0
lowest_avg = 100
class_total = 0

for student_num in range(1, num_students + 1):
    print(f"\n{'-' * 50}")
    print(f"Student {student_num} of {num_students}")
    print(f"{'-' * 50}")
    name = input("Enter student's name: ") 
    # Get scores for 3 subjects
    subjects = ["Math", "Science", "English"]
    scores = []
    for subject in subjects:
        while True:
            score = int(input(f"Enter {subject} score (0-100): "))
            if 0 <= score <= 100:
                scores.append(score)
                break
            print("⚠ Please enter a valid score (0-100): ")
    # Calculate average
    average = sum(scores) / len(scores)
    class_total += average
    # Assign grade
    if average >= 90:
        grade = "A 🏆"
    elif average >= 80:
        grade = "B ✅"
    elif average >= 70:
        grade = "C 📘"
    elif average >= 60:
        grade = "D 📙"
    else:
        grade = "F ❌"
        
    # Track highest and lowest 
    if average > highest_avg:
        highest_avg = average
    if average < lowest_avg:
        lowest_avg = average
    
    # Print report card
    print(f"\n{'=' * 50}")
    print(f"REPORT CARD FOR - {name.upper()}")
    print(f"{'=' * 50}")
    for subject, score in zip(subjects, scores):
        print(f"{subject}: {score}")
    print(f"Average Score: {average:.2f}")
    print(f"Grade: {grade}")
    print(f"{'=' * 50}")

# Step 3: Print class summary
class_average = class_total / num_students
print(f"\n{'=' * 50}")
print("CLASS SUMMARY 📈")
print(f"{'=' * 50}")
print(f"Highest Average: {highest_avg:.2f}")
print(f"Lowest Average: {lowest_avg:.2f}")
print(f"Class Average: {class_average:.2f}")
print(f"{'=' * 50}")
print("✅ Report card generation complete! ")
print("=" * 50)
