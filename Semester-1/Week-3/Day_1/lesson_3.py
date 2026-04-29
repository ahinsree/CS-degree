""" String slicing

# Slicing syntax: s[start:stop:step]
# start → inclusive (default 0)
# stop  → exclusive (default end)
# step  → jump size (default 1)

"""
name = "Ahinsree"

# Basic slicing
print(name[0:4])  # Output: "Ahin"
print(name[4:8])  # Output: "sree"
print(name[2:6])  # Output: "insr"

# Omitting start or stop
print(name[:4])   # Output: "Ahin" (start defaults to 0)
print(name[4:8])  # Output: "sree" (stop defaults to end)
print(name[:])    # Output: "Ahinsree" (full string)

# Negative Slicing
print(name[-4:])  # Output: "sree" (last 4 characters)
print(name[:-4])  # Output: "Ahin" (everything except last 4 characters)
print(name[-6:-2]) # Output: "insr" (from index -6 to -2)

# Step slicing

sentence = "Hello, World!"
print(sentence[::2])  # Output: "Hlo ol!" (every 2nd character)
print(sentence[::1])  # Output: "Hello, World!" (every character)
print(sentence[::-1]) # Output: "!dlroW ,olleH" (reversed string)

# Practical patterns:

word = "Python"
print(word[::-1])  # Reverse the string
print(word[::2])  # Get every second character
print(word[1:-1]) # Get all except first and last character

# String as a sequence
print(name[0] + name[-1])  # Concatenate first and last character