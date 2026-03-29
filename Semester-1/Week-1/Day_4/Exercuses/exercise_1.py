# Task 1: Keep asking for numbers
# Stop when user enters a negative number
# Print how many numbers entered before stopping
count = 0
while True:
    num = int(input("Enter a number: "))
    if num < 0:
        print(f"Your entered {count} numbers before stopping")
        break
    count += 1 
    
# Task 2: Find first number 1–50
# divisible by BOTH 6 and 8
for i in range(1, 51):
    if i % 6 == 0 and i % 8 == 0:
        print(f"The first number between 1 and 50 that is divisible by both 6 and 8 is: {i}")
        break
        