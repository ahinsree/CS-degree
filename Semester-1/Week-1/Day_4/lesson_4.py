# Pattern 1 — Right triangle
rows= 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", sep=' ', end=' ')
    print()  # Move to the next line after each row
    
# Pattern 2 — Square grid
size = 4
for i in range(size):
    for j in range(size):
        print("🟥", sep=' ',end=' ')
    print()  # Move to the next line after each row
    
# Pattern 3 — Diagonal
size = 5
for i in range(size):
    for j in range(size):
        if i == j:
            print("🔵", sep=' ', end=' ')
        else:
            print(".", sep=' ', end=' ')
    print()  # Move to the next line after each row
    