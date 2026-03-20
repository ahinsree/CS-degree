# Loop inside a loop — used for grids and tables
for row in range(3):
    for col in range(3):
        print(f"{row}, {col}",end='') 
    print()  # new line after each row
    
# Multiplication table
for i in range(1, 6):
    for j in range(1,6):
        print(f"{i*j:3}", end='')  # 3 spaces for alignment
    print()  # new line after each row