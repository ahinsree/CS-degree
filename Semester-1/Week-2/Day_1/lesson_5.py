def main():
    name = input("Enter student name: ")
    score = get_score()
    grade = get_grade(score)
    print_result(name, score, grade)
    
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

if __name__ == "__main__":
    main()