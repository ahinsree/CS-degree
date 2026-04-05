# Without functions — repetitive code (BAD) ❌
print("Hello Alice!")
print("Welcome to CS Academy")
print("---")
print("Hello Bob!")
print("Welcome to CS Academy")
print("---")
print("Hello Charlie!")
print("Welcome to CS Academy")
print("---")

# With functions — reusable code (GOOD) ✅
def greet(name):
    print(f"Hello {name}!")
    print("Welcome to CS Academy")
    print("---")
# Call it as many times as you want!
greet("Alice")
greet("Bob")
greet("Charlie")