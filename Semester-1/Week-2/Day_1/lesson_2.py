# No parameters — does the same thing every time
def Say_hello():
    print("Hello! .👋")

Say_hello()  # Output: Hello! .👋
Say_hello()  # Output: Hello! .👋    

# One parameter — can be customized with different input
def greet(name):
    print(f"Hello, {name}! .👋")
    
greet("Ahinsree")  # Output: Hello, Ahinsree! .👋
greet("Alice")  # Output: Hello, Alice! 👋

# Multiple parameters — can take multiple inputs

def greet(name, greeting = "Hello"):
    print(f"{greeting}, {name}! .👋")
    
greet("Ahinsree")  # Output: Hello, Ahinsree! .👋
greet("Alice", "Welcome")  # Output: Welcome, Alice! .👋
greet("Bob", "Hi")  # Output: Hi, Bob! .👋