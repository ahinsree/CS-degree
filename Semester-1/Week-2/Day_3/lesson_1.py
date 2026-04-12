# Fixed parameters - only work for exactly 2 numbers
def add(a, b):
    return a + b
add(1, 2)        # ✅ works
#add(1, 2, 3)     # ❌ TypeError — too many arguments!

# Solution — *args collects ALL positional arguments into a tuple
def add(*args):
    print(args)
    print(type(args))
    return sum(args)
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 2, 3, 4, 5))

# How *args works under the hood:

def show_args(*args):
    print(f"Number of args: {len(args)}")
    for i, arg in enumerate(args):
        print(f"Arg[{i}] = {arg}")

show_args("Alice", 32, "Python", True)

# Mixing regular and *args:

# Regular params MUST come before *args
def greet(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")
        
greet("Hello","Alice", "Bob", "Charlie")