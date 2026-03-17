score = int(input("Enter your score: "))

match score:
    case s if s >= 90:
        print("Grade: A.", "Excellent!🏆")
    case s if s >= 80:
        print("Grade: B.", "Good job!✅")
    case s if s >= 70:
        print("Grade: C.", "Keep going!📘")
    case s if s >= 60:
        print("Grade: D.", "You can do better!⚠️")
    case _:
        print("Grade: F.", "Please revise and try again!❌")
        
# Why use case s if s >= 90?
# In Python's pattern matching, the s acts as a temporary variable that captures the value of score. 
# The if statement that follows is called a Guard. 
# The case only executes if the guard evaluates to True.