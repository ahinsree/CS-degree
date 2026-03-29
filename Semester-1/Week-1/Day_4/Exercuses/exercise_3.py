# Task 1: Print this (rows = 5):
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print(i, sep=' ', end=' ')
    print()
    
# Task 2: Print this (size = 5):
size = 5
for i in range(1, 6):
    for j in range(1, 6):
        if i == j:
            print(i, sep=' ', end=' ')
        else:
            print("▪", sep=' ', end=' ')
    print()
    
# Task 3: Hollow square (size = 5):
for row in range(size):
    for col in range(size):
        # Check if we are on the top row, bottom row, 
        # first column, or last column
        if row == 0 or row == size - 1 or col == 0 or col == size - 1:
            print("🔹",sep=' ',end="")
        else:
            # Print two spaces (one for the '*' and one for the space after it)
            print("  ",sep=' ',end="")
    # Move to the next line after finishing a row
    print()