# Real-World Patterns

# Pattern 1 - Flexible math operations

def calculate(*args, operation = "sum"):
    """Perform operation on any number of values."""
    if operation == "sum":
        return sum(args)
    elif operation == "max":
        return max(args)
    elif operation == "min":
        return min(args)
    elif operation == "average":
        return sum(args) / len(args)
    else:
        return None
    
print(calculate(1,2,3,4,5))
print(calculate(1,2,3,4,5, operation = "max"))
print(calculate(1,2,3,4,5, operation = "min"))
print(calculate(1,2,3,4,5, operation = "average"))

# Pattern 2 — Function wrapper (preview of decorators Week 13!)
def log_call(func_name, *args, **kwargs):
    """Log what function was called with what arguments."""
    print(f" Calling : {func_name}")
    print(f" args : {args}")
    print(f" kwargs: {kwargs}")
    
log_call("create_user",
         "Alice", 32,
         city = "New York",
         country = "USA",
         role = "admin"
         )

# Pattern 3 - Building a simple config system
def configure(**settings):
    """Apply configuration settings."""
    defaults = {
        "theme"     :  "light",
        "language"  :  "English",
        "font_size" :  14,
        "debug"     :  False 
        }
    # Merge: user settings override defaults
    config = {**defaults, **settings}
    return config
my_config = configure(theme = "dark", font_size = 16)
print(my_config)

# {'theme': 'dark', 'language': 'English', 'font_size': 16, 'debug': False}