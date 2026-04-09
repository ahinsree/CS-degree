#  Nested Functions & Scope

# Function defined inside another function
def outer():
    message = "Hello from outer!"

    def inner():              # nested function
        print(message)        # can access outer's variable ✅

    inner()                   # call inner from inside outer

outer()                       # Hello from outer!
#inner()                      # ❌ NameError — inner doesn't exist outside!

# nonlocal keyword — modify enclosing variable:

def counter():
    count = 0                # enclosing variable
    
    def increment():
        nonlocal count       # tell Python : use Enclosing count
        count += 1
        print(f"Count: {count}")
    increment()
    increment()
    increment()
counter() 

# Real-world use — factory functions:

def make_multiplier(factor):
    """Returns a function that multiplies by factor."""
    def multiply(number):
        return number * factor               # factor from enclosing scope
    return multiply                          # return the function itself!

double = make_multiplier(2)                  # What happens?
triple = make_multiplier(3)                  # make_multiplier(2) returns a function
                                             
print(double(5))  # Output: 10               # That returned function is assigned to double
print(triple(5))  # Output: 15               #make_multiplier(2) ───► returns multiply function
                                             #(with factor = 2)

                                             # double ───────────────► that function
print(double(10)) # Output: 20

"""💡 This pattern is called a closure — a function that remembers 
variables from its enclosing scope. You'll use closures a lot in Week 13 (Decorators)!"""

"""🎯 One-Line Understanding

A closure is a function that “remembers” values from the environment in which it was created."""
