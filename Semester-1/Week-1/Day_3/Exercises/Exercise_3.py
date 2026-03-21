# Task 1: Print 1-20 but SKIP multiples of 3
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)
    
# Task 2: Find FIRST number divisible by both 7 and 3
for i in range(1, 200):
    if i % 7 == 0 and i % 3 == 0:
        print(f"The first number divisible by both 7 and 3 is: {i}")
        break