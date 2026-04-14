# ✅ Use lambda when:
# 1. Short, simple one-line operation
# 2. Passing as argument to another function
# 3. Temporary use — won't be reused elsewhere

# Example — good lambda use:
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort(key=lambda x: -x)    # sort descending
print(numbers)    # [9, 6, 5, 4, 3, 2, 1, 1]

# ❌ Use def when:
# 1. Function has multiple lines
# 2. Function will be reused in many places
# 3. Function needs a docstring
# 4. Complex logic

# Example — bad lambda use (too complex):
# ❌ Hard to read:
process = lambda x: x**2 if x > 0 else x * -1 if x < 0 else 0

# ✅ Much clearer as def:
def process(x):
    """Process a number based on its sign."""
    if x > 0:
        return x ** 2
    elif x < 0:
        return x * -1
    return 0

# Lambda with *args and **kwargs:

# Lambda works with *args too!
total = lambda *args: sum(args)
print(total(1, 2, 3, 4, 5))    # 15

# Lambda with **kwargs
greeting = lambda **kwargs: f"{kwargs.get('msg','Hello')}, {kwargs.get('name','World')}!"
print(greeting(name="Alice", msg="Hi"))    # Hi, Alice!
print(greeting(name="Bob"))               # Hello, Bob!