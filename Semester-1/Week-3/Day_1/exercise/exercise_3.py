# Task 1: Write 'count_consonants(s)'
#         Counts consonants (non-vowel letters) in a string
#         count_consonants("Ahinsree") → 4

def count_consonants(s):
    """Counts consonants (non-vowel letters) in a string."""
    count = 0
    vowels = "aeiouAEIOU"
    for char in s:
        if char.isalpha() and char not in vowels:
            count += 1
    return count
print(count_consonants("Ahinsree"))  # Output: 4

# Task 2: Write 'is_pangram(s)'
#         Returns True if string contains every letter a-z
#         is_pangram("The quick brown fox jumps over the lazy dog")
#         → True
def is_pangram(s):
    """Returns True if string contains every letter a-z."""
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    s = s.lower()
    return alphabet.issubset(set(s))
print(is_pangram("The quick brown fox jumps over the lazy dog"))  # Output: True

# Task 3: Write 'caesar_cipher(text, shift)'
#         Shifts each letter by 'shift' positions
#         caesar_cipher("Hello", 3) → "Khoor"
#         Hint: use ord() and chr()

def caesar_cipher(text, shift):
    """Shifts each letter by 'shift' positions."""
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result
print(caesar_cipher("Hello", 3))  # Output: "Khoor"