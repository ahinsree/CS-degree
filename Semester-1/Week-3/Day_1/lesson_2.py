name = "Ahinsree"
#       01234567   ← positive indices
#      -8-7-6-5-4-3-2-1  ← negative indices

"""  
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
"""

# Positive indexing — left to right
print(name[0])    # 'A'  ← first character
print(name[1])    # 'h'
print(name[7])    # 'e'  ← last character

# Negative indexing — right to left
print(name[-1])   # 'e'  ← last character
print(name[-2])   # 'e'
print(name[-8])   # 'A'  ← first character

# Useful patterns:

print(name[0])    # first character
print(name[-1])   # last character
print(len(name) - 1) # index of last character = 7

# IndexError — going out of bounds
# print(name[8])   # ❌ IndexError: string index out of range

# Checking a character

word = "Python"
if word[0].isupper():
    print("Starts with uppercase letter ✅")
else:
    print("Does not start with uppercase letter ❌")