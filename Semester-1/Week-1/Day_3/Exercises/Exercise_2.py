# Task 1: Countdown from 10 to 1 then print "Blast off! 🚀"
count = 10
while count > 0:
    print(count)
    count -= 1
print("Blast off! 🚀")

# Task 2: Keep asking for numbers until user enters 0
# Print running total each time
total = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num
    print(f"Running total: {total}")
print(f"Final total: {total}")