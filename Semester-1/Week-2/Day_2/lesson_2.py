# Globel Scope & global keyword

# Global variable - defined outside all functions and can be accessed anywhere in the program
name = "Ahinsree"    # Global variable
def greet():
    print(f"Hello, {name}!")  # Accessing global variable inside a function
 # ✅ can READ global variable
greet()  # Output: Hello, Ahinsree!
print(name)  # Output: Ahinsree

# But you CANNOT modify a global inside a function

counter = 0  # Global variable
def increment():
     counter += 1    #❌ UnboundLocalError!
    # Python sees 'counter =' and thinks it's local
    # but then tries to read it before assigning → crash!
    
# Fix - use the "global" keyword to tell Python we mean the global variable
def increment():
    global counter
    counter += 1
increment()
increment()
print(counter)  # Output: 2

# When to use global — and when NOT to:

# ✅ Acceptable use of global — simple counters/flags
score = 0
def add_points(points):
    global score
    score += points
add_points(10)
add_points(25)
print(score)  # Output: 35

# ❌ BAD practice — overusing global makes code hard to debug
# Rule: if you can use return instead of global — do it!

# ❌ Bad — uses global unnecessarily
result = 0
def square(n):
    global result
    result = n ** 2
    
# ✅ Good — use return instead
def square(n):
    return n ** 2

result = square(5)
print(result)  # Output: 25