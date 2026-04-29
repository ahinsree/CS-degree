# 📘 LESSON 4 — String Immutability

# Strings are immutable in Python, which means that once a string is created, it cannot be changed. When you perform operations that seem to modify a string, what happens is that a new string is created with the desired changes, while the original string remains unchanged.

name = "Ahinsree"
# ❌ This will Crash because strings are immutable
# name[0] = "a"  # This will raise a TypeError: str does not support item assignment

# ✅ To change the string, you can create a new string by concatenating parts of the original string with the new character:

name_lower = "a" + name[1:]
print(name_lower)

# The original is unchanged:
print(name) # "Ahinsree" -> still the same!

# Common misconception: reassignment ≠ mutation:
name = "Ahinsree"
name = name.upper()   # NOT modifying — creating a NEW string
                      # and pointing 'name' to the new one
print(name)           # "AHINSREE"

# Why immutability matters:
# 1. Strings are safe to share — no one can secretly modify them
# 2. Strings can be used as dictionary keys (lists cannot!)
# 3. Python can optimise memory by reusing identical strings

# String interning — Python reuses strings:
a = "hello"
b = "hello"
print(a is b)     # True  — same object in memory!
print(a == b)     # True  — same value

# But:
x = "hello world"   # space prevents interning
y = "hello world"
print(x is y)     # might be False
print(x == y)     # True  — always check with ==