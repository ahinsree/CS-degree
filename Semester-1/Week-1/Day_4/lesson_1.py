''' break immediately stops the loop and exits it completely — no more iterations, 
even if the condition is still true.'''
# Basoc break example.
for i in range(1, 11):
    if i == 6:
        break
    print(i, end=' ')
print( )

# search through a list:
students = ["Alice", "Bob", "Charlie", "David"]
search_name = input("Search for a student: ")

found = False
for student in students:
    if student == search_name:
        print(f"✅ Found: {student}")
        found = True
        break
if not found:
    print("❌ Student not found.")
    
#  password with max attempts:
attempts = 0
while True:
    password = input("Enter the password: ")
    attempts += 1
    if password == "python123":
        print(f"✅ Correct! Took {attempts} attempts.")
        break
    elif attempts >= 3:
        print("❌ Too many attempts. Access denied.")
        break
    else:
        print(f"❌ Wrong! {3 - attempts} attempts left.")