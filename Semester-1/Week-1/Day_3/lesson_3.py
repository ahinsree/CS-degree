count = 0
while count < 5:
    print(count)
    count += 1
    
    
password = ""
while password != "python123":
    password = input("Enter the password: ")
    if password != "python123":
        print("❌Incorrect password. Try again.")
print("✅Access granted!")