# Combining logic in conditions:
username = input("Enter your username:")
password = input("Enter your password:")
if username == "admin" and password == "python123":
    print("✅ Login successful!")
else:
    print("❌ Invalid username or password.")