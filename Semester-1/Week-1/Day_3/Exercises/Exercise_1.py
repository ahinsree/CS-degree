# Task 1: Print number 1 to 10
for i in range(1, 11):
    print(i)

# Task 2: Print even numbers from 1 to 20
for i in range(2, 21, 2):
    print(i)
# Alternative way to print even numbers
for i in range(1, 21,):
    if i % 2 == 0:
        print(i)
    
# Task 3: Print sum of all numbers from 1 to 50
total = 0
for i in range(1, 51):
    total += i
print("Sum of numbers from 1 to 50 is:", total)

# Task 4: Print each letter of your name on a new line
name = "Ahinsree"
for letter in name:
    print(letter)
    