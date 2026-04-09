# Find and fix ALL the scope bugs:

total_students = 0
student_name = ""

def enroll_student(name):
    global total_students
    global student_name
    total_students += 1          # Bug 1
    student_name = name
    print(f"Enrolled: {student_name}")

def show_total():
    print(f"Total: {total_students}")
    print(f"Last: {student_name}")   # Bug 2

enroll_student("Alice")
enroll_student("Bob")
show_total()