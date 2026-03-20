# Repeats while condition is True
count = 0
while count < 5:
    print(count)
    count += 1
    
# Real-world: keep asking until correct password   
password = ""
while password != "python123":
    password = input("Enter the password: ")
    if password != "python123":
        print("❌Incorrect password. Try again.")
print("✅Access granted!")