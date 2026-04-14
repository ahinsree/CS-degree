#Lambda Functions

"""A lambda is a small, anonymous (nameless) one-line function. 
   Think of it as a throwaway function you create on the spot without using def.
"""
# Regular function
def square(n):
    return n**2
print(square(5))

# Lambda function                  
square = lambda x: x**2
print(square(7))
"""lambda parameters : expression
    ↑                     ↑
keyword           single return value
                (no return keyword needed)
"""

# ✅ Lambda can only have ONE expression
# ✅ Always returns the result of that expression
# ❌ Cannot have multiple lines
# ❌ Cannot have statements (if blocks, loops, etc.)
#    — only expressions

# One parameter
double = lambda x: x * 2
print(double(5))        # 10

# Multiple parameters
add = lambda x, y: x + y
print(add(3, 4))        # 7

# With default parameter
greet = lambda name, msg="Hello": f"{msg}, {name}!"
print(greet("Alice"))           # Hello, Alice!
print(greet("Alice", "Hi"))     # Hi, Alice!

# No parameters
say_hi = lambda: "Hello World!"
print(say_hi())         # Hello World!