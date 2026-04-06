# ============================================
#   WEEK 2 DAY 1 REVISION NOTES — Functions
#   Date: __06-04-2026_________
# ============================================

# FUNCTION → in my own words:
# _A reusable block of code that performs a specific task. Think of it as a "mini-program" inside your main program that you can call by name whenever you need it._______________________________________________

# WHY USE FUNCTIONS? (DRY principle):
# DRY stands for Don't Repeat Yourself. Functions allow you to write logic once and reuse it multiple times, making your code easier to read, test, and maintain. If you find a bug, you only have to fix it in one place.________________________________________________

# PARAMETER vs ARGUMENT (difference):
# _Parameter: The variable name listed in the function definition (the "placeholder").

#  Argument: The actual value passed into the function when you call it._______________________________________________

# RETURN vs PRINT (difference):
# Print: Simply displays a value to the console for a human to see. It does not save the data.

# Return: Sends a value back to the "caller" so the program can use it for further calculations. It is the output of the function.________________________________________________

# DOCSTRING → what is it and why use it?
# A string literal that appears as the first statement in a function, usually wrapped in triple quotes """Like this""". It explains what the function does. It’s used for documentation and help________________________________________________

# DEFAULT PARAMETER → in my own words:
"""A "fallback" value assigned to a parameter in the function header. If the caller doesn't provide an argument for that parameter, the function uses the default.

   Example: def power(base, exponent=2): (Here, exponent defaults to 2 if not specified).""" 
# BIGGEST INSIGHT FROM CS50P:
# David Malan often emphasizes that functions are about abstraction—hiding the "how" so you can focus on the "what."________________________________________________

# BIGGEST INSIGHT FROM MIT 6.0001:
# Dr. Ana Bell focuses heavily on decomposition—breaking a large, complex problem into smaller, manageable functions that interact with each other.________________________________________________

# SOMETHING I FOUND DIFFICULT:
# Think about Scope (global vs local variables) or the logic of when to use a return value versus just printing.________________________________________________

# SOMETHING I EXPLORED BEYOND THE LESSON:
# ________________________________________________