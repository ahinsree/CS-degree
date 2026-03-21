print("=" * 40)
print("          PATTERN PRINTERR")
print("=" * 40)
rows = int(input("Enter the number of rows: "))
print("\n--- pattern 1: Right Triangele ---")
for i in range(1, rows + 1):
    print("*" * i)
print("\n--- pattern 2: Countdown ---")
for i in range(rows, 0, -1):
    print("*" * i)
print("\n--- pattern 3: Number Pyramid ---")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()  # new line after each row
print("\n--- pattern 4: Multiplication Table ---")
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        print(f"{i*j:4}", end="")
    print()  # new line after each row
print("\n" + "=" * 40)
print("✅ All patterns completed!")
print("=" * 40)