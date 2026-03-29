# Task 1: Print 1–30, skip multiples of 3 OR 5
for i in range(1, 31):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i, sep=' ', end=' ')
# Task 2: Print only valid ages, count them
ages = [15, 22, -3, 17, 0, 25, 31, -1, 19, 150, 45]
valid_count = 0
for age in ages:
    if age < 1 or age > 120:
        continue
    valid_count += 1
    print(f"valid age: {age}")
print(f"Total valid ages: {valid_count}")