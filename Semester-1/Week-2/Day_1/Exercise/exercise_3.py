'''Task: Write 3 functions that work together:
 1. get_score()  → asks user for score, returns it
 2. get_grade(score) → takes score, returns grade
3. print_result(name, score, grade) → prints report'''

def main():
    name = input("Enter your name: ")
    score = get_score()
    grade = get_grade(score)
    print_result(name, score, grade)
    
def get_score():
    while True:
        score = int(input("Enter your score (0-100): "))
        if 0 <= score <= 100:
            return score
        print("Invalid score. Please enter a number between 0 and 100.")

def get_grade(score):
    if 90 <= score <= 100:
        return 'A🏆'
    elif 80 <= score < 90:
        return 'B✅'
    elif 70 <= score < 80:
        return 'C📘'
    elif 60 <= score < 70:
        return 'D⚠'
    else:
        return 'F❌'

def print_result(name, score, grade):
    print(f"{name}, your score is {score} and your grade is {grade}.")

if __name__ == "__main__":
    main()