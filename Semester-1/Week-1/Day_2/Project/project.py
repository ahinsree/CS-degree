print("=" * 45)
print("       WELCOME TO CS ACADEMY LOGIN")
print("=" * 45)
correct_username = "ahinsree"
correct_password = "python2026"
min_age = 16
username = input("Enter your username: ")
password = input("Enter your password: ")
age = int(input("Age      :"))
print("-"*45)
if username == correct_username and password == correct_password:
    if age >= min_age:
        print(f"✅ Welcome back,{username.upper()}!")
        print(f"   You are {age} years old.")
        print(f"   Access granted to CS Academy 🎓")
    else:
        print(f"⚠️  Sorry, you must be at least {min_age} to join.")
else:
    print("❌ Incorrect username or password.")
    print("   Please try again.")

print("=" * 45)