# One-Line Ternary
age = int(input("Enter your age:"))

''' normal if-else statement
if age >= 18:
    status = "Adult"
else:
    status = "Minor"'''
# one-line ternary operator
status = "Adult" if age >= 18 else "Minor"
print(status)