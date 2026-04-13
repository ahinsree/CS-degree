# Unpacking with * and **

# The * and ** operators work in BOTH directions:
# Direction 1 - PACKING (inside function definition)
def add(*args):
    return sum(args)

# Direction 2 - UNPACKING (outside function call)
number = [1, 2, 3, 4, 5]
print(add(*number)) # unpacks list INTO separate arguments
# Same as: add(1, 2, 3, 4, 5)

# Unpacking a dictionary with **
def greet(name, greeting, punctuation):
    print(f"{greeting}, {name}{punctuation}")
    
details = {"name" : "Alice",
           "greeting" : "Hello",
           "punctuation" : "!"
           }
greet(**details) #unpacks dict into keyword arguments
# Same as: greet(name = "Alice", greeting = "Hello", punctuation = "!")

# Practical unpacking:

# Merge two dictionaries using **
defaults = {"color": "blue","size": 10, "bold": False}
custom = {"color": "red", "bold": True}

merged = {**defaults, **custom}   # custom overrides defaults
print(merged)
# {'color': 'red', 'size': 10, 'bold': True}