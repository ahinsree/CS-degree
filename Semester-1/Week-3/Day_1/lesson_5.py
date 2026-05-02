# Iterate Character by character

name = "Ahinsree"

# Method 1: direct iteration (cleanest)

for char in name:
    print(char,end=" ")
print()

# Method 2: With index using enumerate
for i, char in enumerate(name):
    print(f"[{i}] = {char}")
    
# Method 3: With range (less pythonic)
for i in range(len(name)):
    print(name[i], end=" ")
print()

# Practical use: count vowels in the name

def count_vowels(s):
    """Count vowels in a string."""
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
print(count_vowels(name))  # Output: 4 (A, i, e, e)

# Even cleaner with sum + generator:
def count_vowels_v2(s):
    """Count vowels in a string."""
    return sum(1 for char in s if char in "aeiouAEIOU")
print(count_vowels_v2(name))  # Output: 4 (A, i, e, e)

# Build a New String from iteration
def remove_vowels(s):
    """Remove all vowels from string."""
    result = ""
    for char in s:
        if char not in "aeiouAEIOU":
            result += char
    return result
print(remove_vowels(name))  # Output: "hnsr"

# Cleaner with join + comprehension:
def remove_vowels_v2(s):
    """Remove all vowels from string."""
    return "".join(c for c in s if c not in "aeiouAEIOU")
print(remove_vowels_v2(name))  # Output: "hnsr"